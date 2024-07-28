
import numpy as np
import pandas as pd

def AdvertisingPredictor():
    data=pd.read_csv("Advertising.csv")
    # Load data
    x1=data['TV'].values
    x2=data['radio'].values
    x3=data['newspaper'].values
    Y=data['sales'].values


    # Least Square method
    mean_x1 = np.mean(x1)
    mean_x2 = np.mean(x2)
    mean_x3 = np.mean(x3)
    mean_y = np.mean(Y)
    

    print("Mean of Dependent variable y",mean_y)
    n = len(x1)

    sum_x1=0
    sum_x2=0
    sum_x3=0
    sum_x1_sq=0
    sum_x1_x2=0
    sum_x1_x3=0
    sum_x2_sq=0
    sum_x3_sq=0
    sum_x2_x3=0
    sum_y=0
    sum_Y_x1=0
    sum_Y_x2=0
    sum_Y_x3=0

    for i in range (n):
        sum_x1+=x1[i]
        sum_x2+=x2[i]
        sum_x3+=x3[i]
        sum_x1_sq+=x1[i]**2
        sum_x1_x2+=(x1[i]*x2[i])
        sum_x1_x3+=(x1[i]*x3[i])
        sum_x2_sq+=x2[i]**2
        sum_x3_sq+=x3[i]**2
        sum_x2_x3+=(x2[i]*x3[i])
        sum_y+=Y[i]
        sum_Y_x1+=(Y[i]*x1[i])
        sum_Y_x2+=(Y[i]*x2[i])
        sum_Y_x3+=(Y[i]*x3[i])


    Sum_x1_sq=sum_x1_sq-(((sum_x1)**2)/200)
    Sum_x1x2=sum_x1_x2-(((sum_x1)*(sum_x2))/200)
    Sum_x1x3=sum_x1_x3-(((sum_x1)*(sum_x3))/200)
    Sum_x2_sq=sum_x2_sq-(((sum_x2)**2)/200)
    Sum_x2x3=sum_x2_x3-(((sum_x2)*(sum_x3))/200)
    Sum_x3_sq=sum_x3_sq-(((sum_x3)**2)/200)

    Sum_x1Y=sum_Y_x1-(((sum_x1)*(sum_y))/200)
    Sum_x2Y=sum_Y_x2-(((sum_x2)*(sum_y))/200)
    Sum_x3Y=sum_Y_x3-(((sum_x3)*(sum_y))/200)

    

    X=np.array([[Sum_x1_sq,Sum_x1x2,Sum_x1x3],
    [Sum_x1x2,Sum_x2_sq,Sum_x2x3],
    [Sum_x1x3,Sum_x2x3,Sum_x3_sq]])
    
   
    
    Yp=np.array([[Sum_x1Y],
        [Sum_x2Y],
        [Sum_x3Y]])

    x_inv=np.linalg.inv(X)
    B=np.dot(x_inv,Yp)
   
    
    B0=mean_y-(B[0]*mean_x1)-(B[1]*mean_x2)-(B[2]*mean_x3)
    

    # Findout goodness of fit ie R Square
    ss_t=0
    ss_r=0

    for i in range(n):
        y_p=B0+(B[0]*x1[i])+(B[1]*x2[i])+(B[2]*x3[i])
        ss_t+=(Y[i]-mean_y)**2
        ss_r+=(Y[i]-y_p)**2

    r2=1-(ss_r/ss_t)

    print("Value of R square",r2[0])
    
   




def main():
    print("---- Pratiksha Hake -----")
    
    print("Suervised Machine Learning")
    
    print("Multi Linear Regreesion")
    
    AdvertisingPredictor()

if __name__ == "__main__":
    main()
