if __name__=="__main__":
    n=int(input())
    roll_num_eng=set(map(int,input().split()))
    m=int(input())
    roll_num_fre=list(map(int,input().split()))
    union_set=roll_num_eng.union(roll_num_fre)
    print(len(union_set))