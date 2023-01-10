from views import Game
from copy import deepcopy, copy
import sys

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
        if not(len(i) == game.tube_size and len(list(filter(lambda a: a != i[0], i))) == 0):
            new_tubes_lst.append(i)
            merged+=i

    
    for i in merged:
        if i not in temp:
            temp.append(i)

    new_max_colors = len(temp)

    return Game(game.tube_size, new_tubes_lst, new_max_colors)

def is_finished(game):
    '''
    Returns 'true' if a game is finished, 'false' otherwise

    A game is finished if all its tubes are empty, or each tube is full with all balls of the same colour
    '''

    # check if a game has no tubes, or has all of its tube empty
    empty_tubes_cond = len(list(filter(lambda k: len(k) != 0, game.tubes_lst))) == 0

    # check if there remains no uncomplete tubes after removing all completed tubes
    remain_tubes = remove_completed(game).tubes_lst

    remain_tubes = list(filter(lambda k: len(k) != 0, remain_tubes))

    remove_completed_cond = len(remain_tubes) == 0


    return (empty_tubes_cond or remove_completed_cond)

def num_blocks(tubes_lst):
    '''
    Returns the number of "blocks" contained in tubes_lst

    A block is a consecutive sequence of identical colors within one list. A single color is a block itself
    '''

    blocks_num = 0

    def count_block_lst(tube, counter, curr_color):

        '''
        Return the block count inside a list
        '''

        if(len(tube) == 0):
            return counter

        else:
            temp = tube.pop(0)

            if(temp == curr_color):
                return count_block_lst(tube, counter, curr_color)

            else:
                return count_block_lst(tube, counter+1, temp)

    for i in tubes_lst:
        blocks_num += count_block_lst(i, 0, '')


    return blocks_num

def are_equiv_games(game1, game2):
    '''
    Return 'true' if game1 and game2 are equivalent, false otherwise

    Two games are equivalent if they have:
        -> the same 'max_colors' value;
        -> the same 'tube_size' value;
        -> the same number of tubes; and
        -> the tubes contain identical balls in identical order within the tube

    '''
    flag = True

    for i in game1.tubes_lst:
        flag = flag and (i in game2.tubes_lst)   
    
    return (game1.max_colors == game2.max_colors) and (game1.tube_size == game2.tube_size) and flag

def next_games(game):
    '''
    Return a list of next possible games resulted from moving 1 ball in 'game.tubes_lst'
    '''

    tubes_lst = copy(game.tubes_lst)
    adjusted_new_tubes_lst = []
    final_set=[]

    def remove_curr_tube(tube_index):
        '''
        Return a tubes_lst with tubes_lst[tube_index] removed
        '''

        temp = copy(tubes_lst)
        del temp[tube_index]

        return temp

    def add_ball_everywhere(ball, tubes_lst):
        '''
        Return a list of possible tubes_lst resulted from moving 1 ball in tubes_lst
        '''

        possible_moves = []

        for j in range(len(tubes_lst)):
            temp_arr=deepcopy(tubes_lst)

            if len(temp_arr[j]) == game.tube_size:
                pass
            else:
                temp_arr[j].insert(0, ball)
                possible_moves.append(temp_arr)
        
        return possible_moves
                

    # loop throught the game's tubes_lst
    for i in range(len(tubes_lst)):
        # if the loop is empty, ignore it
        if len(tubes_lst[i]) == 0:
            pass
        else:
            # temporary variables (lists in python are weird, the list does not reset after the function is done)
            temp_holder = copy(tubes_lst[i])
            temp_holder.pop(0)
            temp_arr = remove_curr_tube(i)
            top_ball = tubes_lst[i][0]
           
            # creat a temporary list to hold all possible tubes_lst
            added_ball_arr = add_ball_everywhere(top_ball, temp_arr)

            # add in the removed list
            for k in added_ball_arr:
                k.insert(i, temp_holder)

            # add together all possible tubes_lst
            adjusted_new_tubes_lst += added_ball_arr

    # Make a list of possible games
    for i in adjusted_new_tubes_lst:
        final_set.append(Game(game.tube_size, i, game.max_colors))

    return final_set

def solve(game):

    '''
    If the game is solvable, return True. Return False otherwise
    '''

    def solve_helper(to_visit, visited):
        temp = deepcopy(to_visit)

        if visited == None:
            visited = []

        if(len(temp) == 0):
            print("Game is unsolvable")
            return False

        else:
            if(is_finished(temp[0])):
                return True
            
            elif (temp[0] in visited):
                temp.pop(0)
                return solve_helper(temp, visited)

            else:
                nbrs = next_games(temp[0])

                new_to_visit = list(filter(lambda x: not(x in visited), nbrs))
                new_visited = deepcopy(visited)

                new_visited.insert(0, temp.pop(0))
                new_to_visit.append(temp) 

                
                return solve_helper(new_to_visit, new_visited)

    return solve_helper([game], None)



            



    
    

    
# valid
test_game_1 = Game(2,[['blue', 'red'], ['blue', 'red'], []], 0)

test_game_2 = Game(2,[['white', 'white'], \
                      [], \
                      ['yellow', 'yellow']], 0)

test_game_5 = Game(2, [['green', 'green'], ['red', 'blue']], 0)

test_game_6 = Game(2, [['red', 'red'], \
                        ['blue', 'blue']], 0)

test_game_7 = Game(5, [[], \
                    ['red', 'red'], \
                    ['blue', 'red', 'red', 'blue'], \
                    ['red', 'blue', 'blue']], 0)

test_game_8 = Game(2, [['blue', 'blue'], ['red', 'red'], []], 0)
# invalid

test_game_3 = Game(4, [['green']], 0)

test_game_4 = Game(3, [['brown', 'blue'], ['red', 'red']], 0)

test_game_a = Game(2,[['red'], ['blue', 'red'], ['blue']], 0)


temp = solve(test_game_1)
print(temp.tubes_lst)

# temp_1 = next_games(test_game_1)
# temp_2 = next_games(temp_1[0])
# temp_3 = next_games(temp_2[2])
# temp_4 = next_games(temp_3[0])
# for i in temp_1:
#     print("temp_1: ", i.tubes_lst)
# print()
# for i in temp_2:
#     print("temp_2: ", i.tubes_lst)
# print()
# for i in temp_3:
#     print("temp_3: ", i.tubes_lst)
# print()
# print(is_finished(temp_3[0]))

# temp = solve(temp_1[0])
# print(temp)

# print(is_finished(test_game_8))






