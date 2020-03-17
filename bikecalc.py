# bikecalc.py

from tkinter import *
import math
import time
from collections import Counter
import csv
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import operator

bikes = open('bikes.csv',encoding= 'unicode_escape')
reader = csv.reader(bikes)

record_header = [] #column [0]
date_header = [] #column [1]
day_header = [] #column [2]
time_header = [] #column [3]
location_header = [] #column [4]
reason_header = [] #column [5]
make_header = [] #column [6]
model_header = [] #column [7]
frame_header = [] #column [8]
bike_type_header = [] #column [9]
color_header = [] #column [10]
speeds_header = [] #column [11]

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

######### FUNCTIONS ##########
def count_all_values(dictselection):
    count = 0
    for i in dictselection.values():
        if i == "":
            pass
        else:
            count = count + 1
    # a = (f"Count of all values: {count}\n")
    print(f"Count of all values: {count}\n")
    # results_printed = str(a)
    # results_printed_input_text.set(results_printed)
    print("")

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
    print(f"Count of all unique values: {count}\n")
    print(Counter(dictselection.values()))
    # a = (f"Count of all unique values: {count}\n")
    # b = (Counter(dictselection.values()))
    # results_printed = str(a)
    # results_printed_input_text.set(results_printed)
    # results_printed = str(b)
    # results_printed_input_text.set(results_printed)
    print("")


def count_greatest_value(dictselection):
    count = 1
    print(f"Count total: {count}\n")
    data_breakdown = Counter(dictselection.values())
    greatest_value = data_breakdown.most_common(1)
    greatest_value_list = [item for i in greatest_value for item in i]
    print("Info: '"+greatest_value_list[0] +"', Value: " +str(greatest_value_list[1]))
    print("")
def count_least_value(dictselection):
    count = 1
    print(f"Count total: {count}\n")
    data_breakdown = Counter(dictselection.values())
    least_value = data_breakdown.most_common()[:-2:-1]
    least_value_list = [item for i in least_value for item in i]
    print("Info: '"+least_value_list[0] +"', Value: " +str(least_value_list[1]))
    print("")
def count_over_time(dictselection):
    print("Sorry, calculation is too large to complete. Try graphing over time instead.")
def count_comparison(dictselection):
    count = 0
    for i in dictselection.values():
        if i == "":
            pass
        else:
            count = count + 1
    print(f"Comparison of all values: {count}\n")
    print(Counter(dictselection.values()))
    print("")
def list_all_values(dictselection):
    all_values = []
    for i in dictselection.values():
        if i == "":
            pass
        else:
            all_values.append(i)
    # unique_values.sort()
    print(f"List of all values: {all_values}\n")
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
    print(f"List of all unique values: {unique_values}\n")
def list_greatest_value(dictselection):
    data_breakdown = Counter(dictselection.values())
    greatest_value = data_breakdown.most_common(1)
    print("Greatest value: "+greatest_value[0][0])
    print("")
def list_least_value(dictselection):
    data_breakdown = Counter(dictselection.values())
    least_value = data_breakdown.most_common()[:-2:-1]
    print("Least value: "+least_value[0][0])
    print("")
def list_over_time(dictselection):
    print("Sorry, calculation is too large to complete.")
def list_comparison(dictselection):
    count = 0
    for i in dictselection.values():
        if i == "":
            pass
        else:
            count = count + 1
    print(f"Comparison of all values as % of total: \n")

    data_breakdown = Counter(dictselection.values())
    # print(type(a))
    def Convert(tup, di): 
        di = dict(tup) 
        return di 
    percent_values = data_breakdown.most_common(count)
    dictionary = {} 
    percent_values_dict = Convert(percent_values, dictionary)
    # print(b_dict)
    for i in percent_values_dict:
        percent_values_dict[i] = (percent_values_dict[i]/count)*100
        percent_values_dict[i] = ("%.2f" % percent_values_dict[i])
    # print(type(b_dict))
    print(percent_values_dict)
    print("")
def graph_all_values(dictselection):
    print("Sorry, calculation is too large to complete. Try graphing 'Unique Values' instead.")
def graph_unique_values(dictselection):
    count = 0
    for i in dictselection.values():
        if i == "":
            pass
        else:
            count = count + 1
    # print(count)
    print("")
    data_breakdown = Counter(dictselection.values())
    def Convert(tup, di): 
        di = dict(tup) 
        return di 
    greatest_values = data_breakdown.most_common(count)
    dictionary = {} 
    greatest_values_dict = Convert(greatest_values, dictionary)
    
    bike_info = greatest_values_dict.keys()
    amount = greatest_values_dict.values()
    y_pos = np.arange(len(bike_info))

    plt.bar(y_pos, amount, align='center', alpha=0.5)
    plt.xticks(y_pos, bike_info)
    plt.ylabel('Count of Value')
    plt.title('Unique Values')
    plt.show()
def graph_greatest_value(dictselection):
    count = 0
    for i in dictselection.values():
        if i == "":
            pass
        else:
            count = count + 1
    data_breakdown = Counter(dictselection.values())
    def Convert(tup, di): 
        di = dict(tup) 
        return di
    greatest_values = data_breakdown.most_common(count)
    largest = data_breakdown.most_common(1)
    dictionary = {} 
    greatest_values_dict = Convert(greatest_values, dictionary)    
    largest_dict = Convert(largest, dictionary)

    largest_dict_values_list = [i for i in largest_dict.values()]
    strings = [str(largest_dict_values_list) for largest_dict_values_list in largest_dict_values_list]
    value_string = "".join(strings)
    value_integer = int(value_string)

    largest_dict_keys_list = [i for i in largest_dict]
    strings = [str(largest_dict_keys_list) for largest_dict_keys_list in largest_dict_keys_list]
    key_string = "".join(strings)

    bike_info = ["Largest Value"] #list(greatest_values_dict.values()) #[2014, 2015, 2016, 2017, 2018, 2019]  
    largest_bike = largest_dict_values_list #[39, 117, 98, 54, 28, 15]  
    total_minus_large = count - value_integer
    rest = []
    rest.append(total_minus_large)
    plt.bar(bike_info, largest_bike, color="blue")
    plt.bar(bike_info, rest, bottom=largest_bike, color="orange")
    plt.xlabel(f"Info: {key_string}, Largest Value: {value_integer}")
    plt.ylabel('Value Count')
    plt.title("Largest Value vs. Rest of Values")
    plt.show()
def graph_least_value(dictselection):
    count = 0
    for i in dictselection.values():
        if i == "":
            pass
        else:
            count = count + 1
    data_breakdown = Counter(dictselection.values())
    def Convert(tup, di): 
        di = dict(tup) 
        return di
    least_values = data_breakdown.most_common(count)
    least = data_breakdown.most_common()[:-2:-1]
    dictionary = {} 
    least_values_dict = Convert(least_values, dictionary)    
    least_dict = Convert(least, dictionary)

    least_dict_values_list = [i for i in least_dict.values()]
    strings = [str(least_dict_values_list) for least_dict_values_list in least_dict_values_list]
    value_string = "".join(strings)
    value_integer = int(value_string)

    least_dict_keys_list = [i for i in least_dict]
    strings = [str(least_dict_keys_list) for least_dict_keys_list in least_dict_keys_list]
    key_string = "".join(strings)

    bike_info = ["Least Value"] #list(greatest_values_dict.values()) #[2014, 2015, 2016, 2017, 2018, 2019]  
    least_bike = least_dict_values_list #[39, 117, 98, 54, 28, 15]  
    total_minus_least = count - value_integer
    rest = []
    rest.append(total_minus_least)
    plt.bar(bike_info, least_bike, color="blue")
    plt.bar(bike_info, rest, bottom=least_bike, color="orange")
    plt.xlabel(f"Info: {key_string}, Least Value: {value_integer}")
    plt.ylabel('Value Count')
    plt.title("Least Value vs. Rest of Values")
    plt.show()
def graph_over_time(dictselection):
    fig1 = px.scatter(x=list(date_dict.values()), y=list(dictselection.values()))#.sort())
    fig1.update_layout(title="Bike Impounds Over Time", xaxis_title="Time",yaxis_title="Count")
    fig1.show()
def graph_comparison(dictselection):
    count = 0
    for i in dictselection.values():
        if i == "":
            pass
        else:
            count = count + 1
    # print(count)
    print("")
    data_breakdown = Counter(dictselection.values())
    def Convert(tup, di): 
        di = dict(tup) 
        return di 
    greatest_values = data_breakdown.most_common(count)
    dictionary = {} 
    greatest_values_dict = Convert(greatest_values, dictionary)
    # print(type(greatest_values_dict))
    # print(greatest_values_dict)
    # print("")

    labels = greatest_values_dict.keys()
    sizes = greatest_values_dict.values()
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

######### TKINTER FUNCTIONS ##########
bikeinfo_value = ""
datatype_value = ""
datarep_value = ""
result_value = ""
results_printed_value = ""
datarep_list = ["Count","List","Graph"]
bikeinfo_list = ["Date","Day of Week","Time","Location","Record","Reason","Make","Model","Frame","Type","Color","Speeds"]
datatype_list = ["All Values","Unique Values","Greatest Value","Least Value","Comparison","Over Time"]

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
    global results_printed_value
    results_printed_value = ""
    results_printed_input_text.set("")
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
def combo_button_press():
    print("")
    print("Buttons Pressed:")
    print(f"'{result_list[0]}', '{result_list[1]}', '{result_list[2]}'")
    print("")
    if "Count" in result_list:                          ####### COUNT ####### done
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
                count_all_values(record_dict)
            elif "Reason" in result_list:
                count_all_values(reason_dict)
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
            else:
                print("Sorry, unable to perform this calculation.")
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
                count_unique_values(record_dict)
            elif "Reason" in result_list:
                count_unique_values(reason_dict)
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
            else:
                print("Sorry, unable to perform this calculation.")
        elif "Greatest Value" in result_list:
            if "Date" in result_list:
                count_greatest_value(date_dict)
            elif "Day of Week" in result_list:
                count_greatest_value(day_dict)
            elif "Time" in result_list:
                count_greatest_value(time_dict)
            elif "Location" in result_list:
                count_greatest_value(location_dict)
            elif "Record" in result_list:
                count_greatest_value(record_dict)
            elif "Reason" in result_list:
                count_greatest_value(reason_dict)
            elif "Make" in result_list:
                count_greatest_value(make_dict)
            elif "Model" in result_list:
                count_greatest_value(model_dict)
            elif "Frame" in result_list:
                count_greatest_value(frame_dict)
            elif "Type" in result_list:
                count_greatest_value(bike_type_dict)
            elif "Color" in result_list:
                count_greatest_value(color_dict)
            elif "Speeds" in result_list:
                count_greatest_value(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        elif "Least Value" in result_list:
            if "Date" in result_list:
                count_least_value(date_dict)
            elif "Day of Week" in result_list:
                count_least_value(day_dict)
            elif "Time" in result_list:
                count_least_value(time_dict)
            elif "Location" in result_list:
                count_least_value(location_dict)
            elif "Record" in result_list:
                count_least_value(record_dict)
            elif "Reason" in result_list:
                count_least_value(reason_dict)
            elif "Make" in result_list:
                count_least_value(make_dict)
            elif "Model" in result_list:
                count_least_value(model_dict)
            elif "Frame" in result_list:
                count_least_value(frame_dict)
            elif "Type" in result_list:
                count_least_value(bike_type_dict)
            elif "Color" in result_list:
                count_least_value(color_dict)
            elif "Speeds" in result_list:
                count_least_value(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        elif "Comparison" in result_list:
            if "Date" in result_list:
                count_comparison(date_dict)
            elif "Day of Week" in result_list:
                count_comparison(day_dict)
            elif "Time" in result_list:
                count_comparison(time_dict)
            elif "Location" in result_list:
                count_comparison(location_dict)
            elif "Record" in result_list:
                count_comparison(record_dict)
            elif "Reason" in result_list:
                count_comparison(reason_dict)
            elif "Make" in result_list:
                count_comparison(make_dict)
            elif "Model" in result_list:
                count_comparison(model_dict)
            elif "Frame" in result_list:
                count_comparison(frame_dict)
            elif "Type" in result_list:
                count_comparison(bike_type_dict)
            elif "Color" in result_list:
                count_comparison(color_dict)
            elif "Speeds" in result_list:
                count_comparison(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        elif "Over Time" in result_list:
            if "Date" in result_list:
                count_over_time(date_dict)
            elif "Day of Week" in result_list:
                count_over_time(day_dict)
            elif "Time" in result_list:
                count_over_time(time_dict)
            elif "Location" in result_list:
                count_over_time(location_dict)
            elif "Record" in result_list:
                count_over_time(record_dict)
            elif "Reason" in result_list:
                count_over_time(reason_dict)
            elif "Make" in result_list:
                count_over_time(make_dict)
            elif "Model" in result_list:
                count_over_time(model_dict)
            elif "Frame" in result_list:
                count_over_time(frame_dict)
            elif "Type" in result_list:
                count_over_time(bike_type_dict)
            elif "Color" in result_list:
                count_over_time(color_dict)
            elif "Speeds" in result_list:
                count_over_time(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        else:
            print("Sorry, unable to perform this calculation.")
    elif "List/Print" in result_list:                   ####### LIST/PRINT ####### done
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
                list_all_values(record_dict)
            elif "Reason" in result_list:
                list_all_values(reason_dict)
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
            else:
                print("Sorry, unable to perform this calculation.")
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
                list_unique_values(record_dict)
            elif "Reason" in result_list:
                list_unique_values(reason_dict)
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
            else:
                print("Sorry, unable to perform this calculation.")
        elif "Greatest Value" in result_list:
            if "Date" in result_list:
                list_greatest_value(date_dict)
            elif "Day of Week" in result_list:
                list_greatest_value(day_dict)
            elif "Time" in result_list:
                list_greatest_value(time_dict)
            elif "Location" in result_list:
                list_greatest_value(location_dict)
            elif "Record" in result_list:
                list_greatest_value(record_dict)
            elif "Reason" in result_list:
                list_greatest_value(reason_dict)
            elif "Make" in result_list:
                list_greatest_value(make_dict)
            elif "Model" in result_list:
                list_greatest_value(model_dict)
            elif "Frame" in result_list:
                list_greatest_value(frame_dict)
            elif "Type" in result_list:
                list_greatest_value(bike_type_dict)
            elif "Color" in result_list:
                list_greatest_value(color_dict)
            elif "Speeds" in result_list:
                list_greatest_value(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        elif "Least Value" in result_list:            
            if "Date" in result_list:
                list_least_value(date_dict)
            elif "Day of Week" in result_list:
                list_least_value(day_dict)
            elif "Time" in result_list:
                list_least_value(time_dict)
            elif "Location" in result_list:
                list_least_value(location_dict)
            elif "Record" in result_list:
                list_least_value(record_dict)
            elif "Reason" in result_list:
                list_least_value(reason_dict)
            elif "Make" in result_list:
                list_least_value(make_dict)
            elif "Model" in result_list:
                list_least_value(model_dict)
            elif "Frame" in result_list:
                list_least_value(frame_dict)
            elif "Type" in result_list:
                list_least_value(bike_type_dict)
            elif "Color" in result_list:
                list_least_value(color_dict)
            elif "Speeds" in result_list:
                list_least_value(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        elif "Comparison" in result_list:
            if "Date" in result_list:
                list_comparison(date_dict)
            elif "Day of Week" in result_list:
                list_comparison(day_dict)
            elif "Time" in result_list:
                list_comparison(time_dict)
            elif "Location" in result_list:
                list_comparison(location_dict)
            elif "Record" in result_list:
                list_comparison(record_dict)
            elif "Reason" in result_list:
                list_comparison(reason_dict)
            elif "Make" in result_list:
                list_comparison(make_dict)
            elif "Model" in result_list:
                list_comparison(model_dict)
            elif "Frame" in result_list:
                list_comparison(frame_dict)
            elif "Type" in result_list:
                list_comparison(bike_type_dict)
            elif "Color" in result_list:
                list_comparison(color_dict)
            elif "Speeds" in result_list:
                list_comparison(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        elif "Over Time" in result_list:
            if "Date" in result_list:
                list_over_time(date_dict)
            elif "Day of Week" in result_list:
                list_over_time(day_dict)
            elif "Time" in result_list:
                list_over_time(time_dict)
            elif "Location" in result_list:
                list_over_time(location_dict)
            elif "Record" in result_list:
                list_over_time(record_dict)
            elif "Reason" in result_list:
                list_over_time(reason_dict)
            elif "Make" in result_list:
                list_over_time(make_dict)
            elif "Model" in result_list:
                list_over_time(model_dict)
            elif "Frame" in result_list:
                list_over_time(frame_dict)
            elif "Type" in result_list:
                list_over_time(bike_type_dict)
            elif "Color" in result_list:
                list_over_time(color_dict)
            elif "Speeds" in result_list:
                list_over_time(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        else:
            print("Sorry, unable to perform this calculation.")
    elif "Graph" in result_list:                        ####### GRAPH ####### done
        if "All Values" in result_list:
            if "Date" in result_list:
                graph_all_values(date_dict)
            elif "Day of Week" in result_list:
                graph_all_values(day_dict)
            elif "Time" in result_list:
                graph_all_values(time_dict)
            elif "Location" in result_list:
                graph_all_values(location_dict)
            elif "Record" in result_list:
                graph_all_values(record_dict)
            elif "Reason" in result_list:
                graph_all_values(reason_dict)
            elif "Make" in result_list:
                graph_all_values(make_dict)
            elif "Model" in result_list:
                graph_all_values(model_dict)
            elif "Frame" in result_list:
                graph_all_values(frame_dict)
            elif "Type" in result_list:
                graph_all_values(bike_type_dict)
            elif "Color" in result_list:
                graph_all_values(color_dict)
            elif "Speeds" in result_list:
                graph_all_values(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        elif "Unique Values" in result_list:
            if "Date" in result_list:
                graph_unique_values(date_dict)
            elif "Day of Week" in result_list:
                graph_unique_values(day_dict)
            elif "Time" in result_list:
                graph_unique_values(time_dict)
            elif "Location" in result_list:
                graph_unique_values(location_dict)
            elif "Record" in result_list:
                graph_unique_values(record_dict)
            elif "Reason" in result_list:
                graph_unique_values(reason_dict)
            elif "Make" in result_list:
                graph_unique_values(make_dict)
            elif "Model" in result_list:
                graph_unique_values(model_dict)
            elif "Frame" in result_list:
                graph_unique_values(frame_dict)
            elif "Type" in result_list:
                graph_unique_values(bike_type_dict)
            elif "Color" in result_list:
                graph_unique_values(color_dict)
            elif "Speeds" in result_list:
                graph_unique_values(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        elif "Greatest Value" in result_list:
            if "Date" in result_list:
                graph_greatest_value(date_dict)
            elif "Day of Week" in result_list:
                graph_greatest_value(day_dict)
            elif "Time" in result_list:
                graph_greatest_value(time_dict)
            elif "Location" in result_list:
                graph_greatest_value(location_dict)
            elif "Record" in result_list:
                graph_greatest_value(record_dict)
            elif "Reason" in result_list:
                graph_greatest_value(reason_dict)
            elif "Make" in result_list:
                graph_greatest_value(make_dict)
            elif "Model" in result_list:
                graph_greatest_value(model_dict)
            elif "Frame" in result_list:
                graph_greatest_value(frame_dict)
            elif "Type" in result_list:
                graph_greatest_value(bike_type_dict)
            elif "Color" in result_list:
                graph_greatest_value(color_dict)
            elif "Speeds" in result_list:
                graph_greatest_value(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        elif "Least Value" in result_list:
            if "Date" in result_list:
                graph_least_value(date_dict)
            elif "Day of Week" in result_list:
                graph_least_value(day_dict)
            elif "Time" in result_list:
                graph_least_value(time_dict)
            elif "Location" in result_list:
                graph_least_value(location_dict)
            elif "Record" in result_list:
                graph_least_value(record_dict)
            elif "Reason" in result_list:
                graph_least_value(reason_dict)
            elif "Make" in result_list:
                graph_least_value(make_dict)
            elif "Model" in result_list:
                graph_least_value(model_dict)
            elif "Frame" in result_list:
                graph_least_value(frame_dict)
            elif "Type" in result_list:
                graph_least_value(bike_type_dict)
            elif "Color" in result_list:
                graph_least_value(color_dict)
            elif "Speeds" in result_list:
                graph_least_value(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        elif "Comparison" in result_list:
            if "Date" in result_list:
                graph_comparison(date_dict)
            elif "Day of Week" in result_list:
                graph_comparison(day_dict)
            elif "Time" in result_list:
                graph_comparison(time_dict)
            elif "Location" in result_list:
                graph_comparison(location_dict)
            elif "Record" in result_list:
                graph_comparison(record_dict)
            elif "Reason" in result_list:
                graph_comparison(reason_dict)
            elif "Make" in result_list:
                graph_comparison(make_dict)
            elif "Model" in result_list:
                graph_comparison(model_dict)
            elif "Frame" in result_list:
                graph_comparison(frame_dict)
            elif "Type" in result_list:
                graph_comparison(bike_type_dict)
            elif "Color" in result_list:
                graph_comparison(color_dict)
            elif "Speeds" in result_list:
                graph_comparison(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        elif "Over Time" in result_list:
            if "Date" in result_list:
                graph_over_time(date_dict)
            elif "Day of Week" in result_list:
                graph_over_time(day_dict)
            elif "Time" in result_list:
                graph_over_time(time_dict)
            elif "Location" in result_list:
                graph_over_time(location_dict)
            elif "Record" in result_list:
                graph_over_time(record_dict)
            elif "Reason" in result_list:
                graph_over_time(reason_dict)
            elif "Make" in result_list:
                graph_over_time(make_dict)
            elif "Model" in result_list:
                graph_over_time(model_dict)
            elif "Frame" in result_list:
                graph_over_time(frame_dict)
            elif "Type" in result_list:
                graph_over_time(bike_type_dict)
            elif "Color" in result_list:
                graph_over_time(color_dict)
            elif "Speeds" in result_list:
                graph_over_time(speeds_dict)
            else:
                print("Sorry, unable to perform this calculation.")
        else:
            print("Sorry, unable to perform this calculation.")
    else:
        print("Sorry, unable to perform this calculation.")
def btn_equal():
    global datatype_value
    global bikeinfo_value
    global datarep_value
    global result_list
    active = True
    result = str(datarep_value+ ", " +bikeinfo_value+ ", " +datatype_value)
    result_list = [datarep_value, bikeinfo_value, datatype_value]
    if datarep_value != "" and bikeinfo_value != "" and datatype_value != "":
        result_input_text.set(result)
    else:
        result_input_text.set("")
    TextEntry()
    btn_clear_top()
    combo_button_press()

########## TKINTER SETUP ##########
root = Tk()
root.title("Bike Calculator")

datarep_input_text = StringVar()
bikeinfo_input_text = StringVar()
datatype_input_text = StringVar()
result_input_text = StringVar()
results_printed_input_text = StringVar()

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
result_entry_frame.pack()
result_input_field = Entry(result_entry_frame, textvariable = result_input_text, bg="black", fg="white", width=30).grid(row=0, column=0)

results_printed_label = Label(root, text="SEARCH HISTORY", font='Arial 14 bold')
results_printed_label.pack()



###### ###### ###### TEST TEST TEST TEST TEST ###### ###### ######                              ***THIS WOULD PRINT OUTPUT IN APP***
def TextEntry():
    # results_printed_label = Label(root, text="SEARCH HISTORY", font='Arial 14 bold')
    # results_printed_label.pack()
    results_printed_label = Label(root, text=result_list, font='Arial 14 bold')
    results_printed_label.pack()
# results_printed_entry_frame = Frame(root)
# results_printed_entry_frame.pack(expand=1)   #, fill=x)
# results_printed_input_field = Entry(results_printed_entry_frame, textvariable = results_printed_input_text, bg="black", fg="white", width=30).grid(row=0, column=0)





root.mainloop()

