class Solution:
    def rotateMatrix(self, mat):
        rows=len(mat)
        cols=len(mat[0])
        top=0
        left=0
        bottom=rows-1
        right=cols-1
        
        while left<right and top<bottom:
            temp=mat[bottom][left]
            
        #leftcolumn:
            if left<=right:
                for i in range(bottom,top,-1):
                    mat[i][left]=mat[i-1][left]
            
        #upperrow
            for i in range(left,right):
                mat[top][i]=mat[top][i+1]
            
        #rightcolum:
            for i in range(top,bottom):
                mat[i][right]=mat[i+1][right]
        
        #bottomrow:
            if top<=bottom:
                for i in range(right,left+1,-1):
                    mat[bottom][i]=mat[bottom][i-1]
        
        
            
            mat[bottom][left+1]=temp
        
            top+=1
            left+=1
            right-=1
            bottom-=1
        
        return mat
        
    
                
            
        