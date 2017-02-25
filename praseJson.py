# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 10:18:26 2017

@author: shakar
"""
import json
from pprint import pprint
import pandas as pd
import datetime, time
import random


class ParseData:
    def __init__(self,filename):
        self.filename=filename
        self.openFile()
        
    
    def openFile(self):
        
        with open(self.filename) as data_file:
            data=json.load(data_file)
        self.datafile=data
        
    def getDF(self):  
        data=self.datafile
        df_complete=pd.DataFrame()
        df_active=pd.DataFrame()
        dts = datetime.datetime.utcnow()
        epochtime = int(time.mktime(dts.timetuple()) + dts.microsecond/1e6)
        for release in data['releases']:
            projectName=release['planning']['budget']['budgetProjectTitle']
            
            if release['tender']['tenderStatus']=='complete':
                number_of_tenderers=release['tender']['totalTenderers']
                for each_tenderer in release['tender']['tenderer']:
                    tenderer_name=each_tenderer['legalName']  
                    
                    tenderer_contactname=each_tenderer['contactPersonName']
                    tenderer_contactnumber=each_tenderer['contactPersonEmail']
                task_undertaken=release['contract']['periodStartDate']
                task_tocomplete=release['contract']['periodEndDate']
                status=bool(random.getrandbits(1)) #Represents work is on progress or not expired
                print status
                value=pd.DataFrame({
                    'projectName':[projectName],
                    'tendererCompany':[tenderer_name],
                    'tendererContact':[tenderer_contactname],
                    'tendererNumber':[tenderer_contactnumber],
                    'taskStarted':[task_undertaken],
                    'taskEnd':[task_tocomplete],
                    'status':[status] 
                
                })
                
                df_complete=df_complete.append(value)
                    
            else:
                amount=release['tender']['tenderAmount']
                tender_start_date=release['tender']['startDate']
                tender_end_date=release['tender']['endDate']
                tender_enquiry_start=release['tender']['enquiryStartDate']
                tender_enquiry_end=release['tender']['enquiryEndDate']
                
               
                
                value2=pd.DataFrame({
                    'projectName':[projectName],
                    'tenderAmount':[amount],
                    
                    'StartDate':[tender_start_date],
                    'EndDate':[tender_end_date],
                    'EnquiryStart':[tender_enquiry_start],
                    'taskEnd':[tender_enquiry_end]
                
                
                })
                df_active=df_active.append(value2)
        
        return df_complete,df_active


