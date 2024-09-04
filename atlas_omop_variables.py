
URL_atlas="https://cdp1.mole4.local:31443/api/atlas/v2/"
atlas_OMOP_classification="OMOP CDM v5.4"
#######################################################################################################################
# GLOSSARY
#######################################################################################################################
omop_cdm_54_glossary= {
    "guid" : "",
    "language": "English",
    "longDescription": "This is the documented Glossary of the version 5.4 as described in \
                       <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>, ",
    "name": "OMOP CDM v5.4",
    "qualifiedName": "OMOP CDM v5.4",
    "shortDescription": "The Observational Medical Outcomes Partnership (OMOP) Common Data Model (CDM) is an open \
         community data standard, designed to standardize the structure and content of observational data and \
         to enable efficient analyses that can produce reliable evidence"
     }

#######################################################################################################################
# CLASIFICATION
#######################################################################################################################
omop_cdm_54_classification= {
    "classificationDefs" : [{
        "description": "This is a tag to classify terms and entities related to OMOP CDM version 5.4",
        "guid":"",
        "name":atlas_OMOP_classification
    }]
}
#######################################################################################################################
# CATEGORIES
#######################################################################################################################
omop_category_list=[]
omop_cdm_54_category_person = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "This table serves as the central identity management for all Persons in the database.<br> \
        It contains records that uniquely identify each person or patient, and some demographic information.<br>\
        <b>ETL Conventions:</b> <br> \
        All Persons in a database needs one record in this table, unless they fail data quality requirements \
        specified in the ETL. Persons with no Events should have a record nonetheless. If more than one data source \
        contributes Events to the database, Persons must be reconciled, if possible, across the sources to create \
        one single record per Person. The content of the BIRTH_DATETIME must be equivalent to the content of \
        BIRTH_DAY, BIRTH_MONTH and BIRTH_YEAR. <br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
    "name": "OMOP CDM Person",
    "shortDescription": "This is the category of a PERSON in OMOP CDM v5.4",
    "guid": ""
}
omop_category_list.append(["PERSON",omop_cdm_54_category_person])

omop_cdm_54_category_observation_period = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "This table contains records which define spans of time during which two conditions \
        are expected to hold:<br>(i)   Clinical Events that happened to the Person are recorded in the Event \
        tables, and <br>   (ii) absence of records indicate such Events did not occur during this span of time. \
        <br><b>User Guide</b><br> \
        For each Person, one or more OBSERVATION_PERIOD records may be present, but they will not overlap or be \
        back to back to each other. Events may exist outside all of the time spans of the OBSERVATION_PERIOD \
        records for a patient, however, absence of an Event outside these time spans cannot be construed as evidence\
        of absence of an Event. Incidence or prevalence rates should only be calculated for the time \
        of active OBSERVATION_PERIOD records. When constructing cohorts, outside Events can be used for \
        inclusion criteria definition, but without any guarantee for the performance of these criteria. \
        Also, OBSERVATION_PERIOD records can be as short as a single day, greatly disturbing the denominator \
        of any rate calculation as part of cohort characterizations. \
        To avoid that, apply minimal observation time as a requirement for any cohort definition.<br> \
        <b>ETL Conventions</b><br> \
        Each Person needs to have at least one OBSERVATION_PERIOD record, which should represent time intervals \
        with a high capture rate of Clinical Events. Some source data have very similar concepts, \
        such as enrollment periods in insurance claims data. In other source data such as most EHR systems \
        these time spans need to be inferred under a set of assumptions. It is the discretion of the ETL developer \
        to define these assumptions. In many ETL solutions the start date of the first occurrence or the first \
        high quality occurrence of a Clinical Event (Condition, Drug, Procedure, Device, Measurement, Visit) is \
        defined as the start of the OBSERVATION_PERIOD record, and the end date of the last occurrence of last \
        high quality occurrence of a Clinical Event, or the end of the database period becomes the end of the \
        OBSERVATOIN_PERIOD for each Person. If a Person only has a single Clinical Event the OBSERVATION_PERIOD \
        record can be as short as one day. Depending on these definitions it is possible that Clinical Events \
        fall outside the time spans defined by OBSERVATION_PERIOD records. Family history or history of Clinical \
        Events generally are not used to generate OBSERVATION_PERIOD records around the time they are referring to. \
        Any two overlapping or adjacent OBSERVATION_PERIOD records have to be merged into one.<br> \
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
    "name": "OMOP CDM Observation Period",
    "shortDescription": "This table contains records which define spans of time during which two conditions \
        are expected to hold:<br> (i) Clinical Events that happened to the Person are recorded in the Event tables, \
        and <br>(ii) absence of records indicate such Events did not occur during this span of time.",
    "guid": ""
}
omop_category_list.append(["OBSERVATION PERIOD",omop_cdm_54_category_observation_period])

omop_cdm_54_category_visit_occurrence = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br> This table contains Events where Persons engage with the \
       healthcare system for a duration of time. They are often also called “Encounters”. Visits are defined \
       by a configuration of circumstances under which they occur, such as: <br>\
       (i) whether the patient comes to a healthcare institution, the other way around, or the interaction \
       is remote,<br>(ii) whether and what kind of trained medical staff is delivering the service during \
       the Visit, and <br>(iii) whether the Visit is transient or for a longer period involving a stay in bed. \
       <br><b>User Guide</b><br>The configuration defining the Visit are described by Concepts in the Visit Domain, \
       which form a hierarchical structure, but rolling up to generally familiar Visits adopted in most healthcare \
       systems worldwide: <br> <ul> \
       <li><b>Inpatient Visit:</b> Person visiting hospital, at a Care Site, in bed, for duration of more than one \
       day, with physicians and other Providers permanently available to deliver service around the clock. </li> \
       <li><b>Emergency Room Visit:</b> Person visiting dedicated healthcare institution for treating emergencies, \
       at a Care Site, within one day, with physicians and Providers permanently available to deliver service \
       around the clock. </li>\
       <li><b>Emergency Room and Inpatient Visit: </b> Person visiting ER followed by a subsequent Inpatient Visit, \
       where Emergency department is part of hospital, and transition from the ER to other hospital departments \
       is undefined. </li>\
       <li><b>Non-hospital institution Visit:</b> Person visiting dedicated institution for reasons of poor health, \
       at a Care Site, long-term or permanently, with no physician but possibly other Providers permanently available \
       to deliver service around the clock.</li>\
       <li><b>Outpatient Visit:</b> Person visiting dedicated ambulatory healthcare institution, at a Care Site, \
       within one day, without bed, with physicians or medical Providers delivering service during Visit. </li>\
       <li><b>Home Visit:</b> Provider visiting Person, without a Care Site, within one day, delivering service. </li>\
       <li><b>Telehealth Visit:</b> Patient engages with Provider through communication media. </li>\
       <li><b>Pharmacy Visit:</b> Person visiting pharmacy for dispensing of Drug, at a Care Site, within one day.</li>\
       <li><b>Laboratory Visit:</b> Patient visiting dedicated institution, at a Care Site, within one day, \
       for the purpose of a Measurement.</li>\
       <li><b>Ambulance Visit:</b> Person using transportation service for the purpose of initiating one of \
       the other Visits, without a Care Site, within one day, potentially with Providers accompanying the Visit \
       and delivering service. </li>\
       <li><b>Case Management Visit</b>: Person interacting with healthcare system, without a Care Site, \
       within a day, with no Providers involved, for administrative purposes. </li></ul>\
       The Visit duration, or ‘length of stay’, is defined as VISIT_END_DATE - VISIT_START_DATE. For all Visits \
       this is <1 day, except Inpatient Visits and Non-hospital institution Visits. \
       The CDM also contains the VISIT_DETAIL table where additional information about the Visit is stored, \
       for example, transfers between units during an inpatient Visit.\
       <br><b>ETL Conventions</b><br>\
       Visits can be derived easily if the source data contain coding systems for Place of Service or Procedures, \
       like CPT codes for well visits. In those cases, the codes can be looked up and mapped to a Standard \
       Visit Concept. Otherwise, Visit Concepts have to be identified in the ETL process. This table will contain \
       concepts in the Visit domain. These concepts are arranged in a hierarchical structure to facilitate cohort \
       definitions by rolling up to generally familiar Visits adopted in most healthcare systems worldwide. \
       Visits can be adjacent to each other, i.e. the end date of one can be identical with the start date of \
       the other. As a consequence, more than one-day Visits or their descendants can be recorded for the same \
       day. Multi-day visits must not overlap, i.e. share days other than start and end days. It is often the \
       case that some logic should be written for how to define visits and how to assign Visit_Concept_Id.<br> \
       For example, in US claims outpatient visits that appear to occur within the time period of an inpatient \
       visit can be rolled into one with the same Visit_Occurrence_Id. In EHR data inpatient visits that are \
       within one day of each other may be strung together to create one visit. It will all depend on the source \
       data and how encounter records should be translated to visit occurrences. Providers can be associated \
       with a Visit through the PROVIDER_ID field, or indirectly through PROCEDURE_OCCURRENCE records linked \
       both to the VISIT and PROVIDER tables.<br> \
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
    "name": "OMOP CDM Visit Occurrence",
    "shortDescription": "This table contains Events where Persons engage with the \
       healthcare system for a duration of time. They are often also called “Encounters”. Visits are defined \
       by a configuration of circumstances under which they occur, such as: \
       (i) whether the patient comes to a healthcare institution, the other way around, or the interaction \
       is remote,(ii) whether and what kind of trained medical staff is delivering the service during \
       the Visit, and (iii) whether the Visit is transient or for a longer period involving a stay in bed. ",
    "guid": ""
}
omop_category_list.append(["VISIT OCCURRENCE",omop_cdm_54_category_visit_occurrence])

omop_cdm_54_category_visit_detail = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>The VISIT_DETAIL table is an optional table used to represents \
       details of each record in the parent VISIT_OCCURRENCE table. A good example of this would be the movement \
       between units in a hospital during an inpatient stay or claim lines associated with a one insurance claim. <br> \
       For every record in the VISIT_OCCURRENCE table there may be 0 or more records in the VISIT_DETAIL table \
       with a 1:n relationship where n may be 0. <br> The VISIT_DETAIL table is structurally very similar to \
       VISIT_OCCURRENCE table and belongs to the visit domain. <br> \
       <b>User Guide</b><br>\
       The configuration defining the Visit Detail is described by Concepts in the Visit Domain, which form a \
       hierarchical structure. The Visit Detail record will have an associated to the Visit Occurrence record \
       in two ways:<br>\
       1. The Visit Detail record will have the VISIT_OCCURRENCE_ID it is associated to <br>\
       2. The VISIT_DETAIL_CONCEPT_ID will be a descendant of the VISIT_CONCEPT_ID for the Visit.<br>\
       <b>ETL Conventions</b><br>\
       It is not mandatory that the VISIT_DETAIL table be filled in, but if you find that the logic to create \
       VISIT_OCCURRENCE records includes the roll-up of multiple smaller records to create one picture of a Visit \
       then it is a good idea to use VISIT_DETAIL. <br> In EHR data, for example, a Person may be in the hospital \
       but instead of one over-arching Visit their encounters are recorded as times they interacted with a health \
       care provider. A Person in the hospital interacts with multiple providers multiple times a day so the \
       encounters must be strung together using some heuristic (defined by the ETL) to identify the entire Visit. <br>\
       In this case the encounters would be considered Visit Details and the entire Visit would be the Visit Occurrence.\
       <br> In this example it is also possible to use the Vocabulary to distinguish Visit Details from a Visit \
       Occurrence by setting the VISIT_CONCEPT_ID to 9201 and the VISIT_DETAIL_CONCEPT_IDs either to 9201 or its \
       children to indicate where the patient was in the hospital at the time of care. <br>\
       As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
    "name": "OMOP CDM Visit Detail",
    "shortDescription": "The VISIT_DETAIL table is an optional table used to represents \
       details of each record in the parent VISIT_OCCURRENCE table. A good example of this would be the \
       movement between units in a hospital during an inpatient stay or claim lines associated with a one \
       insurance claim. For every record in the VISIT_OCCURRENCE table there may be 0 or more records in the \
       VISIT_DETAIL table  with a 1:n relationship where n may be 0. The VISIT_DETAIL table is structurally \
       very similar to  VISIT_OCCURRENCE table and belongs to the visit domain.",
    "guid": ""
}
omop_category_list.append(["VISIT DETAIL",omop_cdm_54_category_visit_detail])

omop_cdm_54_category_condition_occurrence = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        This table contains records of Events of a Person suggesting the presence of a disease or medical \
        condition stated as a diagnosis, a sign, or a symptom, which is either observed by a Provider or \
        reported by the patient.<br>\
        <b>User Guide</b><br>\
        Conditions are defined by Concepts from the Condition domain, which form a complex hierarchy. \
        As a result, the same Person with the same disease may have multiple Condition records, which belong \
        to the same hierarchical family. Most Condition records are mapped from diagnostic codes, \
        but recorded signs, symptoms and summary descriptions also contribute to this table. <br>\
        Rule out diagnoses should not be recorded in this table, but in reality their negating nature is \
        not always captured in the source data, and other precautions must be taken when when identifying \
        Persons who should suffer from the recorded Condition. <br>\
        Record all conditions as they exist in the source data. Any decisions about diagnosis/phenotype \
        definitions would be done through cohort specifications. These cohorts can be housed in the COHORT \
        table. Conditions span a time interval from start to end, but are typically recorded as single snapshot \
        records with no end date. The reason is twofold: (i) At the time of the recording the duration is not \
        known and later not recorded, and (ii) the Persons typically cease interacting with the healthcare \
        system when they feel better, which leads to incomplete capture of resolved Conditions. <br>\
        The CONDITION_ERA table addresses this issue. Family history and past diagnoses (‘history of’) are \
        not recorded in this table. Instead, they are listed in the OBSERVATION table. Codes written in \
        the process of establishing the diagnosis, such as ‘question of’ of and ‘rule out’, should not \
        represented here. Instead, they should be recorded in the OBSERVATION table, if they are used \
        for analyses. However, this information is not always available.<br>\
        <b>ETL Conventions</b><br>\
        Source codes and source text fields mapped to Standard Concepts of the Condition Domain have to be \
        recorded here.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
    "name": "OMOP CDM Condition Occurrence",
    "shortDescription": "This table contains records of Events of a Person suggesting the presence of a \
        disease or medical condition stated as a diagnosis, a sign, or a symptom, which is either observed \
        by a Provider or reported by the patient.",
    "guid": ""
}
omop_category_list.append(["CONDITION OCCURRENCE",omop_cdm_54_category_condition_occurrence])

omop_cdm_54_category_drug_exposure = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        This table captures records about the exposure to a Drug ingested or otherwise introduced into \
        the body. <br> A Drug is a biochemical substance formulated in such a way that when administered to \
        a Person it will exert a certain biochemical effect on the metabolism. Drugs include prescription \
        and over-the-counter medicines, vaccines, and large-molecule biologic therapies. <br> Radiological \
        devices ingested or applied locally do not count as Drugs.<br>\
        <b>User Guide</b><br>\
        The purpose of records in this table is to indicate an exposure to a certain drug as best as possible. \
        In this context a drug is defined as an active ingredient. <br> Drug Exposures are defined by Concepts \
        from the Drug domain, which form a complex hierarchy. As a result, one DRUG_SOURCE_CONCEPT_ID may map \
        to multiple standard concept ids if it is a combination product. <br>Records in this table represent \
        prescriptions written, prescriptions dispensed, and drugs administered by a provider to name a few. <br>\
        The DRUG_TYPE_CONCEPT_ID can be used to find and filter on these types. This table includes additional \
        information about the drug products, the quantity given, and route of administration.<br>\
        <b>ETL Conventions</b><br>\
        Information about quantity and dose is provided in a variety of different ways and it is important for \
        the ETL to provide as much information as possible from the data. Depending on the provenance of the \
        data fields may be captured differently i.e. quantity for drugs administered may have a separate meaning\
        from quantity for prescriptions dispensed. <br>If a patient has multiple records on the same day for the \
        same drug or procedures the ETL should not de-dupe them unless there is probable reason to believe the \
        item is a true data duplicate. <br>Take note on how to handle refills for prescriptions written.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
    "name": "OMOP CDM Drug Exposure",
    "shortDescription": "This table captures records about the exposure to a Drug ingested or otherwise introduced \
        into the body. <br> A Drug is a biochemical substance formulated in such a way that when administered to \
        a Person it will exert a certain biochemical effect on the metabolism. Drugs include prescription \
        and over-the-counter medicines, vaccines, and large-molecule biologic therapies. <br> Radiological \
        devices ingested or applied locally do not count as Drugs.",
    "guid": ""
}
omop_category_list.append(["DRUG EXPOSURE",omop_cdm_54_category_drug_exposure])

omop_cdm_54_category_procedure_occurrence = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
       This table contains records of activities or processes ordered by, or carried out by, a healthcare provider \
       on the patient with a diagnostic or therapeutic purpose.<br>\
       <b>User Guide</b><br>\
       Lab tests are not a procedure, if something is observed with an expected resulting amount and unit then \
       it should be a measurement. <br> Phlebotomy is a procedure but so trivial that it tends to be rarely \
       captured. It can be assumed that there is a phlebotomy procedure associated with many lab tests, \
       therefore it is unnecessary to add them as separate procedures. <br>If the user finds the same procedure \
       over concurrent days, it is assumed those records are part of a procedure lasting more than a day. \
       This logic is in lieu of the procedure_end_date, which will be added in a future version of the CDM.<br>\
       <b>ETL Conventions</b><br>\
       When dealing with duplicate records, the ETL must determine whether to sum them up into one record or \
       keep them separate. Things to consider are:<br>\
       - Same Procedure <br>\
       - Same PROCEDURE_DATETIME<br> \
       - Same Visit Occurrence or Visit Detail <br>\
       - Same Provider <br>\
       - Same Modifier for Procedures. <br>\
       Source codes and source text fields mapped to Standard Concepts of the Procedure Domain have to be \
       recorded here.<br>\
       As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
    "name": "OMOP CDM Procedure Occurrence",
    "shortDescription": "This table contains records of activities or processes ordered by, or carried out by, \
    a healthcare provider on the patient with a diagnostic or therapeutic purpose",
    "guid": ""
}
omop_category_list.append(["PROCEDURE OCCURRENCE",omop_cdm_54_category_procedure_occurrence])

omop_cdm_54_category_device_exposure = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The Device domain captures information about a person’s exposure to a foreign physical object or \
        instrument which is used for diagnostic or therapeutic purposes through a mechanism beyond \
        chemical action. <br> Devices include implantable objects (e.g. pacemakers, stents, artificial joints), \
        medical equipment and supplies (e.g. bandages, crutches, syringes), other instruments used in medical \
        procedures (e.g. sutures, defibrillators) and material used in clinical care (e.g. adhesives, body \
        material, dental material, surgical material).<br>\
        <b>User Guide</b><br>\
        The distinction between Devices or supplies and Procedures are sometimes blurry, but the former are \
        physical objects while the latter are actions, often to apply a Device or supply.<br>\
        <b>ETL Conventions</b><br>\
       Source codes and source text fields mapped to Standard Concepts of the Device Domain have to be recorded \
       here.<br>\
       As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
    "name": "OMOP CDM Device Exposure",
    "shortDescription": "The Device domain captures information about a person’s exposure to a foreign physical \
        object or instrument which is used for diagnostic or therapeutic purposes through a mechanism beyond \
        chemical action. Devices include implantable objects (e.g. pacemakers, stents, artificial joints), \
        medical equipment and supplies (e.g. bandages, crutches, syringes), other instruments used in medical \
        procedures (e.g. sutures, defibrillators) and material used in clinical care (e.g. adhesives, body \
        material, dental material, surgical material)",
    "guid": ""
}
omop_category_list.append(["DEVICE EXPOSURE",omop_cdm_54_category_device_exposure])

omop_cdm_54_category_measurement = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The MEASUREMENT table contains records of Measurements, i.e. structured values (numerical or categorical) \
        obtained through systematic and standardized examination or testing of a Person or Person’s sample.<br>\
        The MEASUREMENT table contains both orders and results of such Measurements as laboratory tests, \
        vital signs, quantitative findings from pathology reports, etc. <br>\
        Measurements are stored as attribute value pairs, with the attribute as the Measurement Concept \
        and the value representing the result. <br>\
        The value can be a Concept (stored in VALUE_AS_CONCEPT), or a numerical value (VALUE_AS_NUMBER) \
        with a Unit (UNIT_CONCEPT_ID). <br>The Procedure for obtaining the sample is housed in the \
        PROCEDURE_OCCURRENCE table, though it is unnecessary to create a PROCEDURE_OCCURRENCE record for \
        each measurement if one does not exist in the source data. <br>Measurements differ from Observations \
        in that they require a standardized test or some other activity to generate a quantitative or \
        qualitative result. If there is no result, it is assumed that the lab test was conducted but the \
        result was not captured.<br>\
        <b>User Guide</b><br>\
        Measurements are predominately lab tests with a few exceptions, like blood pressure or function tests. <br>\
        Results are given in the form of a value and unit combination. When investigating measurements, look for \
        operator_concept_ids (<, >, etc.).<br>\
        <b>ETL Conventions</b><br>\
        Only records where the source value maps to a Concept in the measurement domain should be included in \
        this table. Even though each Measurement always has a result, the fields VALUE_AS_NUMBER and \
        VALUE_AS_CONCEPT_ID are not mandatory as often the result is not given in the source data. <br>\
        When the result is not known, the Measurement record represents just the fact that the corresponding \
        Measurement was carried out, which in itself is already useful information for some use cases. <br>\
        For some Measurement Concepts, the result is included in the test. <br>\
        For example, ICD10 CONCEPT_ID 45548980 ‘Abnormal level of unspecified serum enzyme’ indicates a Measurement \
        and the result (abnormal). In those situations, the CONCEPT_RELATIONSHIP table in addition to the \
        ‘Maps to’ record contains a second record with the relationship_id set to ‘Maps to value’. <br>\
        In this example, the ‘Maps to’ relationship directs to 4046263 ‘Enzyme measurement’ as well as \
        a ‘Maps to value’ record to 4135493 ‘Abnormal’.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
    "name": "OMOP CDM Measurement",
    "shortDescription": "The MEASUREMENT table contains records of Measurements, i.e. structured values (numerical or\
       categorical) obtained through systematic and standardized examination or testing of a Person or Person’s sample.\
        The MEASUREMENT table contains both orders and results of such Measurements as laboratory tests, \
        vital signs, quantitative findings from pathology reports, etc.\
        Measurements are stored as attribute value pairs, with the attribute as the Measurement Concept \
        and the value representing the result. \
        The value can be a Concept (stored in VALUE_AS_CONCEPT), or a numerical value (VALUE_AS_NUMBER) \
        with a Unit (UNIT_CONCEPT_ID). The Procedure for obtaining the sample is housed in the \
        PROCEDURE_OCCURRENCE table, though it is unnecessary to create a PROCEDURE_OCCURRENCE record for \
        each measurement if one does not exist in the source data. Measurements differ from Observations \
        in that they require a standardized test or some other activity to generate a quantitative or \
        qualitative result. If there is no result, it is assumed that the lab test was conducted but the \
        result was not captured",
    "guid": ""
}
omop_category_list.append(["MEASUREMENT",omop_cdm_54_category_measurement])

omop_cdm_54_category_observation = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The OBSERVATION table captures clinical facts about a Person obtained in the context of examination, \
        questioning or a procedure. <br>\
        Any data that cannot be represented by any other domains, such as social \
        and lifestyle facts, medical history, family history, etc. are recorded here.<br>\
        <b>User Guide</b><br>\
        Observations differ from Measurements in that they do not require a standardized test or some other \
        activity to generate clinical fact. Typical observations are medical history, family history, \
        the stated need for certain treatment, social circumstances, lifestyle choices, healthcare \
        utilization patterns, etc. <br>\
        If the generation clinical facts requires a standardized testing such as lab testing or imaging and leads \
        to a standardized result, the data item is recorded in the MEASUREMENT table.<br>\
        If the clinical fact observed determines a sign, symptom, diagnosis of a disease or other medical \
        condition, it is recorded in the CONDITION_OCCURRENCE table. <br>\
        Valid Observation Concepts are not enforced to be from any domain but they must not belong to the \
        Condition, Procedure, Drug, Device, Specimen, or Measurement domains and they must be Standard Concepts.<br>\
        <br>The observation table usually records the date or datetime of when the observation was obtained, \
        not the date of the observation starting. <br>\
        For example, if the patient reports that they had a heart attack when they were 50, the observation date \
        or datetime is the date of the report, the heart attack observation can have a value_as_concept which \
        captures how long ago the observation applied to the patient.<br>\
        <b>ETL Conventions</b><br>\
        Records whose Source Values map to any domain besides Condition, Procedure, Drug, Specimen, Measurement \
        or Device should be stored in the Observation table. Observations can be stored as attribute value pairs, \
        with the attribute as the Observation Concept and the value representing the clinical fact. <br>\
        This fact can be a Concept (stored in VALUE_AS_CONCEPT), a numerical value (VALUE_AS_NUMBER), \
        a verbatim string (VALUE_AS_STRING), or a datetime (VALUE_AS_DATETIME). <br>\
        Even though Observations do not have an explicit result, the clinical fact can be stated separately from \
        the type of Observation in the VALUE_AS_* fields. <br>\
        It is recommended for Observations that are suggestive statements of positive assertion should have a \
        value of ‘Yes’ (concept_id=4188539), recorded, even though the null value is the equivalent.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Observation",
    "shortDescription": "The OBSERVATION table captures clinical facts about a Person obtained in the context of \
        examination, questioning or a procedure.\
        Any data that cannot be represented by any other domains, such as social \
        and lifestyle facts, medical history, family history, etc. are recorded here",
    "guid": ""
}
omop_category_list.append(["OBSERVATION",omop_cdm_54_category_observation])

omop_cdm_54_category_death = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The death domain contains the clinical event for how and when a Person dies. <br>\
        A person can have up to one record if the source system contains evidence about the Death, \
        such as: Condition in an administrative claim, status of enrollment into a health plan, or \
        explicit record in EHR data.<br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        For specific conventions on how to populate this table, please refer to the THEMIS repository.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Death",
    "shortDescription": "The death domain contains the clinical event for how and when a Person dies.\
        A person can have up to one record if the source system contains evidence about the Death, \
        such as: Condition in an administrative claim, status of enrollment into a health plan, or \
        explicit record in EHR data.",
    "guid": ""
}
omop_category_list.append(["DEATH",omop_cdm_54_category_death])

omop_cdm_54_category_note = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The NOTE table captures unstructured information that was recorded by a provider about a patient \
        in free text (in ASCII, or preferably in UTF8 format) notes on a given date. The type of note_text \
        is CLOB or varchar(MAX) depending on RDBMS.<br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        HL7/LOINC CDO is a standard for consistent naming of documents to support a range of use cases: \
        retrieval, organization, display, and exchange. It guides the creation of LOINC codes for clinical \
        notes. CDO annotates each document with 5 dimensions: <br><ul>\
        <li><b>Kind of Document</b>: Characterizes the general structure of the document at a macro level \
        (e.g. Anesthesia Consent)</li>\
        <il><b>Type of Service</b>: Characterizes the kind of service or activity (e.g. evaluations, \
        consultations, and summaries). The notion of time sequence, e.g., at the beginning (admission) \
        at the end (discharge) is subsumed in this axis. Example: Discharge Teaching.</il>\
        <li><b>Setting</b>: Setting is an extension of CMS’s definitions (e.g. Inpatient, Outpatient)</il>\
        <li><b>Subject Matter Domain (SMD)</b>: Characterizes the subject matter domain of a note \
        (e.g. Anesthesiology) </il>\
        <li><b>Role</b>: Characterizes the training or professional level of the author of the document, \
        but does not break down to specialty or subspecialty (e.g. Physician) Each combination of these 5 \
        dimensions rolls up to a unique LOINC code.</li></ul>\
        According to CDO requirements, only 2 of the 5 dimensions are required to properly annotate a \
        document; Kind of Document and any one of the other 4 dimensions. However, not all the permutations \
        of the CDO dimensions will necessarily yield an existing LOINC code. \
        Each of these dimensions are contained in the OMOP Vocabulary under the domain of ‘Meas Value’ \
        with each dimension represented as a Concept Class.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Note",
    "shortDescription": "The NOTE table captures unstructured information that was recorded by a provider about \
        a patient in free text (in ASCII, or preferably in UTF8 format) notes on a given date. The type of note_text \
        is CLOB or varchar(MAX) depending on RDBMS.",
    "guid": ""
}
omop_category_list.append(["NOTE",omop_cdm_54_category_note])

omop_cdm_54_category_note_nlp = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The NOTE_NLP table encodes all output of NLP on clinical notes. Each row represents a single \
        extracted term from a note.<br>\
        <b>User Guide</b><br>\
        NA<br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Note NLP",
    "shortDescription": "The NOTE_NLP table encodes all output of NLP on clinical notes. Each row represents a single \
        extracted term from a note.",
    "guid": ""
}
omop_category_list.append(["NOTE NLP",omop_cdm_54_category_note_nlp])

omop_cdm_54_category_specimen = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The specimen domain contains the records identifying biological samples from a person.<br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        Anatomic site is coded at the most specific level of granularity possible, such that higher level \
        classifications can be derived using the Standardized Vocabularies.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Specimen",
    "shortDescription": "The specimen domain contains the records identifying biological samples from a person.",
    "guid": ""
}
omop_category_list.append(["SPECIMEN",omop_cdm_54_category_specimen])

omop_cdm_54_category_fact_relationship = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The FACT_RELATIONSHIP table contains records about the relationships between facts stored as \
        records in any table of the CDM. Relationships can be defined between facts from the same domain, \
        or different domains. Examples of Fact Relationships include: <br>\
        -Person relationships (parent-child), <br>\
        -care site relationships (hierarchical organizational structure of facilities within a health system), <br>\
        -indication relationship (between drug exposures and associated conditions),<br>\
        -usage relationships (of devices during the course of an associated procedure), <br>\
        or facts derived from one another (measurements derived from an associated specimen).<br>\
        <b>User Guide</b><br>\
        NA<br>\
        <b>ETL Conventions</b><br>\
        All relationships are directional, and each relationship is represented twice symmetrically within \
        the FACT_RELATIONSHIP table. <br>\
        For example, two persons if person_id = 1 is the mother of person_id = 2 two records are in the \
        FACT_RELATIONSHIP table (all strings in fact concept_id records in the Concept table: <br>\
         - Person, 1, Person, 2, parent of <br>\
         - Person, 2, Person, 1, child of  <br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Fact Relationship",
    "shortDescription": "The FACT_RELATIONSHIP table contains records about the relationships between facts stored as \
        records in any table of the CDM. Relationships can be defined between facts from the same domain, \
        or different domains. Examples of Fact Relationships include: \
        -Person relationships (parent-child), \
        -care site relationships (hierarchical organizational structure of facilities within a health system), \
        -indication relationship (between drug exposures and associated conditions), \
        -usage relationships (of devices during the course of an associated procedure), \
        or facts derived from one another (measurements derived from an associated specimen).",
    "guid": ""
}
omop_category_list.append(["FACT RELATIONSHIP",omop_cdm_54_category_fact_relationship])

omop_cdm_54_category_location = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
    The LOCATION table represents a generic way to capture physical location or address information \
    of Persons and Care Sites. <br>\
    <b>User Guide</b><br>\
    The current iteration of the LOCATION table is US centric. Until a major release to correct this, \
    certain fields can be used to represent different international values.<br>\
    - STATE can also be used for province or district<br>\
    - ZIP is also the postal code or postcode<br>\
    - COUNTY can also be used to represent region<br><br>\
    <b>ETL Conventions</b><br>\
    Each address or Location is unique and is present only once in the table. Locations do not \
    contain names, such as the name of a hospital. In order to construct a full address that can be used \
    in the postal service, the address information from the Location needs to be combined with information \
    from the Care Site.<br>\
    As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Location",
    "shortDescription": "The LOCATION table represents a generic way to capture physical location or address \
    information of Persons and Care Sites",
    "guid": ""
}
omop_category_list.append(["LOCATION",omop_cdm_54_category_location])

omop_cdm_54_category_care_site = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
    The CARE_SITE table contains a list of uniquely identified institutional \
    (physical or organizational) units where healthcare delivery is practiced (offices, \
    wards, hospitals, clinics, etc.). <br>\
    <b>User Guide</b><br>\
    NA <br>\
    <b>ETL Conventions</b><br>\
    Care site is a unique combination of location_id and nature of the site - the latter could be the \
    place of service, name, or another characteristic in your source data. Care site does not t\
    ake into account the provider (human) information such a specialty. <br>\
    Many source data do not make a distinction between individual and institutional providers. <br>\
    The CARE_SITE table contains the institutional providers. If the source, instead of uniquely \
    identifying individual Care Sites, only provides limited information such as Place of Service, \
    generic or “pooled” Care Site records are listed in the CARE_SITE table. <br>\
    There can be hierarchical and business relationships between Care Sites. For example, wards can \
    belong to clinics or departments, which can in turn belong to hospitals, which in turn can belong \
    to hospital systems, which in turn can belong to HMOs.<br>\
    The relationships between Care Sites are defined in the FACT_RELATIONSHIP table.\
    For additional detailed conventions on how to populate this table, please refer to THEMIS repository.<br>\
    As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Care Site",
    "shortDescription": "The CARE_SITE table contains a list of uniquely identified institutional \
    (physical or organizational) units where healthcare delivery is practiced (offices, \
    wards, hospitals, clinics, etc.).",
    "guid": ""
}
omop_category_list.append(["CARE SITE",omop_cdm_54_category_care_site])

omop_cdm_54_category_provider = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
    The PROVIDER table contains a list of uniquely identified healthcare providers; \
    duplication is not allowed. These are individuals providing hands-on healthcare \
    to patients, such as physicians, nurses, midwives, physical therapists etc. <br>\
    <b>User Guide</b><br>\
    Many sources do not make a distinction between individual and institutional providers. <br>\
    The PROVIDER table contains the individual providers. If the source only provides limited information \
    such as specialty instead of uniquely identifying individual providers, generic or ‘pooled’ Provider \
    records are listed in the PROVIDER table. <br>\
    <b>ETL Conventions</b><br>\
    NA.<br>\
    As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Provider",
    "shortDescription": "The PROVIDER table contains a list of uniquely identified healthcare providers; \
    duplication is not allowed. These are individuals providing hands-on healthcare \
    to patients, such as physicians, nurses, midwives, physical therapists etc.",
    "guid": ""
}
omop_category_list.append(["PROVIDER",omop_cdm_54_category_provider])

omop_cdm_54_category_payer_plan_period = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
    The PAYER_PLAN_PERIOD table captures details of the period of time that a Person is \
    continuously enrolled under a specific health Plan benefit structure from a given Payer. \
    Each Person receiving healthcare is typically covered by a health benefit plan, \
    which pays for (fully or partially), or directly provides, the care. These benefit plans \
    are provided by payers, such as health insurances or state or government agencies. In each \
    plan the details of the health benefits are defined for the Person or her family, and the \
    health benefit Plan might change over time typically with increasing utilization (reaching \
    certain cost thresholds such as deductibles), plan availability and purchasing choices of \
    the Person. The unique combinations of Payer organizations, health benefit Plans and time \
    periods in which they are valid for a Person are recorded in this table. <br>\
    <b>User Guide</b><br>\
    A Person can have multiple, overlapping, Payer_Plan_Periods in this table. <br> \
    For example, medical and drug coverage in the US can be represented by two Payer_Plan_Periods. <br>\
    The details of the benefit structure of the Plan is rarely known, the idea is just to identify that \
    the Plans are different.<br>\
    <b>ETL Conventions</b><br>\
    NA<br>\
    As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Payer Plan Period",
    "shortDescription": "The PROVIDER table contains a list of uniquely identified healthcare providers; \
    duplication is not allowed. These are individuals providing hands-on healthcare \
    to patients, such as physicians, nurses, midwives, physical therapists etc.",
    "guid": ""
}
omop_category_list.append(["PAYER PLAN PERIOD",omop_cdm_54_category_payer_plan_period])

omop_cdm_54_category_cost = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The COST table captures records containing the cost of any medical event recorded \
        in one of the OMOP clinical event tables such as DRUG_EXPOSURE, PROCEDURE_OCCURRENCE, \
        VISIT_OCCURRENCE, VISIT_DETAIL, DEVICE_OCCURRENCE, OBSERVATION or MEASUREMENT. <br> \
        Each record in the cost table account for the amount of money transacted for the \
        clinical event. So, the COST table may be used to represent both receivables (charges) \
        and payments (paid), each transaction type represented by its COST_CONCEPT_ID. <br>\
        The COST_TYPE_CONCEPT_ID field will use concepts in the Standardized Vocabularies \
        to designate the source (provenance) of the cost data. <br>\
        A reference to the health plan information in the PAYER_PLAN_PERIOD table is stored \
        in the record for information used for the adjudication system to determine the persons \
        benefit for the clinical event. <br>\
        <b>User Guide</b><br>\
        When dealing with summary costs, the cost of the goods or services the provider provides \
        is often not known directly, but derived from the hospital charges multiplied by an average \
        cost-to-charge ratio.<br>\
        <b>ETL Conventions</b><br>\
        One cost record is generated for each response by a payer. In a claims databases, the payment \
        and payment terms reported by the payer for the goods or services billed will generate one \
        cost record. If the source data has payment information for more than one payer (i.e. primary \
        insurance and secondary insurance payment for one entity), then a cost record is created for \
        each reporting payer. <br>\
        Therefore, it is possible for one procedure to have multiple cost records for each payer, \
        but typically it contains one or no record per entity. Payer reimbursement cost records will be \
        identified by using the PAYER_PLAN_ID field. <br>\
        Drug costs are composed of ingredient cost (the amount charged by the wholesale distributor \
        or manufacturer), the dispensing fee (the amount charged by the pharmacy and the sales tax).<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Cost",
    "shortDescription": "The COST table captures records containing the cost of any medical event recorded \
        in one of the OMOP clinical event tables such as DRUG_EXPOSURE, PROCEDURE_OCCURRENCE, \
        VISIT_OCCURRENCE, VISIT_DETAIL, DEVICE_OCCURRENCE, OBSERVATION or MEASUREMENT. \
        Each record in the cost table account for the amount of money transacted for the \
        clinical event. So, the COST table may be used to represent both receivables (charges) \
        and payments (paid), each transaction type represented by its COST_CONCEPT_ID. \
        The COST_TYPE_CONCEPT_ID field will use concepts in the Standardized Vocabularies \
        to designate the source (provenance) of the cost data. \
        A reference to the health plan information in the PAYER_PLAN_PERIOD table is stored \
        in the record for information used for the adjudication system to determine the persons \
        benefit for the clinical event.",
    "guid": ""
}
omop_category_list.append(["COST",omop_cdm_54_category_cost])

omop_cdm_54_category_drug_era = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        A Drug Era is defined as a span of time when the Person is assumed to be exposed to \
        a particular active ingredient. A Drug Era is not the same as a Drug Exposure: \
        Exposures are individual records corresponding to the source when Drug was delivered \
        to the Person, while successive periods of Drug Exposures are combined under certain \
        rules to produce continuous Drug Eras. Every record in the DRUG_EXPOSURE table should \
        be part of a drug era based on the dates of exposure.<br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        The SQL script for generating DRUG_ERA records can be found here:<br>\
        https://ohdsi.github.io/CommonDataModel/sqlScripts.html#drug_eras <br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Drug Era",
    "shortDescription": "A Drug Era is defined as a span of time when the Person is assumed to be exposed to \
        a particular active ingredient. A Drug Era is not the same as a Drug Exposure: \
        Exposures are individual records corresponding to the source when Drug was delivered \
        to the Person, while successive periods of Drug Exposures are combined under certain \
        rules to produce continuous Drug Eras. Every record in the DRUG_EXPOSURE table should \
        be part of a drug era based on the dates of exposure",
    "guid": ""
}
omop_category_list.append(["DRUG ERA",omop_cdm_54_category_drug_era])

omop_cdm_54_category_dose_era = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        A Dose Era is defined as a span of time when the Person is assumed to be exposed to a \
        constant dose of a specific active ingredient. <br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        Dose Eras will be derived from records in the DRUG_EXPOSURE table and the Dose information \
        from the DRUG_STRENGTH table using a standardized algorithm. <br>\
        Dose Form information is not taken into account. So, if the patient changes between different \
        formulations, or different manufacturers with the same formulation, the Dose Era is still \
        spanning the entire time of exposure to the Ingredient. <br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Dose Era",
    "shortDescription": "A Dose Era is defined as a span of time when the Person is assumed to be exposed to a \
        constant dose of a specific active ingredient.",
    "guid": ""
}
omop_category_list.append(["DOSE ERA",omop_cdm_54_category_dose_era])

omop_cdm_54_category_condition_era = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        A Condition Era is defined as a span of time when the Person is assumed to have a \
        given condition. Similar to Drug Eras, Condition Eras are chronological periods of \
        Condition Occurrence and every Condition Occurrence record should be part of a Condition Era. \
        Combining individual Condition Occurrences into a single Condition Era serves two purposes: <br>\
        - It allows aggregation of chronic conditions that require frequent ongoing care, instead of \
        treating each Condition Occurrence as an independent event.<br>\
        - It allows aggregation of multiple, closely timed doctor visits for the same Condition to \
        avoid double-counting the Condition Occurrences. For example, consider a Person who visits \
        her Primary Care Physician (PCP) and who is referred to a specialist. At a later time, \
        the Person visits the specialist, who confirms the PCP’s original diagnosis and provides \
        the appropriate treatment to resolve the condition. These two independent doctor visits should \
        be aggregated into one Condition Era. <br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        Each Condition Era corresponds to one or many Condition Occurrence records that form a \
        continuous interval. The condition_concept_id field contains Concepts that are identical \
        to those of the CONDITION_OCCURRENCE table records that make up the Condition Era. In contrast \
        to Drug Eras, Condition Eras are not aggregated to contain Conditions of different hierarchical \
        layers. <br>\
        The SQl Script for generating CONDITION_ERA records can be found here:<br> \
        https://ohdsi.github.io/CommonDataModel/sqlScripts.html#condition_eras <br>\
        The Condition Era Start Date is the start date of the first Condition Occurrence. <br>\
        The Condition Era End Date is the end date of the last Condition Occurrence. <br>\
        Condition Eras are built with a Persistence Window of 30 days, meaning, if no occurrence \
        of the same condition_concept_id happens within 30 days of any one occurrence, \
        it will be considered the condition_era_end_date. <br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Condition Era",
    "shortDescription": "A Condition Era is defined as a span of time when the Person is assumed to have a \
        given condition. Similar to Drug Eras, Condition Eras are chronological periods of \
        Condition Occurrence and every Condition Occurrence record should be part of a Condition Era. \
        Combining individual Condition Occurrences into a single Condition Era serves two purposes: \
        - It allows aggregation of chronic conditions that require frequent ongoing care, instead of \
        treating each Condition Occurrence as an independent event.\
        - It allows aggregation of multiple, closely timed doctor visits for the same Condition to \
        avoid double-counting the Condition Occurrences. For example, consider a Person who visits \
        her Primary Care Physician (PCP) and who is referred to a specialist. At a later time, \
        the Person visits the specialist, who confirms the PCP’s original diagnosis and provides \
        the appropriate treatment to resolve the condition. These two independent doctor visits should \
        be aggregated into one Condition Era.",
    "guid": ""
}
omop_category_list.append(["CONDITION ERA",omop_cdm_54_category_condition_era])

omop_cdm_54_category_episode = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The EPISODE table aggregates lower-level clinical events (VISIT_OCCURRENCE, DRUG_EXPOSURE, \
        PROCEDURE_OCCURRENCE, DEVICE_EXPOSURE) into a higher-level abstraction representing \
        clinically and analytically relevant disease phases,outcomes and treatments. <br>\
        The EPISODE_EVENT table connects qualifying clinical events (VISIT_OCCURRENCE, \
        DRUG_EXPOSURE, PROCEDURE_OCCURRENCE, DEVICE_EXPOSURE) to the appropriate EPISODE entry. <br>\
        For example cancers including their development over time, their treatment, and final resolution. <br>\
        <b>User Guide</b><br>\
        Valid Episode Concepts belong to the ‘Episode’ domain. For cancer episodes please see [article], \
        for non-cancer episodes please see [article]. <br>\
        If your source data does not have all episodes that are relevant to the therapeutic area, \
        write only those you can easily derive from the data. <br>\
        It is understood that that table is not currently expected to be comprehensive.<br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Episode",
    "shortDescription": "The EPISODE table aggregates lower-level clinical events (VISIT_OCCURRENCE, DRUG_EXPOSURE, \
        PROCEDURE_OCCURRENCE, DEVICE_EXPOSURE) into a higher-level abstraction representing \
        clinically and analytically relevant disease phases,outcomes and treatments. <br>\
        The EPISODE_EVENT table connects qualifying clinical events (VISIT_OCCURRENCE, \
        DRUG_EXPOSURE, PROCEDURE_OCCURRENCE, DEVICE_EXPOSURE) to the appropriate EPISODE entry. <br>\
        For example cancers including their development over time, their treatment, and final resolution.",
    "guid": ""
}
omop_category_list.append(["EPISODE",omop_cdm_54_category_episode])

omop_cdm_54_category_episode_event = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The EPISODE_EVENT table connects qualifying clinical events (such as CONDITION_OCCURRENCE,\
        DRUG_EXPOSURE, PROCEDURE_OCCURRENCE, MEASUREMENT) to the appropriate EPISODE entry. <br>\
        For example, linking the precise location of the metastasis (cancer modifier in MEASUREMENT) \
        to the disease episode.<br>\
        <b>User Guide</b><br>\
        This connecting table is used instead of the FACT_RELATIONSHIP table for linking low-level \
        events to abstracted Episodes. <br>\
        <b>ETL Conventions</b><br>\
        Some episodes may not have links to any underlying clinical events. For such episodes, \
        the EPISODE_EVENT table is not populated.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Episode Event",
    "shortDescription": "The EPISODE_EVENT table connects qualifying clinical events (such as CONDITION_OCCURRENCE,\
        DRUG_EXPOSURE, PROCEDURE_OCCURRENCE, MEASUREMENT) to the appropriate EPISODE entry. \
        For example, linking the precise location of the metastasis (cancer modifier in MEASUREMENT) \
        to the disease episode.",
    "guid": ""
}
omop_category_list.append(["EPISODE EVENT",omop_cdm_54_category_episode_event])

omop_cdm_54_category_metadata = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The METADATA table contains metadata information about a dataset that has been transformed \
        to the OMOP Common Data Model.<br>\
        <b>User Guide</b><br>\
        NA<br>\
        <b>ETL Conventions</b><br>\
        NA.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Metadata",
    "shortDescription": "The METADATA table contains metadata information about a dataset that has been transformed \
        to the OMOP Common Data Model.",
    "guid": ""
}
omop_category_list.append(["METADATA",omop_cdm_54_category_metadata])

omop_cdm_54_category_cdm_source = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The CDM_SOURCE table contains detail about the source database and the process used to \
        transform the data into the OMOP Common Data Model.<br>\
        <b>User Guide</b><br>\
        NA.<br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM CDM Source",
    "shortDescription": "The CDM_SOURCE table contains detail about the source database and the process used to \
        transform the data into the OMOP Common Data Model",
    "guid": ""
}
omop_category_list.append(["CDM SOURCE",omop_cdm_54_category_cdm_source])

omop_cdm_54_category_concept = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The Standardized Vocabularies contains records, or Concepts, that uniquely identify each \
        fundamental unit of meaning used to express clinical information in all domain tables of \
        the CDM. <br>\
        Concepts are derived from vocabularies, which represent clinical information across a domain \
        (e.g. conditions, drugs, procedures) through the use of codes and associated descriptions. <br>\
        Some Concepts are designated Standard Concepts, meaning these Concepts can be used as normative \
        expressions of a clinical entity within the OMOP Common Data Model and standardized analytics. <br>\
        Each Standard Concept belongs to one Domain, which defines the location where the Concept would \
        be expected to occur within the data tables of the CDM. <br>\
        Concepts can represent broad categories (‘Cardiovascular disease’), detailed clinical elements \
        (‘Myocardial infarction of the anterolateral wall’), or modifying characteristics and attributes \
        that define Concepts at various levels of detail (severity of a disease, associated morphology\
        , etc.). <br>\
        Records in the Standardized Vocabularies tables are derived from national or international \
        vocabularies such as SNOMED-CT, RxNorm, and LOINC, or custom OMOP Concepts defined to cover \
        various aspects of observational data analysis. <br>\
        <b>User Guide</b><br>\
        The primary purpose of the CONCEPT table is to provide a standardized representation of medical \
        Concepts, allowing for consistent querying and analysis across the healthcare databases. <br>\
        Users can join the CONCEPT table with other tables in the CDM to enrich clinical data with \
        standardized Concept information or use the CONCEPT table as a reference for mapping clinical \
        data from source terminologies to Standard Concepts.<br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Concept",
    "shortDescription": "The Standardized Vocabularies contains records, or Concepts, that uniquely identify each \
        fundamental unit of meaning used to express clinical information in all domain tables of \
        the CDM. \
        Concepts are derived from vocabularies, which represent clinical information across a domain \
        (e.g. conditions, drugs, procedures) through the use of codes and associated descriptions. \
        Some Concepts are designated Standard Concepts, meaning these Concepts can be used as normative \
        expressions of a clinical entity within the OMOP Common Data Model and standardized analytics. \
        Each Standard Concept belongs to one Domain, which defines the location where the Concept would \
        be expected to occur within the data tables of the CDM. \
        Concepts can represent broad categories (‘Cardiovascular disease’), detailed clinical elements \
        (‘Myocardial infarction of the anterolateral wall’), or modifying characteristics and attributes \
        that define Concepts at various levels of detail (severity of a disease, associated morphology\
        , etc.). \
        Records in the Standardized Vocabularies tables are derived from national or international \
        vocabularies such as SNOMED-CT, RxNorm, and LOINC, or custom OMOP Concepts defined to cover \
        various aspects of observational data analysis.",
    "guid": ""
}
omop_category_list.append(["CONCEPT",omop_cdm_54_category_concept])

omop_cdm_54_category_vocabulary = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The VOCABULARY table includes a list of the Vocabularies integrated from various sources or \
        created de novo in OMOP CDM. This reference table contains a single record for each Vocabulary \
        and includes a descriptive name and other associated attributes for the Vocabulary. <br>\
        <b>User Guide</b><br>\
        The primary purpose of the VOCABULARY table is to provide explicit information about specific \
        vocabulary versions and the references to the sources from which they are asserted. <br>\
        Users can identify the version of a particular vocabulary used in the database, enabling \
        consistency and reproducibility in data analysis. <br>\
        Besides, users can check the vocabulary release version in their CDM which refers to the \
        vocabulary_id = ‘None’. <br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Vocabulary",
    "shortDescription": "The VOCABULARY table includes a list of the Vocabularies integrated from various sources or \
        created de novo in OMOP CDM. This reference table contains a single record for each Vocabulary \
        and includes a descriptive name and other associated attributes for the Vocabulary.",
    "guid": ""
}
omop_category_list.append(["VOCABULARY",omop_cdm_54_category_vocabulary])

omop_cdm_54_category_domain = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The DOMAIN table includes a list of OMOP-defined Domains to which the Concepts of the \
        Standardized Vocabularies can belong. A Domain represents a clinical definition whereby \
        we assign matching Concepts for the standardized fields in the CDM tables. <br>\
        For example, the Condition Domain contains Concepts that describe a patient condition, \
        and these Concepts can only be used in the condition_concept_id field of the \
        CONDITION_OCCURRENCE and CONDITION_ERA tables. This reference table is populated with a \
        single record for each Domain, including a Domain ID and a descriptive name for every Domain. <br>\
        <b>User Guide</b><br>\
        Users can leverage the DOMAIN table to explore the full spectrum of health-related data Domains \
        available in the Standardized Vocabularies. <br>\
        Also, the information in the DOMAIN table may be used as a reference for mapping source data to \
        OMOP domains, facilitating data harmonization and interoperability. <br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Domain",
    "shortDescription": "The DOMAIN table includes a list of OMOP-defined Domains to which the Concepts of the \
        Standardized Vocabularies can belong. A Domain represents a clinical definition whereby \
        we assign matching Concepts for the standardized fields in the CDM tables. \
        For example, the Condition Domain contains Concepts that describe a patient condition, \
        and these Concepts can only be used in the condition_concept_id field of the \
        CONDITION_OCCURRENCE and CONDITION_ERA tables. This reference table is populated with a \
        single record for each Domain, including a Domain ID and a descriptive name for every Domain.",
    "guid": ""
}
omop_category_list.append(["DOMAIN",omop_cdm_54_category_domain])

omop_cdm_54_category_concept_class = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The CONCEPT_CLASS table includes semantic categories that reference the source structure of \
        each Vocabulary. <br>\
        Concept Classes represent so-called horizontal (e.g. MedDRA, RxNorm) or vertical levels \
        (e.g. SNOMED) of the vocabulary structure. <br>\
        Vocabularies without any Concept Classes, such as HCPCS, use the vocabulary_id as the \
        Concept Class. <br>\
        This reference table is populated with a single record for each Concept Class, which includes \
        a Concept Class ID and a fully specified Concept Class name. <br>\
        <b>User Guide</b><br>\
        Users can utilize the CONCEPT_CLASS table to explore the different classes or categories of concepts \
        within the OHDSI vocabularies.<br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Concept Class",
    "shortDescription": "The CONCEPT_CLASS table includes semantic categories that reference the source structure of \
        each Vocabulary. \
        Concept Classes represent so-called horizontal (e.g. MedDRA, RxNorm) or vertical levels \
        (e.g. SNOMED) of the vocabulary structure. \
        Vocabularies without any Concept Classes, such as HCPCS, use the vocabulary_id as the \
        Concept Class. \
        This reference table is populated with a single record for each Concept Class, which includes \
        a Concept Class ID and a fully specified Concept Class name.",
    "guid": ""
}
omop_category_list.append(["CONCEPT CLASS",omop_cdm_54_category_concept_class])

omop_cdm_54_category_concept_relationship = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The CONCEPT_RELATIONSHIP table contains records that define relationships between any two \
        Concepts and the nature or type of the relationship. This table captures various types of \
        relationships, including hierarchical, associative, and other semantic connections, enabling \
        comprehensive analysis and interpretation of clinical concepts. Every kind of relationship is \
        defined in the RELATIONSHIP table.<br>\
        <b>User Guide</b><br>\
        The CONCEPT_RELATIONSHIP table can be used to explore hierarchical or attribute relationships \
        between concepts to understand the hierarchical structure of clinical concepts and uncover \
        implicit connections and associations within healthcare data. <br>\
        For example, users can utilize mapping relationships (‘Maps to’) to harmonize data from \
        different sources and terminologies, enabling interoperability and data integration across \
        disparate datasets.<br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Concept Relationship",
    "shortDescription": "The CONCEPT_RELATIONSHIP table contains records that define relationships between any two \
        Concepts and the nature or type of the relationship. This table captures various types of \
        relationships, including hierarchical, associative, and other semantic connections, enabling \
        comprehensive analysis and interpretation of clinical concepts. Every kind of relationship is \
        defined in the RELATIONSHIP table.",
    "guid": ""
}
omop_category_list.append(["CONCEPT RELATIONSHIP",omop_cdm_54_category_concept_relationship])

omop_cdm_54_category_relationship = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The RELATIONSHIP table provides a reference list of all types of relationships that can be \
        used to associate any two concepts in the CONCEPT_RELATIONSHIP table. <br>\
        <b>User Guide</b><br> \
        NA <br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Relationship",
    "shortDescription": "The RELATIONSHIP table provides a reference list of all types of relationships that can be \
        used to associate any two concepts in the CONCEPT_RELATIONSHIP table.",
    "guid": ""
}
omop_category_list.append(["RELATIONSHIP",omop_cdm_54_category_relationship])

omop_cdm_54_category_concept_synonym = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The CONCEPT_SYNONYM table is used to store alternate names and descriptions for Concepts.<br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Concept Synonym",
    "shortDescription": "The CONCEPT_SYNONYM table is used to store alternate names and descriptions for Concepts.",
    "guid": ""
}
omop_category_list.append(["CONCEPT SYNONYM",omop_cdm_54_category_concept_synonym])

omop_cdm_54_category_concept_ancestor = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The CONCEPT_ANCESTOR table is designed to simplify observational analysis by providing the \
        complete hierarchical relationships between Concepts. <br>\
        Only direct parent-child relationships between Concepts are stored in the CONCEPT_RELATIONSHIP table. <br>\
        To determine higher level ancestry connections, all individual direct relationships would have to be \
        navigated at analysis time. <br>\
        The CONCEPT_ANCESTOR table includes records for all parent-child relationships, as well as \
        grandparent-grandchild relationships and those of any other level of lineage. <br>\
        Using the CONCEPT_ANCESTOR table allows for querying for all descendants of a hierarchical concept. <br>\
        For example, drug ingredients and drug products are all descendants of a drug class ancestor.<br><br>\
        This table is entirely derived from the CONCEPT, CONCEPT_RELATIONSHIP and RELATIONSHIP tables. <br>\
        <b>User Guide</b><br>\
        NA<br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Concept Ancestor",
    "shortDescription": "The CONCEPT_ANCESTOR table is designed to simplify observational analysis by providing the \
        complete hierarchical relationships between Concepts.\
        Only direct parent-child relationships between Concepts are stored in the CONCEPT_RELATIONSHIP table. \
        To determine higher level ancestry connections, all individual direct relationships would have to be \
        navigated at analysis time. \
        The CONCEPT_ANCESTOR table includes records for all parent-child relationships, as well as \
        grandparent-grandchild relationships and those of any other level of lineage. \
        Using the CONCEPT_ANCESTOR table allows for querying for all descendants of a hierarchical concept. \
        For example, drug ingredients and drug products are all descendants of a drug class ancestor.\
        This table is entirely derived from the CONCEPT, CONCEPT_RELATIONSHIP and RELATIONSHIP tables.",
    "guid": ""
}
omop_category_list.append(["CONCEPT ANCESTOR",omop_cdm_54_category_concept_ancestor])

omop_cdm_54_category_source_to_concept_map = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The source to concept map table is recommended for use in ETL processes to maintain local \
        source codes which are not available as Concepts in the Standardized Vocabularies, and to \
        establish mappings for each source code into a Standard Concept as target_concept_ids that \
        can be used to populate the Common Data Model tables. <br>\
        The SOURCE_TO_CONCEPT_MAP table is no longer populated with content within the Standardized \
        Vocabularies published to the OMOP community. <br>\
        There are OHDSI tools to help you populate this table; <br>\
        - Usagi: https://github.com/OHDSI/Usagi <br>\
        - and Perseus: https://github.com/ohdsi/Perseus <br>\
        You can read more about OMOP vocabulary mapping in The Book of OHDSI Chapter 6.3. <br>\
        https://ohdsi.github.io/TheBookOfOhdsi/ExtractTransformLoad.html#step-2-create-the-code-mappings <br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Source to Concept Map",
    "shortDescription": "The source to concept map table is recommended for use in ETL processes to maintain local \
        source codes which are not available as Concepts in the Standardized Vocabularies, and to \
        establish mappings for each source code into a Standard Concept as target_concept_ids that \
        can be used to populate the Common Data Model tables. \
        The SOURCE_TO_CONCEPT_MAP table is no longer populated with content within the Standardized \
        Vocabularies published to the OMOP community. \
        There are OHDSI tools to help you populate this table; \
        - Usagi: https://github.com/OHDSI/Usagi \
        - and Perseus: https://github.com/ohdsi/Perseus \
        You can read more about OMOP vocabulary mapping in The Book of OHDSI Chapter 6.3. \
        https://ohdsi.github.io/TheBookOfOhdsi/ExtractTransformLoad.html#step-2-create-the-code-mappings",
    "guid": ""
}
omop_category_list.append(["SOURCE TO CONCEPT MAP",omop_cdm_54_category_source_to_concept_map])

omop_cdm_54_category_drug_strength = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The DRUG_STRENGTH table contains structured content about the amount or concentration and \
        associated units of a specific ingredient contained within a particular drug product. <br>\
        This table is supplemental information to support standardized analysis of drug utilization.<br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Drug Strength",
    "shortDescription": "The DRUG_STRENGTH table contains structured content about the amount or concentration and \
        associated units of a specific ingredient contained within a particular drug product. \
        This table is supplemental information to support standardized analysis of drug utilization.",
    "guid": ""
}
omop_category_list.append(["DRUG STRENGTH",omop_cdm_54_category_drug_strength])

omop_cdm_54_category_cohort = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The subject of a cohort can have multiple, discrete records in the cohort table per \
        cohort_definition_id, subject_id, and non-overlapping time periods. <br>\
        The definition of the cohort is contained within the COHORT_DEFINITION table. <br>\
        It is listed as part of the RESULTS schema because it is a table that users of the database \
        as well as tools such as ATLAS need to be able to write to. <br>\
        The CDM and Vocabulary tables are all read-only so it is suggested that the COHORT \
        and COHORT_DEFINTION tables are kept in a separate schema to alleviate confusion. <br>\
        <b>User Guide</b><br>\
        NA<br>\
        <b>ETL Conventions</b><br>\
        Cohorts typically include patients diagnosed with a specific condition, patients exposed to a \
        particular drug, but can also be Providers who have performed a specific Procedure. <br>\
        Cohort records must have a Start Date and an End Date, but the End Date may be set to Start Date \
        or could have an applied censor date using the Observation Period Start Date. <br>\
        Cohort records must contain a Subject Id, which can refer to the Person, Provider, Visit record \
        or Care Site though they are most often Person Ids. <br>\
        The Cohort Definition will define the type of subject through the subject concept id. <br>\
        A subject can belong (or not belong) to a cohort at any moment in time. <br>\
        A subject can only have one record in the cohort table for any moment of time, i.e. it is not \
        possible for a person to contain multiple records indicating cohort membership that are overlapping \
        in time<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Cohort",
    "shortDescription": "The subject of a cohort can have multiple, discrete records in the cohort table per \
        cohort_definition_id, subject_id, and non-overlapping time periods. \
        The definition of the cohort is contained within the COHORT_DEFINITION table. \
        It is listed as part of the RESULTS schema because it is a table that users of the database \
        as well as tools such as ATLAS need to be able to write to. \
        The CDM and Vocabulary tables are all read-only so it is suggested that the COHORT \
        and COHORT_DEFINTION tables are kept in a separate schema to alleviate confusion.",
    "guid": ""
}
omop_category_list.append(["COHORT",omop_cdm_54_category_cohort])

omop_cdm_54_category_cohort_definition = {
    "anchor": {
        "glossaryGuid": "te be replaced",
    },
    "longDescription": "<b>Table Description</b><br>\
        The COHORT_DEFINITION table contains records defining a Cohort derived from the data through \
        the associated description and syntax and upon instantiation (execution of the algorithm) placed \
        into the COHORT table. <br>\
        Cohorts are a set of subjects that satisfy a given combination of inclusion criteria for a \
        duration of time. <br>\
        The COHORT_DEFINITION table provides a standardized structure for maintaining the rules governing \
        the inclusion of a subject into a cohort, and can store operational programming code to instantiate \
        the cohort within the OMOP Common Data Model. <br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
    "name": "OMOP CDM Cohort Definition",
    "shortDescription": "The COHORT_DEFINITION table contains records defining a Cohort derived from the data through \
        the associated description and syntax and upon instantiation (execution of the algorithm) placed \
        into the COHORT table. \
        Cohorts are a set of subjects that satisfy a given combination of inclusion criteria for a \
        duration of time. \
        The COHORT_DEFINITION table provides a standardized structure for maintaining the rules governing \
        the inclusion of a subject into a cohort, and can store operational programming code to instantiate \
        the cohort within the OMOP Common Data Model.",
    "guid": ""
}
omop_category_list.append(["COHORT DEFINITION",omop_cdm_54_category_cohort_definition])








#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# TERMS
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
omop_terms_list =[]
omop_cdm_54_term_table_person = {
  "abbreviation": "OMOP Person",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
      "typeName" : atlas_OMOP_classification

  }],
  "longDescription": "This table serves as the central identity management for all Persons in the database. \
    It contains records that uniquely identify each person or patient, and some demographic information.<br>\
      <b>ETL Conventions:</b></br> \
      All Persons in a database needs one record in this table, unless they fail data quality requirements \
      specified in the ETL. Persons with no Events should have a record nonetheless. If more than one data source \
      contributes Events to the database, Persons must be reconciled, if possible, across the sources to create \
      one single record per Person. The content of the BIRTH_DATETIME must be equivalent to the content of \
      BIRTH_DAY, BIRTH_MONTH and BIRTH_YEAR. <br>\
      As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person </i>",
  "name": "OMOP Person",
  "shortDescription": "This table serves as the central identity management for all Persons in the database. \
      It contains records that uniquely identify each person or patient, and some demographic information.",
  "guid": ""
}
omop_terms_list.append(["PERSON",omop_cdm_54_term_table_person ])

omop_cdm_54_term_table_observation_period = {
  "abbreviation": "OMOP Observation Period",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
      "typeName" : atlas_OMOP_classification

  }],

  "longDescription": "This table contains records which define spans of time during which two conditions \
        are expected to hold:<br>   (i) Clinical Events that happened to the Person are recorded in the Event \
        tables, and <br>   (ii) absence of records indicate such Events did not occur during this span of time. \
        <br><b>User Guide</b><br> \
        For each Person, one or more OBSERVATION_PERIOD records may be present, but they will not overlap or be \
        back to back to each other. Events may exist outside all of the time spans of the OBSERVATION_PERIOD \
        records for a patient, however, absence of an Event outside these time spans cannot be construed as evidence\
        of absence of an Event. Incidence or prevalence rates should only be calculated for the time \
        of active OBSERVATION_PERIOD records. When constructing cohorts, outside Events can be used for \
        inclusion criteria definition, but without any guarantee for the performance of these criteria. \
        Also, OBSERVATION_PERIOD records can be as short as a single day, greatly disturbing the denominator \
        of any rate calculation as part of cohort characterizations. \
        To avoid that, apply minimal observation time as a requirement for any cohort definition.<br> \
        <b>ETL Conventions</b><br> \
        Each Person needs to have at least one OBSERVATION_PERIOD record, which should represent time intervals \
        with a high capture rate of Clinical Events. Some source data have very similar concepts, \
        such as enrollment periods in insurance claims data. In other source data such as most EHR systems \
        these time spans need to be inferred under a set of assumptions. It is the discretion of the ETL developer \
        to define these assumptions. In many ETL solutions the start date of the first occurrence or the first \
        high quality occurrence of a Clinical Event (Condition, Drug, Procedure, Device, Measurement, Visit) is \
        defined as the start of the OBSERVATION_PERIOD record, and the end date of the last occurrence of last \
        high quality occurrence of a Clinical Event, or the end of the database period becomes the end of the \
        OBSERVATOIN_PERIOD for each Person. If a Person only has a single Clinical Event the OBSERVATION_PERIOD \
        record can be as short as one day. Depending on these definitions it is possible that Clinical Events \
        fall outside the time spans defined by OBSERVATION_PERIOD records. Family history or history of Clinical \
        Events generally are not used to generate OBSERVATION_PERIOD records around the time they are referring to. \
        Any two overlapping or adjacent OBSERVATION_PERIOD records have to be merged into one.<br> \
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
  "name": "OMOP Observation Period",
  "shortDescription": "This table contains records which define spans of time during which two conditions \
        are expected to hold:<br> (i) Clinical Events that happened to the Person are recorded in the Event tables, \
        and <br>(ii) absence of records indicate such Events did not occur during this span of time.",
  "guid": ""
}
omop_terms_list.append(["OBSERVATION PERIOD",omop_cdm_54_term_table_observation_period ])

omop_cdm_54_term_table_visit_occurrence = {
  "abbreviation": "OMOP Visit Occurrence",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br> This table contains Events where Persons engage with the \
       healthcare system for a duration of time. They are often also called “Encounters”. Visits are defined \
       by a configuration of circumstances under which they occur, such as: <br>\
       (i) whether the patient comes to a healthcare institution, the other way around, or the interaction \
       is remote,<br>(ii) whether and what kind of trained medical staff is delivering the service during \
       the Visit, and <br>(iii) whether the Visit is transient or for a longer period involving a stay in bed. \
       <br><b>User Guide</b><br>The configuration defining the Visit are described by Concepts in the Visit Domain, \
       which form a hierarchical structure, but rolling up to generally familiar Visits adopted in most healthcare \
       systems worldwide: <br> <ul> \
       <li><b>Inpatient Visit:</b> Person visiting hospital, at a Care Site, in bed, for duration of more than one \
       day, with physicians and other Providers permanently available to deliver service around the clock. </li> \
       <li><b>Emergency Room Visit:</b> Person visiting dedicated healthcare institution for treating emergencies, \
       at a Care Site, within one day, with physicians and Providers permanently available to deliver service \
       around the clock. </li>\
       <li><b>Emergency Room and Inpatient Visit: </b> Person visiting ER followed by a subsequent Inpatient Visit, \
       where Emergency department is part of hospital, and transition from the ER to other hospital departments \
       is undefined. </li>\
       <li><b>Non-hospital institution Visit:</b> Person visiting dedicated institution for reasons of poor health, \
       at a Care Site, long-term or permanently, with no physician but possibly other Providers permanently available \
       to deliver service around the clock.</li>\
       <li><b>Outpatient Visit:</b> Person visiting dedicated ambulatory healthcare institution, at a Care Site, \
       within one day, without bed, with physicians or medical Providers delivering service during Visit. </li>\
       <li><b>Home Visit:</b> Provider visiting Person, without a Care Site, within one day, delivering service. </li>\
       <li><b>Telehealth Visit:</b> Patient engages with Provider through communication media. </li>\
       <li><b>Pharmacy Visit:</b> Person visiting pharmacy for dispensing of Drug, at a Care Site, within one day.</li>\
       <li><b>Laboratory Visit:</b> Patient visiting dedicated institution, at a Care Site, within one day, \
       for the purpose of a Measurement.</li>\
       <li><b>Ambulance Visit:</b> Person using transportation service for the purpose of initiating one of \
       the other Visits, without a Care Site, within one day, potentially with Providers accompanying the Visit \
       and delivering service. </li>\
       <li><b>Case Management Visit</b>: Person interacting with healthcare system, without a Care Site, \
       within a day, with no Providers involved, for administrative purposes. </li></ul>\
       The Visit duration, or ‘length of stay’, is defined as VISIT_END_DATE - VISIT_START_DATE. For all Visits \
       this is <1 day, except Inpatient Visits and Non-hospital institution Visits. \
       The CDM also contains the VISIT_DETAIL table where additional information about the Visit is stored, \
       for example, transfers between units during an inpatient Visit.\
       <br><b>ETL Conventions</b><br>\
       Visits can be derived easily if the source data contain coding systems for Place of Service or Procedures, \
       like CPT codes for well visits. In those cases, the codes can be looked up and mapped to a Standard \
       Visit Concept. Otherwise, Visit Concepts have to be identified in the ETL process. This table will contain \
       concepts in the Visit domain. These concepts are arranged in a hierarchical structure to facilitate cohort \
       definitions by rolling up to generally familiar Visits adopted in most healthcare systems worldwide. \
       Visits can be adjacent to each other, i.e. the end date of one can be identical with the start date of \
       the other. As a consequence, more than one-day Visits or their descendants can be recorded for the same \
       day. Multi-day visits must not overlap, i.e. share days other than start and end days. It is often the \
       case that some logic should be written for how to define visits and how to assign Visit_Concept_Id.<br> \
       For example, in US claims outpatient visits that appear to occur within the time period of an inpatient \
       visit can be rolled into one with the same Visit_Occurrence_Id. In EHR data inpatient visits that are \
       within one day of each other may be strung together to create one visit. It will all depend on the source \
       data and how encounter records should be translated to visit occurrences. Providers can be associated \
       with a Visit through the PROVIDER_ID field, or indirectly through PROCEDURE_OCCURRENCE records linked \
       both to the VISIT and PROVIDER tables.<br> \
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
  "name": "OMOP Visit Occurrence",
  "shortDescription": "This table contains Events where Persons engage with the \
       healthcare system for a duration of time. They are often also called “Encounters”. Visits are defined \
       by a configuration of circumstances under which they occur, such as:\
       (i) whether the patient comes to a healthcare institution, the other way around, or the interaction \
       is remote,(ii) whether and what kind of trained medical staff is delivering the service during \
       the Visit, and (iii) whether the Visit is transient or for a longer period involving a stay in bed.",
  "guid": ""
}
omop_terms_list.append(["VISIT OCCURRENCE",omop_cdm_54_term_table_visit_occurrence ])

omop_cdm_54_term_table_visit_detail = {
  "abbreviation": "OMOP Visit Detail",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>The VISIT_DETAIL table is an optional table used to represents \
    details of each record in the parent VISIT_OCCURRENCE table. A good example of this would be the movement between \
    units in a hospital during an inpatient stay or claim lines associated with a one insurance claim. <br> \
    For every record in the VISIT_OCCURRENCE table there may be 0 or more records in the VISIT_DETAIL table \
    with a 1:n relationship where n may be 0. <br> The VISIT_DETAIL table is structurally very similar to \
    VISIT_OCCURRENCE table and belongs to the visit domain. <br> \
    <b>User Guide</b><br>\
    The configuration defining the Visit Detail is described by Concepts in the Visit Domain, which form a \
    hierarchical structure. The Visit Detail record will have an associated to the Visit Occurrence record \
    in two ways:<br>\
    1. The Visit Detail record will have the VISIT_OCCURRENCE_ID it is associated to <br>\
    2. The VISIT_DETAIL_CONCEPT_ID will be a descendant of the VISIT_CONCEPT_ID for the Visit.<br>\
    <b>ETL Conventions</b><br>\
    It is not mandatory that the VISIT_DETAIL table be filled in, but if you find that the logic to create \
    VISIT_OCCURRENCE records includes the roll-up of multiple smaller records to create one picture of a Visit \
    then it is a good idea to use VISIT_DETAIL. <br> In EHR data, for example, a Person may be in the hospital \
    but instead of one over-arching Visit their encounters are recorded as times they interacted with a health \
    care provider. A Person in the hospital interacts with multiple providers multiple times a day so the \
    encounters must be strung together using some heuristic (defined by the ETL) to identify the entire Visit. <br>\
    In this case the encounters would be considered Visit Details and the entire Visit would be the Visit Occurrence.\
    <br> In this example it is also possible to use the Vocabulary to distinguish Visit Details from a Visit \
    Occurrence by setting the VISIT_CONCEPT_ID to 9201 and the VISIT_DETAIL_CONCEPT_IDs either to 9201 or its \
    children to indicate where the patient was in the hospital at the time of care. <br>\
    As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
  "name": "OMOP Visit Detail",
  "shortDescription": "The VISIT_DETAIL table is an optional table used to represents \
    details of each record in the parent VISIT_OCCURRENCE table. A good example of this would be the movement between \
    units in a hospital during an inpatient stay or claim lines associated with a one insurance claim.  \
    For every record in the VISIT_OCCURRENCE table there may be 0 or more records in the VISIT_DETAIL table \
    with a 1:n relationship where n may be 0.  The VISIT_DETAIL table is structurally very similar to \
    VISIT_OCCURRENCE table and belongs to the visit domain.",
  "guid": ""
}
omop_terms_list.append(["VISIT DETAIL",omop_cdm_54_term_table_visit_detail ])

omop_cdm_54_term_table_condition_occurrence = {
  "abbreviation": "OMOP Condition Occurrence",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        This table contains records of Events of a Person suggesting the presence of a disease or medical \
        condition stated as a diagnosis, a sign, or a symptom, which is either observed by a Provider or \
        reported by the patient.<br>\
        <b>User Guide</b><br>\
        Conditions are defined by Concepts from the Condition domain, which form a complex hierarchy. \
        As a result, the same Person with the same disease may have multiple Condition records, which belong \
        to the same hierarchical family. Most Condition records are mapped from diagnostic codes, \
        but recorded signs, symptoms and summary descriptions also contribute to this table. <br>\
        Rule out diagnoses should not be recorded in this table, but in reality their negating nature is \
        not always captured in the source data, and other precautions must be taken when when identifying \
        Persons who should suffer from the recorded Condition. <br>\
        Record all conditions as they exist in the source data. Any decisions about diagnosis/phenotype \
        definitions would be done through cohort specifications. These cohorts can be housed in the COHORT \
        table. Conditions span a time interval from start to end, but are typically recorded as single snapshot \
        records with no end date. The reason is twofold: (i) At the time of the recording the duration is not \
        known and later not recorded, and (ii) the Persons typically cease interacting with the healthcare \
        system when they feel better, which leads to incomplete capture of resolved Conditions. <br>\
        The CONDITION_ERA table addresses this issue. Family history and past diagnoses (‘history of’) are \
        not recorded in this table. Instead, they are listed in the OBSERVATION table. Codes written in \
        the process of establishing the diagnosis, such as ‘question of’ of and ‘rule out’, should not \
        represented here. Instead, they should be recorded in the OBSERVATION table, if they are used \
        for analyses. However, this information is not always available.<br>\
        <b>ETL Conventions</b><br>\
        Source codes and source text fields mapped to Standard Concepts of the Condition Domain have to be \
        recorded here.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
  "name": "OMOP Condition Occurrence",
  "shortDescription": "This table contains records of Events of a Person suggesting the presence of a \
        disease or medical condition stated as a diagnosis, a sign, or a symptom, which is either observed by a \
        Provider or reported by the patient",
  "guid": ""
}
omop_terms_list.append(["CONDITION OCCURRENCE",omop_cdm_54_term_table_condition_occurrence ])

omop_cdm_54_term_table_drug_exposure = {
  "abbreviation": "OMOP Drug Exposure",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
          This table captures records about the exposure to a Drug ingested or otherwise introduced into \
          the body. <br> A Drug is a biochemical substance formulated in such a way that when administered to \
          a Person it will exert a certain biochemical effect on the metabolism. Drugs include prescription \
          and over-the-counter medicines, vaccines, and large-molecule biologic therapies. <br> Radiological \
          devices ingested or applied locally do not count as Drugs.<br>\
          <b>User Guide</b><br>\
          The purpose of records in this table is to indicate an exposure to a certain drug as best as possible. \
          In this context a drug is defined as an active ingredient. <br> Drug Exposures are defined by Concepts \
          from the Drug domain, which form a complex hierarchy. As a result, one DRUG_SOURCE_CONCEPT_ID may map \
          to multiple standard concept ids if it is a combination product. <br>Records in this table represent \
          prescriptions written, prescriptions dispensed, and drugs administered by a provider to name a few. <br>\
          The DRUG_TYPE_CONCEPT_ID can be used to find and filter on these types. This table includes additional \
          information about the drug products, the quantity given, and route of administration.<br>\
          <b>ETL Conventions</b><br>\
          Information about quantity and dose is provided in a variety of different ways and it is important for \
          the ETL to provide as much information as possible from the data. Depending on the provenance of the \
          data fields may be captured differently i.e. quantity for drugs administered may have a separate meaning\
          from quantity for prescriptions dispensed. <br>If a patient has multiple records on the same day for the \
          same drug or procedures the ETL should not de-dupe them unless there is probable reason to believe the \
          item is a true data duplicate. <br>Take note on how to handle refills for prescriptions written.<br>\
          As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
  "name": "OMOP Drug Exposure",
  "shortDescription": "This table captures records about the exposure to a Drug ingested or otherwise introduced into \
          the body. A Drug is a biochemical substance formulated in such a way that when administered to \
          a Person it will exert a certain biochemical effect on the metabolism. Drugs include prescription \
          and over-the-counter medicines, vaccines, and large-molecule biologic therapies. Radiological \
          devices ingested or applied locally do not count as Drugs",
  "guid": ""
}
omop_terms_list.append(["DRUG EXPOSURE",omop_cdm_54_term_table_drug_exposure ])

omop_cdm_54_term_table_procedure_occurrence = {
  "abbreviation": "OMOP Procedure Occurrence",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
       This table contains records of activities or processes ordered by, or carried out by, a healthcare provider \
       on the patient with a diagnostic or therapeutic purpose.<br>\
       <b>User Guide</b><br>\
       Lab tests are not a procedure, if something is observed with an expected resulting amount and unit then \
       it should be a measurement. <br> Phlebotomy is a procedure but so trivial that it tends to be rarely \
       captured. It can be assumed that there is a phlebotomy procedure associated with many lab tests, \
       therefore it is unnecessary to add them as separate procedures. <br>If the user finds the same procedure \
       over concurrent days, it is assumed those records are part of a procedure lasting more than a day. \
       This logic is in lieu of the procedure_end_date, which will be added in a future version of the CDM.<br>\
       <b>ETL Conventions</b><br>\
       When dealing with duplicate records, the ETL must determine whether to sum them up into one record or \
       keep them separate. Things to consider are:<br>\
       - Same Procedure <br>\
       - Same PROCEDURE_DATETIME<br> \
       - Same Visit Occurrence or Visit Detail <br>\
       - Same Provider <br>\
       - Same Modifier for Procedures. <br>\
       Source codes and source text fields mapped to Standard Concepts of the Procedure Domain have to be \
       recorded here.<br>\
       As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
  "name": "OMOP Procedure Occurrence",
  "shortDescription": "This table contains records of activities or processes ordered by, or carried out by, \
       a healthcare provider on the patient with a diagnostic or therapeutic purpose",
  "guid": ""
}
omop_terms_list.append(["PROCEDURE OCCURRENCE",omop_cdm_54_term_table_procedure_occurrence])

omop_cdm_54_term_table_device_exposure = {
  "abbreviation": "OMOP Device Exposure",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The Device domain captures information about a person’s exposure to a foreign physical object or \
        instrument which is used for diagnostic or therapeutic purposes through a mechanism beyond \
        chemical action. <br> Devices include implantable objects (e.g. pacemakers, stents, artificial joints), \
        medical equipment and supplies (e.g. bandages, crutches, syringes), other instruments used in medical \
        procedures (e.g. sutures, defibrillators) and material used in clinical care (e.g. adhesives, body \
        material, dental material, surgical material).<br>\
        <b>User Guide</b><br>\
        The distinction between Devices or supplies and Procedures are sometimes blurry, but the former are \
        physical objects while the latter are actions, often to apply a Device or supply.<br>\
        <b>ETL Conventions</b><br>\
       Source codes and source text fields mapped to Standard Concepts of the Device Domain have to be recorded \
       here.<br>\
       As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
  "name": "OMOP Device Exposure",
  "shortDescription": "The Device domain captures information about a person’s exposure to a foreign physical \
        object or instrument which is used for diagnostic or therapeutic purposes through a mechanism beyond \
        chemical action. <br> Devices include implantable objects (e.g. pacemakers, stents, artificial joints), \
        medical equipment and supplies (e.g. bandages, crutches, syringes), other instruments used in medical \
        procedures (e.g. sutures, defibrillators) and material used in clinical care (e.g. adhesives, body \
        material, dental material, surgical material)",
  "guid": ""
}
omop_terms_list.append(["DEVICE EXPOSURE",omop_cdm_54_term_table_device_exposure ])

omop_cdm_54_term_table_measurement = {
  "abbreviation": "OMOP Measurement",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
    "longDescription": "<b>Table Description</b><br>\
          The MEASUREMENT table contains records of Measurements, i.e. structured values (numerical or categorical) \
          obtained through systematic and standardized examination or testing of a Person or Person’s sample.<br>\
          The MEASUREMENT table contains both orders and results of such Measurements as laboratory tests, \
          vital signs, quantitative findings from pathology reports, etc. <br>\
          Measurements are stored as attribute value pairs, with the attribute as the Measurement Concept \
          and the value representing the result. <br>\
          The value can be a Concept (stored in VALUE_AS_CONCEPT), or a numerical value (VALUE_AS_NUMBER) \
          with a Unit (UNIT_CONCEPT_ID). <br>The Procedure for obtaining the sample is housed in the \
          PROCEDURE_OCCURRENCE table, though it is unnecessary to create a PROCEDURE_OCCURRENCE record for \
          each measurement if one does not exist in the source data. <br>Measurements differ from Observations \
          in that they require a standardized test or some other activity to generate a quantitative or \
          qualitative result. If there is no result, it is assumed that the lab test was conducted but the \
          result was not captured.<br>\
          <b>User Guide</b><br>\
          Measurements are predominately lab tests with a few exceptions, like blood pressure or function tests. <br>\
          Results are given in the form of a value and unit combination. When investigating measurements, look for \
          operator_concept_ids (<, >, etc.).<br>\
          <b>ETL Conventions</b><br>\
          Only records where the source value maps to a Concept in the measurement domain should be included in \
          this table. Even though each Measurement always has a result, the fields VALUE_AS_NUMBER and \
          VALUE_AS_CONCEPT_ID are not mandatory as often the result is not given in the source data. <br>\
          When the result is not known, the Measurement record represents just the fact that the corresponding \
          Measurement was carried out, which in itself is already useful information for some use cases. <br>\
          For some Measurement Concepts, the result is included in the test. <br>\
          For example, ICD10 CONCEPT_ID 45548980 ‘Abnormal level of unspecified serum enzyme’ indicates a Measurement \
          and the result (abnormal). In those situations, the CONCEPT_RELATIONSHIP table in addition to the \
          ‘Maps to’ record contains a second record with the relationship_id set to ‘Maps to value’. <br>\
          In this example, the ‘Maps to’ relationship directs to 4046263 ‘Enzyme measurement’ as well as \
          a ‘Maps to value’ record to 4135493 ‘Abnormal’.<br>\
          As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html#person</i>",
  "name": "OMOP Measurement",
  "shortDescription": "The MEASUREMENT table contains records of Measurements, i.e. structured values (numerical or \
      categorical) obtained through systematic and standardized examination or testing of a Person or Person’s sample.\
      The MEASUREMENT table contains both orders and results of such Measurements as laboratory tests, \
      vital signs, quantitative findings from pathology reports, etc.\
      Measurements are stored as attribute value pairs, with the attribute as the Measurement Concept \
      and the value representing the result. \
      The value can be a Concept (stored in VALUE_AS_CONCEPT), or a numerical value (VALUE_AS_NUMBER) \
      with a Unit (UNIT_CONCEPT_ID). The Procedure for obtaining the sample is housed in the \
      PROCEDURE_OCCURRENCE table, though it is unnecessary to create a PROCEDURE_OCCURRENCE record for \
      each measurement if one does not exist in the source data. Measurements differ from Observations \
      in that they require a standardized test or some other activity to generate a quantitative or \
      qualitative result. If there is no result, it is assumed that the lab test was conducted but the \
      result was not captured.",
  "guid": ""
}
omop_terms_list.append(["MEASUREMENT",omop_cdm_54_term_table_measurement ])

omop_cdm_54_term_table_observation = {
  "abbreviation": "OMOP Observation",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The OBSERVATION table captures clinical facts about a Person obtained in the context of examination, \
        questioning or a procedure. <br>\
        Any data that cannot be represented by any other domains, such as social \
        and lifestyle facts, medical history, family history, etc. are recorded here.<br>\
        <b>User Guide</b><br>\
        Observations differ from Measurements in that they do not require a standardized test or some other \
        activity to generate clinical fact. Typical observations are medical history, family history, \
        the stated need for certain treatment, social circumstances, lifestyle choices, healthcare \
        utilization patterns, etc. <br>\
        If the generation clinical facts requires a standardized testing such as lab testing or imaging and leads \
        to a standardized result, the data item is recorded in the MEASUREMENT table.<br>\
        If the clinical fact observed determines a sign, symptom, diagnosis of a disease or other medical \
        condition, it is recorded in the CONDITION_OCCURRENCE table. <br>\
        Valid Observation Concepts are not enforced to be from any domain but they must not belong to the \
        Condition, Procedure, Drug, Device, Specimen, or Measurement domains and they must be Standard Concepts.<br>\
        <br>The observation table usually records the date or datetime of when the observation was obtained, \
        not the date of the observation starting. <br>\
        For example, if the patient reports that they had a heart attack when they were 50, the observation date \
        or datetime is the date of the report, the heart attack observation can have a value_as_concept which \
        captures how long ago the observation applied to the patient.<br>\
        <b>ETL Conventions</b><br>\
        Records whose Source Values map to any domain besides Condition, Procedure, Drug, Specimen, Measurement \
        or Device should be stored in the Observation table. Observations can be stored as attribute value pairs, \
        with the attribute as the Observation Concept and the value representing the clinical fact. <br>\
        This fact can be a Concept (stored in VALUE_AS_CONCEPT), a numerical value (VALUE_AS_NUMBER), \
        a verbatim string (VALUE_AS_STRING), or a datetime (VALUE_AS_DATETIME). <br>\
        Even though Observations do not have an explicit result, the clinical fact can be stated separately from \
        the type of Observation in the VALUE_AS_* fields. <br>\
        It is recommended for Observations that are suggestive statements of positive assertion should have a \
        value of ‘Yes’ (concept_id=4188539), recorded, even though the null value is the equivalent.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Observation",
  "shortDescription": "The OBSERVATION table captures clinical facts about a Person obtained in the context of \
      examination, questioning or a procedure. \
      Any data that cannot be represented by any other domains, such as social \
      and lifestyle facts, medical history, family history, etc. are recorded here.",
  "guid": ""
}
omop_terms_list.append(["OBSERVATION",omop_cdm_54_term_table_observation])

omop_cdm_54_term_table_death = {
  "abbreviation": "OMOP Death",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The death domain contains the clinical event for how and when a Person dies. <br>\
        A person can have up to one record if the source system contains evidence about the Death, \
        such as: Condition in an administrative claim, status of enrollment into a health plan, or \
        explicit record in EHR data.<br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        For specific conventions on how to populate this table, please refer to the THEMIS repository.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Death",
  "shortDescription": "The death domain contains the clinical event for how and when a Person dies. \
        A person can have up to one record if the source system contains evidence about the Death, \
        such as: Condition in an administrative claim, status of enrollment into a health plan, or \
        explicit record in EHR data.",
  "guid": ""
}
omop_terms_list.append(["DEATH",omop_cdm_54_term_table_death])

omop_cdm_54_term_table_note = {
  "abbreviation": "OMOP Note",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The NOTE table captures unstructured information that was recorded by a provider about a patient \
        in free text (in ASCII, or preferably in UTF8 format) notes on a given date. The type of note_text \
        is CLOB or varchar(MAX) depending on RDBMS.<br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        HL7/LOINC CDO is a standard for consistent naming of documents to support a range of use cases: \
        retrieval, organization, display, and exchange. It guides the creation of LOINC codes for clinical \
        notes. CDO annotates each document with 5 dimensions: <br><ul>\
        <li><b>Kind of Document</b>: Characterizes the general structure of the document at a macro level \
        (e.g. Anesthesia Consent)</li>\
        <il><b>Type of Service</b>: Characterizes the kind of service or activity (e.g. evaluations, \
        consultations, and summaries). The notion of time sequence, e.g., at the beginning (admission) \
        at the end (discharge) is subsumed in this axis. Example: Discharge Teaching.</il>\
        <li><b>Setting</b>: Setting is an extension of CMS’s definitions (e.g. Inpatient, Outpatient)</il>\
        <li><b>Subject Matter Domain (SMD)</b>: Characterizes the subject matter domain of a note \
        (e.g. Anesthesiology) </il>\
        <li><b>Role</b>: Characterizes the training or professional level of the author of the document, \
        but does not break down to specialty or subspecialty (e.g. Physician) Each combination of these 5 \
        dimensions rolls up to a unique LOINC code.</li></ul>\
        According to CDO requirements, only 2 of the 5 dimensions are required to properly annotate a \
        document; Kind of Document and any one of the other 4 dimensions. However, not all the permutations \
        of the CDO dimensions will necessarily yield an existing LOINC code. \
        Each of these dimensions are contained in the OMOP Vocabulary under the domain of ‘Meas Value’ \
        with each dimension represented as a Concept Class.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Note",
  "shortDescription": "The NOTE table captures unstructured information that was recorded by a provider about a \
        patient in free text (in ASCII, or preferably in UTF8 format) notes on a given date. The type of note_text \
        is CLOB or varchar(MAX) depending on RDBMS",
  "guid": ""
}
omop_terms_list.append(["NOTE",omop_cdm_54_term_table_note])

omop_cdm_54_term_table_note_nlp = {
  "abbreviation": "OMOP Note NLP",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The NOTE_NLP table encodes all output of NLP on clinical notes. Each row represents a single \
        extracted term from a note.<br>\
        <b>User Guide</b><br>\
        NA<br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Note NLP",
  "shortDescription": "The NOTE_NLP table encodes all output of NLP on clinical notes. Each row represents a single \
        extracted term from a note.",
  "guid": ""
}
omop_terms_list.append(["NOTE NLP",omop_cdm_54_term_table_note_nlp])

omop_cdm_54_term_table_specimen = {
  "abbreviation": "OMOP Specimen",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The specimen domain contains the records identifying biological samples from a person.<br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        Anatomic site is coded at the most specific level of granularity possible, such that higher level \
        classifications can be derived using the Standardized Vocabularies.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Specimen",
  "shortDescription": "The specimen domain contains the records identifying biological samples from a person.",
  "guid": ""
}
omop_terms_list.append(["SPECIMEN",omop_cdm_54_term_table_specimen])

omop_cdm_54_term_table_fact_relationship = {
  "abbreviation": "OMOP Fact Relationship",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The FACT_RELATIONSHIP table contains records about the relationships between facts stored as \
        records in any table of the CDM. Relationships can be defined between facts from the same domain, \
        or different domains. Examples of Fact Relationships include: <br>\
        -Person relationships (parent-child), <br>\
        -care site relationships (hierarchical organizational structure of facilities within a health system), <br>\
        -indication relationship (between drug exposures and associated conditions), <br>\
        -usage relationships (of devices during the course of an associated procedure), <br>\
        or facts derived from one another (measurements derived from an associated specimen).<br>\
        <b>User Guide</b><br>\
        NA<br>\
        <b>ETL Conventions</b><br>\
        All relationships are directional, and each relationship is represented twice symmetrically within \
        the FACT_RELATIONSHIP table. <br>\
        For example, two persons if person_id = 1 is the mother of person_id = 2 two records are in the \
        FACT_RELATIONSHIP table (all strings in fact concept_id records in the Concept table: <br>\
         - Person, 1, Person, 2, parent of <br>\
         - Person, 2, Person, 1, child of  <br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Fact Relationship",
  "shortDescription": "The FACT_RELATIONSHIP table contains records about the relationships between facts stored as \
        records in any table of the CDM. Relationships can be defined between facts from the same domain, \
        or different domains. Examples of Fact Relationships include: \
        -Person relationships (parent-child), \
        -care site relationships (hierarchical organizational structure of facilities within a health system), \
        -indication relationship (between drug exposures and associated conditions),\
        -usage relationships (of devices during the course of an associated procedure), \
        or facts derived from one another (measurements derived from an associated specimen).",
  "guid": ""
}
omop_terms_list.append(["FACT RELATIONSHIP",omop_cdm_54_term_table_fact_relationship])

omop_cdm_54_term_table_location = {
  "abbreviation": "OMOP Location",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
    The LOCATION table represents a generic way to capture physical location or address information \
    of Persons and Care Sites. <br>\
    <b>User Guide</b><br>\
    The current iteration of the LOCATION table is US centric. Until a major release to correct this, \
    certain fields can be used to represent different international values.<br>\
    - STATE can also be used for province or district<br>\
    - ZIP is also the postal code or postcode<br>\
    - COUNTY can also be used to represent region<br><br>\
    <b>ETL Conventions</b><br>\
    Each address or Location is unique and is present only once in the table. Locations do not \
    contain names, such as the name of a hospital. In order to construct a full address that can be used \
    in the postal service, the address information from the Location needs to be combined with information \
    from the Care Site.<br>\
    As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Location",
  "shortDescription": "The LOCATION table represents a generic way to capture physical location or address information \
    of Persons and Care Sites.",
  "guid": ""
}
omop_terms_list.append(["LOCATION",omop_cdm_54_term_table_location])

omop_cdm_54_term_table_care_site = {
  "abbreviation": "OMOP Care Site",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "longDescription": "<b>Table Description</b><br>\
The CARE_SITE table contains a list of uniquely identified institutional \
(physical or organizational) units where healthcare delivery is practiced (offices, \
wards, hospitals, clinics, etc.). <br>\
<b>User Guide</b><br>\
NA <br>\
<b>ETL Conventions</b><br>\
Care site is a unique combination of location_id and nature of the site - the latter could be the \
place of service, name, or another characteristic in your source data. Care site does not t\
ake into account the provider (human) information such a specialty. <br>\
Many source data do not make a distinction between individual and institutional providers. <br>\
The CARE_SITE table contains the institutional providers. If the source, instead of uniquely \
identifying individual Care Sites, only provides limited information such as Place of Service, \
generic or “pooled” Care Site records are listed in the CARE_SITE table. <br>\
There can be hierarchical and business relationships between Care Sites. For example, wards can \
belong to clinics or departments, which can in turn belong to hospitals, which in turn can belong \
to hospital systems, which in turn can belong to HMOs.<br>\
The relationships between Care Sites are defined in the FACT_RELATIONSHIP table.\
For additional detailed conventions on how to populate this table, please refer to THEMIS repository.<br>\
As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Care Site",
  "shortDescription": "The CARE_SITE table contains a list of uniquely identified institutional \
(physical or organizational) units where healthcare delivery is practiced (offices, \
wards, hospitals, clinics, etc.)",
  "guid": ""
}
omop_terms_list.append(["CARE SITE",omop_cdm_54_term_table_care_site])

omop_cdm_54_term_table_provider = {
  "abbreviation": "OMOP Provider",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
    The PROVIDER table contains a list of uniquely identified healthcare providers; \
    duplication is not allowed. These are individuals providing hands-on healthcare \
    to patients, such as physicians, nurses, midwives, physical therapists etc. <br>\
    <b>User Guide</b><br>\
    Many sources do not make a distinction between individual and institutional providers. <br>\
    The PROVIDER table contains the individual providers. If the source only provides limited information \
    such as specialty instead of uniquely identifying individual providers, generic or ‘pooled’ Provider \
    records are listed in the PROVIDER table. <br>\
    <b>ETL Conventions</b><br>\
    NA.<br>\
    As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",

   "name": "OMOP Provider",
   "shortDescription": "The PROVIDER table contains a list of uniquely identified healthcare providers; \
    duplication is not allowed. These are individuals providing hands-on healthcare \
    to patients, such as physicians, nurses, midwives, physical therapists etc.",
   "guid": ""
}
omop_terms_list.append(["PROVIDER",omop_cdm_54_term_table_provider])

omop_cdm_54_term_table_payer_plan_period = {
  "abbreviation": "OMOP Payer Plan Period",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The PAYER_PLAN_PERIOD table captures details of the period of time that a Person is \
        continuously enrolled under a specific health Plan benefit structure from a given Payer. \
        <br>Each Person receiving healthcare is typically covered by a health benefit plan, \
        which pays for (fully or partially), or directly provides, the care. <br>These benefit plans \
        are provided by payers, such as health insurances or state or government agencies. In each \
        plan the details of the health benefits are defined for the Person or her family, and the \
        health benefit Plan might change over time typically with increasing utilization (reaching \
        certain cost thresholds such as deductibles), plan availability and purchasing choices of \
        the Person. <br>The unique combinations of Payer organizations, health benefit Plans and time \
        periods in which they are valid for a Person are recorded in this table. <br>\
        <b>User Guide</b><br>\
        A Person can have multiple, overlapping, Payer_Plan_Periods in this table. <br> \
        For example, medical and drug coverage in the US can be represented by two Payer_Plan_Periods. <br>\
        The details of the benefit structure of the Plan is rarely known, the idea is just to identify that \
        the Plans are different.<br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
   "name": "OMOP Payer Plan Period",
   "shortDescription": "The PAYER_PLAN_PERIOD table captures details of the period of time that a Person is \
        continuously enrolled under a specific health Plan benefit structure from a given Payer. \
        Each Person receiving healthcare is typically covered by a health benefit plan, \
        which pays for (fully or partially), or directly provides, the care. These benefit plans \
        are provided by payers, such as health insurances or state or government agencies. In each \
        plan the details of the health benefits are defined for the Person or her family, and the \
        health benefit Plan might change over time typically with increasing utilization (reaching \
        certain cost thresholds such as deductibles), plan availability and purchasing choices of \
        the Person. The unique combinations of Payer organizations, health benefit Plans and time \
        periods in which they are valid for a Person are recorded in this table.",
   "guid": ""
}
omop_terms_list.append(["PAYER PLAN PERIOD",omop_cdm_54_term_table_payer_plan_period])

omop_cdm_54_term_table_cost = {
  "abbreviation": "OMOP Cost",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The COST table captures records containing the cost of any medical event recorded \
        in one of the OMOP clinical event tables such as DRUG_EXPOSURE, PROCEDURE_OCCURRENCE, \
        VISIT_OCCURRENCE, VISIT_DETAIL, DEVICE_OCCURRENCE, OBSERVATION or MEASUREMENT. <br> \
        Each record in the cost table account for the amount of money transacted for the \
        clinical event. So, the COST table may be used to represent both receivables (charges) \
        and payments (paid), each transaction type represented by its COST_CONCEPT_ID. <br>\
        The COST_TYPE_CONCEPT_ID field will use concepts in the Standardized Vocabularies \
        to designate the source (provenance) of the cost data. <br>\
        A reference to the health plan information in the PAYER_PLAN_PERIOD table is stored \
        in the record for information used for the adjudication system to determine the persons \
        benefit for the clinical event. <br>\
        <b>User Guide</b><br>\
        When dealing with summary costs, the cost of the goods or services the provider provides \
        is often not known directly, but derived from the hospital charges multiplied by an average \
        cost-to-charge ratio.<br>\
        <b>ETL Conventions</b><br>\
        One cost record is generated for each response by a payer. In a claims databases, the payment \
        and payment terms reported by the payer for the goods or services billed will generate one \
        cost record. If the source data has payment information for more than one payer (i.e. primary \
        insurance and secondary insurance payment for one entity), then a cost record is created for \
        each reporting payer. <br>\
        Therefore, it is possible for one procedure to have multiple cost records for each payer, \
        but typically it contains one or no record per entity. Payer reimbursement cost records will be \
        identified by using the PAYER_PLAN_ID field. <br>\
        Drug costs are composed of ingredient cost (the amount charged by the wholesale distributor \
        or manufacturer), the dispensing fee (the amount charged by the pharmacy and the sales tax).<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
   "name": "OMOP Cost",
   "shortDescription": "The COST table captures records containing the cost of any medical event recorded \
        in one of the OMOP clinical event tables such as DRUG_EXPOSURE, PROCEDURE_OCCURRENCE, \
        VISIT_OCCURRENCE, VISIT_DETAIL, DEVICE_OCCURRENCE, OBSERVATION or MEASUREMENT. \
        Each record in the cost table account for the amount of money transacted for the \
        clinical event. So, the COST table may be used to represent both receivables (charges) \
        and payments (paid), each transaction type represented by its COST_CONCEPT_ID. \
        The COST_TYPE_CONCEPT_ID field will use concepts in the Standardized Vocabularies \
        to designate the source (provenance) of the cost data. \
        A reference to the health plan information in the PAYER_PLAN_PERIOD table is stored \
        in the record for information used for the adjudication system to determine the persons \
        benefit for the clinical event",
   "guid": ""
}
omop_terms_list.append(["COST",omop_cdm_54_term_table_cost])

omop_cdm_54_term_table_drug_era = {
  "abbreviation": "OMOP Drug Era",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        A Drug Era is defined as a span of time when the Person is assumed to be exposed to \
        a particular active ingredient. A Drug Era is not the same as a Drug Exposure: \
        Exposures are individual records corresponding to the source when Drug was delivered \
        to the Person, while successive periods of Drug Exposures are combined under certain \
        rules to produce continuous Drug Eras. Every record in the DRUG_EXPOSURE table should \
        be part of a drug era based on the dates of exposure.<br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        The SQL script for generating DRUG_ERA records can be found here:<br>\
        https://ohdsi.github.io/CommonDataModel/sqlScripts.html#drug_eras <br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
   "name": "OMOP Drug Era",
   "shortDescription": "A Drug Era is defined as a span of time when the Person is assumed to be exposed to \
        a particular active ingredient. A Drug Era is not the same as a Drug Exposure: \
        Exposures are individual records corresponding to the source when Drug was delivered \
        to the Person, while successive periods of Drug Exposures are combined under certain \
        rules to produce continuous Drug Eras. Every record in the DRUG_EXPOSURE table should \
        be part of a drug era based on the dates of exposure",
   "guid": ""
}
omop_terms_list.append(["DRUG ERA",omop_cdm_54_term_table_drug_era])

omop_cdm_54_term_table_dose_era = {
  "abbreviation": "OMOP Dose Era",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        A Dose Era is defined as a span of time when the Person is assumed to be exposed to a \
        constant dose of a specific active ingredient. <br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        Dose Eras will be derived from records in the DRUG_EXPOSURE table and the Dose information \
        from the DRUG_STRENGTH table using a standardized algorithm. <br>\
        Dose Form information is not taken into account. So, if the patient changes between different \
        formulations, or different manufacturers with the same formulation, the Dose Era is still \
        spanning the entire time of exposure to the Ingredient. <br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
   "name": "OMOP Dose Era",
   "shortDescription": "A Dose Era is defined as a span of time when the Person is assumed to be exposed to a \
        constant dose of a specific active ingredient.",
   "guid": ""
}
omop_terms_list.append(["DOSE ERA",omop_cdm_54_term_table_dose_era])

omop_cdm_54_term_table_condition_era = {
  "abbreviation": "OMOP Condition Era",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        A Condition Era is defined as a span of time when the Person is assumed to have a \
        given condition. Similar to Drug Eras, Condition Eras are chronological periods of \
        Condition Occurrence and every Condition Occurrence record should be part of a Condition Era. \
        Combining individual Condition Occurrences into a single Condition Era serves two purposes: <br>\
        - It allows aggregation of chronic conditions that require frequent ongoing care, instead of \
        treating each Condition Occurrence as an independent event.<br>\
        - It allows aggregation of multiple, closely timed doctor visits for the same Condition to \
        avoid double-counting the Condition Occurrences. For example, consider a Person who visits \
        her Primary Care Physician (PCP) and who is referred to a specialist. At a later time, \
        the Person visits the specialist, who confirms the PCP’s original diagnosis and provides \
        the appropriate treatment to resolve the condition. These two independent doctor visits should \
        be aggregated into one Condition Era. <br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        Each Condition Era corresponds to one or many Condition Occurrence records that form a \
        continuous interval. The condition_concept_id field contains Concepts that are identical \
        to those of the CONDITION_OCCURRENCE table records that make up the Condition Era. In contrast \
        to Drug Eras, Condition Eras are not aggregated to contain Conditions of different hierarchical \
        layers. <br>\
        The SQl Script for generating CONDITION_ERA records can be found here:<br> \
        https://ohdsi.github.io/CommonDataModel/sqlScripts.html#condition_eras <br>\
        The Condition Era Start Date is the start date of the first Condition Occurrence. <br>\
        The Condition Era End Date is the end date of the last Condition Occurrence. <br>\
        Condition Eras are built with a Persistence Window of 30 days, meaning, if no occurrence \
        of the same condition_concept_id happens within 30 days of any one occurrence, \
        it will be considered the condition_era_end_date. <br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Condition Era",
  "shortDescription": "A Condition Era is defined as a span of time when the Person is assumed to have a \
        given condition. Similar to Drug Eras, Condition Eras are chronological periods of \
        Condition Occurrence and every Condition Occurrence record should be part of a Condition Era. \
        Combining individual Condition Occurrences into a single Condition Era serves two purposes: \
        - It allows aggregation of chronic conditions that require frequent ongoing care, instead of \
        treating each Condition Occurrence as an independent event.\
        - It allows aggregation of multiple, closely timed doctor visits for the same Condition to \
        avoid double-counting the Condition Occurrences. For example, consider a Person who visits \
        her Primary Care Physician (PCP) and who is referred to a specialist. At a later time, \
        the Person visits the specialist, who confirms the PCP’s original diagnosis and provides \
        the appropriate treatment to resolve the condition. These two independent doctor visits should \
        be aggregated into one Condition Era.",
   "guid": ""
}
omop_terms_list.append(["CONDITION ERA",omop_cdm_54_term_table_condition_era])

omop_cdm_54_term_table_episode = {
  "abbreviation": "OMOP Episode",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
      The EPISODE table aggregates lower-level clinical events (VISIT_OCCURRENCE, DRUG_EXPOSURE, \
      PROCEDURE_OCCURRENCE, DEVICE_EXPOSURE) into a higher-level abstraction representing \
      clinically and analytically relevant disease phases,outcomes and treatments. <br>\
      The EPISODE_EVENT table connects qualifying clinical events (VISIT_OCCURRENCE, \
      DRUG_EXPOSURE, PROCEDURE_OCCURRENCE, DEVICE_EXPOSURE) to the appropriate EPISODE entry. <br>\
      For example cancers including their development over time, their treatment, and final resolution. <br>\
      <b>User Guide</b><br>\
      Valid Episode Concepts belong to the ‘Episode’ domain. For cancer episodes please see [article], \
      for non-cancer episodes please see [article]. <br>\
      If your source data does not have all episodes that are relevant to the therapeutic area, \
      write only those you can easily derive from the data. <br>\
      It is understood that that table is not currently expected to be comprehensive.<br>\
      <b>ETL Conventions</b><br>\
      NA<br>\
      As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Episode",
  "shortDescription": "The EPISODE table aggregates lower-level clinical events (VISIT_OCCURRENCE, DRUG_EXPOSURE, \
        PROCEDURE_OCCURRENCE, DEVICE_EXPOSURE) into a higher-level abstraction representing \
        clinically and analytically relevant disease phases,outcomes and treatments. <br>\
        The EPISODE_EVENT table connects qualifying clinical events (VISIT_OCCURRENCE, \
        DRUG_EXPOSURE, PROCEDURE_OCCURRENCE, DEVICE_EXPOSURE) to the appropriate EPISODE entry. <br>\
        For example cancers including their development over time, their treatment, and final resolution.",
   "guid": ""
}
omop_terms_list.append(["EPISODE",omop_cdm_54_term_table_episode])

omop_cdm_54_term_table_episode_event = {
  "abbreviation": "OMOP Episode Event",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The EPISODE_EVENT table connects qualifying clinical events (such as CONDITION_OCCURRENCE,\
        DRUG_EXPOSURE, PROCEDURE_OCCURRENCE, MEASUREMENT) to the appropriate EPISODE entry. <br>\
        For example, linking the precise location of the metastasis (cancer modifier in MEASUREMENT) \
        to the disease episode.<br>\
        <b>User Guide</b><br>\
        This connecting table is used instead of the FACT_RELATIONSHIP table for linking low-level \
        events to abstracted Episodes. <br>\
        <b>ETL Conventions</b><br>\
        Some episodes may not have links to any underlying clinical events. For such episodes, \
        the EPISODE_EVENT table is not populated.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Episode Event",
  "shortDescription": "The EPISODE_EVENT table connects qualifying clinical events (such as CONDITION_OCCURRENCE,\
        DRUG_EXPOSURE, PROCEDURE_OCCURRENCE, MEASUREMENT) to the appropriate EPISODE entry. \
        For example, linking the precise location of the metastasis (cancer modifier in MEASUREMENT) \
        to the disease episode.",
   "guid": ""
}
omop_terms_list.append(["EPISODE EVENT",omop_cdm_54_term_table_episode_event])

omop_cdm_54_term_table_metadata = {
  "abbreviation": "OMOP Metadata",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The METADATA table contains metadata information about a dataset that has been transformed \
        to the OMOP Common Data Model.<br>\
        <b>User Guide</b><br>\
        NA<br>\
        <b>ETL Conventions</b><br>\
        NA.<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Metadata",
  "shortDescription": "The METADATA table contains metadata information about a dataset that has been transformed \
        to the OMOP Common Data Model.",
   "guid": ""
}
omop_terms_list.append(["METADATA",omop_cdm_54_term_table_metadata])

omop_cdm_54_term_table_cdm_source = {
  "abbreviation": "OMOP CDM Source",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The CDM_SOURCE table contains detail about the source database and the process used to \
        transform the data into the OMOP Common Data Model.<br>\
        <b>User Guide</b><br>\
        NA.<br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP CDM Source",
  "shortDescription": "The CDM_SOURCE table contains detail about the source database and the process used to \
        transform the data into the OMOP Common Data Model.",
   "guid": ""
}
omop_terms_list.append(["CDM SOURCE",omop_cdm_54_term_table_cdm_source])

omop_cdm_54_term_table_concept = {
  "abbreviation": "OMOP Concept",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The Standardized Vocabularies contains records, or Concepts, that uniquely identify each \
        fundamental unit of meaning used to express clinical information in all domain tables of \
        the CDM. <br>\
        Concepts are derived from vocabularies, which represent clinical information across a domain \
        (e.g. conditions, drugs, procedures) through the use of codes and associated descriptions. <br>\
        Some Concepts are designated Standard Concepts, meaning these Concepts can be used as normative \
        expressions of a clinical entity within the OMOP Common Data Model and standardized analytics. <br>\
        Each Standard Concept belongs to one Domain, which defines the location where the Concept would \
        be expected to occur within the data tables of the CDM. <br>\
        Concepts can represent broad categories (‘Cardiovascular disease’), detailed clinical elements \
        (‘Myocardial infarction of the anterolateral wall’), or modifying characteristics and attributes \
        that define Concepts at various levels of detail (severity of a disease, associated morphology\
        , etc.). <br>\
        Records in the Standardized Vocabularies tables are derived from national or international \
        vocabularies such as SNOMED-CT, RxNorm, and LOINC, or custom OMOP Concepts defined to cover \
        various aspects of observational data analysis. <br>\
        <b>User Guide</b><br>\
        The primary purpose of the CONCEPT table is to provide a standardized representation of medical \
        Concepts, allowing for consistent querying and analysis across the healthcare databases. <br>\
        Users can join the CONCEPT table with other tables in the CDM to enrich clinical data with \
        standardized Concept information or use the CONCEPT table as a reference for mapping clinical \
        data from source terminologies to Standard Concepts.<br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Concept",
  "shortDescription": "The Standardized Vocabularies contains records, or Concepts, that uniquely identify each \
        fundamental unit of meaning used to express clinical information in all domain tables of \
        the CDM. \
        Concepts are derived from vocabularies, which represent clinical information across a domain \
        (e.g. conditions, drugs, procedures) through the use of codes and associated descriptions. \
        Some Concepts are designated Standard Concepts, meaning these Concepts can be used as normative \
        expressions of a clinical entity within the OMOP Common Data Model and standardized analytics. \
        Each Standard Concept belongs to one Domain, which defines the location where the Concept would \
        be expected to occur within the data tables of the CDM. \
        Concepts can represent broad categories (‘Cardiovascular disease’), detailed clinical elements \
        (‘Myocardial infarction of the anterolateral wall’), or modifying characteristics and attributes \
        that define Concepts at various levels of detail (severity of a disease, associated morphology\
        , etc.). \
        Records in the Standardized Vocabularies tables are derived from national or international \
        vocabularies such as SNOMED-CT, RxNorm, and LOINC, or custom OMOP Concepts defined to cover \
        various aspects of observational data analysis.",
   "guid": ""
}
omop_terms_list.append(["CONCEPT",omop_cdm_54_term_table_concept])

omop_cdm_54_term_table_vocabulary = {
  "abbreviation": "OMOP Vocabulary",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The VOCABULARY table includes a list of the Vocabularies integrated from various sources or \
        created de novo in OMOP CDM. This reference table contains a single record for each Vocabulary \
        and includes a descriptive name and other associated attributes for the Vocabulary. <br>\
        <b>User Guide</b><br>\
        The primary purpose of the VOCABULARY table is to provide explicit information about specific \
        vocabulary versions and the references to the sources from which they are asserted. <br>\
        Users can identify the version of a particular vocabulary used in the database, enabling \
        consistency and reproducibility in data analysis. <br>\
        Besides, users can check the vocabulary release version in their CDM which refers to the \
        vocabulary_id = ‘None’. <br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Vocabulary",
  "shortDescription": "The VOCABULARY table includes a list of the Vocabularies integrated from various sources or \
        created de novo in OMOP CDM. This reference table contains a single record for each Vocabulary \
        and includes a descriptive name and other associated attributes for the Vocabulary.",
   "guid": ""
}
omop_terms_list.append(["VOCABULARY",omop_cdm_54_term_table_vocabulary])

omop_cdm_54_term_table_domain = {
  "abbreviation": "OMOP Domain",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The DOMAIN table includes a list of OMOP-defined Domains to which the Concepts of the \
        Standardized Vocabularies can belong. A Domain represents a clinical definition whereby \
        we assign matching Concepts for the standardized fields in the CDM tables. <br>\
        For example, the Condition Domain contains Concepts that describe a patient condition, \
        and these Concepts can only be used in the condition_concept_id field of the \
        CONDITION_OCCURRENCE and CONDITION_ERA tables. This reference table is populated with a \
        single record for each Domain, including a Domain ID and a descriptive name for every Domain. <br>\
        <b>User Guide</b><br>\
        Users can leverage the DOMAIN table to explore the full spectrum of health-related data Domains \
        available in the Standardized Vocabularies. <br>\
        Also, the information in the DOMAIN table may be used as a reference for mapping source data to \
        OMOP domains, facilitating data harmonization and interoperability. <br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Domain",
  "shortDescription": "The DOMAIN table includes a list of OMOP-defined Domains to which the Concepts of the \
        Standardized Vocabularies can belong. A Domain represents a clinical definition whereby \
        we assign matching Concepts for the standardized fields in the CDM tables. \
        For example, the Condition Domain contains Concepts that describe a patient condition, \
        and these Concepts can only be used in the condition_concept_id field of the \
        CONDITION_OCCURRENCE and CONDITION_ERA tables. This reference table is populated with a \
        single record for each Domain, including a Domain ID and a descriptive name for every Domain.",
   "guid": ""
}
omop_terms_list.append(["DOMAIN",omop_cdm_54_term_table_domain])

omop_cdm_54_term_table_concept_class = {
  "abbreviation": "OMOP Concept Class",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The CONCEPT_CLASS table includes semantic categories that reference the source structure of \
        each Vocabulary. <br>\
        Concept Classes represent so-called horizontal (e.g. MedDRA, RxNorm) or vertical levels \
        (e.g. SNOMED) of the vocabulary structure. <br>\
        Vocabularies without any Concept Classes, such as HCPCS, use the vocabulary_id as the \
        Concept Class. <br>\
        This reference table is populated with a single record for each Concept Class, which includes \
        a Concept Class ID and a fully specified Concept Class name. <br>\
        <b>User Guide</b><br>\
        Users can utilize the CONCEPT_CLASS table to explore the different classes or categories of concepts \
        within the OHDSI vocabularies.<br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Concept Class",
  "shortDescription": "The CONCEPT_CLASS table includes semantic categories that reference the source structure of \
        each Vocabulary. \
        Concept Classes represent so-called horizontal (e.g. MedDRA, RxNorm) or vertical levels \
        (e.g. SNOMED) of the vocabulary structure. \
        Vocabularies without any Concept Classes, such as HCPCS, use the vocabulary_id as the \
        Concept Class. \
        This reference table is populated with a single record for each Concept Class, which includes \
        a Concept Class ID and a fully specified Concept Class name.",
   "guid": ""
}
omop_terms_list.append(["CONCEPT CLASS",omop_cdm_54_term_table_concept_class])

omop_cdm_54_term_table_concept_relationship = {
  "abbreviation": "OMOP Concept Relationship",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The CONCEPT_RELATIONSHIP table contains records that define relationships between any two \
        Concepts and the nature or type of the relationship. This table captures various types of \
        relationships, including hierarchical, associative, and other semantic connections, enabling \
        comprehensive analysis and interpretation of clinical concepts. Every kind of relationship is \
        defined in the RELATIONSHIP table.<br>\
        <b>User Guide</b><br>\
        The CONCEPT_RELATIONSHIP table can be used to explore hierarchical or attribute relationships \
        between concepts to understand the hierarchical structure of clinical concepts and uncover \
        implicit connections and associations within healthcare data. <br>\
        For example, users can utilize mapping relationships (‘Maps to’) to harmonize data from \
        different sources and terminologies, enabling interoperability and data integration across \
        disparate datasets.<br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Concept Relationship",
  "shortDescription": "The CONCEPT_RELATIONSHIP table contains records that define relationships between any two \
        Concepts and the nature or type of the relationship. This table captures various types of \
        relationships, including hierarchical, associative, and other semantic connections, enabling \
        comprehensive analysis and interpretation of clinical concepts. Every kind of relationship is \
        defined in the RELATIONSHIP table.",
   "guid": ""
}
omop_terms_list.append(["CONCEPT RELATIONSHIP",omop_cdm_54_term_table_concept_relationship])

omop_cdm_54_term_table_relationship = {
  "abbreviation": "OMOP Relationship",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The RELATIONSHIP table provides a reference list of all types of relationships that can be \
        used to associate any two concepts in the CONCEPT_RELATIONSHIP table. <br>\
        <b>User Guide</b><br> \
        NA <br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Relationship",
  "shortDescription": "The RELATIONSHIP table provides a reference list of all types of relationships that can be \
        used to associate any two concepts in the CONCEPT_RELATIONSHIP table.",
   "guid": ""
}
omop_terms_list.append(["RELATIONSHIP",omop_cdm_54_term_table_relationship])

omop_cdm_54_term_table_concept_synonym = {
  "abbreviation": "OMOP Concept Synonym",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
    "longDescription": "<b>Table Description</b><br>\
          The CONCEPT_SYNONYM table is used to store alternate names and descriptions for Concepts.<br>\
          <b>User Guide</b><br>\
          NA <br>\
          <b>ETL Conventions</b><br>\
          NA<br>\
          As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Concept Synonym",
  "shortDescription": "The CONCEPT_SYNONYM table is used to store alternate names and descriptions for Concepts.",
   "guid": ""
}
omop_terms_list.append(["CONCEPT SYNONYM",omop_cdm_54_term_table_concept_synonym])

omop_cdm_54_term_table_concept_ancestor = {
  "abbreviation": "OMOP Concept Ancestor",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
    "longDescription": "<b>Table Description</b><br>\
            The CONCEPT_ANCESTOR table is designed to simplify observational analysis by providing the \
            complete hierarchical relationships between Concepts. <br>\
            Only direct parent-child relationships between Concepts are stored in the CONCEPT_RELATIONSHIP table. <br>\
            To determine higher level ancestry connections, all individual direct relationships would have to be \
            navigated at analysis time. <br>\
            The CONCEPT_ANCESTOR table includes records for all parent-child relationships, as well as \
            grandparent-grandchild relationships and those of any other level of lineage. <br>\
            Using the CONCEPT_ANCESTOR table allows for querying for all descendants of a hierarchical concept. <br>\
            For example, drug ingredients and drug products are all descendants of a drug class ancestor.<br><br>\
            This table is entirely derived from the CONCEPT, CONCEPT_RELATIONSHIP and RELATIONSHIP tables. <br>\
            <b>User Guide</b><br>\
            NA<br>\
            <b>ETL Conventions</b><br>\
            NA<br>\
            As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
   "name": "OMOP Concept Ancestor",
   "shortDescription": "The CONCEPT_ANCESTOR table is designed to simplify observational analysis by providing the \
        complete hierarchical relationships between Concepts.\
        Only direct parent-child relationships between Concepts are stored in the CONCEPT_RELATIONSHIP table. \
        To determine higher level ancestry connections, all individual direct relationships would have to be \
        navigated at analysis time. \
        The CONCEPT_ANCESTOR table includes records for all parent-child relationships, as well as \
        grandparent-grandchild relationships and those of any other level of lineage. \
        Using the CONCEPT_ANCESTOR table allows for querying for all descendants of a hierarchical concept. \
        For example, drug ingredients and drug products are all descendants of a drug class ancestor.\
        This table is entirely derived from the CONCEPT, CONCEPT_RELATIONSHIP and RELATIONSHIP tables.",
   "guid": ""
}
omop_terms_list.append(["CONCEPT ANCESTOR",omop_cdm_54_term_table_concept_ancestor])

omop_cdm_54_term_table_source_to_concept_map = {
  "abbreviation": "OMOP Source to Concept Map",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
    "longDescription": "<b>Table Description</b><br>\
        The source to concept map table is recommended for use in ETL processes to maintain local \
        source codes which are not available as Concepts in the Standardized Vocabularies, and to \
        establish mappings for each source code into a Standard Concept as target_concept_ids that \
        can be used to populate the Common Data Model tables. <br>\
        The SOURCE_TO_CONCEPT_MAP table is no longer populated with content within the Standardized \
        Vocabularies published to the OMOP community. <br>\
        There are OHDSI tools to help you populate this table; <br>\
        - Usagi: https://github.com/OHDSI/Usagi <br>\
        - and Perseus: https://github.com/ohdsi/Perseus <br>\
        You can read more about OMOP vocabulary mapping in The Book of OHDSI Chapter 6.3. <br>\
        https://ohdsi.github.io/TheBookOfOhdsi/ExtractTransformLoad.html#step-2-create-the-code-mappings <br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
   "name": "OMOP Source to Concept Map",
   "shortDescription": "The source to concept map table is recommended for use in ETL processes to maintain local \
        source codes which are not available as Concepts in the Standardized Vocabularies, and to \
        establish mappings for each source code into a Standard Concept as target_concept_ids that \
        can be used to populate the Common Data Model tables. \
        The SOURCE_TO_CONCEPT_MAP table is no longer populated with content within the Standardized \
        Vocabularies published to the OMOP community. \
        There are OHDSI tools to help you populate this table; \
        - Usagi: https://github.com/OHDSI/Usagi \
        - and Perseus: https://github.com/ohdsi/Perseus \
        You can read more about OMOP vocabulary mapping in The Book of OHDSI Chapter 6.3. \
        https://ohdsi.github.io/TheBookOfOhdsi/ExtractTransformLoad.html#step-2-create-the-code-mappings",
   "guid": ""
}
omop_terms_list.append(["SOURCE TO CONCEPT MAP",omop_cdm_54_term_table_source_to_concept_map])

omop_cdm_54_term_table_drug_strength = {
  "abbreviation": "OMOP Drug Strength",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The DRUG_STRENGTH table contains structured content about the amount or concentration and \
        associated units of a specific ingredient contained within a particular drug product. <br>\
        This table is supplemental information to support standardized analysis of drug utilization.<br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Drug Strength",
  "shortDescription": "The DRUG_STRENGTH table contains structured content about the amount or concentration and \
        associated units of a specific ingredient contained within a particular drug product. \
        This table is supplemental information to support standardized analysis of drug utilization.",
  "guid": ""
}
omop_terms_list.append(["DRUG STRENGTH",omop_cdm_54_term_table_drug_strength])

omop_cdm_54_term_table_cohort = {
  "abbreviation": "OMOP Cohort",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The subject of a cohort can have multiple, discrete records in the cohort table per \
        cohort_definition_id, subject_id, and non-overlapping time periods. <br>\
        The definition of the cohort is contained within the COHORT_DEFINITION table. <br>\
        It is listed as part of the RESULTS schema because it is a table that users of the database \
        as well as tools such as ATLAS need to be able to write to. <br>\
        The CDM and Vocabulary tables are all read-only so it is suggested that the COHORT \
        and COHORT_DEFINTION tables are kept in a separate schema to alleviate confusion. <br>\
        <b>User Guide</b><br>\
        NA<br>\
        <b>ETL Conventions</b><br>\
        Cohorts typically include patients diagnosed with a specific condition, patients exposed to a \
        particular drug, but can also be Providers who have performed a specific Procedure. <br>\
        Cohort records must have a Start Date and an End Date, but the End Date may be set to Start Date \
        or could have an applied censor date using the Observation Period Start Date. <br>\
        Cohort records must contain a Subject Id, which can refer to the Person, Provider, Visit record \
        or Care Site though they are most often Person Ids. <br>\
        The Cohort Definition will define the type of subject through the subject concept id. <br>\
        A subject can belong (or not belong) to a cohort at any moment in time. <br>\
        A subject can only have one record in the cohort table for any moment of time, i.e. it is not \
        possible for a person to contain multiple records indicating cohort membership that are overlapping \
        in time<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Cohort",
  "shortDescription": "The subject of a cohort can have multiple, discrete records in the cohort table per \
        cohort_definition_id, subject_id, and non-overlapping time periods. \
        The definition of the cohort is contained within the COHORT_DEFINITION table. \
        It is listed as part of the RESULTS schema because it is a table that users of the database \
        as well as tools such as ATLAS need to be able to write to. \
        The CDM and Vocabulary tables are all read-only so it is suggested that the COHORT \
        and COHORT_DEFINTION tables are kept in a separate schema to alleviate confusion.",
  "guid": ""
}
omop_terms_list.append(["COHORT",omop_cdm_54_term_table_cohort])

omop_cdm_54_term_table_cohort_definition = {
  "abbreviation": "OMOP Cohort Definition",
  "anchor": {
    "glossaryGuid": "to be replaced"
  },
  "categories":  [{
      "categoryGuid": "To be replaced"
  }],
  "classifications": [{
        "typeName": atlas_OMOP_classification
   }],
  "longDescription": "<b>Table Description</b><br>\
        The COHORT_DEFINITION table contains records defining a Cohort derived from the data through \
        the associated description and syntax and upon instantiation (execution of the algorithm) placed \
        into the COHORT table. <br>\
        Cohorts are a set of subjects that satisfy a given combination of inclusion criteria for a \
        duration of time. <br>\
        The COHORT_DEFINITION table provides a standardized structure for maintaining the rules governing \
        the inclusion of a subject into a cohort, and can store operational programming code to instantiate \
        the cohort within the OMOP Common Data Model. <br>\
        <b>User Guide</b><br>\
        NA <br>\
        <b>ETL Conventions</b><br>\
        NA<br>\
        As documented on: <i>https://ohdsi.github.io/CommonDataModel/cdm54.html</i>",
  "name": "OMOP Cohort Definition",
  "shortDescription": "The COHORT_DEFINITION table contains records defining a Cohort derived from the data through \
        the associated description and syntax and upon instantiation (execution of the algorithm) placed \
        into the COHORT table. \
        Cohorts are a set of subjects that satisfy a given combination of inclusion criteria for a \
        duration of time. \
        The COHORT_DEFINITION table provides a standardized structure for maintaining the rules governing \
        the inclusion of a subject into a cohort, and can store operational programming code to instantiate \
        the cohort within the OMOP Common Data Model.",
  "guid": ""
}
omop_terms_list.append(["COHORT DEFINITION",omop_cdm_54_term_table_cohort_definition])


