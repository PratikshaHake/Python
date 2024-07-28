# Wine predictor application using KNN algorithm

from sklearn.metrics import accuracy_score
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def WinePredictor():
    wine=datasets.load_wine()

    data_train,data_test,target_train,target_test=train_test_split(wine.data,wine.target,test_size=0.3)

    knn=KNeighborsClassifier(n_neighbors=3)

    knn.fit(data_train,target_train)
    predictions=knn.predict(data_test)

    Accuracy=accuracy_score(target_test,predictions)

    return Accuracy

def main():
    print("Wine Predictor application using K nearest Neighbour algorithm")
    Accuracy=WinePredictor()
    print("Accuracy of wine predictor application using KNN algorithm",Accuracy*100,"%")

if __name__=="__main__":
    main()