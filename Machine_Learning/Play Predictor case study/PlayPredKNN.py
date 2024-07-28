# Play Predictor using KNN algorithm 
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

def PlayPredictor():
    data=pd.read_csv('PlayPredictor.csv')

    whether=data.Whether
    Temperature=data.Temperature
    play=data.Play

    le=preprocessing.LabelEncoder()

    whether_encoded=le.fit_transform(whether)
    print()
    Temp_encoded=le.fit_transform(Temperature)
    labels=le.fit_transform(play)

    features=list(zip(whether_encoded,Temp_encoded))

    model=KNeighborsClassifier(n_neighbors=3)
    data_train,data_test,target_train,target_test=train_test_split(features,labels,test_size=0.5)
    model.fit(data_train,target_train)

    predicted=model.predict(data_test)
    Accuracy=accuracy_score(target_test,predicted)

    return Accuracy

def main():
    print("Play Predictor application using K Nearest Neighbor algorithm")

    Accuracy=PlayPredictor()
    print("Accuracy of Play Precitor aaplication using KNN is",Accuracy*100)

if __name__=="__main__":
    main()

