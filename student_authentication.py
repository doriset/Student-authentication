from collections import defaultdict

op_star = [
    [2, 3, 4, 1, 0, 5],
    [4, 5, 1, 0, 2, 3],
    [3, 4, 5, 2, 1, 0],
    [0, 2, 3, 4, 5, 1],
    [1, 0, 2, 5, 3, 4],
    [5, 1, 0, 3, 4, 2]
]

op_circ = [
    [4, 2, 1, 0, 5, 3],
    [5, 0, 3, 2, 4, 1],
    [3, 5, 1, 0, 2, 4],
    [1, 3, 2, 4, 0, 5],
    [2, 4, 5, 3, 1, 0],
    [0, 1, 4, 5, 3, 2]
]

A_values = defaultdict(int)
B_values = defaultdict(int)

for x1 in range(6):
    for x2 in range(6):
        for x3 in range(6):
            for x4 in range(6):
                A = op_star[op_star[op_star[x1][x2]][x3]][x4]
                print(f'A = {A}')
                A_values[A] += 1

for x5 in range(6):
    for x6 in range(6):
        for x7 in range(6):
            B = op_circ[op_circ[x5][x6]][x7]
            print(f'B = {B}')
            B_values[B] += 1

max_students = 0
for key in A_values:
    max_students += min(A_values[key], B_values[key])
    print(f'Max_stud = {max_students}')

print(max_students)