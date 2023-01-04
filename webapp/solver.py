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

def remove_completed(game):
    new_tubes_lst = []
    merged = []
    temp = []
    new_max_colors = 0

    for i in game.tubes_lst:
        merged += i
        if not(len(i) == game.tube_size and len(list(filter(lambda a: a != i[0], i))) == 0):
            new_tubes_lst.append(i)
    
    for i in merged:
        if i not in temp:
            temp.append(i)

    new_max_colors = len(temp)

    return Game(game.tube_size, new_tubes_lst, new_max_colors)




    
# valid
test_game_1 = Game(5,[['red', 'red'], \
                    ['blue'], \
                    ['blue', 'red', 'red', 'blue'], \
                    ['red', 'blue', 'blue']], 0)

test_game_2 = Game(2,[['white', 'green'], \
                      [], \
                      ['white', 'green']], 0)

test_game_5 = Game(2, [['green', 'green'], ['red', 'blue']], 0)

# invalid

test_game_3 = Game(4, [['green']], 0)

test_game_4 = Game(3, [['brown', 'blue'], ['red', 'red']], 0)













