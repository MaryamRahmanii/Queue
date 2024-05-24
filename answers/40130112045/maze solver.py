class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None


    def is_empty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)



class mazesolver:

    def __init__(self, maze):

        self.maze = maze

        self.rows = len(maze)

        self.cols = len(maze[0])

        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        self.parent = [[None for _ in range(self.cols)] for _ in range(self.rows)]



    def is_valid_move(self, row, col):

        return 0 <= row < self.rows and 0 <= col < self.cols and not self.visited[row][col] and self.maze[row][col] == 0



    def bfs(self, start, end):

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = Queue()

        q.enqueue(start)

        self.visited[start[0]][start[1]] = True



        while not q.is_empty():

            current = q.dequeue()

            if current == end:

                break

            for dr, dc in directions:

                new_row, new_col = current[0] + dr, current[1] + dc

                if self.is_valid_move(new_row, new_col):

                    q.enqueue((new_row, new_col))

                    self.visited[new_row][new_col] = True

                    self.parent[new_row][new_col] = current



        path = []

        current = end

        while current is not None:

            path.append(current)

            current = self.parent[current[0]][current[1]]

        return path[::-1]







maze=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

start=(0,0)
end=(3,3)

solver=mazesolver(maze)

shortestpath=solver.bfs(start,end)

print(shortestpath)
