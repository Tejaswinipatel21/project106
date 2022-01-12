"""import plotly.express as px
import csv
with open("D:/teju/Python/Size of TV,_Average time spent watching TV in a week (hours).csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Size of TV", y="\tAverage time spent watching TV in a week (hours)")
    fig.show()"""




import csv
import numpy as np


def getDataSource(data_path):
    marks_of_student = []
    noof_days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_of_student.append(float(row["Days Present"]))
            noof_days_present.append(float(row["Marks In Percentage"]))

    return {"x" : marks_of_student, "y": noof_days_present }

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Student Marks and Days Present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "D:/teju/Python/Student Marks vs Days Present.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
