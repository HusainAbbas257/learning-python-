import random
class tictactoe:
    def __init__(self):
        self.row1 = [' ', ' ', ' ']
        self.row2 = [' ', ' ', ' ']
        self.row3 = [' ', ' ', ' ']
        self.board = [self.row1, self.row2, self.row3]
        self.player = 'o'
        self.bot = 'x'

    def display(self):
        print()
        for r in self.board:
            print(r)
        print()
    
    def isfull(self):
        l = list(filter(self.isvalid, ['a1','a2','a3','b1','b2','b3','c1','c2','c3']))
        return l == []
    
    def change(self, loc: str, move: str):
        if self.isvalid(loc):
            match(loc):
                case 'a1': self.row1[0] = move
                case 'a2': self.row1[1] = move
                case 'a3': self.row1[2] = move
                case 'b1': self.row2[0] = move
                case 'b2': self.row2[1] = move
                case 'b3': self.row2[2] = move
                case 'c1': self.row3[0] = move
                case 'c2': self.row3[1] = move
                case 'c3': self.row3[2] = move
                case _: print('error in change()')
    
    def isvalid(self, move):
        match(move):
            case 'a1': return self.row1[0] == ' '
            case 'a2': return self.row1[1] == ' '
            case 'a3': return self.row1[2] == ' '
            case 'b1': return self.row2[0] == ' '
            case 'b2': return self.row2[1] == ' '
            case 'b3': return self.row2[2] == ' '
            case 'c1': return self.row3[0] == ' '
            case 'c2': return self.row3[1] == ' '
            case 'c3': return self.row3[2] == ' '
            case _: return False

    def can_winin1(self, who) -> tuple[str, bool]:
        for i in range(3):
            row = self.board[i]
            # Check rows
            if (row[0] == row[1] == who and row[2] == ' '):
                movetowin = ['a','b','c'][i] + '3'
                return (movetowin, True)
            if (row[1] == row[2] == who and row[0] == ' '):
                movetowin = ['a','b','c'][i] + '1'
                return (movetowin, True)
            if (row[0] == row[2] == who and row[1] == ' '):
                movetowin = ['a','b','c'][i] + '2'
                return (movetowin, True)

            # Check columns
            if (self.board[0][i] == self.board[1][i] == who and self.board[2][i] == ' '):
                movetowin = ['a','b','c'][2] + str(i+1)
                return (movetowin, True)
            if (self.board[1][i] == self.board[2][i] == who and self.board[0][i] == ' '):
                movetowin = ['a','b','c'][0] + str(i+1)
                return (movetowin, True)
            if (self.board[0][i] == self.board[2][i] == who and self.board[1][i] == ' '):
                movetowin = ['a','b','c'][1] + str(i+1)
                return (movetowin, True)

        # Diagonals
        if (self.board[0][0] == self.board[1][1] == who and self.board[2][2] == ' '):
            return ('c3', True)
        if (self.board[1][1] == self.board[2][2] == who and self.board[0][0] == ' '):
            return ('a1', True)
        if (self.board[0][0] == self.board[2][2] == who and self.board[1][1] == ' '):
            return ('b2', True)
        
        if (self.board[0][2] == self.board[1][1] == who and self.board[2][0] == ' '):
            return ('c1', True)
        if (self.board[1][1] == self.board[2][0] == who and self.board[0][2] == ' '):
            return ('a3', True)
        if (self.board[0][2] == self.board[2][0] == who and self.board[1][1] == ' '):
            return ('b2', True)

        return ('', False)

    def xcan_winin1(self, who, bd) -> tuple[str, bool]:
        for i in range(3):
            row = bd[i]
            if (row[0] == row[1] == who and row[2] == ' '):
                movetowin = ['a','b','c'][i] + '3'
                return (movetowin, True)
            if (row[1] == row[2] == who and row[0] == ' '):
                movetowin = ['a','b','c'][i] + '1'
                return (movetowin, True)
            if (row[0] == row[2] == who and row[1] == ' '):
                movetowin = ['a','b','c'][i] + '2'
                return (movetowin, True)

            # Check columns
            if (bd[0][i] == bd[1][i] == who and bd[2][i] == ' '):
                movetowin = ['a','b','c'][2] + str(i+1)
                return (movetowin, True)
            if (bd[1][i] == bd[2][i] == who and bd[0][i] == ' '):
                movetowin = ['a','b','c'][0] + str(i+1)
                return (movetowin, True)
            if (bd[0][i] == bd[2][i] == who and bd[1][i] == ' '):
                movetowin = ['a','b','c'][1] + str(i+1)
                return (movetowin, True)

        # Diagonals
        if (bd[0][0] == bd[1][1] == who and bd[2][2] == ' '):
            return ('c3', True)
        if (bd[1][1] == bd[2][2] == who and bd[0][0] == ' '):
            return ('a1', True)
        if (bd[0][0] == bd[2][2] == who and bd[1][1] == ' '):
            return ('b2', True)
        
        if (bd[0][2] == bd[1][1] == who and bd[2][0] == ' '):
            return ('c1', True)
        if (bd[1][1] == bd[2][0] == who and bd[0][2] == ' '):
            return ('a3', True)
        if (bd[0][2] == bd[2][0] == who and bd[1][1] == ' '):
            return ('b2', True)

        return ('', False)
    
    def can_winin2(self, who) -> tuple[str, str, bool]:
        for i in range(3):
            for j in range(3):
                move = 'a' if i == 0 else 'b' if i == 1 else 'c'
                move += f'{j+1}'
                if self.isvalid(move):
                    copy = [row[:] for row in self.board]
                    copy[i][j] = self.bot
                    tmp = self.xcan_winin1(who, copy)
                    if tmp[1]:
                        return (move, tmp[0], True)
        return ('', '', False)

    def bot_play(self):
        player_win = self.can_winin1(self.player)
        bot_win = self.can_winin1(self.bot)
        bot_win2 = self.can_winin2(self.bot)
        
        if player_win[1]:
            self.change(player_win[0], self.bot)
            print('bot playing to block player at', player_win[0])
        elif bot_win[1]:
            self.change(bot_win[0], self.bot)
            print('bot playing to win at', bot_win[0])
        elif bot_win2[2]:
            if self.isvalid(bot_win2[0]):
                self.change(bot_win2[0], self.bot)
                print('bot playing (can win in 2) at', bot_win2[0])
            elif self.isvalid(bot_win2[1]):
                self.change(bot_win2[1], self.bot)
                print('bot playing (can win in 2) at', bot_win2[1])
        else:
            l = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
            nl = list(filter(self.isvalid, l))
            if nl:
                self.change(nl[random.randint(0, len(nl)-1)], self.bot)
                print('bot playing randomly')
            else:
                print('No moves left for bot!')

    def won(self) -> str:
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
        for i in range(3):
            if self.row1[i] == self.row2[i] == self.row3[i] != ' ':
                return self.row1[i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != ' ':
            return self.board[2][0]
        return 'l'


def main():
    while True:
        ttt = tictactoe()

        # Ask who starts first
        first = input("Do you want to play first? (y/n): ").strip().lower()
        if first == 'y':
            player_turn = True
        else:
            player_turn = False

        ttt.display()

        while True:
            if player_turn:
                move = input("Your move (e.g. a1, b2): ").strip().lower()
                if not ttt.isvalid(move):
                    print("Invalid move, try again.")
                    continue
                ttt.change(move, ttt.player)
                ttt.display()
                if ttt.won() == ttt.player:
                    print("You won! 🔥")
                    break
                if ttt.isfull():
                    print("Game draw!")
                    break
                player_turn = False
            else:
                ttt.bot_play()
                ttt.display()
                if ttt.won() == ttt.bot:
                    print("Bot won! 😵‍💫")
                    break
                if ttt.isfull():
                    print("Game draw!")
                    break
                player_turn = True

        # Ask for replay
        replay = input("Play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing! Peace dude ✌️")
            break

if __name__ == "__main__":
    main()
