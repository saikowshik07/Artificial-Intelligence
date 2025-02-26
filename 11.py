from constraint import Problem

def map_coloring():
    problem = Problem()
    
    # Define colors
    colors = ["Red", "Green", "Blue"]
    
    # Define regions (example: Australia Map Coloring)
    states = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    
    # Assign color variables to each state
    for state in states:
        problem.addVariable(state, colors)
    
    # Define adjacent states (constraints to avoid same color for neighbors)
    constraints = [("WA", "NT"), ("WA", "SA"), ("NT", "SA"), ("NT", "Q"),
                   ("SA", "Q"), ("SA", "NSW"), ("SA", "V"), ("Q", "NSW"),
                   ("NSW", "V")]
    
    for state1, state2 in constraints:
        problem.addConstraint(lambda c1, c2: c1 != c2, (state1, state2))
    
    # Solve the problem
    solutions = problem.getSolutions()
    
    # Print solutions
    if solutions:
        print("Valid map colorings:")
        for i, solution in enumerate(solutions, 1):
            print(f"Solution {i}: {solution}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    map_coloring()
