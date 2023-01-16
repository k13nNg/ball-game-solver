class Game:
    tube_size = 0
    max_colors = 0
    tubes_lst = []

    def __init__(self, tube_size, lst_of_tubes, mc=0):
        self.tubes_lst = lst_of_tubes
        self.max_colors = mc
        if(mc==0):
            self.max_colors = len(lst_of_tubes)
        self.tube_size = tube_size


class Ball:
    color = ""
    y_pos = 0

    def __init__(self, c, yp):
        self.color=c
        self.y_pos=yp