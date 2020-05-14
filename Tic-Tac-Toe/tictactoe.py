#
#   T I C - T A C - T O E
#

moves_data = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

#
#  Functions
#

def print_coordinate():
	print(" -----------------")
	print("|(1,3) (2,3) (3,3)|")
	print("|(1,2) (2,2) (2,3)|")
	print("|(1,1) (1,2) (1,3)|")
	print(" -----------------")

def print_tic_tac_toe(matrix):  # printing tic-tac-toe matrix
    print("---------")
    print('| ' + matrix[0] + ' ' + matrix[1] + ' ' + matrix[2] + ' |')
    print('| ' + matrix[3] + ' ' + matrix[4] + ' ' + matrix[5] + ' |')
    print('| ' + matrix[6] + ' ' + matrix[7] + ' ' + matrix[8] + ' |')
    print("---------")


def win(matrix, player):  # checking player wins
    i = 0
    while i < 7:  # checking the rows data
        if matrix[0 + i] == matrix[1 + i] == matrix[2 + i] == player:
            return True
        i += 3
    i = 0
    while i < 3:  # checking the column data
        if matrix[0 + i] == matrix[3 + i] == matrix[6 + i] == player:
            return True
        i += 1
    # checking both diagonal data
    if matrix[0] == matrix[4] == matrix[8] == player:
        return True
    if matrix[2] == matrix[4] == matrix[6] == player:
        return True
    return False


def draw(matrix):  # checking for draw condition
    if win(matrix, 'X') or win(matrix, 'O'):
        return False
    i = 0
    while i < 9:
        if matrix[i] == ' ':
            return False
        i += 1
    return True


def read_coordinate():  # analysing the coordinates input
    text = input("Enter the coordinates: ")
    # text = input()
    text_list = text.split()
    for a in text_list:
        for d in a:
            if d < '0' or d > '9':
                print("You should enter numbers!")
                return []
    x_coordinate = int(text_list[0])
    y_coordinate = int(text_list[1])
    if x_coordinate > 3 or x_coordinate < 1 or y_coordinate > 3 or y_coordinate < 1:
        print("Coordinates should be from 1 to 3!")
        return []
    return [x_coordinate, y_coordinate]


def coordinate_to_index(coordinate):  # mapping coordinate to index
    x = coordinate[0]
    y = coordinate[1]
    if x == 1 and y == 3:
        return 0
    if x == 2 and y == 3:
        return 1
    if x == 3 and y == 3:
        return 2
    if x == 1 and y == 2:
        return 3
    if x == 2 and y == 2:
        return 4
    if x == 3 and y == 2:
        return 5
    if x == 1 and y == 1:
        return 6
    if x == 2 and y == 1:
        return 7
    if x == 3 and y == 1:
        return 8

#
#  Functions ends here
#

print_coordinate()
print_tic_tac_toe(moves_data)  # printing empty matrix
toggle = 1  # to toggle between 'X' and 'O'
while True:
    coordinate = read_coordinate()
    if len(coordinate) == 0:
        continue
    index = coordinate_to_index(coordinate)
    if moves_data[index] != ' ':
        print("This cell is occupied! Choose another one!")
        continue
    else:
        if toggle:
            moves_data[index] = 'X'
        else:
            moves_data[index] = 'O'
        toggle = 1 - toggle
        print_tic_tac_toe(moves_data)
        if win(moves_data, 'X'):
            print("X wins")
            break
        elif win(moves_data, 'O'):
            print("O wins")
            break
        elif draw(moves_data):
            print("Draw")
            break


