"""
Given a 2D Maze M represented as a 2D matrix surrounded with walls represented as 1 on all four sides. There are walls inside the maze as well. 0 in the matrix represent free passage. Roll the ball from starting point S given as an input to the hole, represented as the value 2 in the matrix. The ball goes until it hits a wall (1) and stops, and goes to another direction. 
1 1 1 1 1 1
1 S 0 0 0 1
1 0 1 1 0 1
1 0 0 1 0 1
1 0 0 1 0 1
1 1 0 2 P 1
1 1 1 1 1 1
"""
#S starting point
#M Maze 2D Matrix 1 for walls and 0 for free paths and 2 for the hole
# Return the path from S to the hole

def solve_maze(si, maze, path=[]):
  
  r, c = si
  
  dir_up = (r-1, c)
  dir_down = (r+1, c)
  dir_left  = (r, c-1)
  dir_right = (r, c +1) 
  
  active_dir = []
  
  for diri in [dir_up, dir_down, dir_left, dir_right]:
    ri, ci = diri
    
    if maze(ri, ci) == 0:
      active_dir.append(diri)
      pos = solve_maze(pos, maze, path=path)
      
    if maze(ri, ci) == 2:
      return((ri, ci))
 
   elif:
      continue
  
  return(pos)