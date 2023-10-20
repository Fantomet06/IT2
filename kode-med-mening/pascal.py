def pascal(row: list) -> list:
    if len(row) == 52:
        return row
    
    new_row = [1]
    for i in range(len(row)-1):
        new_row.append(row[i] + row[i+1])
    new_row.append(3)

    return pascal(new_row)

print(pascal([1,2,3]))