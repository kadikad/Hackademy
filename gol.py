import random 


def setup_game(size,max_alive):
    a_grid = get_empty_grid(size)
    fill_grid_random(a_grid, max_alive)


def get_empty_grid(size):
    new_grid=[]
    for row in range(size):
        new_sublist=[]
        for column in range(size):
            new_sublist.append('-')
        new_grid.append(new_sublist)
    return new_sublist


def rand_alive():     #random generator of numbers 
    number=random.randint(1,3)
    if number == 1:
        return True
    else:
        return False

def fill_grid_random(a_grid,max_alive):
    size=len(a_grid)
    remaining = max_alive
    for r_i in range(size):
        for c_i in range(size):
            if remaining > 0 and (rand_alive()==True):
                if rand_alive() == True:
                    a_grid[r_i][c_i] = 'X'
            else:
            a_grid[r_i][c_i] = '-' 


    for row in a_grid:
        for element in row:
            if rand_alive() == True
                element = 'x'
            else:
                element = '-'



#[['-','-','-'],
#['-','-','-'],
#['-','-','-']]

# prints the following on screen:
# ---
# -X-
# ---

def print_grid(a_grid):
    size = len(grid)
    for r_i in range(size):
        for c_i in range(size):
            print(a_grid[r_i][c_i],end="")
        print("")


