""" Customer Relationship Management (CRM) module
Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""
#from model import data_manager, util
import pandas as pd
import xlrd
import csv
#import numpy as np
DATAFILE = "C:/Users/Maciej Bedkowski/Desktop/CODECOOL TASKS/secure-erp-python-sjafernik-development/model/crm/crm.xlsx"
HEADERS = ["id", "name", "email", "subscribed"]
headres_id = []
headers_name = []
headers_email = []
headers_subscribed = []
def read_customer():
    df = pd.read_excel(DATAFILE)
    print(df)
def read_customer2():
    with open(DATAFILE) as csvfile:
        for line in csvfile:
            fields = line.split(";")
            headres_id.append(fields[0])
            headers_name.append(fields[1])
            headers_email.append(fields[2])
            headers_subscribed.append(fields[3])

        
def show_customer():
    for i in range (len(headres_id)):
        print("------")
        print("|   {:^10}   |   {:^10}   |   {:^10}   |   {:^10}   |".format(headres_id[i],headers_name[i],headers_email[i],headers_subscribed[i]))
#read_customer()
read_customer2()
#show_customer()