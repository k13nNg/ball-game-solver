from views import Game

def check_color(tube_size, num, lst_of_colors):
    '''
     -> Returns true if each symbol in the list apears exactly 'tube_size' times and if there are at most 'num' different symbols
     -> Returns false otherwise
    '''

    if (len(lst_of_colors) == 0):
        return True

    if (num == 0):
        return False
    
    return (tube_size == len(list(filter(lambda k: k==lst_of_colors[0], lst_of_colors)))) and \
        check_color (tube_size, num-1, list(filter(lambda m: m!= lst_of_colors[0], lst_of_colors))) 


def valid_game(game):
    '''
        Returns true if a game is valid, false otherwise

        -> A game is valid if the following conditions hold:
            * all tubes have at most tube_size symbols in them;
            * there are at most max_colours different symbols; and
            * there are exactly tube_size occurence of each different symbol
    '''

    merged = []
    temp = []        

    for i in game.tubes_lst:
        temp.append(len(i))
        merged += i

    flag = (len(list(filter(lambda a: a > game.tube_size, temp))) == 0)
    
    return flag and (len(merged) == 0 or (len(merged) <= (game.tube_size * game.max_colors) and (check_color(game.tube_size, game.max_colors, merged))))
    

test_game = Game([  ['red', 'red'], \
                    ['blue'], \
                    ['blue', 'red', 'red', 'blue'], \
                    ['red', 'blue', 'blue']])






