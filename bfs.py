from copy import deepcopy
from collections import deque

q = deque() # A queue to perform the BFS search.

visited = set() # A set to avoid reaching the previously visited state.

# To print the intermediate states while performing the BFS.

def print_current_state(a):
  for i in a:
    for j in i:
      print(j, end = " ")
    print()
  print()

def left(a):
  b = deepcopy(a);
  for i in range(len(b)):
    for j in range(len(b)):
      if a[i][j] == 0:
        if j - 1 >= 0:
          temp = b[i][j - 1]
          b[i][j - 1] = b[i][j]
          b[i][j] = temp
          c = tuple(map(tuple, b)) # Since lists are mutable it is required to be converted into some immutable container which can be used as a key in the dictionary. 
          if c in visited:
            return
          visited.add(c)
          q.append(b)
          return

def right(a):
  b = deepcopy(a);
  for i in range(len(b)):
    for j in range(len(b)):
      if a[i][j] == 0:
        if j + 1 < len(b):
          temp = b[i][j + 1]
          b[i][j + 1] = b[i][j]
          b[i][j] = temp
          c = tuple(map(tuple, b))
          if c in visited:
            return
          visited.add(c)
          q.append(b)
          return

def up(a):
  b = deepcopy(a);
  for i in range(len(b)):
    for j in range(len(b)):
      if a[i][j] == 0:
        if i - 1 >= 0:
          temp = b[i - 1][j]
          b[i - 1][j] = b[i][j]
          b[i][j] = temp
          c = tuple(map(tuple, b))
          if c in visited:
            return
          visited.add(c)
          q.append(b)
          return

def down(a):
  b = deepcopy(a);
  for i in range(len(b)):
    for j in range(len(b)):
      if a[i][j] == 0:
        if i + 1 < len(b):
          temp = b[i + 1][j]
          b[i + 1][j] = b[i][j]
          b[i][j] = temp
          c = tuple(map(tuple, b))
          if c in visited:
            return
          visited.add(c)
          q.append(b)
          return

def bfs(a, b):

  q.append(a)

  count = 0
  
  while len(q) is not 0:
    
    count += 1;

    now = q.popleft()

    print_current_state(now)

    if now == b:
      print("Reached destination at iteration ", count)
      return
    
    for i in range(len(now)):
      for j in range(len(now)):
        if now[i][j] == 0:
            left(now)
            up(now)
            down(now)
            right(now)
     
a = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
b = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]

bfs(a, b)
