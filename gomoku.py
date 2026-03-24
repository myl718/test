BOARD_SIZE = 15

def create_board():
    return [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(board):
    print('  ' + ' '.join([str(i).rjust(2) for i in range(BOARD_SIZE)]))
    for i, row in enumerate(board):
        print(str(i).rjust(2) + ' ' + ' '.join(row))

def check_win(board, row, col, player):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        count = 1
        for sign in [1, -1]:
            r, c = row + dr * sign, col + dc * sign
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
                count += 1
                r += dr * sign
                c += dc * sign
        if count >= 5:
            return True
    return False

def is_valid_move(board, row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == '.'

def main():
    board = create_board()
    players = ['X', 'O']
    current = 0

    print("五子棋游戏")
    print("输入格式: 行 列 (例如: 7 7)")
    print()

    while True:
        print_board(board)
        print(f"\n玩家 {players[current]} 的回合")

        try:
            move = input("请输入位置: ").split()
            row, col = int(move[0]), int(move[1])
        except (ValueError, IndexError):
            print("输入无效，请重新输入")
            continue

        if not is_valid_move(board, row, col):
            print("位置无效，请重新输入")
            continue

        board[row][col] = players[current]

        if check_win(board, row, col, players[current]):
            print_board(board)
            print(f"\n玩家 {players[current]} 获胜!")
            break

        if all(board[r][c] != '.' for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)):
            print_board(board)
            print("\n平局!")
            break

        current = 1 - current

if __name__ == "__main__":
    main()
