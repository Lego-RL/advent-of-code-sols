from xmlrpc.client import FastMarshaller


with open('input.txt', 'r') as f:
    data = f.readlines()

data = [x.strip('\n') for x in data if x != '\n']

rolls, unparsed_boards = data[0], data[1:]


class Board():

    #board is 2d list of each row of board
    def __init__(self, board: list):
        self.board = board
        self.hits = [[0, 0, 0, 0, 0], [0, 0, 0, 0 ,0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


    def notify_roll(self, roll: int) -> None:
        '''
        Update hits list in the case that
        the roll is a number on this board.
        '''

        for i in range(5):
            for j in range(5):
                if self.board[i][j] == roll:
                    self.hits[i][j] = 1
                    return


    
    def check_for_win(self) -> bool:
        '''
        Returns True if this is a winning
        board, false otherwise.
        '''

        #check rows
        for row in self.hits:
            if sum(row) == 5:
                return True

        #check columns
        for i in range(5):
            for j in range(5):
                if self.hits[j][i] == 0:
                    break

                elif j == 4:
                    return True

        return False



    def get_sum_of_misses(self) -> int:
        '''
        Return sum of all the numbers
        on this board that weren't called.
        
        This function running implies that
        this board was a winner.
        '''

        sum = 0

        for i in range(5):
            for j in range(5):
                if self.hits[i][j] == 0:
                    sum += int(self.board[i][j])


        return sum




def construct_boards(boards: list) -> list:
    '''
    Take list of individual strings and
    return full board representations
    in the form of a 2d list.
    '''
    board_objs = []


    for i in range(0, len(boards), 5):
        board = []

        for j in range(i, i+5):
            row = boards[j].split(' ')
            for count, element in enumerate(row):
                if element == '':
                    del row[count]

                else:
                    row[count] = element.strip()

            board.append(row)
    
        board_objs.append(Board(board))

    return board_objs



rolls = rolls.split(',')
boards = construct_boards(unparsed_boards)


count = 0
for roll in rolls:

    for board in boards:
        board.notify_roll(roll)


    if count >= 5:
        for count, board in enumerate(boards):
            if board.check_for_win():
                print(board.get_sum_of_misses() * int(roll))
                exit(0)

    count += 1


