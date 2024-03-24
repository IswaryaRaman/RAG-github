if __name__=="__main__":
    N=int(input())
    N_countries=[]
    country_stamp=0
    for _ in range(0,N):
        N_countries.extend(input().split("\n"))
    print(N_countries)
    set1=set()
    [set1.add(i) for i in N_countries]
    print(len(set1))