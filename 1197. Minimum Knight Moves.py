class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dx = [2, 2, -2, -2, 1, 1, -1, -1] #8 direction option
        dy = [1, -1, 1, -1, 2, -2, 2, -2] #
        x,y=abs(x),abs(y) #absolute value
        queue = [] 

        queue.append((0 ,0, 0)) 

        visited = [[False for j in range(y + 3)]  
                          for i in range(x + 3)] 

        visited[0][0] = True
 
        while(len(queue) > 0): 

            q = queue[0] 
            queue.pop(0) 

            if(q[0] == x and q[1] == y): #found our destination
                return q[2] 

            for i in range(8): 
                X = q[0] + dx[i] 
                Y = q[1] + dy[i] 
                if(X<=x+2 and X>=0 and Y>=0 and Y<=y+2): 
                    if not visited[X][Y]: 
                        visited[X][Y] = True
                        queue.append((X, Y,q[2] + 1))


        