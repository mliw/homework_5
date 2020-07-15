import pandas as pd
import numpy as np
from scipy import stats


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
    home : str
        The name of home team.
    away : str
        The name of away team.
    data_cache : tuple
        home_data,mean_home,mean_away.
    Returns
    -------
    expected_home_score and expected_away_score
    """
    home_data,mean_home,mean_away = data_cache
    expected_home_score = mean_home*home_data.loc[home,"attack_strength"]*home_data.loc[away,"defence_weakness"]
    expected_away_score = mean_away*home_data.loc[away,"attack_strength"]*home_data.loc[home,"defence_weakness"]    
    return expected_home_score,expected_away_score
    

def cal_probability(expected_home_score,expected_away_score,tol=100):
    md_home = stats.poisson(expected_home_score)
    md_away = stats.poisson(expected_away_score)
    p_draw = sum([md_home.pmf(i)*md_away.pmf(i) for i in range(tol)])
    p_home_win = sum([(1-md_home.cdf(i))*md_away.pmf(i) for i in range(tol)])
    p_home_loss = sum([(1-md_away.cdf(i))*md_home.pmf(i) for i in range(tol)])
    return p_home_win,p_draw,p_home_loss
    

class assemble:
    
    def __init__(self,num=2019):
        self.data_cache = parser_data(num)
        home_data,mean_home,mean_away = self.data_cache
        self.team_list = home_data.index
        
    def produce_result(self,home,away):
        expected_home_score,expected_away_score = cal_teams(home,away,self.data_cache)
        p_home_win,p_draw,p_home_loss = cal_probability(expected_home_score,expected_away_score)
        print("Home:{}, Away:{},home_win:{},home_draw:{},home_loss:{}".format(home,away,np.round(p_home_win,4),np.round(p_draw,4),np.round(p_home_loss,4)))
    
    def produce_whole(self,):
        print("="*70)
        for i in range(len(self.team_list)):
            for j in range(len(self.team_list)):        
                if i!=j:
                    self.produce_result(self.team_list[i],self.team_list[j])
        print("="*70)
        

if __name__=="__main__":
    whole = assemble(2019)
    whole.produce_whole()
 
 
