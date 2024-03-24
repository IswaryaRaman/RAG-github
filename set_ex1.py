if __name__=="__main__":
    n,m=list(map(int,input().split()))
    n_array=list(map(int,input().split()))
    A=set(map(int,input().split()))
    B=set(map(int,input().split()))

    happiness=0

    for i in n_array:
        if i in A:
            happiness+=1
        elif i in B:
            happiness-=1
        
    print(happiness)