import abc
import csv
import pandas as bear
import plotly.figure_factory as pff

choose = str(input("Avg Rating (a) OR Sr.No (b): "))

df = bear.read_csv("data.csv")

if (choose == "a"):
    fig = pff.create_distplot([df["Avg Rating"].tolist()], ["abc"])
    fig.show()
elif (choose == "b"):
    fig = pff.create_distplot([df["Sr.No"].tolist()], ["abc"])
    fig.show()