
#################################################################################################################################################
#貝氏呆帳率的分布 (視覺化、1~4階動差)
from scipy.stats import bernoulli
from scipy.stats import beta
import numpy as np


def default_distribution(n,y):

    a0 = 0.5 #alpha 先驗
    b0 = 0.5 #beta 先驗
    #貝氏共軛
    a = a0+y #alpha 後驗
    b = b0 + n -y  #beta 後驗

    x = np.linspace(0,0.15,1002)[1:-1]
    dist = beta(a=a,b=b)
    y = dist.pdf(x)

    return x,y
    # plt.plot(x,y)
    # plt.title('default distribution')
    # plt.show()

    # print(f'貝氏推論呆帳率95%的信賴區間{round(beta.ppf(0.025,60.5,1304.5),5)}~{round(beta.ppf(0.975,60.5,1304.5),5)}')
    # mean, var, skew, kurt = beta.stats(60.5,1304.5,moments='mvsk')
    # print('均值:', mean.astype('float16'), '變異數:', var.astype('float16'), '偏態:', skew.astype('float16'), '峰值:', kurt.astype('float16'))
##################################################################################################################################################
