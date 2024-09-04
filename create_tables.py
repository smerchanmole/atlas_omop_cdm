from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, BooleanType, TimestampType
from pyspark.sql.functions import *
from variables_create_tables import *



# ###########################################################
#
# VARIABLES
#
# ###########################################################
# LIST_TABLES is with iceberg format, LIST_HIVE_TABLES is with HIVE PARQUET

LIST_TABLES=[]
LIST_TABLES.append(["PERSON",SQL_DDL_PERSON, "PERSON"])
LIST_TABLES.append (["VISIT OCCURRENCE",SQL_DDL_VISIT_OCCURRENCE, "VISIT_OCCURRENCE"])
LIST_TABLES.append (["VISIT DETAIL",SQL_DDL_VISIT_DETAIL, "VISIT_DETAIL"])
LIST_TABLES.append (["CONDITION OCCURRENCE", SQL_DDL_CONDITION_OCCURRENCE,"CONDITION_OCCURRENCE"])
LIST_TABLES.append (["DRUG EXPOSURE",SQL_DDL_DRUG_EXPOSURE, "DRUG_EXPOSURE"])
LIST_TABLES.append (["PROCEDURE OCCURRENCE",SQL_DDL_PROCEDURE_OCCURRENCE,"PROCEDURE_OCCURRENCE"])
LIST_TABLES.append (["DEVICE EXPOSURE",SQL_DDL_DEVICE_EXPOSURE, "DEVICE_EXPOSURE"])
LIST_TABLES.append (["MEASUREMENT",SQL_DDL_MEASUREMENT, "MEASUREMENT"])
LIST_TABLES.append (["OBSERVATION",SQL_DDL_OBSERVATION, "OBSERVATION"])
LIST_TABLES.append (["DEATH",SQL_DDL_DEATH, "DEATH"])
LIST_TABLES.append (["NOTE",SQL_DDL_NOTE, "NOTE"])
LIST_TABLES.append (["NOTE NLP",SQL_DDL_NOTE_NLP, "NOTE_NLP"])
LIST_TABLES.append (["SPECIMEN",SQL_DDL_SPECIMEN, "SPECIMEN"])
LIST_TABLES.append (["FACT RELATIONSHIP",SQL_DDL_FACT_RELATIONSHIP, "FACT_RELATIONSHIP"])
LIST_TABLES.append (["LOCATION",SQL_DDL_FACT_LOCATION, "LOCATION"])
LIST_TABLES.append (["CARE SITE",SQL_DDL_CARE_SITE, "CARE_SITE"])
LIST_TABLES.append (["PROVIDER",SQL_DDL_PROVIDER, "PROVIDER"])
LIST_TABLES.append (["PAYER PLAN PERIOD",SQL_DDL_PAYER_PLAN_PERIOD, "PAYER_PLAN_PERIOD"])
LIST_TABLES.append (["COST",SQL_DDL_COST, "COST"])
LIST_TABLES.append (["DRUG ERA",SQL_DDL_DRUG_ERA, "DRUG_ERA"])
LIST_TABLES.append (["DOSE ERA",SQL_DDL_DOSE_ERA, "DOSE_ERA"])
LIST_TABLES.append (["CONDITION ERA",SQL_DDL_CONDITION_ERA, "CONDITION_ERA"])
LIST_TABLES.append (["EPISODE",SQL_DDL_EPISODE, "EPISODE"])
LIST_TABLES.append (["EPISODE EVENT",SQL_DDL_EPISODE_EVENT, "EPISODE_EVENT"])
LIST_TABLES.append (["METADATA",SQL_DDL_METADATA, "METADATA"])
LIST_TABLES.append (["CDM SOURCE",SQL_DDL_CDM_SOURCE, "CDM_SOURCE"])
LIST_TABLES.append (["CONCEPT",SQL_DDL_CONCEPT, "CONCEPT"])
LIST_TABLES.append (["VOCABULARY",SQL_DDL_VOCABULARY, "VOCABULARY"])
LIST_TABLES.append (["DOMAIN",SQL_DDL_DOMAIN, "DOMAIN"])
LIST_TABLES.append (["CONCEPT CLASS",SQL_DDL_CONCEPT_CLASS, "CONCEPT_CLASS"])
LIST_TABLES.append (["CONCEPT RELATIONSHIP",SQL_DDL_CONCEPT_RELATIONSHIP, "CONCEPT_RELATIONSHIP"])
LIST_TABLES.append (["RELATIONSHIP",SQL_DDL_RELATIONSHIP, "RELATIONSHIP"])
LIST_TABLES.append (["CONCEPT SYNONYM",SQL_DDL_CONCEPT_SYNONYM, "CONCEPT_SYNONYM"])
LIST_TABLES.append (["CONCEPT ANCESTOR",SQL_DDL_CONCEPT_ANCESTOR, "CONCEPT_ANCESTOR"])
LIST_TABLES.append (["SOURCE TO CONCEPT MAP",SQL_DDL_SOURCE_TO_CONCEPT_MAP, "SOURCE_TO_CONCEPT_MAP"])
LIST_TABLES.append (["DRUG STRENGTH",SQL_DDL_DRUG_STRENGTH, "DRUG_STRENGTH"])
LIST_TABLES.append (["COHORT",SQL_DDL_COHORT, "COHORT"])
LIST_TABLES.append (["COHORT DEFINITION",SQL_DDL_COHORT_DEFINITION, "COHORT_DEFINITION"])

LIST_HIVE_TABLES=[]
LIST_HIVE_TABLES.append(["PERSON",HIVE_SQL_DDL_PERSON, "person"])
LIST_HIVE_TABLES.append (["VISIT OCCURRENCE",HIVE_SQL_DDL_VISIT_OCCURRENCE,"visit_occurrence"])
LIST_HIVE_TABLES.append (["VISIT DETAIL",HIVE_SQL_DDL_VISIT_DETAIL,"visit_detail"])
LIST_HIVE_TABLES.append (["CONDITION OCCURRENCE", HIVE_SQL_DDL_CONDITION_OCCURRENCE,"condition_occurrence"])
LIST_HIVE_TABLES.append (["DRUG EXPOSURE",HIVE_SQL_DDL_DRUG_EXPOSURE,"drug_exposure"])
LIST_HIVE_TABLES.append (["PROCEDURE OCCURRENCE",HIVE_SQL_DDL_PROCEDURE_OCCURRENCE,"procedure_occurrence"])
LIST_HIVE_TABLES.append (["DEVICE EXPOSURE",HIVE_SQL_DDL_DEVICE_EXPOSURE, "device_exposure"])
LIST_HIVE_TABLES.append (["MEASUREMENT",HIVE_SQL_DDL_MEASUREMENT,"measurement"])
LIST_HIVE_TABLES.append (["OBSERVATION",HIVE_SQL_DDL_OBSERVATION,"observation"])
LIST_HIVE_TABLES.append (["DEATH",HIVE_SQL_DDL_DEATH,"death"])
LIST_HIVE_TABLES.append (["NOTE",HIVE_SQL_DDL_NOTE,"note"])
LIST_HIVE_TABLES.append (["NOTE NLP",HIVE_SQL_DDL_NOTE_NLP,"note_nlp"])
LIST_HIVE_TABLES.append (["SPECIMEN",HIVE_SQL_DDL_SPECIMEN,"specimen"])
LIST_HIVE_TABLES.append (["FACT RELATIONSHIP",HIVE_SQL_DDL_FACT_RELATIONSHIP, "fact_relationship"])
LIST_HIVE_TABLES.append (["LOCATION",HIVE_SQL_DDL_FACT_LOCATION,"location"])
LIST_HIVE_TABLES.append (["CARE SITE",HIVE_SQL_DDL_CARE_SITE,"care_site"])
LIST_HIVE_TABLES.append (["PROVIDER",HIVE_SQL_DDL_PROVIDER,"provider"])
LIST_HIVE_TABLES.append (["PAYER PLAN PERIOD",HIVE_SQL_DDL_PAYER_PLAN_PERIOD,"payer_plan_period"])
LIST_HIVE_TABLES.append (["COST",HIVE_SQL_DDL_COST,"cost"])
LIST_HIVE_TABLES.append (["DRUG ERA",HIVE_SQL_DDL_DRUG_ERA,"drug_era"])
LIST_HIVE_TABLES.append (["DOSE ERA",HIVE_SQL_DDL_DOSE_ERA,"dose_era"])
LIST_HIVE_TABLES.append (["CONDITION ERA",HIVE_SQL_DDL_CONDITION_ERA,"condition_era"])
LIST_HIVE_TABLES.append (["EPISODE",HIVE_SQL_DDL_EPISODE, "episode"])
LIST_HIVE_TABLES.append (["EPISODE EVENT",HIVE_SQL_DDL_EPISODE_EVENT,"episode_event"])
LIST_HIVE_TABLES.append (["METADATA",HIVE_SQL_DDL_METADATA,"metadata"])
LIST_HIVE_TABLES.append (["CDM SOURCE",HIVE_SQL_DDL_CDM_SOURCE,"cdm_source"])
LIST_HIVE_TABLES.append (["CONCEPT",HIVE_SQL_DDL_CONCEPT,"concept"])
LIST_HIVE_TABLES.append (["VOCABULARY",HIVE_SQL_DDL_VOCABULARY,"vocabulary"])
LIST_HIVE_TABLES.append (["DOMAIN",HIVE_SQL_DDL_DOMAIN,"domain"])
LIST_HIVE_TABLES.append (["CONCEPT CLASS",HIVE_SQL_DDL_CONCEPT_CLASS,"concept_class"])
LIST_HIVE_TABLES.append (["CONCEPT RELATIONSHIP",HIVE_SQL_DDL_CONCEPT_RELATIONSHIP,"concept_relationship"])
LIST_HIVE_TABLES.append (["RELATIONSHIP",HIVE_SQL_DDL_RELATIONSHIP, "relationship"])
LIST_HIVE_TABLES.append (["CONCEPT SYNONYM",HIVE_SQL_DDL_CONCEPT_SYNONYM, "concept_synonym"])
LIST_HIVE_TABLES.append (["CONCEPT ANCESTOR",HIVE_SQL_DDL_CONCEPT_ANCESTOR, "concept_ancestor"])
LIST_HIVE_TABLES.append (["SOURCE TO CONCEPT MAP",HIVE_SQL_DDL_SOURCE_TO_CONCEPT_MAP,"source_to_concept_map"])
LIST_HIVE_TABLES.append (["DRUG STRENGTH",HIVE_SQL_DDL_DRUG_STRENGTH, "drug_strength"])
LIST_HIVE_TABLES.append (["COHORT",HIVE_SQL_DDL_COHORT,"cohort"])
LIST_HIVE_TABLES.append (["COHORT DEFINITION",HIVE_SQL_DDL_COHORT_DEFINITION, "cohort_definition"])

def create_omop_tables (DATABASE, TableFormat):
    # ###########################################################
    # Generate the Spark Session
    #############################################################
    print ("\n***** Creando la sesion Spark ...\n")
    spark = (SparkSession\
        .builder.appName("Spark-SQL-Test") \
        .config("spark.sql.iceberg.handle-timestamp-without-timezone", "true") \
        .enableHiveSupport() \
        .getOrCreate())

    spark.sparkContext.setLogLevel("ERROR")
    print ("\n****** Sesion creada.\n")

    # ###########################################################
    # Generate the tables with DDLs
    #############################################################

    # Listing the tables adquired in the list variable.
    if TableFormat == "Iceberg":
        # Generating the tables
        print("***** TABLES TO BE LOADED WITH DDL:")
        for duple in LIST_TABLES:
            print ("***** Table name: ", duple[0])

        print("****** CREATING THE CORRECT DATABASE (IF NOT EXIST):", DATABASE)
        resultados = spark.sql(SQL_DDL_CREATE_DATABASE)
        resultados.show(1)
        print("****** SELECTING THE CORRECT DATABASE:", DATABASE)
        resultados = spark.sql(SQL_DDL_USE_DATABASE)
        resultados.show(1)

        # Generating the tables
        for duple in LIST_HIVE_TABLES:
           print("****** CREATING TABLE:", duple[0])
           resultados = spark.sql(duple[1])
           resultados.show(1)
    elif TableFormat=="Hive":
        # Generating the tables
        print("***** TABLES TO BE LOADED WITH DDL:")
        for duple in LIST_HIVE_TABLES:
            print("***** Table name: ", duple[0])

        print("****** CREATING THE CORRECT DATABASE (IF NOT EXIST):", DATABASE)
        resultados = spark.sql(SQL_DDL_CREATE_DATABASE)
        resultados.show(1)
        print("****** SELECTING THE CORRECT DATABASE:", DATABASE)
        resultados = spark.sql(SQL_DDL_USE_DATABASE)
        resultados.show(1)

        # Generating the tables
        for duple in LIST_HIVE_TABLES:
            print("****** CREATING TABLE:", duple[0])
            resultados = spark.sql(duple[1])
            resultados.show(1)
    else:
        print ("##### ERROR !!! Wrong Table Format, no tables were created")

    # ###########################################################
    # CLOSING THE SESSION
    #############################################################
    print ("\n****** Cerrando sesion spark...\n")
    spark.stop


