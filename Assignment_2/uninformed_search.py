def valid_state(M1, C1):
    if M1 < 0 or M1 > 3 or C1 < 0 or C1 > 3:
        return False

    M2 = 3 - M1
    C2 = 3 - C1

    if M1 > 0 and C1 > M1:
        return False

    if M2 > 0 and C2 > M2:
        return False

    return True


def get_next_state(state, moves):
    M_left, C_left, BL, M_right, C_right, BR = state
    children = []

    if BL == 1:
        for m, c in moves:
            new_ML = M_left - m
            new_CL = C_left - c
            if valid_state(new_ML, new_CL):
                children.append([
                    new_ML, new_CL, 0,
                    M_right + m, C_right + c, 1
                ])

    if BR == 1:
        for m, c in moves:
            new_MR = M_right - m
            new_CR = C_right - c
            if valid_state(new_MR, new_CR):
                children.append([
                    M_left + m, C_left + c, 1,
                    new_MR, new_CR, 0
                ])

    return children


def print_path(parent, final_state):
    path = []
    temp = tuple(final_state)

    while temp is not None:
        path.insert(0, temp)
        temp = parent[temp]

    print(path)


initial_state = [3,3,1,0,0,0]
final_state   = [0,0,0,3,3,1]
moves = [[1,1], [1,0], [0,1], [2,0], [0,2]]


visited = []
parent = {}
queue = []

queue.append(initial_state)
visited.append(initial_state)
parent[tuple(initial_state)] = None

while queue:
    curr = queue.pop(0)

    if curr == final_state:
        break

    children = get_next_state(curr, moves)

    for child in children:
        if child not in visited:
            queue.append(child)
            visited.append(child)
            parent[tuple(child)] = tuple(curr)

print("BFS Solution:")
print_path(parent, final_state)


visited = []
parent = {}
stack = []

stack.append(initial_state)
visited.append(initial_state)
parent[tuple(initial_state)] = None

while stack:
    curr = stack.pop()

    if curr == final_state:
        break

    children = get_next_state(curr, moves)

    for child in children:
        if child not in visited:
            stack.append(child)
            visited.append(child)
            parent[tuple(child)] = tuple(curr)

print("\nDFS Solution:")
print_path(parent, final_state)


limit = 4
visited = []
parent = {}
stack = []
found = False

stack.append((initial_state, 0))
visited.append(initial_state)
parent[tuple(initial_state)] = None

while stack:
    curr, depth = stack.pop()

    if curr == final_state:
        found = True
        break

    if depth < limit:
        children = get_next_state(curr, moves)

        for child in children:
            if child not in visited:
                stack.append((child, depth+1))
                visited.append(child)
                parent[tuple(child)] = tuple(curr)

if found:
    print(f"\nDepth Bounded DFS Solution (limit={limit}):")
    print_path(parent, final_state)
else:
    print(f"\nDepth Bounded DFS did not find solution with limit {limit}")


limit = 0
found = False

while not found:
    visited = []
    parent = {}
    stack = []

    stack.append((initial_state, 0))
    visited.append(initial_state)
    parent[tuple(initial_state)] = None

    while stack:
        curr, depth = stack.pop()

        if curr == final_state:
            found = True
            break

        if depth < limit:
            children = get_next_state(curr, moves)

            for child in children:
                if child not in visited:
                    stack.append((child, depth+1))
                    visited.append(child)
                    parent[tuple(child)] = tuple(curr)

    limit += 1

print(f"\nDFID Solution (found at depth {limit-1}):")
print_path(parent, final_state)
