import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


if __name__=="__main__":
    
    # 0 Load data
    f = open("data/GasPrices.csv")
    total_data = pd.read_csv(f)
    total_data["highway_num"] = np.array(total_data.Highway=="Y").astype(int)
    
    
    # 1 Calculate \mu and \sigma
    highway = total_data.loc[total_data["highway_num"]==1,:]
    not_highway = total_data.loc[total_data["highway_num"]==0,:]    
    
    sigma_x_square = np.var(highway.Price)
    mu_x = np.mean(highway.Price)
    sigma_y_square = np.var(not_highway.Price)
    mu_y = np.mean(not_highway.Price)
    sd_delta = np.sqrt(sigma_x_square/highway.shape[0]+sigma_y_square/not_highway.shape[0])
    
    print("="*80)
    print("The difference of mean value is {}".format(mu_x-mu_y))
    print("The standard deviation of delta is {}".format(sd_delta))  
    print("="*80)   
        
    
    # 2 bootstrapig 
    highway.index = np.arange(highway.shape[0])
    not_highway.index = np.arange(not_highway.shape[0])

    result = []
    for i in range(10000):
        sample_highway = np.random.randint(0,highway.shape[0],highway.shape[0])
        sample_not_highway = np.random.randint(0,not_highway.shape[0],not_highway.shape[0])

        tem_highway = highway.loc[sample_highway,:]          
        tem_not_highway = not_highway.loc[sample_not_highway,:]
        highway_p = np.mean(tem_highway.Price)
        not_highway_p = np.mean(tem_not_highway.Price)
        result.append(highway_p-not_highway_p)
    
    sns.set()
    sns.distplot(result, kde=True,color="blue")
    plt.savefig("pic/boot.png",dpi=400)
    plt.close()
    
    print("The 95% confidence interval is [{},{}]".format(np.percentile(result,2.5),np.percentile(result,97.5)))
    """
    import scipy.stats as stats
    1-stats.norm.cdf(2.511)
    """
    