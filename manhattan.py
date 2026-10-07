import heapq

def manhattan_distance(state, goal):
    distance = 0

    for tile in range(1, 9):
        current = state.index(tile)
        target = goal.index(tile)

        r1, c1 = divmod(current, 3)
        r2, c2 = divmod(target, 3)

        distance += abs(r1 - r2) + abs(c1 - c2)

    return distance

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = list(state)
            new_zero = nr * 3 + nc

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors

def astar(start, goal):
    pq = []
    heapq.heappush(pq, (manhattan_distance(start, goal), 0, start, [start]))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                h = manhattan_distance(neighbor, goal)
                new_f = new_g + h

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None

start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

path = astar(start, goal)

for state in path:
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()
