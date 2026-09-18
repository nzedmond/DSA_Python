# Transposing matrix

def transpose_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    transp_matrix = [[0]*num_rows for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transp_matrix[j][i] = matrix[i][j]

    return transp_matrix


def main():
    matrix_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(transpose_matrix(matrix_1))


if __name__ == "__main__":
    main()