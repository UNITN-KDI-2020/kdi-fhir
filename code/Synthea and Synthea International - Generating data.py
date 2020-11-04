"""
The source of the dataset can be found at this link: https://github.com/synthetichealth/synthea.git
The instructions here will be the same of the ones found at the page. 
"""
git clone https://github.com/synthetichealth/synthea.git #1 Clone the repository
cd synthea #2 Go to the synthea folder
./run_synthea #3 generate data

'''
We can change the features of our data, like country and zip code. In order to do that, we need to use other repository as complementary data (https://github.com/synthetichealth/synthea-international). For this case, we choose the desired country from the available list (github page of synthea-international) and copy its contents into "synthea" folder. Afterwards is just running the code as usual from "synthea" folder (./run_synthea)
'''
run_synthea [-s seed] [-p populationSize] [-m moduleFilter] [state [city]] #this command is used in case we want to generate data with specific features. Be aware that the name of the state/city need to be according to the data used (country choosen). The default country is US.

./gradlew graphviz #This command generate graphical visualizations 

#The commands bellow generate a list of concepts (used in the records) or attributes (variables on each patient).
./gradlew concepts 
./gradlew attributes