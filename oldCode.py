"""
No Relevanace 

# #Utilizing the some columns and dropping others
# Project_status.drop('Monthly Status', axis = 1, inplace = True)
# Project_status.drop(' Next Steps', axis = 1, inplace = True)
# Project_status['Completed Y/N?'] = None

# collist_rearranged = ['Project Number:', ' Date of Completion or Last PM Check', 'Balance','Completed Y/N?', 'PM','Accountant']

# #Regex Expression


#Convert the PM container to Dataframe
DarrelPMs_df= pd.DataFrame(Project_Managers.pms)
DarrelPMs_df["Accountant"] = S["ACCOUNTANT"]
DarrelPMs_df.rename(columns={0: "PM"})
DarrelPMs_df.columns = ["PM", "Accountant"]


#print(DarrelPMs_df.columns)
#Merge of the PM listing and the ProjectStatus DataFrame
merge1 = Project_status.merge(DarrelPMs_df, on= 'PM')


#new - "Non Completed Projects"
# New_Project_Status_Container ={}

# for name in  Project_Status_Container.keys():
#     New_Project_Status_Container[name] = pd.DataFrame()

#new - "Completed and now Accural based Projects"
# Accrual_Project_Status_Container = {}

# for name in Project_Status_Container.keys():
#     Accrual_Project_Status_Container[name] = pd.DataFrame()



# for name in  Project_Status_Container.keys():
#     temp = Project_Status_Container[name]
#     if Project_Status_Container[name].empty:
#         print(f"{name} in if condition")
#         continue
    
#     elif (temp[' Date of Completion or Last PM Check'].apply(type).eq(str).any()):
#         print(temp[temp[' Date of Completion or Last PM Check'].str.contains("New", na= False)])
#         New_Project_Status_Container[name] =  temp[(~temp[' Date of Completion or Last PM Check'].apply(type).eq(datetime)) &
#                                            (temp[' Date of Completion or Last PM Check'].str.contains("New") | 
#                                             temp[' Date of Completion or Last PM Check'].str.contains("Not Complete") | 
#                                             temp[' Date of Completion or Last PM Check'].str.contains("Completion") | 
#                                             temp[' Date of Completion or Last PM Check'].str.contains("", na= True))]
#     else:
#         print(f"{name} in Else condition")
#         continue

#filtersfilter_notcomplete = Accrual_Project_Status_Container[' Date of Completion or Last PM Check'].str.contains("complete",na= False)| Accrual_Project_Status_Container[' Date of Completion or Last PM Check'].str.contains("Complete",na= False) |Accrual_Project_Status_Container[' Date of Completion or Last PM Check'].str.contains("completion",na= False)




#Small exact loop for the non completed - this is in effort to create accrual database        
for name in  Project_Status_Container.keys():
    temp = Project_Status_Container[name]
    
    
    if Project_Status_Container[name].empty:
        print(f"{name} in if condition")
        continue
    
    elif temp[' Date of Completion or Last PM Check'].apply(type).eq(str).any():
            filter_notcomplete = temp[' Date of Completion or Last PM Check'].str.contains("complete",na= False)| temp[' Date of Completion or Last PM Check'].str.contains("Complete",na= False) | temp[' Date of Completion or Last PM Check'].str.contains("completion",na= False) | temp[' Date of Completion or Last PM Check'].str.contains("New") 
            Accrual_Project_Status_Container[name] = temp.loc[~filter_notcomplete]

    
    elif temp[' Date of Completion or Last PM Check'].apply(type).eq(datetime).any() :
            filter_datatype = temp[' Date of Completion or Last PM Check'].apply(type).eq(datetime)
            Accrual_Project_Status_Container[name] = temp.loc[filter_datatype]

    else:
        print(f"{name} in Else condition")
        continue
        #New_Project_Status_Container[name] =  temp[(temp['Date of Completion or Last PM Check'].str.contains("New")) | (temp['Date of Completion or Last PM Check'].str.contains("Not Complete"))]
    
#writing to an excel sheet
##output = workbook('outputfiles/Project Status Report -  November.xlsx')

##writer = pd.ExcelWriter(output) 


#am_df=New_Project_Status_Container['Adam Moy']

#am_df.to_excel('outputfiles/sheet1.xlsx')

#Sorting
for i in New_Project_Status_Container.keys():
    df = New_Project_Status_Container[i]
    if df.empty:
        continue
    if df['Project Number:'].apply(type).eq(int).any():
        df = df.applymap(str)
        print("Inner"+i)
    New_Project_Status_Container[i] = df.sort_values(by= ["Project Number:"])
    print("reached")


#Sorting for accural dfs
for i in Accrual_Project_Status_Container.keys():
    df = Accrual_Project_Status_Container[i]
    if df.empty:
        continue
    if df['Project Number:'].apply(type).eq(int).any():
        df = df.applymap(str)
        print("Inner"+i)
    Accrual_Project_Status_Container[i] = df.sort_values(by= ["Project Number:"])
    print("reached")


    #creating xl workbooks for PM accrual dataframes
for i in Accrual_Project_Status_Container.keys():
    pm = i.replace(" ","")
    stringlink = 'outputfiles/Accrual'+pm+' - '+accountant+'.xlsx'

    Accrual_Project_Status_Container[i].to_excel(stringlink)

    
#creating a master dataframe to index and match 

concat_dataframe = []

for ind in Accrual_Project_Status_Container.keys():
    concat_dataframe.append(Accrual_Project_Status_Container[ind])

masterdf = pd.concat(concat_dataframe)


class masterdataframe:

    master = pd.DataFrame()
    pms = Darrel_PMs
    getter_PM = []

    def __new__(cls):  
        master = masterdf
        pms = Darrel_PMs
        return master

"""
