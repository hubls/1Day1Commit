import sys

n = int(input())


lst = []
dic = {}
for i in range(n):
    s = sys.stdin.readline().strip()
    s = int(s)
    lst.append(s)
    if s in dic:
        dic[s] +=1
    else:
        dic[s] = 1

max_dic = max(dic.values())
n_lst = [k for k, v in dic.items() if v == max_dic]
n_lst.sort()

#print("max dic ; ", max_dic)



lst.sort()
print(round(sum(lst)/len(lst))) # 1. 산술평균
print(lst[int(len(lst)/2)]) # 2. 중앙값
if len(n_lst) > 1 :
    print(n_lst[1])         #3. 최빈값중 두번째값
else:
    print(n_lst[0])
print(max(lst)- min(lst)) #4. 범위




