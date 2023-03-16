
from datetime import datetime
import pandas as pd
from xlsxwriter import workbook
import ProjectStatusGenerator_helper
import subprocess
import openpyxl
from xlsxwriter.workbook import *
import xlwt
import re
from pmContainer import PMs
from config  import SETTINGS as S
from config import REGEX as REG

file = "ProjectGeneratorSourcefiles/"+ S['MONTH'] + "_project_status.xlsx"

#display option 
# pd.set_option("display.max_rows", None, "display.max_columns", None)

REGEX_CANCEL = REG["CANCEL_STRING"] 
REGEX_FUNDING = REG["FUNDING_STRING"]
REGEX_COMPLETE =REG["COMPLETE_STRING"]

#Setting the object for Project Managers
Project_Managers = PMs(S["MONTH"])
Project_Managers.pms = S["ACCOUNTANT"]

#Object Containing Project Managers
Project_Managers.pms

masterdf = pd.DataFrame()

date = datetime(datetime.today().year, datetime.today().month,  1)
date = date.strftime("%m/%y")



 
PMs_columns = ['PM','Total','Funded','Remaining','Accountant']

# Make sure that the columns are adjusted properly OR refactor code to make it dynamic

Project_status = pd.read_excel(file, sheet_name = "Project List", 
                               usecols = "A:N",
                               header = 3,
                               na_filter = True)

#Filters
filter_funded = (Project_status["Project Description"].str.contains(REGEX_FUNDING ,regex=True, flags=re.IGNORECASE, na=False))
filter_cancelled = ( Project_status[" Date of Completion or Last PM Check "].str.contains(REGEX_CANCEL, regex=True, flags=re.IGNORECASE, na=False))
filter_date = (Project_status[" Date of Completion or Last PM Check "].apply(type).eq(datetime))

#Remove all Funding  and cancelled Projects out
Project_status = Project_status.loc[~filter_funded &
                                    ~filter_cancelled &
                                    ~filter_date] 


filter_complete= ( Project_status[" Date of Completion or Last PM Check "].str.contains(REGEX_COMPLETE, regex=True, flags=re.IGNORECASE, na=True))
filter_capital = ( Project_status["Capital Project?"].str.contains("Yes", regex=True, flags=re.IGNORECASE, na=True))
Project_status = Project_status[ filter_complete & filter_capital ]

#Drop Unnecessary Columns
Project_status.drop(['Funded'
                     ,' Next Steps '
                     ,'Monthly Status'
                     ,'Capital Project?'
                     , 'Start Date'
                     ], axis = 1, inplace = True)

Project_status['Completed Y/N?'] = None

#New Order
column_List = [
            'Project Number'
            ,'Completed Y/N?'
            ,'Entity'
            ,'Project Description'
            ,'Cost Remaining'
            ,'Accrual Total (Feb 2023)'
            ,'Cost Less Accrual'
            ,'Project Manager'
            ,' Date of Completion or Last PM Check '
            ,'Responsible Accountant'
           ]
#Applying the new order of columns
Project_status = Project_status[column_List]

#create a datafram for each to the PM,
#Link of assistance https://newbedev.com/create-multiple-dataframes-in-loop

#creation of unique names 
    #already did that 

#Creation of a datafram dictionary to store my data frames
Project_Status_Container = {elem : pd.DataFrame() for elem in Project_Managers.pms}

#Create sorted dataframe 
for i in Project_Status_Container.keys():
    Project_Status_Container[i] = Project_status[Project_status['Project Manager'] == i]
    df = Project_Status_Container[i]
    if df.empty:
        continue
    if df['Project Description'].apply(type).eq(int).any():
        df = df.applymap(str)
        print("Inner"+i)
    Project_Status_Container[i] = df.sort_values(by= ["Project Description"])
    print(f"Project Status Report has been created for: {i}")

Project_Status_Container.values

#creating xl workbooks for PM dataframes
for i in Project_Status_Container.keys():
    pm = i.replace(" ","")
    stringlink = 'outputfiles/'+pm+' - '+S['ACCOUNTANT']+'.xlsx'
    print(f"{i} has no projects")   if Project_Status_Container[i].empty else Project_Status_Container[i].to_excel(stringlink)


   
  