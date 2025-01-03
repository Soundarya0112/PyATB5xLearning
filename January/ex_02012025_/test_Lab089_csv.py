import pandas as pd
import csv

from December.ex_09122024_Modules_pipPackages.Lab078_modules import readMySQLDB


class test_read():
    def test_read_csv(self):
        with open('userdata.csv') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                 print(row[0],row[1])


def test_read_pandas(self):
    df=pd.read_csv('userdata.csv')
    print(df)