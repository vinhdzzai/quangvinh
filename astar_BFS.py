import heapq
from collections import deque

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0  # Chi phí từ điểm bắt đầu đến node hiện tại
        self.h = 0  # Chi phí ước lượng từ node hiện tại đến đích
        self.f = 0  # Tổng chi phí (g + h)
        self.parent = None  # Con trỏ đến node cha

    def __lt__(self, other):
        return self.f < other.f

class Pathfinding:
    def __init__(self, grid):
        self.grid = grid

    # Hàm tính khoảng cách Manhattan
    def heuristic(self, a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)

    # Thuật toán A* kết hợp với BFS
    def a_star_bfs(self, start, goal):
        open_set = []
        heapq.heappush(open_set, start)
        all_nodes = {}
        path = []

        all_nodes[(start.x, start.y)] = start

        while open_set:
            current = heapq.heappop(open_set)

            if current.x == goal.x and current.y == goal.y:
                # Xây dựng đường đi
                while current:
                    path.append(current)
                    current = current.parent
                path.reverse()  # Đảo ngược để có đường đi từ start đến goal
                return path  # Trả về đường đi

            # Các điểm lân cận
            neighbors = [
                Node(current.x + 1, current.y),
                Node(current.x - 1, current.y),
                Node(current.x, current.y + 1),
                Node(current.x, current.y - 1)
            ]

            for neighbor in neighbors:
                if self.is_valid(neighbor):
                    tentative_g = current.g + 1

                    if (neighbor.x, neighbor.y) not in all_nodes or tentative_g < neighbor.g:
                        neighbor.g = tentative_g
                        neighbor.h = self.heuristic(neighbor, goal)
                        neighbor.f = neighbor.g + neighbor.h
                        neighbor.parent = current

                        all_nodes[(neighbor.x, neighbor.y)] = neighbor
                        heapq.heappush(open_set, neighbor)

        return path  # Trả về đường đi (rỗng nếu không tìm thấy)

    # Kiểm tra tính hợp lệ của node
    def is_valid(self, node):
        return (0 <= node.x < len(self.grid) and
                0 <= node.y < len(self.grid[0]) and
                self.grid[node.x][node.y] == 0)

# Ví dụ sử dụng
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    pathfinding = Pathfinding(grid)
    start = Node(0, 0)
    goal = Node(4, 4)

    a_star_bfs_path = pathfinding.a_star_bfs(start, goal)
    print("Path found using A* with BFS:")
    for node in a_star_bfs_path:
        print(f"({node.x}, {node.y}) ", end="")
    print()