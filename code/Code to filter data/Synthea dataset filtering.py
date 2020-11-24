import json
import pandas as pd
import os
'''
Instructions:
1-If you haven't done yet, clone the repository 'Synthea': (https://github.com/synthetichealth/synthea) 
2-Update the vaiable 'directory_path_synthea' with the path of the 'fhir' folder that is on your machine. You will find this folder inside 'synthea/output'.
3-Move this code file to the 'fhir' folder from step 2.
4-Remove any file that is not in the format 'patient-name.json'. (i.e. hospitalInformation and practitionerInformation)
5-Run the code
6-The desired output is the file created named 'patientList.json' on your folder
'''
directory_path_synthea = '~/synthea/output/fhir' #path where all json files are

patients_list = [] #final dictionary/list containing information of all patients of all JSON files
entry_list = ['Patient', 'AllergyIntolerance', 'Immunization', 'Condition', 'Procedure', 'DiagnosticReport', 'Observation'] #all columns that we are interested

file_names = []
for filename in os.listdir(directory_path_synthea): 
    if filename.endswith('.json'):
        file_names.append(filename)
#print(file_names)

for filename in file_names:
    with open(filename, encoding='cp437') as f: 
        print(f)
        if (filename != 'patientList.json'):
            patient_fhir = json.loads(f.read()) #loading each patient file
            
    patient = {} #dictionary of a single patient. It will interate over all patients

    #Initializing all the lists of our "patient" JSON. They will have the same name as "entry_list". Our desired columns
    patient['Patient'] = []
    patient['AllergyIntolerance'] = []
    patient['Immunization'] = []
    patient['Condition'] = []
    patient['Procedure'] = []
    patient['DiagnosticReport'] = []
    patient['Observation'] = []

    for entry in patient_fhir["entry"]: #interating over all entries in our JSON file 
        for values in entry_list: #interating over all fields that we want. 
            if entry["resource"]["resourceType"] == values:
                patient[values] = entry['resource']
        
        pat = json.dumps(patient)
        #patients_list.update(patient) #adding the patient to our list of patients
        #patients_list.update({patient}) #adding the patient to our list of patients
        patients_list.append(pat) #adding the patient to our list of patients
        #patients_list.add(patient) #adding the patient to our list of patients
        #patients_list[entry] = patient
#print(patients_list) #verification of the process

with open("patientList.json", "w") as fout:
    json.dump(patients_list, fout)
