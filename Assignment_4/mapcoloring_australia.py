graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Queensland'],
    'Queensland': ['NT', 'SA', 'NSW'],
    'SA': ['NT', 'WA', 'Queensland', 'NSW', 'V'],
    'NSW': ['V', 'SA', 'Queensland'],
    'V': ['NSW', 'SA'],
    'T': []
}

colors = ['Pink', 'Green', 'Blue']

def is_valid(region, color, assignment):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(graph):
        return assignment

    for region in graph:
        if region not in assignment:
            break

    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]

    return None

solution = backtrack({})
print("Solution:", solution)
