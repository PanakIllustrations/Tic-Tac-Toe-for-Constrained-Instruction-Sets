import math

WIN_MASKS = [
    448, 56, 7,     # 0b111000000, 0b000111000, 0b000000111 - rows
    292, 146, 73,   # 0b100100100, 0b010010010, 0b001001001 - cols
    273, 84         # 0b100010001, 0b001010100 - diag
    ] 

def float_set_bit(bb, i):
    return bb + 2 ** i

def float_get_bit(bb, i):
    return math.floor(bb / 2 ** i) % 2

def float_and_operation(bb, m):
    result = 0
    v11 = 0
    while v11 < 9:
        b1 = float_get_bit(bb, v11)
        b2 = float_get_bit(m, v11)
        if b1 == 1 and b2 == 1:
            result += 2 ** v11
        v11 += 1
    return result

def is_win(bb):
    v10 = 0
    while v10 < 8:
        if float_and_operation(bb, WIN_MASKS[v10]) == WIN_MASKS[v10]:
            return True
        v10 += 1
    return False

def is_square_occupied(bb_x, bb_o, i):
    if float_get_bit(bb_x, i) == 1:
        return True
    if float_get_bit(bb_o, i) == 1:
        return True
    return False

def print_board(bb_x, bb_o):
    v10 = 0
    while v10 < 9:
        if float_get_bit(bb_x, v10) == 1:
            print("X", end=" ")
        elif float_get_bit(bb_o, v10) == 1:
            print("O", end=" ")
        else:
            print(".", end=" ")
        
        if v10 % 3 == 2:
            print("")
        v10 += 1
    print("")

def get_valid_moves(bb_x, bb_o):
    moves = []
    v10 = 0
    while v10 < 9:
        if not is_square_occupied(bb_x, bb_o, v10):
            moves.append(v10)
        v10 += 1
    return moves

def count_in_row(bb, mask):
    count = 0
    v11 = 0
    while v11 < 9:
        if float_get_bit(mask, v11) == 1:
            if float_get_bit(bb, v11) == 1:
                count += 1
        v11 += 1
    return count

def has_two_in_row(bb):
    v10 = 0
    while v10 < 8:
        if count_in_row(bb, WIN_MASKS[v10]) == 2:
            return True
        v10 += 1
    return False

def generate_ai_strategy_easy():
    # edges > corners > center
    return [1, 3, 5, 7, 0, 2, 6, 8, 4]

def generate_ai_strategy_medium():
    # corners > center > edges
    return [0, 2, 6, 8, 4, 1, 3, 5, 7]

def generate_ai_strategy_impossible():
    # center > corners > edges
    return [4, 0, 2, 6, 8, 1, 3, 5, 7]

def simple_ai(bb_x, bb_o, strategy, move_num):
    valid = get_valid_moves(bb_x, bb_o)
    
    # 1. Only block if player is about to win
    if has_two_in_row(bb_x):
        for move in valid:
            bb_test = float_set_bit(bb_x, move)
            if is_win(bb_test):
                return move
    
    # 2. Only win if 2 already in a row
    if has_two_in_row(bb_o):
        for move in valid:
            bb_test = float_set_bit(bb_o, move)
            if is_win(bb_test):
                return move
    
    # 3. Otherwise follow preset preference
    for pos in strategy:
        if pos in valid:
            return pos
    
    return valid[0]

bb_x = 0
bb_o = 0
move_count = 0
game_active = 1
ai_strategy = generate_ai_strategy()

print_board(bb_x, bb_o)

while game_active == 1:
    
    # PLAYER TURN
    player_move = int(input(""))
    
    if player_move < 0 or player_move > 8:
        print("Must be 0-8")
        continue
    if is_square_occupied(bb_x, bb_o, player_move):
        print("Square occupied")
        continue
    
    bb_x = float_set_bit(bb_x, player_move)
    move_count += 1
    print_board(bb_x, bb_o)
    
    if is_win(bb_x):
        print("Player Wins!\n")
        game_active = 0
        break
    
    if move_count >= 9:
        print("Draw!\n")
        game_active = 0
        break
    
    # AI TURN
    ai_move = simple_ai(bb_x, bb_o, ai_strategy, move_count)
    bb_o = float_set_bit(bb_o, ai_move)
    move_count += 1
    print_board(bb_x, bb_o)
    
    if is_win(bb_o):
        print("AI Wins!\n")
        game_active = 0
        break
    
    if move_count >= 9:
        print("Draw!\n")
        game_active = 0
        break