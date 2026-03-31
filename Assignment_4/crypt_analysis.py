from itertools import permutations

def solve_cryptarithm():
    variables = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    domain = range(10)

    for perm in permutations(domain, len(variables)):
        assignment = dict(zip(variables, perm))

        # Leading digit constraint
        if assignment['S'] == 0 or assignment['M'] == 0:
            continue

        send = (1000 * assignment['S'] +
                100 * assignment['E'] +
                10 * assignment['N'] +
                assignment['D'])

        more = (1000 * assignment['M'] +
                100 * assignment['O'] +
                10 * assignment['R'] +
                assignment['E'])

        money = (10000 * assignment['M'] +
                 1000 * assignment['O'] +
                 100 * assignment['N'] +
                 10 * assignment['E'] +
                 assignment['Y'])

        # Constraint check
        if send + more == money:
            print("Solution Found:\n")
            print(f"S={assignment['S']} E={assignment['E']} N={assignment['N']} D={assignment['D']}")
            print(f"M={assignment['M']} O={assignment['O']} R={assignment['R']} Y={assignment['Y']}")
            print("\nVerification:")
            print(f"{send} + {more} = {money}")
            return

    print("No solution found")


solve_cryptarithm()
