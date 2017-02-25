# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:45:22 2017

@author: shakar
"""
from praseJson import ParseData
import pandas as pd

class SendData():
    def __init__(self):
        parser=ParseData('file.json') 
        self.complete,self.active=parser.getDF() #This returns complete and active biddings
        for_json=self.active.reset_index()
        for_json.to_json('out.json')
    
    def getTenderData(self):
        companies=self.complete['tendererCompany'].unique()
        columns=['TenderName','Numberofcomplete','Numberofincomplete','Effectiveness']
        finalDf=pd.DataFrame(columns=columns)
        
        df=pd.DataFrame()
        
        for each_company in companies:
            values=self.complete.loc[self.complete['tendererCompany']== each_company]
           
            incompletecount=len(values.loc[values['status']==False])
            totalcount=len(values)
            complete=totalcount-incompletecount
            """df=pd.DataFrame({
                "Name":[each_company],
                "Number of taken projects":[totalcount],
                "Number of incomplete":[incompletecount],
                "Number of complete":[complete],
                "Percentage effectiveness":[complete/totalcount]
            #)
            })"""
            df_temp=pd.DataFrame({
                "Name":[each_company],
                "Number of taken projects":[totalcount],
                "Number of incomplete":[incompletecount],
                "Number of complete":[complete],
                "Percentage effectiveness":[float(complete)/totalcount]
            #)
            })
            df=df.append(df_temp)
            
        df=df.transpose()
        print df.to_csv('output.csv')
            
        """for each_data[1] in self.complete:
            for each_company in self.complete['tendererCompany'].unique():
                print each_data"""
        
ans=SendData()
ans.getTenderData()