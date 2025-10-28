import util

class SearchProblem:
    def getStartState(self):
        util.raiseNotDefined()

    def isGoalState(self, state):
        util.raiseNotDefined()

    def getSuccessors(self, state):
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    search algorithm needs to return a list of actions that reaches the
    goal.
    """
    fringe = util.Stack()
    visited = set()

    # The fringe will store tuples of (state, list_of_actions)
    start_state = problem.getStartState()
    fringe.push( (start_state, []) )

    while not fringe.isEmpty():
        current_state, actions = fringe.pop()

        if current_state in visited:
            continue

        visited.add(current_state)

        if problem.isGoalState(current_state):
            return actions

        # Get the next possible states
        successors = problem.getSuccessors(current_state)
        for next_state, action, cost in successors:
            if next_state not in visited:
                new_actions = actions + [action]
                fringe.push( (next_state, new_actions) )

    return [] # Return an empty list if no solution is found

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    fringe = util.Queue()
    visited = set()

    # The fringe will store tuples of (state, list_of_actions)
    start_state = problem.getStartState()
    fringe.push( (start_state, []) )
    visited.add(start_state) # Avoid re-visiting the start node

    while not fringe.isEmpty():
        current_state, actions = fringe.pop()

        if problem.isGoalState(current_state):
            return actions
        
        # Get the next possible states
        successors = problem.getSuccessors(current_state)
        for next_state, action, cost in successors:
            if next_state not in visited:
                visited.add(next_state)
                new_actions = actions + [action]
                fringe.push( (next_state, new_actions) )
    
    return [] # Return an empty list if no solution is found

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    fringe = util.PriorityQueue()
    visited = set()

    # Fringe stores tuples of ( (state, actions, cost), priority )
    start_state = problem.getStartState()
    fringe.push( (start_state, [], 0), 0 )

    while not fringe.isEmpty():
        current_state, actions, current_cost = fringe.pop()

        if current_state in visited:
            continue

        visited.add(current_state)

        if problem.isGoalState(current_state):
            return actions

        successors = problem.getSuccessors(current_state)
        for next_state, action, cost in successors:
            if next_state not in visited:
                new_actions = actions + [action]
                new_cost = current_cost + cost
                fringe.push( (next_state, new_actions, new_cost), new_cost )

    return [] # Return an empty list if no solution is found

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    fringe = util.PriorityQueue()
    visited = set()

    # Fringe stores tuples of ( (state, actions), priority )
    start_state = problem.getStartState()
    initial_heuristic = heuristic(start_state, problem)
    fringe.push( (start_state, []), initial_heuristic )

    while not fringe.isEmpty():
        current_state, actions = fringe.pop()

        if current_state in visited:
            continue

        visited.add(current_state)

        if problem.isGoalState(current_state):
            return actions

        successors = problem.getSuccessors(current_state)
        for next_state, action, cost in successors:
            if next_state not in visited:
                new_actions = actions + [action]
                # g(n): Cost of the path from the start to the successor
                g_cost = problem.getCostOfActions(new_actions)
                # h(n): Heuristic estimate from the successor to the goal
                h_cost = heuristic(next_state, problem)
                # f(n) = g(n) + h(n)
                f_cost = g_cost + h_cost
                fringe.push( (next_state, new_actions), f_cost )

    return [] 
