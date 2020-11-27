import json


project_metadata = {
        "Project" : "2020-FHIR Health Record.kdi",
        "Creator": "FHIR Health Record",
        "Creation date": " ",
        "KDI edition" : "2020",
        "Members" : [
            {"Project Manager" : "Shaun McNaughton"},
            {"Knowledge Engineer" : ("Shaun McNaughton", "Jacopo Mocellin")}, 
            {"Domain Expert" : "Jacopo Mocellin"}, 
            {"Data Scientist" : ("Zuhairia Ibnat", "Sander Martins Gonçalves")}
                    ],
        "Codebook" : "",
        "Demo" : " ",
        "Demo Slides" : " ",
        "Project Slides" : " ",
        "Repository" : "https://github.com/UNITN-KDI-2020/kdi-fhir"
    }

database_metadata = {
    'emrbots_metadata' :   [
        {"Input" : "FHIR Health Record-3.in"}, 
        {"Creator" : "FHIR Health Record"},
        {"Creation Date" : '04/2015'},
        {"Dataset Name" : "EMRBOTS"},
        {"Dataset description" : "The dataset was created by Uri Kartoun, PhD, in 2015. We are using the 100000-patients dataset, which comprises total data about 	100.000 patients, 361.760 admissions, and 107.535.387 lab observations. The dataset was generated according to the literature on patient population studies in 	order to create a realistic set of observations."},
        {"List of column names" : [
            {"Patient ID" : "Patient ID"}, 
            {"Patient Gender" : "Patient Gender"}, 
            {"Patient Race" : "Patient Race"}, 
            {"Patient Marital Status" : "Patient Marital Status"}, 
            {"Patient Population Percentage Below Poverty" : "Patient Population Percentage Below Poverty"}, 
            {"Primary Diagnosis Code" : "Primary Diagnosis Code"}, 
            {"Primary Diagnosis Description" : "Primary Diagnosis Description"}, 
            {"Lab Name" : "Lab Name"}, 
            {"Lab Value" : "Lab Value"}, 
            {"Lab Units" : "Lab Units"}, 
            {"Lab Date Time" : "Lab Date Time"}
        ]},
        {"Source data set URL" : "https://github.com/UNITN-KDI-2020/kdi-fhir/tree/master/dataset/Scope%20Definition%20%26%20Inception/data/EMRbots"},
        {"Reference SKG metadata file" : "FHIR Health Record.skg"},
        {"Reference DKG metadata file" : "FHIR Health Record.dkg"},
        {"Number of Items" : [
            {"Rows" : 100001},
            {"Columns" : 11}
        ]}
                            ],

    'synthea_metadata'  :  [
        {"Input" : "FHIR Health Record-3.in"}, 
        {"Creator" : "FHIR Health Record"},
        {"Creation Date" : '2017'},
        {"Dataset Name" : "Synthea"},
        {"Dataset description" : "This tool was developed by the MITRE corporation and released freely under an Apache license. The datasets generated with this tool 	can include data about over 90 different conditions thanks to its modular structure. Data generated includes: Conditions, Allergies, Medications, Vaccinations, 	Observations/Vitals, Labs, Procedures, CarePlans ,Primary Care Encounters, Emergency Room Encounters, and Symptom-Driven Encounters. This data is matched with 	Configuration-based statistics and demographics. The data can be formatted in unstructured formats or structured (JSON) ones. The latter also allows for 	formatting according to HL7 standards. The generator can be queried thanks to a Java-based interface."},
        {"List of column names" : [
            {"Patient" : "Patient"}, 
            {"Allergy Intolerance" : "Allergy Intolerance"}, 
            {"Immunization" : "Immunization"}, 
            {"Patient Condition" : "Patient Condition"}, 
            {"Procedure" : "Procedure"}, 
            {"Diagnostic Report" : "Diagnostic Report"}, 
            {"Observation" : "Observation"}
        ]},
       { "Source data set URL" : "https://github.com/UNITN-KDI-2020/kdi-fhir/tree/master/dataset/Scope%20Definition%20%26%20Inception/data/Synthea"},
        {"Reference SKG metadata file" : "FHIR Health Record.skg"},
        {"Reference DKG metadata file" : "FHIR Health Record.dkg"},
        {"Number of Items" : [
            {"Rows" : 1245},
            {"Columns" : 8}
        ]}
                            ],

    'smart_metadata' :   [
        {"Input" : "FHIR Health Record-3.in"}, 
        {"Creator" : "FHIR Health Record"},
        {"Creation Date" : '21/10/2020'},
        {"Dataset Name" : "SMART FHIR"},
        {"Dataset description" : "This tools is provided as a test suite for SMART on FHIR applications by SMART itself. We are going to exploit it to generate 	structured data that fits the FHIR specifications about a population of patients."},
        {"List of column names" : [
            {"Patient" : "Patient"}, 
            {"Condition" : "Condition"}, 
            {"Immunization" : "Immunization"}, 
            {"List" : "List"}, 
            {"Observation" : "Observation"}
        ]},
        {"Source data set URL" : "https://github.com/UNITN-KDI-2020/kdi-fhir/tree/master/dataset/Scope%20Definition%20%26%20Inception/data/Smart%20on%20FHIR"},
        {"Reference SKG metadata file" : "FHIR Health Record.skg"},
        {"Reference DKG metadata file" : "FHIR Health Record.dkg"},
        {"Number of Items" : [
            {"Rows" : 67},
            {"Columns" : 6}
        ]}
                        ]
                            }

skg_metadata =    {
        "For SKG" : "FHIR Health Record.skg",
        "Creator" : "FHIR Health Record",
        "Creation date" : '26/11/2020',
        "Reference LKG metadata file" : "FHIR Health Record.lkg",
        "Reference DKG metadata file" : "FHIR Health Record.dkg",
        "List of entities" : [
                                {'Patient': [
                                            {'address': 'string'},
                                            {'birthdate':  'dateTime'},
                                            {'communication':  'string'},
                                            {'gender':  'string'},
                                            {'id':  'string'},
                                            {'name':  'string'},
                                            {'source':  [
                                                        {'URL': 'string'},
                                                        {'dateTimeAccessed':  'dateTime'}
                                                        ]
                                             }
                                            ]}, 
                                {'Condition': [
                                              {'ClinicalStatus':  'string'},
                                              {'encounter':  'dateTime'},
                                              {'onsetDateTime':  'dateTime'},
                                              {'gender':  'string'},
                                              {'code':  'string'},
                                              {'subject':  'string'}
                                              ]},
                                {'Encounter': [
                                              {'id':  'string'},
                                              {'period':  'dateTime'},
                                              {'reasonCode':  'string'},
                                              {'participant':  'string'},
                                              {'type':  'string'}
                                              ]},
                                {'Observation': [
                                              {'category':  'string'},
                                              {'effectiveDateTime':  'dateTime'},
                                              {'id':  'string'},
                                              {'subject':  'string'},
                                              {'id':  'string'},
                                              {'valueQuantity':  'float'},
                                              {'unit':  'string'}
                                              ]},
                                {'Procedure': [
                                              {'code':  'string'},
                                              {'id':  'string'},
                                              {'patient':  'string'},
                                              {'reasonReference':  'string'},
                                              {'performedPeriod':  [
                                                            {'start':  'dateTime'},
                                                            {'end':  'dateTime'}
                                                          ]
                                                }
                                              ]},
                                {'Immunization': [
                                              {'vaccineCode':  'string'},
                                              {'id':  'string'},
                                              {'patient':  'string'},
                                              {'occurrenceDateTime':  'dateTime'}
                                              ]},
                                {'Allergy Intolerance': [
                                              {'code':  'string'},
                                              {'id':  'string'},
                                              {'patient':  'string'},
                                              {'clinicalStatus':  'string'},
                                              {'recordedDate':  'dateTime'}
                                              ]},
                                {'Medication Order': [
                                              {'code':  'string'},
                                              {'id':  'string'},
                                              {'patient':  'string'},
                                              {'dosageInstructions':  'string'},
                                              {'dosageQuantity':  'float'},
                                              {'unit':  'string'}
                                              ]}
                             ]
                }
     
lkg_metadata =   {
    "For LKG" : "FHIR Health Record.lkg",
    "Creator" : "FHIR Health Record",
    "Creation date" : " ",
    "Reference SKG metadata file" : "FHIR Health Record.skg",
    "Reference DKG metadata file" : "FHIR Health Record.dkg",
    "Languages" : "English",
    "List of words added to UKC" :[ 
        {"Words" : " "}
                                ]
                }

  
file_metadata = {'project_metadata': project_metadata, 'database_metadata':database_metadata, 'skg_metadata':skg_metadata}

for key,value in file_metadata.items():
    print(key)
    name = key+'.json'
    with open(name, "w") as fout:
        json.dump(value, fout)
