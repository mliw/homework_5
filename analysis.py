import pandas as pd
import numpy as np


def parser_data(num=2019):
    home_str = "data/"+str(num)+"-"+str(num+1)+"-home.csv"
    away_str = "data/"+str(num)+"-"+str(num+1)+"-away.csv"  
    
    
    home_str = "data/test.csv"    
    f=open(home_str,encoding="utf-8")
    home_data = pd.read_csv(f)
    
    
    
    import xlrd
home_str = "data/"+str(num)+"-"+str(num+1)+"-home.xlsx" 
data = xlrd.open_workbook(home_str)
table = data.sheet()[0]
 
