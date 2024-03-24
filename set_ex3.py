n = int(input())
s = set(map(int, input().split()))
N=int(input())
for _ in range(0,N):
    N_commands=input()
    if N_commands!="pop":
        command,value=N_commands.split()
        if command=="remove":
            s.remove(int(value))
        elif command=="discard":
            s.discard(int(value))
    else:
        s.pop()
print(len(s))