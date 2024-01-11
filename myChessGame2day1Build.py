# to add : 
    # pawn can en pessant
        # if the other pawn just moved from original spot to new spot,
            # enable the pawn to move diagonally
                # remove the enemy piece

    # make 8 extra queens just in case of promotion

    # check mate

        # i think we need a new function to store all the other sides attacked squares
            # get all moves
                # for each move add to attacked squares

        # if king is attacked
            # and king has no legal moves
            # and no piece has the ability to step into a blocking square (in between attacker and king)
            # it is check mate

# This is a chess game designed by Daniel Zeegler
# Jan 2, 2024
class Piece():
    def __init__(self, pos, name, cn, player):
        self.pos = pos
        self.name = name
        self.display_name = name[:2]
        self.capital_name = cn
        self.color = self.name[0]
        self.onBoard = True
        self.moves = []
        self.value = self.value_of_piece()
        self.player = player

    def value_of_piece(self):
        if self.name[1] == 'q':
            return 9
        if self.name[1] == 'r':
            return 5
        if self.name[1] == 'b' or self.name[1] == 'n':
            return 3
        if self.name[1] == 'p':
            return 1

    def move_piece(self, squares_taken):
         #show squares this piece can move to and save to self.moves
        possible_moves = []
        row = self.pos[0]
        rank = self.pos[1]
        self.moves = []
        rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        row_index = rows.index(row)
        rank_int = int(rank)

        if self.name[1] == 'p':
            if self.color == 'w':
                move = f'{row}{int(rank) + 1}'
                if move not in squares_taken:
                    self.moves.append(move)
                if rank == '2':
                    move = f'{row}{int(rank) + 2}'
                    if move not in squares_taken:
                        self.moves.append(move)
                if row_index > 1:
                    attack_left = f'{rows[row_index - 1]}{int(rank) + 1}'
                    if attack_left in squares_taken:
                        self.attack_or_not(attack_left, squares_taken)   
                if row_index < 7:
                    attack_right = f'{rows[row_index + 1]}{int(rank) + 1}'
                    if attack_right in squares_taken:
                        self.attack_or_not(attack_right, squares_taken)
            if self.color == 'b':
                if rank == '7':
                    move = f'{row}{int(rank) - 2}'
                    if move not in squares_taken:
                        self.moves.append(move)
                move = f'{row}{int(rank) - 1}'
                if move not in squares_taken:
                    self.moves.append(move)
                if row_index < 7:
                    attack_left = f'{rows[row_index + 1]}{int(rank) - 1}'
                    if attack_left in squares_taken:
                        self.attack_or_not(attack_left, squares_taken)
                if row_index > 1:
                    attack_right = f'{rows[row_index - 1]}{int(rank) - 1}'
                    if attack_right in squares_taken:
                        self.attack_or_not(attack_right, squares_taken)

        # queen is rook + bishop
        if self.name[1] == 'b' or self.name[1] == 'q':
            for i in range(1, 8 - row_index):
                if int(rank) + i < 9:
                    move = f'{rows[row_index + i]}{int(rank) + i}'
                    if move in squares_taken:
                        self.attack_or_not(move, squares_taken)
                        break
                    else:
                        self.moves.append(move)
            for i in range(1, row_index + 1):
                if int(rank) + i < 9:
                    move = f'{rows[row_index - i]}{int(rank) + i}'
                    if move in squares_taken:
                        self.attack_or_not(move, squares_taken)
                        break
                    else:
                        self.moves.append(move)
                        
            i = 1
            while rank_int > 1:
                if row_index + i < 8:
                    move = f'{rows[row_index + i]}{int(rank) - i}'
                    if move in squares_taken:
                        self.attack_or_not(move, squares_taken)
                        break
                    else:
                        self.moves.append(move)
                i += 1
                rank_int -= 1

            i = 1
            row_index = rows.index(row)
            while rank_int > 1:
                if row_index - i >= 0:
                    move = f'{rows[row_index - i]}{int(rank) - i}'
                    if move in squares_taken:
                        self.attack_or_not(move, squares_taken)
                        break
                    else:
                        self.moves.append(move)
                i += 1
                rank_int -= 1
        
        if self.name[1] == 'r' or self.name[1] == 'q':
            rank_int = int(rank)
            for i in range(1, 8 - row_index):
                move = f'{rows[row_index + i]}{int(rank)}'
                if move in squares_taken:
                    self.attack_or_not(move, squares_taken)
                    break
                else:
                    self.moves.append(move)
            for i in range(1, row_index + 1):
                move = f'{rows[row_index - i]}{int(rank)}'
                if move in squares_taken:
                    self.attack_or_not(move, squares_taken)
                    break
                else:
                    self.moves.append(move)
            for i in range(1, 9 - rank_int):
                move = f'{rows[row_index]}{int(rank) + i}'
                if move in squares_taken:
                    self.attack_or_not(move, squares_taken)
                    break
                else:
                    self.moves.append(move)
            for i in range(1, rank_int):
                move = f'{rows[row_index]}{int(rank) - i}'
                if move in squares_taken:
                    self.attack_or_not(move, squares_taken)
                    break
                else:
                    self.moves.append(move)

        if self.name[1] == 'k':
            king_moves = []
            if int(rank) < 8:
                king_moves.append(f'{rows[row_index]}{int(rank) + 1}')
            if int(rank) > 1:
                king_moves.append(f'{rows[row_index]}{int(rank) - 1}')
            if row_index < 8:
                king_moves.append(f'{rows[row_index + 1]}{int(rank)}')
                if int(rank) < 8:
                    king_moves.append(f'{rows[row_index + 1]}{int(rank) + 1}')
                if int(rank) > 1:
                    king_moves.append(f'{rows[row_index + 1]}{int(rank) - 1}')
            if row_index > 0:
                king_moves.append(f'{rows[row_index - 1]}{int(rank)}')
                if int(rank) < 8:
                    king_moves.append(f'{rows[row_index - 1]}{int(rank) + 1}')
                if int(rank) > 1:
                    king_moves.append(f'{rows[row_index - 1]}{int(rank) - 1}')
            for move in king_moves:
                if move in squares_taken:
                    self.attack_or_not(move, squares_taken)
                else:
                    self.moves.append(move)

        if self.name[1] == 'n':
            knight_moves = []
            if row_index + 2 < 8:
                if int(rank) + 1 <= 8:
                    knight_moves.append(f'{rows[row_index + 2]}{int(rank) + 1}')
                if int(rank) - 1 > 0:
                    knight_moves.append(f'{rows[row_index + 2]}{int(rank) - 1}')
            if row_index - 2 >= 0:
                if int(rank) + 1 <= 8:
                    knight_moves.append(f'{rows[row_index - 2]}{int(rank) + 1}')
                if int(rank) - 1 > 0:
                    knight_moves.append(f'{rows[row_index - 2]}{int(rank) - 1}')
            if int(rank) + 2 <= 8:
                if row_index + 1 < 8:
                    knight_moves.append(f'{rows[row_index + 1]}{int(rank) + 2}')
                if row_index >= 1:
                    knight_moves.append(f'{rows[row_index - 1]}{int(rank) + 2}')
            if int(rank) - 2 >= 1:
                if row_index + 1 < 8:
                    knight_moves.append(f'{rows[row_index + 1]}{int(rank) - 2}')
                if row_index >= 1:
                    knight_moves.append(f'{rows[row_index - 1]}{int(rank) - 2}')
            
            for move in knight_moves:
                if move in squares_taken:
                    self.attack_or_not(move, squares_taken)
                else:
                    self.moves.append(move)

        return self.moves
    
    def attack_or_not(self, move, squares_taken):
        takes = self.friend_or_foe(move, squares_taken)
        if takes != None:
            self.moves.append(takes)
            return
            
    def friend_or_foe(self, square, squares_taken):
        other_piece = squares_taken.get(square)
        if self.color != other_piece.color:
            return f'{self.display_name[1]}{self.pos}x{square}'
            
    def __repr__(self):
        return self.display_name

class Board:
    #initialize the pieces, linking them to their player
    def __init__(self, wp, bp):
        self.wk = Piece('e1', 'wk', 'King', wp)
        self.wq= Piece('d1', 'wq', 'Queen', wp)
        self.wr1 = Piece('a1', 'wr1', 'Rook', wp)
        self.wr2 = Piece('h1', 'wr2', 'Rook', wp)
        self.wn1 = Piece('b1', 'wn1', 'Knight', wp)
        self.wn2 = Piece('g1', 'wn2', 'Knight', wp)
        self.wb1 = Piece('c1', 'wb1', 'Bishop', wp)
        self.wb2 = Piece('f1', 'wb2', 'Bishop', wp)
        self.wp1 = Piece('a2', 'wp1', 'Pawn', wp)
        self.wp2 = Piece('b2', 'wp2', 'Pawn', wp)
        self.wp3 = Piece('c2', 'wp3', 'Pawn', wp)
        self.wp4 = Piece('d2', 'wp4', 'Pawn', wp)
        self.wp5 = Piece('e2', 'wp5', 'Pawn', wp)
        self.wp6 = Piece('f2', 'wp6', 'Pawn', wp)
        self.wp7 = Piece('g2', 'wp7', 'Pawn', wp)
        self.wp8 = Piece('h2', 'wp8', 'Pawn', wp)
        self.white_pieces = [self.wk, self.wq, self.wr1, self.wr2, self.wn1, self.wn2, self.wb1, self.wb2, self.wp1, self.wp2, self.wp3, self.wp4, self.wp5, self.wp6, self.wp7, self.wp8]

        self.bk = Piece('e8', 'bk', 'King', bp)
        self.bq = Piece('d8', 'bq', 'Queen', bp)
        self.br1 = Piece('h8', 'br1', 'Rook', bp)
        self.br2 = Piece('a8', 'br2', 'Rook', bp)
        self.bn1 = Piece('g8', 'bn1', 'Knight', bp)
        self.bn2 = Piece('b8', 'bn2', 'Knight', bp)
        self.bb1 = Piece('f8', 'bb1', 'Bishop', bp)
        self.bb2 = Piece('c8', 'bb2', 'Bishop', bp)
        self.bp1 = Piece('a7', 'bp1', 'Pawn', bp)
        self.bp2 = Piece('b7', 'bp2', 'Pawn', bp)
        self.bp3 = Piece('c7', 'bp3', 'Pawn', bp)
        self.bp4 = Piece('d7', 'bp4', 'Pawn', bp)
        self.bp5 = Piece('e7', 'bp5', 'Pawn', bp)
        self.bp6 = Piece('f7', 'bp6', 'Pawn', bp)
        self.bp7 = Piece('g7', 'bp7', 'Pawn', bp)
        self.bp8 = Piece('h7', 'bp8', 'Pawn', bp)
        self.black_pieces = [self.bk, self.bq, self.br1, self.br2, self.bn1, self.bn2, self.bb1, self.bb2, self.bp1, self.bp2, self.bp3, self.bp4, self.bp5, self.bp6, self.bp7, self.bp8]

        self.all_pieces = self.white_pieces + self.black_pieces

    def draw_board(self, player): 
        rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        ranks = ['1', '2', '3', '4', '5', '6', '7', '8']
        if player.color == 'w':
            ranks.sort(reverse=True)
        if player.color == 'b':
            rows.sort(reverse=True)
        print('\n   ', end = '')
        for row in rows:
            print(f'  {row}  ', end='')
        print()
        for i in range(8):
            print('  ', end='')
            spaces = ' ----'
            print(spaces * 8, end='')
            print()
            print(ranks[i], end=' ')
            for j in range (8):
                self.draw_square(j, i, rows, ranks)
            print(f'| {ranks[i]}')
        print('  ', end='')
        print(spaces * 8)
        print('  ', end = '')
        for row in rows:
            print(f'  {row}  ', end='')
        
    def draw_square(self, row, rank, rows, ranks):
        self.row = rows[row]
        self.rank = ranks[rank]
        self.pos = self.row + self.rank
        squares_taken = self.find_squares_taken()
        if self.pos in squares_taken:
            print(f'| {squares_taken[self.pos]} ', end= '')
        else:
            #For testing, this shows all square names
            #print(f'| {self.pos} ', end='')
            print('|    ', end='')
    
    def find_squares_taken(self):
        squares_taken = {}
        for piece in self.all_pieces:
            if piece.pos != '':
                squares_taken[piece.pos] = piece
        return squares_taken

    def pieces_taken(self, color):
        off_board_pieces_white = []
        off_board_pieces_black = []
        white_taken_value = 0
        black_taken_value = 0
        for piece in self.all_pieces:
            if piece.onBoard == False:
                if piece.color == 'w':
                    off_board_pieces_white.append(piece)
                    white_taken_value += piece.value
                if piece.color == 'b':
                    off_board_pieces_black.append(piece)
                    black_taken_value += piece.value
        if color == 'w':
            return off_board_pieces_white, white_taken_value
        if color == 'b':
            return off_board_pieces_black, black_taken_value

    def check_checker(self, player):
        squares_taken = self.find_squares_taken()
        checked = 0
        if player.color == 'w':
            white_king_on = self.wk.pos
            for piece in self.black_pieces:
                piece.move_piece(squares_taken)
                attacking_king = f'{piece.name[1]}{piece.pos}x{white_king_on}'
                if attacking_king in piece.moves:
                    checked += 1
          
        if player.color == 'b':
            black_king_on = self.bk.pos
            for piece in self.white_pieces:
                piece.move_piece(squares_taken)
                attacking_king = f'{piece.name[1]}{piece.pos}x{black_king_on}'
                if attacking_king in piece.moves:
                    checked += 1
     
        if checked > 0:
            player.checked = True   
        else:
            player.checked = False

class Player():
    def __init__(self, c):
        self.color = c
        self.turn = False
        self.checked = False

# game loop
class Game():
    def __init__(self):  
        self.white_player = Player('w')
        self.black_player = Player('b')
    
    def game_loop(self):
        board = Board(self.white_player, self.black_player)
        turn_number = 1.0
        check_mate = False
        running = True
        while check_mate == False and running == True:
            piece_moved = False
            
            #show pieces taken up top
            white_pieces_taken = board.pieces_taken('w')
            black_pieces_taken = board.pieces_taken('b')
            white_score = white_pieces_taken[1]
            white_pieces_taken = white_pieces_taken[0]
            black_score = black_pieces_taken[1]
            black_pieces_taken = black_pieces_taken[0]
            if white_pieces_taken != []:
                print(f'White has taken these pieces: {white_pieces_taken}. White\'s score is {white_score}')
            if black_pieces_taken != []:
                print(f'Black has taken these pieces: {black_pieces_taken}. Black\'s score is {black_score}')
            if int(white_score) > int(black_score):
                print(f'White is ahead by {white_score - black_score}.')
            elif int(white_score) < int(black_score):
                print(f'Black is ahead by {black_score - white_score}.')
            
            # draw new board (if turn number is .5, its blacks move so flip the board)
            if turn_number % 1 == 0:
                self.white_player.turn = True
                self.black_player.turn = False
                whose_move = 'white'
                player_turn = 'w'
                player_turn_ref = self.white_player

                
            else:
                self.white_player.turn = True
                self.black_player.turn = False
                whose_move = 'black'
                player_turn = 'b'
                player_turn_ref = self.black_player

            board.draw_board(player_turn_ref)
            board.check_checker(player_turn_ref)

            print(f'\n\nMove number: {int(turn_number)}')
            print(f'It is {whose_move}\'s turn. Type the square of a piece to move it or press q to quit:')
            
            while piece_moved == False:
                if player_turn_ref.checked == True:
                    print('You are in check. You must block the check or move your king.')
                this_piece_location = input('Type the location of the piece you want to move: ')

                # take user input and show the piece of that location
                squares_taken = board.find_squares_taken()
                if this_piece_location in squares_taken:
                    piece = squares_taken.get(this_piece_location)
                    possible_moves = piece.move_piece(squares_taken)

                    piece_moved_complete = False
                    while piece_moved_complete == False:
                        if piece.color != player_turn:
                            print('That is not your piece. Please select one of your own pieces.\n')
                            break
                        elif possible_moves != []:
                            print(f'Possible moves are: {possible_moves}')
                        else:
                            print(f'Your {piece.capital_name} has no moves. Try another piece. \n')
                            piece_moved_complete = True
                            break
                        move_piece_to = input(f'Where would you like to move this {piece.capital_name}? Or enter \'c\' to change pieces: ')
                        if move_piece_to == 'q':
                            print('Thanks for playing!')
                            piece_moved_complete = True
                            piece_moved = True
                            running = False
                            break
                        if move_piece_to == 'c':
                            print()
                            piece_moved_complete = True
                            break

                        if 'x' in move_piece_to:
                            attacked_piece = squares_taken.get(move_piece_to[4:])
                            # if player is in check, take current positions of pieces
                            if player_turn_ref.checked == True:
                                taken_piece_old_pos = attacked_piece.pos
                                piece_old_pos = piece.pos

                            attacked_piece.onBoard = False
                            attacked_piece.pos = 'a9'
                            piece.pos = move_piece_to[4:]
                            

                            if player_turn_ref.checked == True:
                                board.check_checker(player_turn_ref)
                                if player_turn_ref.checked == True:
                                    print('That move does not get you out of check.')
                                    attacked_piece.onBoard = False
                                    attacked_piece.pos = taken_piece_old_pos
                                    piece.pos = piece_old_pos
                                    break

                            piece_moved_complete = True
                            piece_moved = True
                        elif move_piece_to in possible_moves:
                            # if player is in check, make sure the move gets them out of check
                            if player_turn_ref.checked == True:
                                piece_old_pos = piece.pos
                                piece.pos = move_piece_to
                                print('this player in check')
                                board.check_checker(player_turn_ref)
                                if player_turn_ref.checked == True:
                                    print('That move does not get you out of check.')
                                    piece.pos = piece_old_pos
                                    break
                            # if not in check, move the piece
                            else:
                                piece.pos = move_piece_to
                            
                            piece_moved = True
                            piece_moved_complete = True
                        
                        else:
                            print('That is not a legal move. Try another move.\n')
                        
                else:
                    if this_piece_location == 'q':
                        piece_moved = True
                        running = False
                        break
                    print('You do not have a piece on that square. Please choose a square with one of your pieces on it.\n')

            if this_piece_location == 'q':
                print('Thanks for playing')
                break

            #count turns
            if piece_moved == True and piece_moved_complete == True:
                turn_number += .5

            # save move order as move log

game = Game()
game.game_loop()