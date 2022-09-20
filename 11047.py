import sys

nklst = list(map(int, input().split()))


coinlst = []
idx = 0
total = nklst[1]


for i in range(nklst[0]):
    coinlst.append(int(sys.stdin.readline()))



for coin_num in range(len(coinlst)-1, -1, -1):
    recent_coin = coinlst[coin_num]
    #print("recent coin :", recent_coin)
    while (1):
        if total // recent_coin == 0:
            break
        
        else :
            idx = idx + (total // recent_coin)
            total = total % recent_coin
            #print("idx : ", idx)
            #print("total :", total)
            
            

print(idx)
