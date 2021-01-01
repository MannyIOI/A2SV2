# while the row is less than 3 and column is less than 4
#       if there is space to the left:
#           walk left
#       else:
#           reset row number and increase column number by 1

#       if there is space to the bottom:
#           walk down
#       else: 
#           reset column number and increase column number by 1
#       print
col = 0
row = 0
max_col_size = 3
max_row_size = 4

while col < max_col_size and row < max_row_size:
    if col >= 0:
        col = col - 1
    else:
        row = 0
        col = min(col + 1, max_col_size)
    
    if row < 4:
        row = row + 1
    else:
        col = min(col + 1, max_col_size)
