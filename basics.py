def average(array):
    # your code goes here
    new_array=set(array)
    aver_val=sum(new_array)/len(new_array)
    return format(aver_val,".3f")

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)   