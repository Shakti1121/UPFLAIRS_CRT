# 1. Pascal's Triangle using nested loops
def pascals_triangle(rows):
    for i in range(rows):
        row = [1]  # First element is always 1
        if i > 0:
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])  # Sum of two elements above
            row.append(1)  # Last element is always 1
        print(" " * (rows - i), " ".join(map(str, row)))
        prev_row = row

pascals_triangle(5)