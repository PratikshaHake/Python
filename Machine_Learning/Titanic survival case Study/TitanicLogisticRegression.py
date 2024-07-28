import math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def TitanicLogistic():
    titanic_data=pd.read_csv("TitanicDataset.csv")

    print("First 5 entries from loaded dataset")
    print(titanic_data.head())

    print("Number of passangers are"+str(len(titanic_data)))

    print("Visualisation : Survived and non survived passangers")
    figure()
    target="Survived"

    countplot(data=titanic_data,x=target).set_title("Marvellous Infosystems :Survived and non survived passangers")
    show()

    print("Visualization : Survived and non survived passangers based on Gender")
    figure()
    target="Survived"

    countplot(data=titanic_data,x=target,hue="Sex").set_title("Marvellous Infosystems :Survived and non survived passangers based on Gender")
    show()

    print("Visualisation : Survived and non survived passangers based on passanger class")
    figure()
    target="Survived"

    countplot(data=titanic_data,x=target,hue="Pclass").set_title("Marvellous Infosystems :Survived and non survived passangers based on passanger class")
    show()
 
    print("Visualisation : Survived and non survived passangers based on Age")
    figure()
    target="Survived"

    titanic_data["Age"].plot.hist().set_title("Marvellous Infosystems :Survived and non survived passangers based on passanger Age")
    show()
 
    print("Visualisation : Survived and non survived passangers based on fare")
    figure()
    target="Survived"

    titanic_data["Fare"].plot.hist().set_title("Marvellous Infosystems :Survived and non survived passangers based on Fare")
    show()
    
    titanic_data.drop("zero",axis=1,inplace=True)

    print("First 5 entries from loaded dataset after removing one field")
    print(titanic_data.head(5))

    print("Values of Sex column")
    Sex=pd.get_dummies(titanic_data["Sex"])

    print("Values of Sex column after removing one field")
    Sex=pd.get_dummies(titanic_data["Sex"],drop_first=True)
    print(Sex.head(5))

    print("Values of Pclass after removing one field")
    Pclass=pd.get_dummies(titanic_data["Pclass"],drop_first=True)
    print(Pclass.head(5))

    print("Values of data set after concatenating new colums")
    titanic_data=pd.concat([titanic_data,Sex,Pclass],axis=1,inplace=True)
    print(titanic_data.head(5))

    print("Values of data set after removing irrelevent columns")
    titanic_data.drop(["Sex","sibsp","Parch","Embarked"],axis=1,inplace=True)

    x=titanic_data.drop("Survived",axis=1)
    y=titanic_data["Survived"]

    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5)

    logmodel=LogisticRegression()

    logmodel.fit(xtrain,ytrain)

    prediction=logmodel.predict(xtest)

    print("Classification report of logistic Regression is :")
    print(classification_report(ytest,prediction))

    print("Confusion Matrix of Logistic regression is :")
    print(confusion_matrix(ytest,prediction))

    print("Accuracy of Logistic Regression is :")
    print(accuracy_score(ytest,prediction))


def main():
    print("Supervised Machine Learning")
    print("Logistic Regression on titanic data set")

    TitanicLogistic()

if __name__=="__main__":
    main()