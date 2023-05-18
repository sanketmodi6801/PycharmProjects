print('For Player1 : ')
player1 = input(' Select 1 for : Rock\n Select 2 for : Paper\n Select 3 for : Scissors \n')
print('For Player2 : ')
player2 = input(' Select 1 for : Rock\n Select 2 for : Paper\n Select 3 for : Scissors \n')


def game(p1, p2):
    if p1 == '1' and p2 == '3' or p1 == '2' and p2 == '1' or p1 == '3' and p2 == '2':
        print('player1 wins')

    if p1 == '3' and p2 == '1' or p1 == '1' and p2 == '2' or p1 == '2' and p2 == '3':
        print('player2 wins')

    if p1 == p2:
        print('Draw...!! between both')
    else:
        print('Enter a valid number....!! ')


game(player1, player2)
