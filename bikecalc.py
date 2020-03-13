# bikecalc.py

from tkinter import *
import math
import time
import csv
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# bikes = pd.read_csv('bikes.csv', encoding= 'unicode_escape')
# print(bikes.keys())

# # doesnt work: throws error:
# bikes.plot(y='record',x='speeds')
# bikes.plot.barh(y='record',x='date')


#this works
bikes = open('bikes.csv',encoding= 'unicode_escape')
reader = csv.reader(bikes)

record_keys = [] #column [0]
date_values = [] #column [1]
day_values = [] #column [2]
time_values = [] #column [3]
location_values = [] #column [4]
reason_values = [] #column [5]
make_values = [] #column [6]
model_values = [] #column [7]
frame_values = [] #column [8]
bike_type_values = [] #column [9]
color_values = [] #column [10]
speeds_values = [] #column [11]

for i in reader:
    record_keys.append(i[0])
    date_values.append(i[1])
    day_values.append(i[2])
    time_values.append(i[3])
    location_values.append(i[4])
    reason_values.append(i[5])
    make_values.append(i[6])
    model_values.append(i[7])
    frame_values.append(i[8])
    bike_type_values.append(i[9])
    color_values.append(i[10])
    speeds_values.append(i[11])

record_dict = dict(zip(record_keys,record_keys))
date_dict = dict(zip(record_keys,date_values))
day_dict = dict(zip(record_keys,day_values))
time_dict = dict(zip(record_keys,time_values))
location_dict = dict(zip(record_keys,location_values))
reason_dict = dict(zip(record_keys,reason_values))
make_dict = dict(zip(record_keys,make_values))
model_dict = dict(zip(record_keys,model_values))
frame_dict = dict(zip(record_keys,frame_values))
bike_type_dict = dict(zip(record_keys,bike_type_values))
color_dict = dict(zip(record_keys,color_values))
speeds_dict = dict(zip(record_keys,speeds_values))

master_dict_list = [record_dict, date_dict, day_dict, time_dict, location_dict, 
reason_dict, make_dict, model_dict, frame_dict, bike_type_dict, color_dict, speeds_dict]





# for key, value in make_dict.items():
#     print(value)

def graph_record_overtime():
    fig1 = px.scatter(y=list(date_dict.keys()), x=list(date_dict.values()))
    fig1.update_layout(title="Bike Impounds Over Time", xaxis_title="Time",yaxis_title="Bike Count")
    fig1.show()


# data = {}
# header = next(reader)
# print(data.keys())

#this works:
# for column in reader:
#     record = column[0]
#     date = column[1]
#     day_of_week = column[2]
#     time = column[3]
#     location = column[4]
#     reason = column[5]
#     make = column[6]
#     model = column[7]
#     frame = column[8]
#     bike_type = column[9]
#     color = column[10]
#     speeds = column[11]

#use this one:
    # if record in data.keys():
    #     data[record] = data[record]# + date
    # else:
    #     data[record] = date


#don't use this one:
    # if date in data.keys():
    #     data[date] = data[date] + record
    # else:
    #     data[date] = record

# print(list(data.keys()))#[0])
# print(data.keys())


######### FUNCTIONS ##########
# def record_graph():
#     fig = go.Figure(data=go.Scatter(
#         y=list(data.keys()),
#         x=list(data.values())
#     ))
#     fig.update_layout(title="Bike Impounds Over Time", xaxis_title="Time",yaxis_title="Bike Count")
#     fig.show()





#+++++++  FUNCTIONS  +++++++#
def count_all_values(dictselection):
    count = 0
    for i in dictselection.values():
        if i == "":
            pass
        else:
            count = count + 1
    print(f"\nCount all: {count}\n")

def count_unique_values(dictselection):
    unique_values = []
    count = 0
    for i in dictselection.values():
        if i == i in unique_values:
            pass
        else:
            if i == "":
                pass
            else:
                unique_values.append(i)
                count = count + 1
    print(f"\nCount unique: {count}\n")

def list_all_values(dictselection):
    unique_values = []
    for i in dictselection.values():
        if i == "":
            pass
        else:
            unique_values.append(i)
    # unique_values.sort()
    print(f"\nAll values: {unique_values}\n")

def list_unique_values(dictselection):
    unique_values = []
    for i in dictselection.values():
        if i == i in unique_values:
            pass
        else:
            if i == "":
                pass
            else:
                unique_values.append(i)
    unique_values.sort()
    print(f"\nUnique values: {unique_values}\n")

def count_greatest_least_value():
    count = 1
    print(f"\nCount total: {count}\n")


########### NEED TO FINISH THIS ONE #############
def list_greatest_least_value():   #(dictselection):
    print("Still under construction.")
########### NEED TO FINISH THIS ONE #############


######### TKINTER FUNCTIONS ##########
bikeinfo_value = ""
datatype_value = ""
datarep_value = ""
result_value = ""

def bikeinfo_btn_click(item):
    global bikeinfo_value
    bikeinfo_value = bikeinfo_value + str(item)
    bikeinfo_input_text.set(bikeinfo_value)
def datatype_btn_click(item):
    global datatype_value
    datatype_value = datatype_value + str(item)
    datatype_input_text.set(datatype_value)
def datarep_btn_click(item):
    global datarep_value
    datarep_value = datarep_value + str(item)
    datarep_input_text.set(datarep_value)
def btn_clear_all():
    global bikeinfo_value
    bikeinfo_value = ""
    bikeinfo_input_text.set("")
    global datatype_value
    datatype_value = ""
    datatype_input_text.set("")
    global datarep_value
    datarep_value = ""
    datarep_input_text.set("")
    global result_value
    result_value = ""
    result_input_text.set("")
def btn_clear_top():
    global bikeinfo_value
    bikeinfo_value = ""
    bikeinfo_input_text.set("")
    global datatype_value
    datatype_value = ""
    datatype_input_text.set("")
    global datarep_value
    datarep_value = ""
    datarep_input_text.set("")



datarep_list = ["Count","List","Graph"]
bikeinfo_list = ["Date","Day of Week","Time","Location","Record","Reason","Make","Model","Frame","Type","Color","Speeds"]
datatype_list = ["All Values","Unique Values","Greatest Value","Least Value","Comparison","Over Time"]


# def combo_button_press(datarep,bikeinfo,datatype):
#     if (datarep in datarep_list) in result_list:
#         if (bikeinfo in bikeinfo_list) in result_list:
#             if (datatype in datatype_list) in result_list:
#                 count_all_values(date_dict)

# def combo_button_press(datarep,bikeinfo,datatype):
#     for a in datarep_list:
#         if a in result_list:
#             for b in bikeinfo_list:
#                 if b in result_list:
#                     for c in datatype_list:
#                         if c in result_list:
#                             count_all_values(color_dict)


    # if (datarep in datarep_list) in result_list:
    #     if (bikeinfo in bikeinfo_list) in result_list:
    #         if (datatype in datatype_list) in result_list:
    #             count_all_values(date_dict)



def combo_button_press():
    print("in combo_button_press")
    print(result_list)
    if "Count" in result_list:                          ####### COUNT #######
        if "All Values" in result_list:
            if "Date" in result_list:
                count_all_values(date_dict)
            elif "Day of Week" in result_list:
                count_all_values(day_dict)
            elif "Time" in result_list:
                count_all_values(time_dict)
            elif "Location" in result_list:
                count_all_values(location_dict)
            elif "Record" in result_list:
                count_all_values(color_dict)
            elif "Reason" in result_list:
                count_all_values(record_dict)
            elif "Make" in result_list:
                count_all_values(make_dict)
            elif "Model" in result_list:
                count_all_values(model_dict)
            elif "Frame" in result_list:
                count_all_values(frame_dict)
            elif "Type" in result_list:
                count_all_values(bike_type_dict)
            elif "Color" in result_list:
                count_all_values(color_dict)
            elif "Speeds" in result_list:
                count_all_values(speeds_dict)
        elif "Unique Values" in result_list:
            if "Date" in result_list:
                count_unique_values(date_dict)
            elif "Day of Week" in result_list:
                count_unique_values(day_dict)
            elif "Time" in result_list:
                count_unique_values(time_dict)
            elif "Location" in result_list:
                count_unique_values(location_dict)
            elif "Record" in result_list:
                count_unique_values(color_dict)
            elif "Reason" in result_list:
                count_unique_values(record_dict)
            elif "Make" in result_list:
                count_unique_values(make_dict)
            elif "Model" in result_list:
                count_unique_values(model_dict)
            elif "Frame" in result_list:
                count_unique_values(frame_dict)
            elif "Type" in result_list:
                count_unique_values(bike_type_dict)
            elif "Color" in result_list:
                count_unique_values(color_dict)
            elif "Speeds" in result_list:
                count_unique_values(speeds_dict)
        elif "Greatest Value" in result_list:
            count_greatest_least_value()
        elif "Least Value" in result_list:
            count_greatest_least_value()
        elif "Comparison" in result_list:
            print("Sorry, unable to perform this calculation.")
        elif "Over Time" in result_list:
            print("Still under construction.")
    elif "List/Print" in result_list:                   ####### LIST/PRINT #######
        if "All Values" in result_list:
            if "Date" in result_list:
                list_all_values(date_dict)
            elif "Day of Week" in result_list:
                list_all_values(day_dict)
            elif "Time" in result_list:
                list_all_values(time_dict)
            elif "Location" in result_list:
                list_all_values(location_dict)
            elif "Record" in result_list:
                list_all_values(color_dict)
            elif "Reason" in result_list:
                list_all_values(record_dict)
            elif "Make" in result_list:
                list_all_values(make_dict)
            elif "Model" in result_list:
                list_all_values(model_dict)
            elif "Frame" in result_list:
                list_all_values(frame_dict)
            elif "Type" in result_list:
                list_all_values(bike_type_dict)
            elif "Color" in result_list:
                list_all_values(color_dict)
            elif "Speeds" in result_list:
                list_all_values(speeds_dict)
        elif "Unique Values" in result_list:
            if "Date" in result_list:
                list_unique_values(date_dict)
            elif "Day of Week" in result_list:
                list_unique_values(day_dict)
            elif "Time" in result_list:
                list_unique_values(time_dict)
            elif "Location" in result_list:
                list_unique_values(location_dict)
            elif "Record" in result_list:
                list_unique_values(color_dict)
            elif "Reason" in result_list:
                list_unique_values(record_dict)
            elif "Make" in result_list:
                list_unique_values(make_dict)
            elif "Model" in result_list:
                list_unique_values(model_dict)
            elif "Frame" in result_list:
                list_unique_values(frame_dict)
            elif "Type" in result_list:
                list_unique_values(bike_type_dict)
            elif "Color" in result_list:
                list_unique_values(color_dict)
            elif "Speeds" in result_list:
                list_unique_values(speeds_dict)
        elif "Greatest Value" in result_list:
            list_greatest_least_value()
        elif "Least Value" in result_list:
            list_greatest_least_value()
        elif "Comparison" in result_list:
            print("Sorry, unable to perform this calculation.")
        elif "Over Time" in result_list:
            print("Still under construction.")
    elif "Graph" in result_list:                        ####### GRAPH #######
        if "All Values" in result_list:
            if "Date" in result_list:
                list_all_values(date_dict)
            elif "Day of Week" in result_list:
                list_all_values(day_dict)
            elif "Time" in result_list:
                list_all_values(time_dict)
            elif "Location" in result_list:
                list_all_values(location_dict)
            elif "Record" in result_list:
                list_all_values(color_dict)
            elif "Reason" in result_list:
                list_all_values(record_dict)
            elif "Make" in result_list:
                list_all_values(make_dict)
            elif "Model" in result_list:
                list_all_values(model_dict)
            elif "Frame" in result_list:
                list_all_values(frame_dict)
            elif "Type" in result_list:
                list_all_values(bike_type_dict)
            elif "Color" in result_list:
                list_all_values(color_dict)
            elif "Speeds" in result_list:
                list_all_values(speeds_dict)
        elif "Unique Values" in result_list:
            if "Date" in result_list:
                list_unique_values(date_dict)
            elif "Day of Week" in result_list:
                list_unique_values(day_dict)
            elif "Time" in result_list:
                list_unique_values(time_dict)
            elif "Location" in result_list:
                list_unique_values(location_dict)
            elif "Record" in result_list:
                list_unique_values(color_dict)
            elif "Reason" in result_list:
                list_unique_values(record_dict)
            elif "Make" in result_list:
                list_unique_values(make_dict)
            elif "Model" in result_list:
                list_unique_values(model_dict)
            elif "Frame" in result_list:
                list_unique_values(frame_dict)
            elif "Type" in result_list:
                list_unique_values(bike_type_dict)
            elif "Color" in result_list:
                list_unique_values(color_dict)
            elif "Speeds" in result_list:
                list_unique_values(speeds_dict)
        elif "Greatest Value" in result_list:
            list_greatest_least_value()
        elif "Least Value" in result_list:
            list_greatest_least_value()
        elif "Comparison" in result_list:
            print("Sorry, unable to perform this calculation.")
        elif "Over Time" in result_list:
            if "Record" in result_list:
                graph_record_overtime()
            print("Still under construction.")



def btn_equal():
    global datatype_value
    global bikeinfo_value
    global datarep_value
    global result_list
    active = True
    # result_list = []  ###may not need this initially
    result = str(datarep_value+ ", " +bikeinfo_value+ ", " +datatype_value) # 'eval' function evalutes the string expression directly
    result_list = [datarep_value, bikeinfo_value, datatype_value]
    if datarep_value != "" and bikeinfo_value != "" and datatype_value != "":
        result_input_text.set(result) ##only enact this "if" datarep_value, bikeinfo_value, and datatype_value != Null
    else:
        result_input_text.set("")
    # print(f"result is: {result}") ###print this
    # for i in result:
    #     result_list.append(i)
    #     result_list_join = "".join(result_list)
    # result_list = result_list_join.split(", ")
    # print(f"result_list: {result_list}")###print this
    # print(result_list)
    btn_clear_top()
    combo_button_press()#result_list[0],result_list[1],result_list[2])


########## TKINTER SETUP ##########
root = Tk()
root.title("Bike Calculator")

datarep_input_text = StringVar()
bikeinfo_input_text = StringVar()
datatype_input_text = StringVar()
result_input_text = StringVar()

data_rep_label = Label(root, text="DATA REPRESENTATION", fg="blue", font='Arial 14 bold')
data_rep_label.pack()
data_rep_entry_frame = Frame(root)
data_rep_entry_frame.pack()
data_rep_input_field = Entry(data_rep_entry_frame, textvariable = datarep_input_text, bg="black", fg="white", width=30).grid(row=0, column=0)

bikeinfo_label = Label(root, text="BIKE INFO", fg="black", font='Arial 14 bold')
bikeinfo_label.pack()#side=LEFT)
bikeinfo_entry_frame = Frame(root)
bikeinfo_entry_frame.pack()
bikeinfo_input_field = Entry(bikeinfo_entry_frame, textvariable = bikeinfo_input_text, bg="black", fg="white", width=30).grid(row=0, column=0)

datatype_label = Label(root, text="DATA TYPE", fg="orange", font='Arial 14 bold')
datatype_label.pack()
datatype_entry_frame = Frame(root)
datatype_entry_frame.pack()
bikeinfo_input_field = Entry(datatype_entry_frame, textvariable = datatype_input_text, bg="black", fg="white", width=30).grid(row=0, column=0)

button_frame = Frame(root)
button_frame.pack()

button_count = Button(button_frame, text="Count", bg="white", fg="blue", command=lambda: datarep_btn_click("Count")).grid(row=1, column=0, ipadx=0, padx=0, pady=0)
button_list_print = Button(button_frame, text="List/Print", bg="white", fg="blue", command=lambda: datarep_btn_click("List/Print")).grid(row=1, column=1, ipadx=0, padx=0, pady=0)
button_graph = Button(button_frame, text="Graph", bg="white", fg="blue", command=lambda: datarep_btn_click("Graph")).grid(row=1, column=2, ipadx=0, padx=0, pady=0)

button_date = Button(button_frame, text="Date", bg="white", fg="black", command=lambda: bikeinfo_btn_click("Date")).grid(row=3, column=0, ipadx=0, padx=0, pady=0)
button_dayofweek = Button(button_frame, text="Day of Week", bg="white", fg="black", command=lambda: bikeinfo_btn_click("Day of Week")).grid(row=4, column=0, ipadx=0, padx=0, pady=0)
button_time = Button(button_frame, text="Time", bg="white", fg="black", command=lambda: bikeinfo_btn_click("Time")).grid(row=5, column=0, ipadx=0, padx=0, pady=0)
button_location = Button(button_frame, text="Location", bg="white", fg="black", command=lambda: bikeinfo_btn_click("Location")).grid(row=6, column=0, ipadx=0, padx=0, pady=0)
button_recordnum = Button(button_frame, text="Record", bg="white", fg="black", command=lambda: bikeinfo_btn_click("Record")).grid(row=3, column=1, ipadx=0, padx=0, pady=0)
button_reason = Button(button_frame, text="Reason", bg="white", fg="black", command=lambda: bikeinfo_btn_click("Reason")).grid(row=4, column=1, ipadx=0, padx=0, pady=0)
button_make = Button(button_frame, text="Make", bg="white", fg="black", command=lambda: bikeinfo_btn_click("Make")).grid(row=5, column=1, ipadx=0, padx=0, pady=0)
button_model = Button(button_frame, text="Model", bg="white", fg="black", command=lambda: bikeinfo_btn_click("Model")).grid(row=6, column=1, ipadx=0, padx=0, pady=0)
button_frametype = Button(button_frame, text="Frame", bg="white", fg="black", command=lambda: bikeinfo_btn_click("Frame")).grid(row=3, column=2, ipadx=0, padx=0, pady=0)
button_biketype = Button(button_frame, text="Type", bg="white", fg="black", command=lambda: bikeinfo_btn_click("Type")).grid(row=4, column=2, ipadx=0, padx=0, pady=0)
button_color = Button(button_frame, text="Color", bg="white", fg="black", command=lambda: bikeinfo_btn_click("Color")).grid(row=5, column=2, ipadx=0, padx=0, pady=0)
button_speeds = Button(button_frame, text="Speeds", bg="white", fg="black", command=lambda: bikeinfo_btn_click("Speeds")).grid(row=6, column=2, ipadx=0, padx=0, pady=0)

button_all_values = Button(button_frame, text="All Values", bg="white", fg="orange", command=lambda: datatype_btn_click("All Values")).grid(row=8, column=0, ipadx=0, padx=0, pady=0)
button_unique_values = Button(button_frame, text="Unique Values", bg="white", fg="orange", command=lambda: datatype_btn_click("Unique Values")).grid(row=9, column=0, ipadx=0, padx=0, pady=0)
button_greatest_value = Button(button_frame, text="Greatest Value", bg="white", fg="orange", command=lambda: datatype_btn_click("Greatest Value")).grid(row=8, column=1, ipadx=0, padx=0, pady=0)
button_least_value = Button(button_frame, text="Least Value", bg="white", fg="orange", command=lambda: datatype_btn_click("Least Value")).grid(row=9, column=1, ipadx=0, padx=0, pady=0)
button_comparison = Button(button_frame, text="Comparison", bg="white", fg="orange", command=lambda: datatype_btn_click("Comparison")).grid(row=8, column=2, ipadx=0, padx=0, pady=0)
button_over_time = Button(button_frame, text="Over Time", bg="white", fg="orange", command=lambda: datatype_btn_click("Over Time")).grid(row=9, column=2, ipadx=0, padx=0, pady=0)

button_calculate = Button(button_frame, text="Calculate", bg="white", fg="green", command=lambda: btn_equal()).grid(row=10, column=0, ipadx=0, padx=0, pady=0)
button_clear = Button(button_frame, text="Clear All", bg="white", fg="red", command=lambda: btn_clear_all()).grid(row=10, column=2, ipadx=0, padx=0, pady=0)

result_label = Label(root, text="RESULT", font='Arial 14 bold')
result_label.pack()
result_entry_frame = Frame(root)
result_entry_frame.pack()#side=RIGHT)
result_input_field = Entry(result_entry_frame, textvariable = result_input_text, bg="black", fg="white", width=30).grid(row=0, column=0)

root.mainloop()


#the following gives combos:
# from itertools import combinations 
# comb = combinations(["Count","List","Graph","Date","Day of Week","Time","Location","Record","Reason","Make","Model","Frame","Type","Color","Speeds","All Values","Unique Values","Greatest Value","Least Value","Comparison","Over Time"],3)
# for i in list(comb): 
#     print(i) 




('Count', 'Date', 'All Values')
('Count', 'Date', 'Unique Values')
('Count', 'Date', 'Greatest Value')
('Count', 'Date', 'Least Value')
('Count', 'Date', 'Comparison')
('Count', 'Date', 'Over Time')

('Count', 'Day of Week', 'All Values')
('Count', 'Day of Week', 'Unique Values')
('Count', 'Day of Week', 'Greatest Value')
('Count', 'Day of Week', 'Least Value')
('Count', 'Day of Week', 'Comparison')
('Count', 'Day of Week', 'Over Time')

('Count', 'Time', 'All Values')
('Count', 'Time', 'Unique Values')
('Count', 'Time', 'Greatest Value')
('Count', 'Time', 'Least Value')
('Count', 'Time', 'Comparison')
('Count', 'Time', 'Over Time')

('Count', 'Location', 'All Values')
('Count', 'Location', 'Unique Values')
('Count', 'Location', 'Greatest Value')
('Count', 'Location', 'Least Value')
('Count', 'Location', 'Comparison')
('Count', 'Location', 'Over Time')

('Count', 'Record', 'All Values')
('Count', 'Record', 'Unique Values')
('Count', 'Record', 'Greatest Value')
('Count', 'Record', 'Least Value')
('Count', 'Record', 'Comparison')
('Count', 'Record', 'Over Time')

('Count', 'Reason', 'All Values')
('Count', 'Reason', 'Unique Values')
('Count', 'Reason', 'Greatest Value')
('Count', 'Reason', 'Least Value')
('Count', 'Reason', 'Comparison')
('Count', 'Reason', 'Over Time')

('Count', 'Make', 'All Values')
('Count', 'Make', 'Unique Values')
('Count', 'Make', 'Greatest Value')
('Count', 'Make', 'Least Value')
('Count', 'Make', 'Comparison')
('Count', 'Make', 'Over Time')

('Count', 'Model', 'All Values')
('Count', 'Model', 'Unique Values')
('Count', 'Model', 'Greatest Value')
('Count', 'Model', 'Least Value')
('Count', 'Model', 'Comparison')
('Count', 'Model', 'Over Time')

('Count', 'Frame', 'All Values')
('Count', 'Frame', 'Unique Values')
('Count', 'Frame', 'Greatest Value')
('Count', 'Frame', 'Least Value')
('Count', 'Frame', 'Comparison')
('Count', 'Frame', 'Over Time')

('Count', 'Type', 'All Values')
('Count', 'Type', 'Unique Values')
('Count', 'Type', 'Greatest Value')
('Count', 'Type', 'Least Value')
('Count', 'Type', 'Comparison')
('Count', 'Type', 'Over Time')

('Count', 'Color', 'Speeds')
('Count', 'Color', 'All Values')
('Count', 'Color', 'Unique Values')
('Count', 'Color', 'Greatest Value')
('Count', 'Color', 'Least Value')
('Count', 'Color', 'Comparison')
('Count', 'Color', 'Over Time')

('Count', 'Speeds', 'All Values')
('Count', 'Speeds', 'Unique Values')
('Count', 'Speeds', 'Greatest Value')
('Count', 'Speeds', 'Least Value')
('Count', 'Speeds', 'Comparison')
('Count', 'Speeds', 'Over Time')

('List', 'Date', 'All Values')
('List', 'Date', 'Unique Values')
('List', 'Date', 'Greatest Value')
('List', 'Date', 'Least Value')
('List', 'Date', 'Comparison')
('List', 'Date', 'Over Time')

('List', 'Day of Week', 'All Values')
('List', 'Day of Week', 'Unique Values')
('List', 'Day of Week', 'Greatest Value')
('List', 'Day of Week', 'Least Value')
('List', 'Day of Week', 'Comparison')
('List', 'Day of Week', 'Over Time')

('List', 'Time', 'All Values')
('List', 'Time', 'Unique Values')
('List', 'Time', 'Greatest Value')
('List', 'Time', 'Least Value')
('List', 'Time', 'Comparison')
('List', 'Time', 'Over Time')

('List', 'Location', 'All Values')
('List', 'Location', 'Unique Values')
('List', 'Location', 'Greatest Value')
('List', 'Location', 'Least Value')
('List', 'Location', 'Comparison')
('List', 'Location', 'Over Time')

('List', 'Record', 'All Values')
('List', 'Record', 'Unique Values')
('List', 'Record', 'Greatest Value')
('List', 'Record', 'Least Value')
('List', 'Record', 'Comparison')
('List', 'Record', 'Over Time')

('List', 'Reason', 'All Values')
('List', 'Reason', 'Unique Values')
('List', 'Reason', 'Greatest Value')
('List', 'Reason', 'Least Value')
('List', 'Reason', 'Comparison')
('List', 'Reason', 'Over Time')

('List', 'Make', 'All Values')
('List', 'Make', 'Unique Values')
('List', 'Make', 'Greatest Value')
('List', 'Make', 'Least Value')
('List', 'Make', 'Comparison')
('List', 'Make', 'Over Time')

('List', 'Model', 'All Values')
('List', 'Model', 'Unique Values')
('List', 'Model', 'Greatest Value')
('List', 'Model', 'Least Value')
('List', 'Model', 'Comparison')
('List', 'Model', 'Over Time')

('List', 'Frame', 'All Values')
('List', 'Frame', 'Unique Values')
('List', 'Frame', 'Greatest Value')
('List', 'Frame', 'Least Value')
('List', 'Frame', 'Comparison')
('List', 'Frame', 'Over Time')

('List', 'Type', 'All Values')
('List', 'Type', 'Unique Values')
('List', 'Type', 'Greatest Value')
('List', 'Type', 'Least Value')
('List', 'Type', 'Comparison')
('List', 'Type', 'Over Time')

('List', 'Color', 'All Values')
('List', 'Color', 'Unique Values')
('List', 'Color', 'Greatest Value')
('List', 'Color', 'Least Value')
('List', 'Color', 'Comparison')
('List', 'Color', 'Over Time')

('List', 'Speeds', 'All Values')
('List', 'Speeds', 'Unique Values')
('List', 'Speeds', 'Greatest Value')
('List', 'Speeds', 'Least Value')
('List', 'Speeds', 'Comparison')
('List', 'Speeds', 'Over Time')

('Graph', 'Date', 'All Values')
('Graph', 'Date', 'Unique Values')
('Graph', 'Date', 'Greatest Value')
('Graph', 'Date', 'Least Value')
('Graph', 'Date', 'Comparison')
('Graph', 'Date', 'Over Time')

('Graph', 'Day of Week', 'All Values')
('Graph', 'Day of Week', 'Unique Values')
('Graph', 'Day of Week', 'Greatest Value')
('Graph', 'Day of Week', 'Least Value')
('Graph', 'Day of Week', 'Comparison')
('Graph', 'Day of Week', 'Over Time')

('Graph', 'Time', 'All Values')
('Graph', 'Time', 'Unique Values')
('Graph', 'Time', 'Greatest Value')
('Graph', 'Time', 'Least Value')
('Graph', 'Time', 'Comparison')
('Graph', 'Time', 'Over Time')

('Graph', 'Location', 'All Values')
('Graph', 'Location', 'Unique Values')
('Graph', 'Location', 'Greatest Value')
('Graph', 'Location', 'Least Value')
('Graph', 'Location', 'Comparison')
('Graph', 'Location', 'Over Time')

('Graph', 'Record', 'All Values')
('Graph', 'Record', 'Unique Values')
('Graph', 'Record', 'Greatest Value')
('Graph', 'Record', 'Least Value')
('Graph', 'Record', 'Comparison')
('Graph', 'Record', 'Over Time')

('Graph', 'Reason', 'All Values')
('Graph', 'Reason', 'Unique Values')
('Graph', 'Reason', 'Greatest Value')
('Graph', 'Reason', 'Least Value')
('Graph', 'Reason', 'Comparison')
('Graph', 'Reason', 'Over Time')

('Graph', 'Make', 'All Values')
('Graph', 'Make', 'Unique Values')
('Graph', 'Make', 'Greatest Value')
('Graph', 'Make', 'Least Value')
('Graph', 'Make', 'Comparison')
('Graph', 'Make', 'Over Time')

('Graph', 'Model', 'All Values')
('Graph', 'Model', 'Unique Values')
('Graph', 'Model', 'Greatest Value')
('Graph', 'Model', 'Least Value')
('Graph', 'Model', 'Comparison')
('Graph', 'Model', 'Over Time')

('Graph', 'Frame', 'All Values')
('Graph', 'Frame', 'Unique Values')
('Graph', 'Frame', 'Greatest Value')
('Graph', 'Frame', 'Least Value')
('Graph', 'Frame', 'Comparison')
('Graph', 'Frame', 'Over Time')

('Graph', 'Type', 'All Values')
('Graph', 'Type', 'Unique Values')
('Graph', 'Type', 'Greatest Value')
('Graph', 'Type', 'Least Value')
('Graph', 'Type', 'Comparison')
('Graph', 'Type', 'Over Time')

('Graph', 'Color', 'All Values')
('Graph', 'Color', 'Unique Values')
('Graph', 'Color', 'Greatest Value')
('Graph', 'Color', 'Least Value')
('Graph', 'Color', 'Comparison')
('Graph', 'Color', 'Over Time')

('Graph', 'Speeds', 'All Values')
('Graph', 'Speeds', 'Unique Values')
('Graph', 'Speeds', 'Greatest Value')
('Graph', 'Speeds', 'Least Value')
('Graph', 'Speeds', 'Comparison')
('Graph', 'Speeds', 'Over Time')

('Date', 'Day of Week', 'All Values')
('Date', 'Day of Week', 'Unique Values')
('Date', 'Day of Week', 'Greatest Value')
('Date', 'Day of Week', 'Least Value')
('Date', 'Day of Week', 'Comparison')
('Date', 'Day of Week', 'Over Time')

('Date', 'Time', 'All Values')
('Date', 'Time', 'Unique Values')
('Date', 'Time', 'Greatest Value')
('Date', 'Time', 'Least Value')
('Date', 'Time', 'Comparison')
('Date', 'Time', 'Over Time')

('Date', 'Location', 'All Values')
('Date', 'Location', 'Unique Values')
('Date', 'Location', 'Greatest Value')
('Date', 'Location', 'Least Value')
('Date', 'Location', 'Comparison')
('Date', 'Location', 'Over Time')

('Date', 'Record', 'All Values')
('Date', 'Record', 'Unique Values')
('Date', 'Record', 'Greatest Value')
('Date', 'Record', 'Least Value')
('Date', 'Record', 'Comparison')
('Date', 'Record', 'Over Time')

('Date', 'Reason', 'All Values')
('Date', 'Reason', 'Unique Values')
('Date', 'Reason', 'Greatest Value')
('Date', 'Reason', 'Least Value')
('Date', 'Reason', 'Comparison')
('Date', 'Reason', 'Over Time')

('Date', 'Make', 'All Values')
('Date', 'Make', 'Unique Values')
('Date', 'Make', 'Greatest Value')
('Date', 'Make', 'Least Value')
('Date', 'Make', 'Comparison')
('Date', 'Make', 'Over Time')

('Date', 'Model', 'All Values')
('Date', 'Model', 'Unique Values')
('Date', 'Model', 'Greatest Value')
('Date', 'Model', 'Least Value')
('Date', 'Model', 'Comparison')
('Date', 'Model', 'Over Time')

('Date', 'Frame', 'All Values')
('Date', 'Frame', 'Unique Values')
('Date', 'Frame', 'Greatest Value')
('Date', 'Frame', 'Least Value')
('Date', 'Frame', 'Comparison')
('Date', 'Frame', 'Over Time')

('Date', 'Type', 'All Values')
('Date', 'Type', 'Unique Values')
('Date', 'Type', 'Greatest Value')
('Date', 'Type', 'Least Value')
('Date', 'Type', 'Comparison')
('Date', 'Type', 'Over Time')

('Date', 'Color', 'All Values')
('Date', 'Color', 'Unique Values')
('Date', 'Color', 'Greatest Value')
('Date', 'Color', 'Least Value')
('Date', 'Color', 'Comparison')
('Date', 'Color', 'Over Time')

('Date', 'Speeds', 'All Values')
('Date', 'Speeds', 'Unique Values')
('Date', 'Speeds', 'Greatest Value')
('Date', 'Speeds', 'Least Value')
('Date', 'Speeds', 'Comparison')
('Date', 'Speeds', 'Over Time')

('Date', 'All Values', 'Comparison')
('Date', 'All Values', 'Over Time')
('Date', 'Unique Values', 'Greatest Value')
('Date', 'Unique Values', 'Least Value')
('Date', 'Unique Values', 'Comparison')
('Date', 'Unique Values', 'Over Time')

('Date', 'Greatest Value', 'Least Value')
('Date', 'Greatest Value', 'Comparison')
('Date', 'Greatest Value', 'Over Time')
('Date', 'Least Value', 'Comparison')
('Date', 'Least Value', 'Over Time')
('Date', 'Comparison', 'Over Time')

('Day of Week', 'Time', 'All Values')
('Day of Week', 'Time', 'Unique Values')
('Day of Week', 'Time', 'Greatest Value')
('Day of Week', 'Time', 'Least Value')
('Day of Week', 'Time', 'Comparison')
('Day of Week', 'Time', 'Over Time')

('Day of Week', 'Location', 'All Values')
('Day of Week', 'Location', 'Unique Values')
('Day of Week', 'Location', 'Greatest Value')
('Day of Week', 'Location', 'Least Value')
('Day of Week', 'Location', 'Comparison')
('Day of Week', 'Location', 'Over Time')

('Day of Week', 'Record', 'All Values')
('Day of Week', 'Record', 'Unique Values')
('Day of Week', 'Record', 'Greatest Value')
('Day of Week', 'Record', 'Least Value')
('Day of Week', 'Record', 'Comparison')
('Day of Week', 'Record', 'Over Time')

('Day of Week', 'Reason', 'All Values')
('Day of Week', 'Reason', 'Unique Values')
('Day of Week', 'Reason', 'Greatest Value')
('Day of Week', 'Reason', 'Least Value')
('Day of Week', 'Reason', 'Comparison')
('Day of Week', 'Reason', 'Over Time')

('Day of Week', 'Make', 'All Values')
('Day of Week', 'Make', 'Unique Values')
('Day of Week', 'Make', 'Greatest Value')
('Day of Week', 'Make', 'Least Value')
('Day of Week', 'Make', 'Comparison')
('Day of Week', 'Make', 'Over Time')

('Day of Week', 'Model', 'All Values')
('Day of Week', 'Model', 'Unique Values')
('Day of Week', 'Model', 'Greatest Value')
('Day of Week', 'Model', 'Least Value')
('Day of Week', 'Model', 'Comparison')
('Day of Week', 'Model', 'Over Time')

('Day of Week', 'Frame', 'All Values')
('Day of Week', 'Frame', 'Unique Values')
('Day of Week', 'Frame', 'Greatest Value')
('Day of Week', 'Frame', 'Least Value')
('Day of Week', 'Frame', 'Comparison')
('Day of Week', 'Frame', 'Over Time')

('Day of Week', 'Type', 'All Values')
('Day of Week', 'Type', 'Unique Values')
('Day of Week', 'Type', 'Greatest Value')
('Day of Week', 'Type', 'Least Value')
('Day of Week', 'Type', 'Comparison')
('Day of Week', 'Type', 'Over Time')

('Day of Week', 'Color', 'All Values')
('Day of Week', 'Color', 'Unique Values')
('Day of Week', 'Color', 'Greatest Value')
('Day of Week', 'Color', 'Least Value')
('Day of Week', 'Color', 'Comparison')
('Day of Week', 'Color', 'Over Time')

('Day of Week', 'Speeds', 'All Values')
('Day of Week', 'Speeds', 'Unique Values')
('Day of Week', 'Speeds', 'Greatest Value')
('Day of Week', 'Speeds', 'Least Value')
('Day of Week', 'Speeds', 'Comparison')
('Day of Week', 'Speeds', 'Over Time')

('Day of Week', 'All Values', 'Comparison')
('Day of Week', 'All Values', 'Over Time')
('Day of Week', 'Unique Values', 'Greatest Value')
('Day of Week', 'Unique Values', 'Least Value')
('Day of Week', 'Unique Values', 'Comparison')
('Day of Week', 'Unique Values', 'Over Time')

('Day of Week', 'Greatest Value', 'Comparison')
('Day of Week', 'Greatest Value', 'Over Time')
('Day of Week', 'Least Value', 'Comparison')
('Day of Week', 'Least Value', 'Over Time')
('Day of Week', 'Comparison', 'Over Time')

('Time', 'Location', 'All Values')
('Time', 'Location', 'Unique Values')
('Time', 'Location', 'Greatest Value')
('Time', 'Location', 'Least Value')
('Time', 'Location', 'Comparison')
('Time', 'Location', 'Over Time')

('Time', 'Record', 'All Values')
('Time', 'Record', 'Unique Values')
('Time', 'Record', 'Greatest Value')
('Time', 'Record', 'Least Value')
('Time', 'Record', 'Comparison')
('Time', 'Record', 'Over Time')

('Time', 'Reason', 'All Values')
('Time', 'Reason', 'Unique Values')
('Time', 'Reason', 'Greatest Value')
('Time', 'Reason', 'Least Value')
('Time', 'Reason', 'Comparison')
('Time', 'Reason', 'Over Time')

('Time', 'Make', 'All Values')
('Time', 'Make', 'Unique Values')
('Time', 'Make', 'Greatest Value')
('Time', 'Make', 'Least Value')
('Time', 'Make', 'Comparison')
('Time', 'Make', 'Over Time')

('Time', 'Model', 'All Values')
('Time', 'Model', 'Unique Values')
('Time', 'Model', 'Greatest Value')
('Time', 'Model', 'Least Value')
('Time', 'Model', 'Comparison')
('Time', 'Model', 'Over Time')

('Time', 'Frame', 'All Values')
('Time', 'Frame', 'Unique Values')
('Time', 'Frame', 'Greatest Value')
('Time', 'Frame', 'Least Value')
('Time', 'Frame', 'Comparison')
('Time', 'Frame', 'Over Time')

('Time', 'Type', 'All Values')
('Time', 'Type', 'Unique Values')
('Time', 'Type', 'Greatest Value')
('Time', 'Type', 'Least Value')
('Time', 'Type', 'Comparison')
('Time', 'Type', 'Over Time')

('Time', 'Color', 'All Values')
('Time', 'Color', 'Unique Values')
('Time', 'Color', 'Greatest Value')
('Time', 'Color', 'Least Value')
('Time', 'Color', 'Comparison')
('Time', 'Color', 'Over Time')

('Time', 'Speeds', 'All Values')
('Time', 'Speeds', 'Unique Values')
('Time', 'Speeds', 'Greatest Value')
('Time', 'Speeds', 'Least Value')
('Time', 'Speeds', 'Comparison')
('Time', 'Speeds', 'Over Time')

('Time', 'All Values', 'Comparison')
('Time', 'All Values', 'Over Time')
('Time', 'Unique Values', 'Greatest Value')
('Time', 'Unique Values', 'Least Value')
('Time', 'Unique Values', 'Comparison')
('Time', 'Unique Values', 'Over Time')

('Time', 'Greatest Value', 'Comparison')
('Time', 'Greatest Value', 'Over Time')
('Time', 'Least Value', 'Comparison')
('Time', 'Least Value', 'Over Time')
('Time', 'Comparison', 'Over Time')

('Location', 'Record', 'All Values')
('Location', 'Record', 'Unique Values')
('Location', 'Record', 'Greatest Value')
('Location', 'Record', 'Least Value')
('Location', 'Record', 'Comparison')
('Location', 'Record', 'Over Time')

('Location', 'Reason', 'All Values')
('Location', 'Reason', 'Unique Values')
('Location', 'Reason', 'Greatest Value')
('Location', 'Reason', 'Least Value')
('Location', 'Reason', 'Comparison')
('Location', 'Reason', 'Over Time')

('Location', 'Make', 'All Values')
('Location', 'Make', 'Unique Values')
('Location', 'Make', 'Greatest Value')
('Location', 'Make', 'Least Value')
('Location', 'Make', 'Comparison')
('Location', 'Make', 'Over Time')

('Location', 'Model', 'All Values')
('Location', 'Model', 'Unique Values')
('Location', 'Model', 'Greatest Value')
('Location', 'Model', 'Least Value')
('Location', 'Model', 'Comparison')
('Location', 'Model', 'Over Time')

('Location', 'Frame', 'All Values')
('Location', 'Frame', 'Unique Values')
('Location', 'Frame', 'Greatest Value')
('Location', 'Frame', 'Least Value')
('Location', 'Frame', 'Comparison')
('Location', 'Frame', 'Over Time')

('Location', 'Type', 'All Values')
('Location', 'Type', 'Unique Values')
('Location', 'Type', 'Greatest Value')
('Location', 'Type', 'Least Value')
('Location', 'Type', 'Comparison')
('Location', 'Type', 'Over Time')

('Location', 'Color', 'All Values')
('Location', 'Color', 'Unique Values')
('Location', 'Color', 'Greatest Value')
('Location', 'Color', 'Least Value')
('Location', 'Color', 'Comparison')
('Location', 'Color', 'Over Time')

('Location', 'Speeds', 'All Values')
('Location', 'Speeds', 'Unique Values')
('Location', 'Speeds', 'Greatest Value')
('Location', 'Speeds', 'Least Value')
('Location', 'Speeds', 'Comparison')
('Location', 'Speeds', 'Over Time')

('Location', 'All Values', 'Comparison')
('Location', 'All Values', 'Over Time')
('Location', 'Unique Values', 'Greatest Value')
('Location', 'Unique Values', 'Least Value')
('Location', 'Unique Values', 'Comparison')
('Location', 'Unique Values', 'Over Time')

('Location', 'Greatest Value', 'Comparison')
('Location', 'Greatest Value', 'Over Time')
('Location', 'Least Value', 'Comparison')
('Location', 'Least Value', 'Over Time')
('Location', 'Comparison', 'Over Time')

('Record', 'Reason', 'All Values')
('Record', 'Reason', 'Unique Values')
('Record', 'Reason', 'Greatest Value')
('Record', 'Reason', 'Least Value')
('Record', 'Reason', 'Comparison')
('Record', 'Reason', 'Over Time')

('Record', 'Make', 'All Values')
('Record', 'Make', 'Unique Values')
('Record', 'Make', 'Greatest Value')
('Record', 'Make', 'Least Value')
('Record', 'Make', 'Comparison')
('Record', 'Make', 'Over Time')

('Record', 'Model', 'All Values')
('Record', 'Model', 'Unique Values')
('Record', 'Model', 'Greatest Value')
('Record', 'Model', 'Least Value')
('Record', 'Model', 'Comparison')
('Record', 'Model', 'Over Time')

('Record', 'Frame', 'All Values')
('Record', 'Frame', 'Unique Values')
('Record', 'Frame', 'Greatest Value')
('Record', 'Frame', 'Least Value')
('Record', 'Frame', 'Comparison')
('Record', 'Frame', 'Over Time')

('Record', 'Type', 'All Values')
('Record', 'Type', 'Unique Values')
('Record', 'Type', 'Greatest Value')
('Record', 'Type', 'Least Value')
('Record', 'Type', 'Comparison')
('Record', 'Type', 'Over Time')

('Record', 'Color', 'All Values')
('Record', 'Color', 'Unique Values')
('Record', 'Color', 'Greatest Value')
('Record', 'Color', 'Least Value')
('Record', 'Color', 'Comparison')
('Record', 'Color', 'Over Time')

('Record', 'Speeds', 'All Values')
('Record', 'Speeds', 'Unique Values')
('Record', 'Speeds', 'Greatest Value')
('Record', 'Speeds', 'Least Value')
('Record', 'Speeds', 'Comparison')
('Record', 'Speeds', 'Over Time')

('Record', 'All Values', 'Comparison')
('Record', 'All Values', 'Over Time')
('Record', 'Unique Values', 'Greatest Value')
('Record', 'Unique Values', 'Least Value')
('Record', 'Unique Values', 'Comparison')
('Record', 'Unique Values', 'Over Time')

('Record', 'Greatest Value', 'Comparison')
('Record', 'Greatest Value', 'Over Time')
('Record', 'Least Value', 'Comparison')
('Record', 'Least Value', 'Over Time')
('Record', 'Comparison', 'Over Time')

('Reason', 'Make', 'All Values')
('Reason', 'Make', 'Unique Values')
('Reason', 'Make', 'Greatest Value')
('Reason', 'Make', 'Least Value')
('Reason', 'Make', 'Comparison')
('Reason', 'Make', 'Over Time')

('Reason', 'Model', 'All Values')
('Reason', 'Model', 'Unique Values')
('Reason', 'Model', 'Greatest Value')
('Reason', 'Model', 'Least Value')
('Reason', 'Model', 'Comparison')
('Reason', 'Model', 'Over Time')

('Reason', 'Frame', 'All Values')
('Reason', 'Frame', 'Unique Values')
('Reason', 'Frame', 'Greatest Value')
('Reason', 'Frame', 'Least Value')
('Reason', 'Frame', 'Comparison')
('Reason', 'Frame', 'Over Time')

('Reason', 'Type', 'All Values')
('Reason', 'Type', 'Unique Values')
('Reason', 'Type', 'Greatest Value')
('Reason', 'Type', 'Least Value')
('Reason', 'Type', 'Comparison')
('Reason', 'Type', 'Over Time')

('Reason', 'Color', 'All Values')
('Reason', 'Color', 'Unique Values')
('Reason', 'Color', 'Greatest Value')
('Reason', 'Color', 'Least Value')
('Reason', 'Color', 'Comparison')
('Reason', 'Color', 'Over Time')

('Reason', 'Speeds', 'All Values')
('Reason', 'Speeds', 'Unique Values')
('Reason', 'Speeds', 'Greatest Value')
('Reason', 'Speeds', 'Least Value')
('Reason', 'Speeds', 'Comparison')
('Reason', 'Speeds', 'Over Time')

('Reason', 'All Values', 'Comparison')
('Reason', 'All Values', 'Over Time')
('Reason', 'Unique Values', 'Greatest Value')
('Reason', 'Unique Values', 'Least Value')
('Reason', 'Unique Values', 'Comparison')
('Reason', 'Unique Values', 'Over Time')

('Reason', 'Greatest Value', 'Comparison')
('Reason', 'Greatest Value', 'Over Time')
('Reason', 'Least Value', 'Comparison')
('Reason', 'Least Value', 'Over Time')
('Reason', 'Comparison', 'Over Time')

('Make', 'Model', 'All Values')
('Make', 'Model', 'Unique Values')
('Make', 'Model', 'Greatest Value')
('Make', 'Model', 'Least Value')
('Make', 'Model', 'Comparison')
('Make', 'Model', 'Over Time')

('Make', 'Frame', 'All Values')
('Make', 'Frame', 'Unique Values')
('Make', 'Frame', 'Greatest Value')
('Make', 'Frame', 'Least Value')
('Make', 'Frame', 'Comparison')
('Make', 'Frame', 'Over Time')

('Make', 'Type', 'All Values')
('Make', 'Type', 'Unique Values')
('Make', 'Type', 'Greatest Value')
('Make', 'Type', 'Least Value')
('Make', 'Type', 'Comparison')
('Make', 'Type', 'Over Time')

('Make', 'Color', 'All Values')
('Make', 'Color', 'Unique Values')
('Make', 'Color', 'Greatest Value')
('Make', 'Color', 'Least Value')
('Make', 'Color', 'Comparison')
('Make', 'Color', 'Over Time')

('Make', 'Speeds', 'All Values')
('Make', 'Speeds', 'Unique Values')
('Make', 'Speeds', 'Greatest Value')
('Make', 'Speeds', 'Least Value')
('Make', 'Speeds', 'Comparison')
('Make', 'Speeds', 'Over Time')

('Make', 'All Values', 'Comparison')
('Make', 'All Values', 'Over Time')
('Make', 'Unique Values', 'Greatest Value')
('Make', 'Unique Values', 'Least Value')
('Make', 'Unique Values', 'Comparison')
('Make', 'Unique Values', 'Over Time')

('Make', 'Greatest Value', 'Comparison')
('Make', 'Greatest Value', 'Over Time')
('Make', 'Least Value', 'Comparison')
('Make', 'Least Value', 'Over Time')
('Make', 'Comparison', 'Over Time')

('Model', 'Frame', 'All Values')
('Model', 'Frame', 'Unique Values')
('Model', 'Frame', 'Greatest Value')
('Model', 'Frame', 'Least Value')
('Model', 'Frame', 'Comparison')
('Model', 'Frame', 'Over Time')

('Model', 'Type', 'All Values')
('Model', 'Type', 'Unique Values')
('Model', 'Type', 'Greatest Value')
('Model', 'Type', 'Least Value')
('Model', 'Type', 'Comparison')
('Model', 'Type', 'Over Time')

('Model', 'Color', 'All Values')
('Model', 'Color', 'Unique Values')
('Model', 'Color', 'Greatest Value')
('Model', 'Color', 'Least Value')
('Model', 'Color', 'Comparison')
('Model', 'Color', 'Over Time')

('Model', 'Speeds', 'All Values')
('Model', 'Speeds', 'Unique Values')
('Model', 'Speeds', 'Greatest Value')
('Model', 'Speeds', 'Least Value')
('Model', 'Speeds', 'Comparison')
('Model', 'Speeds', 'Over Time')

('Model', 'All Values', 'Comparison')
('Model', 'All Values', 'Over Time')
('Model', 'Unique Values', 'Greatest Value')
('Model', 'Unique Values', 'Least Value')
('Model', 'Unique Values', 'Comparison')
('Model', 'Unique Values', 'Over Time')

('Model', 'Greatest Value', 'Comparison')
('Model', 'Greatest Value', 'Over Time')
('Model', 'Least Value', 'Comparison')
('Model', 'Least Value', 'Over Time')
('Model', 'Comparison', 'Over Time')

('Frame', 'Type', 'All Values')
('Frame', 'Type', 'Unique Values')
('Frame', 'Type', 'Greatest Value')
('Frame', 'Type', 'Least Value')
('Frame', 'Type', 'Comparison')
('Frame', 'Type', 'Over Time')

('Frame', 'Color', 'All Values')
('Frame', 'Color', 'Unique Values')
('Frame', 'Color', 'Greatest Value')
('Frame', 'Color', 'Least Value')
('Frame', 'Color', 'Comparison')
('Frame', 'Color', 'Over Time')

('Frame', 'Speeds', 'All Values')
('Frame', 'Speeds', 'Unique Values')
('Frame', 'Speeds', 'Greatest Value')
('Frame', 'Speeds', 'Least Value')
('Frame', 'Speeds', 'Comparison')
('Frame', 'Speeds', 'Over Time')

('Frame', 'All Values', 'Comparison')
('Frame', 'All Values', 'Over Time')
('Frame', 'Unique Values', 'Greatest Value')
('Frame', 'Unique Values', 'Least Value')
('Frame', 'Unique Values', 'Comparison')
('Frame', 'Unique Values', 'Over Time')

('Frame', 'Greatest Value', 'Comparison')
('Frame', 'Greatest Value', 'Over Time')
('Frame', 'Least Value', 'Comparison')
('Frame', 'Least Value', 'Over Time')
('Frame', 'Comparison', 'Over Time')

('Type', 'Color', 'All Values')
('Type', 'Color', 'Unique Values')
('Type', 'Color', 'Greatest Value')
('Type', 'Color', 'Least Value')
('Type', 'Color', 'Comparison')
('Type', 'Color', 'Over Time')

('Type', 'Speeds', 'All Values')
('Type', 'Speeds', 'Unique Values')
('Type', 'Speeds', 'Greatest Value')
('Type', 'Speeds', 'Least Value')
('Type', 'Speeds', 'Comparison')
('Type', 'Speeds', 'Over Time')

('Type', 'All Values', 'Comparison')
('Type', 'All Values', 'Over Time')
('Type', 'Unique Values', 'Greatest Value')
('Type', 'Unique Values', 'Least Value')
('Type', 'Unique Values', 'Comparison')
('Type', 'Unique Values', 'Over Time')

('Type', 'Greatest Value', 'Comparison')
('Type', 'Greatest Value', 'Over Time')
('Type', 'Least Value', 'Comparison')
('Type', 'Least Value', 'Over Time')
('Type', 'Comparison', 'Over Time')

('Color', 'Speeds', 'All Values')
('Color', 'Speeds', 'Unique Values')
('Color', 'Speeds', 'Greatest Value')
('Color', 'Speeds', 'Least Value')
('Color', 'Speeds', 'Comparison')
('Color', 'Speeds', 'Over Time')

('Color', 'All Values', 'Comparison')
('Color', 'All Values', 'Over Time')
('Color', 'Unique Values', 'Greatest Value')
('Color', 'Unique Values', 'Least Value')
('Color', 'Unique Values', 'Comparison')
('Color', 'Unique Values', 'Over Time')

('Color', 'Greatest Value', 'Comparison')
('Color', 'Greatest Value', 'Over Time')
('Color', 'Least Value', 'Comparison')
('Color', 'Least Value', 'Over Time')
('Color', 'Comparison', 'Over Time')

('Speeds', 'All Values', 'Comparison')
('Speeds', 'All Values', 'Over Time')
('Speeds', 'Unique Values', 'Greatest Value')
('Speeds', 'Unique Values', 'Least Value')
('Speeds', 'Unique Values', 'Comparison')
('Speeds', 'Unique Values', 'Over Time')

('Speeds', 'Greatest Value', 'Comparison')
('Speeds', 'Greatest Value', 'Over Time')
('Speeds', 'Least Value', 'Comparison')
('Speeds', 'Least Value', 'Over Time')
('Speeds', 'Comparison', 'Over Time')












