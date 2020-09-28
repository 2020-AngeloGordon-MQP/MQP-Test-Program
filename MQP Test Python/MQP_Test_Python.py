import pyodbc
import numpy as np
import pandas as pd
from tabulate import tabulate

connection = pyodbc.connect('Driver={SQL Server}; Server=DESKTOP-NUDOMMO\SQLEXPRESS; Database=TestDB;');

cursor = connection.cursor()

cursor.execute('SELECT * FROM TestDB.dbo.VelocityData')


data_obj = {"time": [], "velocity": []}

for row in cursor:
    data_obj["time"].append(row.time)
    data_obj["velocity"].append(row.velocity)

dataFrame = pd.DataFrame(data_obj)
print(dataFrame)


