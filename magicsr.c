def is_magic_square(matrix):
    n = len(matrix)
    reference_sum = sum(matrix[0])

    # Check the sum of each row
    for row in matrix:
        if sum(row) != reference_sum:
            return False

    # Check the sum of each column
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != reference_sum:
            return False

    # Check the sum of the main diagonal
    if sum(matrix[i][i] for i in range(n)) != reference_sum:
        return False

    # Check the sum of the other diagonal
    if sum(matrix[i][n - i - 1] for i in range(n)) != reference_sum:
        return False

    return True

def get_matrix_from_user():
    n = int(input("Enter the size of the square matrix (e.g., 3 for a 3x3 matrix): "))
    matrix = []
    print(f"Enter the {n}x{n} matrix:")
    for _ in range(n):
        row = [int(x) for x in input().split()]
        if len(row) != n:
            print(f"Invalid input. Each row should have {n} elements.")
            return None
        matrix.append(row)
    return matrix

# Get the matrix from the user
matrix = get_matrix_from_user()

if matrix is not None:
    if is_magic_square(matrix):
        print("It is a magic square.")
    else:
        print("It is not a magic square.")
