"""
The source of the dataset can be found at this link: https://github.com/smart-on-fhir/sample-patients
The instructions here will be the same of the ones found at the page. There is only one observance, in order to run the script is necessary to have python version 2.*
"""
#1 Clone the git repository
#2 go to the "bin" folder
python generate.py #3 run this code to generate data. The folder "out" will be created, if not, please create the folder. This is where the data generated will be.
# In case we want a summary of a patient, run the following code (python generate.py --summary PID). In this case, please substitute "PID" by the number of the patient presented on the patient's file name. 

