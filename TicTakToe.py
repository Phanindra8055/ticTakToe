print("""\
    --------------------------TIC TAK TOE----------------------------
    Available moves:
    top left: 1     top middle: 2       top right: 3
    middle left: 4     middle middle: 5       middle right:6
    buttom left: 7      buttom middle: 8        buttom right: 9
    """)


def print_board(theboard):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def is_winner(board, turn):
    return ((board['1'] == board['2'] == board['3'] == turn) or
            (board['4'] == board['5'] == board['6'] == turn) or
            (board['7'] == board['8'] == board['9'] == turn) or
            (board['1'] == board['2'] == board['3'] == turn) or
            (board['4'] == board['5'] == board['6'] == turn) or
            (board['7'] == board['8'] == board['9'] == turn) or
            (board['1'] == board['5'] == board['9'] == turn) or
            (board['3'] == board['5'] == board['7'] == turn))



board = {
    '1': '1', '2': '2', '3': '3',
    '4': '4', '5': '5', '6': '6',
    '7': '7', '8': '8', '9': '9',
}

selected_moves = []

print_board(board)
turn = 'X'
i = 0

while True:
    
    print(f'Turn for {turn}. Move on which space?')
    move = input()
    while len(move) == 0:
        move = input()
        
    if move in selected_moves:
        print("{} already selected.".format(move))
        continue
        
    board[move] = turn
    print_board(board)
    selected_moves.append(move)
    
    if turn == 'X':
        if is_winner(board, turn):
            print("{} wins.".format(turn))
            break
        turn = 'O'
    else:
        if is_winner(board, turn):
            print("{} wins.".format(turn))
            break
        turn = 'X'
        
    if len(selected_moves) == 9:
        print("Game's Draw")
        break
