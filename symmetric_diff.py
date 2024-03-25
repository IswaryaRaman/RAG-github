if __name__=="__main__":
    M=int(input())
    M_vals=set(map(int,input().split()))
    N=int(input())
    N_vals=set(map(int,input().split()))
    total_vals=M_vals.difference(N_vals)
    total_vals.update(N_vals.difference(M_vals))
    print(*sorted(total_vals),sep="\n")
