# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 17:53:52 2021

@author: dla05
"""

'''
1-2)
leetcode 1904. The Number of Full Rounds You Have Played
한 온라인 비디오 게임은 15분짜리 라운드로 이루어져 있다. 즉, HH:00, HH:15, HH:30, HH:45에 새로운 라운드가 시작한다.(이 때 HH는 00시부터 23시까지를 의미.) startTime과 finishTime이 주어졌을 때 플레이어가 온전하게 풀로 플레이하는 라운드 수를 계산하라.
'''

class Solution(object):
    def numberOfRounds(self, startTime, finishTime):
        r=[0,15,30,45]
        time= {}
        for i in range(0,24):
            for j in r:
                time[str(i).zfill(2)+":"+str(j).zfill(2)]=0
        startH, startT = map(int,startTime.split(":"))
        finH, finT = map(int,finishTime.split(":"))
        
        #if startTime < finishTime:
        if startH < finH or (startH==finH and startT<finT):
            #start 시간이 finsh 시간보다 빠르면
            finT = 0 if finT<15 else 15 if 15<=finT<30 else 30 if 30<=finT<45 else 45
            finishTime = finishTime[:2]+":"+str(finT)
            for idx in time:
                if startTime<=idx<finishTime:
                    time[idx]+=1
                    print(idx)
                    
        else:
            #finish 시간이 start 시간 보다 빠르면(다음 날 끝낸 것)
            finT = 0 if finT<15 else 15 if 15<=finT<30 else 30 if 30<=finT<45 else 45
            finishTime = finishTime[:2]+":"+str(finT)
            for idx in time:
                if idx>=startTime or idx<finishTime:
                    time[idx]+=1
                    print(idx)
        
        return sum(time.values())
            
            



solution = Solution()
solution.numberOfRounds("20:00", "06:00")
solution.numberOfRounds("12:01", "12:44")
solution.numberOfRounds("20:00", "06:00")
solution.numberOfRounds("00:00", "23:59")





