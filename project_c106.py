# -*- coding: utf-8 -*-
"""Project-C106

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qYpDBfHb49YCM6XIPkcPxyv8vG__5y8h
"""

import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("data.csv")
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()