def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])  # добавляем список
        for j in range(m):
            matrix[i].append(value)  # Пишем в список значение
    print(matrix)


get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)
