n = 3
a = 'a'
b = 'b'

board = []
#is_a = True
for i in range(n):
    row = []
    for j in range(n):
        row.append(n)
        #row.append(a if is_a else b)
        #is_a = False if is_a else True
    board.append(row)

print(board)

