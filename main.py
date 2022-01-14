import datetime as dt
import pandas as pd

# create a variable containing present datetime
present_datetime = dt.datetime.now()

#create a tuple containing both the present month and day
present_tuple = (present_datetime.month, present_datetime.day)

#use pandas lib to read the the info.csv file and create a dataframe
data = pd.read_csv("info.csv")

# create a dictionary containing tuples as keys and the entire row of dataframe as value using dict comprehension
# key tuples should contain both the month and day in info.csv of respective tasks
info_tuples = {(data_row['month'], data_row['day']):data_row for (index, data_row) in data.iterrows()}