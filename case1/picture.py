import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def trans_med(tem_str):
    if "Med" in tem_str:
        return "MedDiet_Any"
    else:
        return tem_str
    

def trans_num(tem_str):
    if tem_str=="Yes":
        return 1
    else:
        return 0    


if __name__=="__main__":
    
    f = open("data/predimed.csv")
    total_data = pd.read_csv(f)
    total_data["combined_group"] = total_data.group.map(lambda x: trans_med(x))
    total_data["event_num"] = total_data.event.map(lambda x: trans_num(x))
    
    
    # Solutions for Part(C)
    control_group = total_data.loc[total_data["combined_group"]=="Control",:] 
    p = np.sum(control_group.event_num)/control_group.shape[0]
    N = control_group.shape[0]

    med_group = total_data.loc[total_data["combined_group"]=="MedDiet_Any",:] 
    q = np.sum(med_group.event_num)/med_group.shape[0]
    M = med_group.shape[0]
    result = np.sqrt((p-p**2)/N+(q-q**2)/M)
    print("="*80)
    print("p:{},N:{}".format(p,N))
    print("q:{},M:{}".format(q,M))
    print("result is:{}".format(result))
    print("="*80)
    
    
    # Solutions for Part(D)
    med_group.index = np.arange(med_group.shape[0])
    control_group.index = np.arange(control_group.shape[0])

    result = []
    for i in range(10000):
        sample_med = np.random.randint(0,med_group.shape[0],med_group.shape[0])
        sample_control = np.random.randint(0,control_group.shape[0],control_group.shape[0])

        tem_control = control_group.loc[sample_control,:]          
        tem_med = med_group.loc[sample_med,:]
        tem_p = np.sum(tem_control.event_num)/tem_control.shape[0]
        tem_q = np.sum(tem_med.event_num)/tem_med.shape[0]  
        result.append(tem_p-tem_q)
    
    sns.set()
    sns.distplot(result, kde=True,color="red")
    plt.savefig("pic/boot.png",dpi=400)
    plt.close()
    
    print("The 95% confidence interval is [{},{}]".format(np.percentile(result,2.5),np.percentile(result,97.5)))
    
    """
    import scipy.stats as stats
    stats.norm.cdf(2.05454)
    """