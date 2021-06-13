import pandas as pd
path = "path to file" # path to file
df = pd.read_csv("/home/mose/Downloads/2019-Nov_Mixed.csv/2019-Nov.csv") # reading file

low = 0 # Initial Lower Limit2019-Dec.csv2019-Dec.csv
high = 10000 # Initial Higher Limit
while(high < len(df)):
    df_new = df[low:high] # subsetting DataFrame based on index
    low = high #changing lower limit
    high = high + 10000 # givig uper limit with increment of 1000
    df_new.to_csv("/home/mose/Documents/Semester3/AdvancedDataManagement/ProjectADM/jewelry.csv/Mixed.csv") 
