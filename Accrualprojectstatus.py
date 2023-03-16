import pandas as pd 


maindf = pd.read_excel("ProjectGeneratorSourcefiles/05 - Project Status Report May 2022.xlsx", sheet_name='Project Status', usecols="A:G", header = 3, na_filter = True)

def source(inputsource):
    df = pd.read_excel(inputsource)
    return df 


class filters: 

    def __init__(self):
        self.maindf = maindf

    #Filterout anything that is not completed:
    filter_notcomplete = maindf[' Date of Completion or Last PM Check'].str.contains("complete",na= False)| maindf[' Date of Completion or Last PM Check'].str.contains("completion",na= False)
    filter_notfunded = maindf["Project Number:"].str.contains('fund')| maindf["Project Number:"].str.contains('Fund') |maindf["Project Number:"].str.contains('IPAC')
    filter_accountant = maindf['Accountant'] == 'Darrel'
    
    #

    maindf = maindf.loc[~filter_notcomplete]
    maindf = maindf.loc[~filter_notfunded]
    maindf = maindf.loc[filter_accountant]

    pd.to_datetime()

    def get_countforaccount():
        pass

    def applyPMgroup(self, namePM):
       self.maindf = maindf.groupby(['PM'])
       tempdf = maindf.getgroup(namePM)
       return tempdf 

    def get_countPMFreq():
        return maindf['PM'].value_counts()
    
    altdf = maindf   
    
    #IMPORTANT
    # Remeber that if you want to format your dates you must first change the format of dateandtime by using "pd.to_datetime"
    altdf[' Date of Completion or Last PM Check'] = pd.to_datetime(altdf[' Date of Completion or Last PM Check'], format='%B %d,%y')

    #After that has been done you can now format the output utilizing dt.strftime('')
    altdf[' Date of Completion or Last PM Check'] = altdf[' Date of Completion or Last PM Check'].dt.strftime('%B %d,%y')

    #https://datascientyst.com/extract-month-and-year-datetime-column-in-pandas/
    altdf[' Date of Completion or Last PM Check'] = pd.to_datetime(altdf[' Date of Completion or Last PM Check'], errors = "coerce")
    altdf[' Date of Completion or Last PM Check'] = altdf[' Date of Completion or Last PM Check'].dt.to_period('M')
    altdf[' Date of Completion or Last PM Check'] = altdf[' Date of Completion or Last PM Check'].dt.strftime('%B,%Y')

    #copy of what acutally worked 
    maindf = pd.read_excel("ProjectGeneratorSourcefiles/05 - Project Status Report May 2022.xlsx", sheet_name='Project Status', usecols="A:G", header = 3, na_filter = True)
    altdf = maindf
    altdf[' Date of Completion or Last PM Check'] = pd.to_datetime(altdf[' Date of Completion or Last PM Check'], errors = "coerce")
    altdf[' Date of Completion or Last PM Check'] = pd.to_datetime(altdf[' Date of Completion or Last PM Check'], format='%B, %Y')
    altdf[' Date of Completion or Last PM Check'] = altdf[' Date of Completion or Last PM Check'].dt.to_period('M')
    altdf[' Date of Completion or Last PM Check'] = altdf[' Date of Completion or Last PM Check'].dt.strftime('%B, %Y')
    date_group = altdf.groupby([' Date of Completion or Last PM Check'])
    PM_group = altdf.groupby(['PM'])

    #Quantity of Completion  
    def num_compBydate():
        PM_group = altdf.groupby(['PM'])
        return PM_group['Accountant']

    def num_accuredBymonth():
        a = altdf.groupby([' Date of Completed or Last PM Check'])
        return PM_group[' Next Steps'].apply(lambda x:x.str.contains('Accrual').sum())