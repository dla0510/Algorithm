# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 03:12:09 2021

@author: dla05
"""
s='ababcdcdababcdcd'
def Compression(s):
    n = len(s)

    if (n - len(set(s))) < 2:
        return n

    com = [0]
    for d in range(1, int(n / 2) + 1):
        com.append(0)
        cnt = 1
        res = ''
        for q in range(1, int(n / d)):
            p1=d*q
            p2=d*(q-1)
            if s[p1:p1 + d] == s[p2:p2 + d]:
                cnt += 1
            else:
                if cnt>1:
                    res = res+str(cnt)+s[p2:p2+d]
                else:
                    res = res+s[p2:p2+d]
                cnt = 1
            if q==int(n/d)-1:
                if cnt > 1:
                    res = res + str(cnt) + s[p1:p1 + d]
                else:
                    res = res + s[p1:p1 + d]
        com[d] = len(res)+n%d

    ans = n
    for i in range(1, len(com)):
        if com[i] < ans:
            ans = com[i]
    return ans

print(Compression(s))
    
        
    길이 11짜리면 길이 10짜리면
    q는 (5,4,3,2,1)
    5일 때 i는 (0,1)
    4일 때 i는 (0,1,2,3) 0:4 4:8 n/d개, 1:5 5:9, 2:6 6:10, 3:7 7:11 n%d개 0:4 4:8, 1:5 5:9, 2:6 6:10 n%d
    3일 때 i는 (0,1,2) 0:3 3:6 6:9 n/d개
    2일 때 i는 (0,1)
    1일 때 i는 (0)
    