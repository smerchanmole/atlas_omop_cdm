
# importing the requests library
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, BooleanType, TimestampType
from pyspark.sql.functions import *
from datetime import datetime
import requests
requests.packages.urllib3.disable_warnings()

import json
import pandas as pd
import math
import time
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from atlas_omop_variables import * #URL atlas , JSON schemas from ATLAS API and tables DDLs
from user_pass_file import * #your atlas user & pass files & variables called user=your user and pwd=your_pass
from create_tables import * #the functions to create hive or iceberg OMOP CDM 5.4 tables.


######################################################################################
def createGlossary (URL_atlas, user, pwd, json):
    # api-endpoint
    URL = URL_atlas + "glossary"
    headers = {"accept": "application/json","Content-Type": "application/json; charset=utf-8"}
    print ("---> Accessing API URL: ", URL)
    # sending get request and saving the response as response object
    ######
    ###### IMPORTANT NOTE: data has to be sent with data= not with json=
    ######
    response = requests.post(url = URL, verify=False, auth = (user, pwd), headers=headers, data=json)
    return (response)######################################################################################

def createCategory (URL_atlas, user, pwd, json):
    # api-endpoint
    URL = URL_atlas + "glossary/category"
    headers = {"accept": "application/json","Content-Type": "application/json; charset=utf-8"}
    print ("---> Accessing API URL: ", URL)
    # sending get request and saving the response as response object
    ######
    ###### IMPORTANT NOTE: data has to be sent with data= not with json=
    ######
    response = requests.post(url = URL, verify=False, auth = (user, pwd), headers=headers, data=json)
    return (response)

def createTerm (URL_atlas, user, pwd, json):
    # api-endpoint
    URL = URL_atlas + "glossary/term"
    headers = {"accept": "application/json","Content-Type": "application/json; charset=utf-8"}
    print ("---> Accessing API URL: ", URL)
    # sending get request and saving the response as response object
    ######
    ###### IMPORTANT NOTE: data has to be sent with data= not with json=
    ######
    response = requests.post(url = URL, verify=False, auth = (user, pwd), headers=headers, data=json)
    return (response)

def createClassification (URL_atlas, user, pwd, json):
    # api-endpoint
    URL = URL_atlas + "types/typedefs"
    headers = {"accept": "application/json","Content-Type": "application/json; charset=utf-8"}
    print ("---> Accessing API URL: ", URL)
    # sending get request and saving the response as response object
    ######
    ###### IMPORTANT NOTE: data has to be sent with data= not with json=
    ######
    response = requests.post(url = URL, verify=False, auth = (user, pwd), headers=headers, data=json)
    return (response)

def findEntity (URL_atlas, user, pwd, search_text):
    # api-endpoint
    URL = URL_atlas + "search/basic"
    headers = {"accept": "application/json","Content-Type": "application/json; charset=utf-8"}
    print ("---> Accessing API URL: ", URL)
    # sending get request and saving the response as response object
    params = {"excludeDeletedEntities": "true",
              "limit": "1000",
              "offset": "-1",
              "query": search_text,
              "typeName": "hive_table"
             }

    response = requests.get(url = URL, verify=False, auth = (user, pwd), headers=headers, params=params)
    return (response)
def updateEntityClassification (URL_atlas, user, pwd, entity_guid, json):
    # api-endpoint
    URL = URL_atlas + "entity/guid/" +entity_guid+ "/classifications"
    headers = {"accept": "application/json", "Content-Type": "application/json; charset=utf-8"}
    print("---> Accessing API URL: ", URL)
    # sending get request and saving the response as response object
    ######
    ###### IMPORTANT NOTE: data has to be sent with data= not with json=
    ######
    response = requests.post(url=URL, verify=False, auth=(user, pwd), headers=headers, data=json)
    return (response)

def updateTermWithEntity (URL_atlas, user, pwd, term_guid, json):
    # api-endpoint
    URL = URL_atlas + "glossary/terms/"+term_guid+"/assignedEntities"
    headers = {"accept": "application/json", "Content-Type": "application/json; charset=utf-8"}
    print("---> Accessing API URL: ", URL)
    # sending get request and saving the response as response object
    ######
    ###### IMPORTANT NOTE: data has to be sent with data= not with json=
    ######
    response = requests.post(url=URL, verify=False, auth=(user, pwd), headers=headers, data=json)
    return (response)


######################################################################################

######################################################################################
######################################################################################
# M A I N                                                                           ##
######################################################################################
######################################################################################


# --------------------------------------------------------------------------------------------------------------------
# 1st thing is to create the Glossary and get the Glossary GUID
# --------------------------------------------------------------------------------------------------------------------
print("**********************************************************")
print("*****          OMOP GLOSSARY creation                 **** ")
print("**********************************************************")
print()
print("---------------------------------------------------------")
print("CATALOG OMOP CDM v5.4 creation --------------------------")
print("---------------------------------------------------------")
response = createGlossary(URL_atlas, user, pwd, json.dumps(omop_cdm_54_glossary))

if response.status_code != 200:
    print("The response is: ", response)
    print("the text is:", response.text)
    print("We exit as is NOT  '200 OK'")
    exit (-1)

json_glossary = response.json()
#print()
#print("--->Response: ")
#print(json.dumps(json_glossary, indent=4))

print("---> we need the GUI so we store it to use it later to include all the terms to this glossary")
glossary_guid=json_glossary["guid"]
print("---> Glossary GUID: ", glossary_guid)
print()


# --------------------------------------------------------------------------------------------------------------------
# 2nd thing is to create the Classification and get the Classification GUID
# --------------------------------------------------------------------------------------------------------------------
print("**********************************************************")
print("*****          OMOP CLASSIFICATION creation           **** ")
print("**********************************************************")

response = createClassification(URL_atlas, user, pwd, json.dumps(omop_cdm_54_classification))

if response.status_code != 200:
    print("The response is: ", response)
    print("the text is:", response.text)
    print("We exit as is NOT  '200 OK'")
    exit (-1)
json_classification = response.json()
#print()
#print("--->Response: ")
#print(json.dumps(json_classification, indent=4))

print("---> we need the GUI so we store it to use it later to include this calssification to all terms and categories")
classification_guid=json_classification["classificationDefs"][0]["guid"]
print("---> Classification GUID: ", classification_guid)
print()

# --------------------------------------------------------------------------------------------------------------------
# 3rd thing is to create the categories (Tables and columns definitions)
# --------------------------------------------------------------------------------------------------------------------
print()
print("**********************************************************")
print("****              OMOP Categories creation            **** ")
print("**********************************************************")
print()
category_guid_list=[]
for item in omop_category_list:
    print()
    print("---------------------------------------------------------")
    print(f" OMOP {item[0]} Category creation ")
    print("---------------------------------------------------------")
    #We set the Catalog Guid to this term
    item[1]["anchor"]["glossaryGuid"]= glossary_guid
    response = createCategory(URL_atlas, user, pwd, json.dumps(item[1]))

    if response.status_code != 200:
       print("the text is:", response.text)
       print("We exit as is NOT  '200 OK'")
       exit (-1)
    json_category = response.json()
    #print()
    #print("--->Response: ")
    #print(json.dumps(json_category, indent=4))

    print(f"---> we need the GUI so we store it to use it later to include all the terms {item[0]} to this category")

    category_guid_list.append ([item[0],json_category["guid"]])

    print(f"---> Category {item[0]} GUID: ", json_category["guid"])
    print()
##################################################################################

# --------------------------------------------------------------------------------------------------------------------
# 3rd thing is to create the terms (Tables and columns definitions)
# --------------------------------------------------------------------------------------------------------------------
print("**********************************************************")
print("****         OMOP Terms creation                      **** ")
print("**********************************************************")

term_guid_list=[]
for item in omop_terms_list:
    print()
    print("---------------------------------------------------------")
    print(f" OMOP {item[0]} Term creation")
    print("---------------------------------------------------------")

    #let's find the GUID of the category associated.
    i=0
    index=0
    for category in category_guid_list:
        if category[0] == item[0]:
            index=i
        else:
            i+=1
        #We set the Catalog and category Guid to this term
    item[1]["anchor"]["glossaryGuid"]= glossary_guid
    item[1]["categories"][0]["categoryGuid"]= category_guid_list[index][1]
    # To classified a Tern, you put the Classification typeName (the name not the GUI) in the Generation JSON like this
    #"classifications": [{
    #    "typeName": "OMOP CDM 5.4"
    #}],
    #print ("ENTRY JSON: ", json.dumps(item[1]))
    response = createTerm(URL_atlas, user, pwd, json.dumps(item[1]))

    if response.status_code != 200:
        print("the text is:", response.text)
        print("We exit as is NOT  '200 OK'")
        exit (-1)

    json_term = response.json()
    #print()
    #print("--->Response: ")
    #print(json.dumps(json_term, indent=4))

    print("---> we need the GUI so we store it to use it later to include all the terms to this catalog")

    term_guid=json_term["guid"]
    term_guid_list.append([item[0],term_guid])

    print(f"---> {item[0]} GUID: ", term_guid)
print()
##################################################################################

##################################################################################
# we can also create the OMOP tables in HIVE or ICEBERG table format.

print("**********************************************************")
print("****         OMOP Tables creation                    **** ")
print("**********************************************************")
result=create_omop_tables (DATABASE, "Hive")


##################################################################################
# Now we find the GUID of all the terms generated in the create tables.
print("**********************************************************")
print("****   OMOP find Entities guid of Tables in atlas     **** ")
print("**********************************************************")

print (" ---> We have to search in ATLAS for the tables (registered as ENTITIES) we have just generated.")
print (" ---> but, we are going to sleep 30 seconds to let ATLAS time to include the new generated tables...")
time.sleep(30)

omop_entities_list=[]
for table in  LIST_HIVE_TABLES:
    search_text="from table where quialifiedName="+DATABASE+"."+table[2]
    response = findEntity(URL_atlas, user, pwd, search_text)
    if response.status_code != 200:
        print("the text is:", response.text)
        print("We exit as is NOT  '200 OK'")
        exit (-1)

    json_entity = response.json()
    #print()
    #print("--->Response: ")
    #print(json.dumps(json_entity, indent=4))

    omop_entities_list.append([table[0], json_entity['entities'][0]['guid'] ])
    print (f"--->We found Entity for Table: {table[0]} - with GUID: {json_entity['entities'][0]['guid']}")
    print()


##################################################################################
# Now we associate the term and classification with the entity
#################################################################################
print("********************************************************************************")
print("****   Assigning classification and (business Term) to OMOP entities       **** ")
print("********************************************************************************")

json_classification ='[{"typeName": "'+atlas_OMOP_classification+'"}]'

print ("QUERY:   ", json_classification)

for entity in omop_entities_list:
    response=updateEntityClassification (URL_atlas, user, pwd, entity[1], json_classification)
    if response.status_code < 200 or response.status_code > 299:
        print("the text is:", response.text)
        print("We exit as is NOT  '200 OK'")
        exit (-1)
    #print ("EXIT RESPONSE")
    #print (response)

    print(f"--->Table {entity[0]} associate with Classification {atlas_OMOP_classification}")
    print()

print("********************************************************************************")
print("****   Assigning classification and (business Term) to OMOP entities       **** ")
print("********************************************************************************")

for term in term_guid_list:
    entity_guid=""
    entity_name=""
    for entity in omop_entities_list:
        if entity[0]==term[0]:
            print (f"---> Entity found for term {term[0]} with GUID {term[1]}.")
            entity_guid=entity[1]
            entity_name=entity[0]
    if entity_guid=="":
        print (f"---> Entity for Term {term[0]} NOT FOUND! no association done.")
    else:
        # Doing the assignation
        json_assignation='[{ "guid": "' + entity_guid + '" }]'
        response= updateTermWithEntity(URL_atlas, user, pwd, term[1], json_assignation)
        if response.status_code < 200 or response.status_code > 299 :
            print("the text is:", response.text)
            print("We exit as is NOT from '200' family")
            exit (-1)
        #print ("EXIT RESPONSE")
        #print (response)

        print(f"--->Term  {term[0]} associate with entity {entity_name}")
        print()


print ("*** END OF LOADING OMOP DATA: Databases & governded items in ATLAS.")
