from sklearn import tree

#Rough 1
#Smooth 0
def MarvellousML(weight,surface):
    Features=[[35,1],[47,1],[90,0],[48,1],[90,0],
              [35,1],[92,0],[35,1],[35,1],[35,1]]

    Labels=[1,1,2,1,2,1,2,1,1,1]
    clf=tree.DecisionTreeClassifier()
    clf=clf.fit(Features,Labels)
    result=clf.predict([[weight,surface]])

    if result==1:
        print("Your object looks like Tennis ball")
    elif result==2:
        print("Your object looks like Cricket ball")

def main():
    print("Ball Classification case study")

    print("Enter weight of object")
    weight=input()

    print("What is the surface type of your object Smooth or Rough")
    surface=input()

    if surface.lower()=="rough":
        surface=1
    elif surface.lower()=="smooth":
        surface=0
    else:
        print("Error: Wrong input")
        exit()
    
    MarvellousML(weight,surface)
    
    


if __name__=="__main__":
    main()