N = int(input())
List = list(map(int, (str(N))))
List.sort(reverse=True)

if List[-1] != 0 :
    print(-1)
else :
    s = sum(List)
    if s % 3 == 0 :
        print(int(''.join(map(str, List))))
    else :
        print(-1)