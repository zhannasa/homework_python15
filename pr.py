import argparse


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for row in range(rows)] for col in range(cols)]

    for row in range(rows):
        for col in range(cols):
            transposed[col][row] = matrix[row][col]

    return transposed


parser = argparse.ArgumentParser(description='Transpose a matrix.')
parser.add_argument('matrix', metavar='N', type=int, nargs='+',
                    help='The matrix to transpose (provide elements separated by spaces)')


args = parser.parse_args()


rows = int(len(args.matrix) ** 0.5)
matrix = [args.matrix[i:i+rows] for i in range(0, len(args.matrix), rows)]


transposed_matrix = transpose(matrix)

print("Original matrix:")
for row in matrix:
    print(row)

print("Transposed matrix:")
for row in transposed_matrix:
    print(row)

