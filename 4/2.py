with open('data.txt') as data_file:
	data = data_file.read().split('\n\n')

balls = data[0]

balls = [int(number) for number in balls.split(',')]

boards = data[1:]

boards = [[(int(number), False) for number in board.split()] for board in boards]

def check_board(board: list[tuple[int, bool]]) -> bool:
	bool_board = [cell[1] for cell in board]
	rows_check = any([all(bool_board[i*5:i*5+5]) for i in range(5)])
	cols_check = any([all(bool_board[i::5]) for i in range(5)])

	board_check = any([rows_check, cols_check])
	
	return board_check

def mark_board(board: list[tuple[int, bool]], number: int) -> None:
	return [(cell[0], cell[1] or cell[0] == number) for cell in board]

def print_board(board: list[tuple[int, bool]]) -> None:
	for i, cell in enumerate(board):
		print(str(cell).ljust(11), end='\n' if (i+1)%5==0 else ' ')

for number in balls:
	boards = [mark_board(board, number) for board in boards]
	boards = [board for board in boards if not check_board(board)]
	if boards:
		last_board = boards[-1]
	if not boards:
		winning_number = number
		break

last_board = mark_board(last_board, number)
print(winning_number)
print_board(last_board)
print()
print(sum([cell[0] for cell in last_board if not cell[1]])*winning_number)
