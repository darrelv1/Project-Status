import pandas as pd 
from datetime import datetime

#display option 
#pd.set_option("display.max_rows", None, "display.max_columns", None)


class PMs ():

    
    def __init__(self, month): 
        self._source = "ProjectGeneratorSourcefiles/"+ month + "_project_status.xlsx"
        self.datafile = pd.read_excel(self._source, sheet_name = "Accountant per PM", usecols = "A:F", nrows=70)
        self._pms = [0]

    def __str__(self):
        return "from : "+ self.source

    @property
    def source(self):
        return self.source

    @source.setter
    def source(self, month_letter):
        self._source = "ProjectGeneratorSourcefiles/"+ month_letter + "_project_status.xlsx"
        print(self.__str__)

    @property
    def pms(self):
        return self._pms    
    
    @pms.setter
    def pms(self, accountant):
        accountant_filter = self.datafile["Accountant"] == accountant

        print(type(self.datafile[accountant_filter].PM))
        
        self._pms =  self.datafile[accountant_filter].PM
        return self._pms
        

    



     
        