from util import Node, QueueFrontier

initial_state = (3, 3, 'L')
goal_state = (0, 0, 'R')

def is_valid(state):
    missionaries, cannibals, boat = state
    if missionaries < 0 or missionaries > 3:
        return False
    if cannibals < 0 or cannibals > 3:
        return False
    # El número de caníbales no puede exceder el número de misioneros en ninguno de los lados del río.
    if missionaries < cannibals and missionaries > 0:
        return False
    if (3 - missionaries) < (3 - cannibals) and (3 - missionaries) > 0:
        return False
    return True

# Actions: 1 misionero cruza, 1 caníbal cruza, 1 misionero y 1 caníbal cruzan, 2 misioneros cruzan, 2 caníb
def successors(state):
    successors = []
    missionaries, cannibals, boat = state
    if boat == 'L':
        # 1 misionero cruza de izquierda a derecha.
        if missionaries > 0:
            new_state = (missionaries - 1, cannibals, 'R')
            if is_valid(new_state):
                successors.append(("1 misionero cruza", new_state))
        # 1 caníbal cruza de izquierda a derecha.
        if cannibals > 0:
            new_state = (missionaries, cannibals - 1, 'R')
            if is_valid(new_state):
                successors.append(("1 caníbal cruza", new_state))
        # 1 misionero y 1 caníbal cruzan de izquierda a derecha.
        if missionaries > 0 and cannibals > 0:
            new_state = (missionaries - 1, cannibals - 1, 'R')
            if is_valid(new_state):
                successors.append(("1 misionero y 1 caníbal cruzan", new_state))
        # 2 misioneros cruzan de izquierda a derecha.
        if missionaries > 1:
            new_state = (missionaries - 2, cannibals, 'R')
            if is_valid(new_state):
                successors.append(("2 misioneros cruzan", new_state))
        # 2 caníbales cruzan de izquierda a derecha.
        if cannibals > 1:
            new_state = (missionaries, cannibals - 2, 'R')
            if is_valid(new_state):
                successors.append(("2 caníbales cruzan", new_state))
    else:
        # 1 misionero cruza de derecha a izquierda.
        if (3 - missionaries) > 0:
            new_state = (missionaries + 1, cannibals, 'L')
            if is_valid(new_state):
                successors.append(("1 misionero regresa", new_state))
        # 1 caníbal cruza de derecha a izquierda.
        if (3 - cannibals) > 0:
            new_state = (missionaries, cannibals + 1, 'L')
            if is_valid(new_state):
                successors.append(("1 caníbal regresa", new_state))
        # 1 misionero y 1 caníbal cruzan de derecha a izquierda.
        if (3 - missionaries) > 0 and (3 - cannibals) > 0:
            new_state = (missionaries + 1, cannibals + 1, 'L')
            if is_valid(new_state):
                successors.append(("1 misionero y 1 caníbal regresan", new_state))
        # 2 misioneros cruzan de derecha a izquierda.
        if (3 - missionaries) > 1:
            new_state = (missionaries + 2, cannibals, 'L')
            if is_valid(new_state):
                successors.append(("2 misioneros regresan", new_state))
        # 2 caníbales cruzan de derecha a izquierda.
        if (3 - cannibals) > 1:
            new_state = (missionaries, cannibals + 2, 'L')
            if is_valid(new_state):
                successors.append(("2 caníbales regresan", new_state))
    return successors

def resolve_bfs():
    start = Node(state=initial_state, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(start)
    explored = set()

    while True:
        if frontier.empty():
            raise Exception("No se encontró solución")
        node = frontier.remove()

        if node.state == goal_state:
            actions = []
            cells = []
            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
            actions.reverse()
            cells.reverse()
            return actions, cells

        explored.add(node.state)

        for action, state in successors(node.state):
            if not frontier.contains_state(state) and state not in explored:
                child = Node(state=state, parent=node, action=action)
                # print(child)
                frontier.add(child)

# Test
if __name__ == "__main__":
    actions, cells = resolve_bfs()

    print("\nSolución encontrada:")
    for i in range(len(actions)):
        print(f"Paso {i + 1}: {actions[i]} -> {cells[i]}")
