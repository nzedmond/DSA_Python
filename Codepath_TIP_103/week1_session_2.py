# Transposing matrix

def transpose_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    transp_matrix = [[0]*num_rows for _ in range(num_cols)]
    '''
    [0 0 0]
    [0 0 0]
    [0 0 0]
    '''

    for i in range(num_rows):
        for j in range(num_cols):
            transp_matrix[j][i] = matrix[i][j]

    return transp_matrix

def reverse_list(list):
    pass

def main():
    matrix_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(transpose_matrix(matrix_1))

    lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]


if __name__ == "__main__":
    main()