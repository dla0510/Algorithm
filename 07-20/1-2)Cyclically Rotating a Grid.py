# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:43:07 2021

@author: dla05
"""

'''
1-2)
leetCode 1914. Cyclically Rotating a Grid
mxn 크기의 매트릭스가 있다(m과 n은 짝수). 주어진 정수 k개만큼 매트릭스 안의 숫자들을 시계 반대 방향으로 회전시켜라. 이때 매트릭스는 여러개의 레이어로 나뉠 수 있으며 각 레이어별로 회전시켜야 함.
'''

class Solution:
    def assign(self, temp, rows, cols, i, j, arr, topL, topR, bottomR, bottomL):
        ix = 0
        # top row
        while j < topR[1]:
            temp[i][j] = arr[ix]
            ix += 1
            j += 1

        # last column
        while i < bottomR[0]:
            temp[i][j] = arr[ix]
            ix += 1
            i += 1

        # last row
        while j > bottomL[1]:
            temp[i][j] = arr[ix]
            ix += 1
            j -= 1

        # first column
        while i > topR[0]:
            temp[i][j] = arr[ix]
            ix += 1
            i -= 1

        
    
    def rotateGrid(self, grid, k):
        rows, cols, i, j = len(grid), len(grid[0]), 0, 0
		# Marking the 4 points, which will act as boundaries
        topLeft, topRight, bottomRight, bottomLeft = [0,0],[0,cols-1],[rows-1, cols-1],[rows-1, 0]
        temp = [[-1 for _ in range(cols)] for __ in range(rows) ] 
        while topLeft[0] < rows//2 and topLeft[0] < cols//2:
            arr = []
            # top row
            while j < topRight[1]:
                arr.append(grid[i][j])
                j += 1

            # last column
            while i < bottomRight[0]:
                arr.append(grid[i][j])
                i += 1
                
            # last row
            while j > bottomLeft[1]:
                arr.append(grid[i][j])
                j -= 1
            
            # first column
            while i > topRight[0]:
                arr.append(grid[i][j])
                i -= 1

            n = len(arr)
            arr = arr[k % n:] + arr[:k % n] # Taking modulus value
            
            
            self.assign(temp, rows, cols, i, j, arr,topLeft, topRight, bottomRight, bottomLeft )
            
            i += 1
            j += 1
            topLeft[0] += 1
            topLeft[1] += 1
            topRight[0] += 1
            topRight[1] -= 1
            bottomRight[0] -= 1
            bottomRight[1] -= 1
            bottomLeft[0] -= 1
            bottomLeft[1] += 1
            
        
        return temp
                    

solution = Solution()
m=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(solution.rotateGrid(m,2))

















