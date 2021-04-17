def output(v, acc, gyr):
    #results = input()
    if(acc[0][9]>1):
        print("left", acc)
        results = "left"
    elif(acc[0][9]<-1):
        print("right",acc)
        results = "right"
    else:
        return ""
    return results