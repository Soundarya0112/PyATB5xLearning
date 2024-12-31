#CSV--comma separated file
import csv
with open("Testdatacsv.csv") as csvfile:
    reader=csv.reader(csvfile)
    for col in reader:
        print(col[0],col[1],sep="|")
"""
#for easy method download pandas

import pandas as pd
output=pd.read_csv("Testdatacsv.csv")
print(output)
"""

