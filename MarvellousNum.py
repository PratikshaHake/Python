def ChkPrime(No):
    flag=True
    if(No>1):
        for i in range(2,No):
            if(No%i==0):
                flag=False
                break
           

        return flag
    


         