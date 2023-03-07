class Solution:
    def biggest_neighbour(nrows: int, ncols: int, matrix: 'list[list[int]]'):
      '''Return a tuple of number of neighbour, row index of House, column index of House.'''
        neighbour = 0
        for i in range(nrows):
            
            for j in range(ncols):
       
                group = 0
                if matrix[i][j] == 1:
                    if j < ncols - 1 and matrix[i][j + 1] == 1:
                        group += 1


                    if j > 0 and matrix[i][j - 1] == 1:
                        group += 1



                    if i < nrows - 1 and matrix[i + 1][j] == 1:
                        group += 1


                    if i > 0 and matrix[i - 1][j] == 1:
                        group += 1

                    if group > neighbour:
                        neighbour = group
                        
                    if neighbour == 4:
                        return neighbour, i, j
                      
        return neighbour, i, j
      

      
if __name__ == '__main__':
  from random import randint
  
  nrows = 10
  ncols = 10
  matrix = [[randint(0, 1) for col in range(ncols)] for row in range(nrows)]
  print(matrix)
  
  result = Solution.biggest_neighbour(nrows, ncols, matrix)
  # return a tuple (number of neighbour, row index of House, column index of House)
  
  print(result)
