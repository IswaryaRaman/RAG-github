if __name__=="__main__":
    n=int(input())
    roll_num_eng=set(map(int,input().split()))
    m=int(input())
    roll_num_fre=list(map(int,input().split()))
    sym_difference_set=roll_num_eng.symmetric_difference(roll_num_fre)
    print(len(sym_difference_set))