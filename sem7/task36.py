def print_operation_table(operation, num_rows: int = 6, num_columns: int = 6):
    for row in range(1, num_rows + 1):
        print([operation(row, column) for column in range(1, num_columns + 1)])


print_operation_table(lambda x, y: x * y)
