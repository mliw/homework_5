import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


if __name__=="__main__":
    
    # 0 Load data
    total_str = "12 18 15 8 17 13 22 13 13 13 12 11 15 15 12 8 20 12 14 11 9 15 16 20 9 15 13 19 18 14"
    total_arr = np.array([int(items) for items in total_str.split(" ")])
    X_N = np.mean(total_arr)
  
        
    # 1 bootstraping
    result = []
    for i in range(20000):
        index = np.random.randint(0,len(total_arr),len(total_arr))
        tem_mean = np.mean(total_arr[index])
        result.append(tem_mean)

    sns.set()
    sns.distplot(result, kde=True,color="green")
    plt.savefig("pic/boot.png",dpi=400)
    plt.close()
    
    print("The 95% confidence interval is [{},{}]".format(np.percentile(result,2.5),np.percentile(result,97.5)))
    """
    import scipy.stats as stats
    1-stats.norm.cdf(2.511)
    """
    