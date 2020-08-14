import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
CRITICAL = -0.1


if __name__=="__main__":
    
    # 0 Load data
    f = open("data/stocks_bonds.csv")
    total_data = pd.read_csv(f)
    returns = np.array(total_data.SP500)
    F_x = np.sum(returns<=CRITICAL)/len(returns)
    print("Fn(x) is {}".format(F_x))
    print("n is {}".format(len(returns)))
    
    
    # 1 Bootstrap
    result = []
    for i in range(10000):
        index = np.random.randint(0,len(returns),len(returns))
        sample = returns[index]
        F_x = np.sum(sample<=CRITICAL)/len(sample)
        result.append(F_x)
    
    sns.set()
    sns.distplot(result, kde=True,color="pink")
    plt.savefig("pic/boot.png",dpi=400)
    plt.close()
    
    print("The 95% confidence interval is [{},{}]".format(np.percentile(result,2.5),np.percentile(result,97.5)))
    """
    import scipy.stats as stats
    1-stats.norm.cdf(2.511)
    """
    