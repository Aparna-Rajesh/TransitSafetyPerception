#importing pandas as pd 
import pandas as pd 


for x in range(12):
    name = "arrests-in-transit-report-" + str(x + 1) + "-2017"

    # Read and store content 
    # of an excel file 
    read_file = pd.read_excel (name + ".xlsx") 

    # Write the dataframe object 
    # into csv file 
    read_file.to_csv (name + ".csv", 
                    index = None, 
                    header=True) 
        
    # read csv file and convert 
    # into a dataframe object 
    df = pd.DataFrame(pd.read_csv(name + ".csv")) 