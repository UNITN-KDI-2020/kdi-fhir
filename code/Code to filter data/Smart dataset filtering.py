import json
import os
import xml.etree.ElementTree as ET

'''
Instructions:
1-If you haven't done yet, clone the repository 'sample-patients': (https://github.com/smart-on-fhir/sample-patients) 
2-Update the variable 'directory_path_smart' with the path of the 'out' folder that is on your machine. You will find this folder inside 'sample-patients'.
3-Move this code file to the 'out' folder from step 2.
4-Run the code
5-The desired output is the file created named 'patientList.json' on your folder
'''
directory_path_smart = 'C:\\Users\\sande\\Documents\\MyProjects\\sample-patients\\out'




file_names = []
for filename in os.listdir(directory_path_smart): 
    if filename.endswith('.xml'):
        file_names.append(filename)
#print(file_names[0])

#patient_columns = ['Patient', 'Condition', 'Immunization', 'List', 'Observation']
dict_interation = {'Patient' : './/{http://hl7.org/fhir}Patient/*', 'Condition' : '{http://hl7.org/fhir}Condition', 'Immunization' : '{http://hl7.org/fhir}Immunization', 'List' : '{http://hl7.org/fhir}List', 'Observation' : '{http://hl7.org/fhir}Observation' }
patients_list = [] #final dictionary/list containing information of all patients of all JSON files

for filename in file_names:
    var_name = filename
    tree = ET.parse(var_name)
    root = tree.getroot()

    patient = {} #dictionary of a single patient. It will interate over all patients

    #Initializing all the lists of our "patient" JSON. They will have the same name as "entry_list". Our desired columns
    patient['Patient'] = []
    patient['Condition'] = []
    patient['Immunization'] = []
    patient['List'] = []
    patient['Observation'] = []

    for key, value in dict_interation.items():
        #print('Key: {}'.format(key) +20*'---') #checking is all fields
        for elem in root.findall(value):
            tmp_value = elem.tag
            tmp_value = tmp_value.replace('{http://hl7.org/fhir}','')
            patient[key].append(tmp_value)
            patient[key].append(elem.attrib)
            print('Elem.tag = {} Elem.attrib = {}'.format(elem.tag, elem.attrib)) #tag = column, attrib = values
            #print('patient[key]: {}'.format(patient[key])) #checking values
    patients_list.append(patient)
    print('patient'+15*'-')
    print(patient) #checking if patient information was recording is ok
print('patient'+15*'-')
print(patients_list) #checking if patient information was recording is ok


with open("patientList.json", "w") as fout:
    json.dump(patients_list, fout)

