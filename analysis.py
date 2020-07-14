import pandas as pd
import numpy as np


def parser_data(num=2019):
    home_str = "data/"+str(num)+"-"+str(num+1)+"-home.csv"
    away_str = "data/"+str(num)+"-"+str(num+1)+"-away.csv"  
    f=open(home_str,encoding="utf-8")
    home_data = pd.read_csv(f)
    home_data.index = home_data.Name
    f=open(away_str,encoding="utf-8")
    away_data = pd.read_csv(f)
    away_data.index = away_data.Name
    away_data = away_data.loc[home_data.index,:]
    del(away_data["Num"])
    del(home_data["Num"])
    
    total_gf = sum(home_data["GF"])+sum(away_data["GF"])
    total_ga = sum(home_data["GA"])+sum(away_data["GA"])    
    assert total_ga==total_gf
    mean_gf = total_ga/(home_data.shape[0])
    
    home_data["total_GF"] = home_data["GF"]+away_data["GF"]
    home_data["total_GA"] = home_data["GA"]+away_data["GA"]   
    home_data["attack_strength"] = home_data["total_GF"]/mean_gf
    home_data["defence_weakness"] = home_data["total_GA"]/mean_gf  
    
    mean_home = 2*np.mean(home_data["GF"])/mean_gf
    mean_away = 2*np.mean(away_data["GF"])/mean_gf   
    
    return home_data,mean_home,mean_away


def cal_teams(home,away,data_cache):
    """
    Parameters
    ----------
    home : STR
        The name of home team.
    away : STR
        The name of away team.
    data_cache : tuple
        home_data,mean_home,mean_away.
    Returns
    -------
    home_score and away_score
    """
    home_data,mean_home,mean_away = data_cache
    
    
    

if __name__=="__main__":
    
    data_cache = parser_data(2019)
 Liverpool (home) and Tottenham
 
    home_data,mean_home,mean_away  
    
    
home_str = "data/"+str(num)+"-"+str(num+1)+"-home.xlsx" 
data = xlrd.open_workbook(home_str)
table = data.sheet()[0]
 
