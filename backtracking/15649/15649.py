#원본: https://jiwon-coding.tistory.com/21?category=882771
n,m = list(map(int,input().split()))
s = []
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()
 