from microbit import *
from random import randint

# 1D051 (2018) - Programming assignment 1

# Author: Karl Marklund <karl.marklund@it.uu.se> september 2018.

######################
# Abstraction level 0
######################


def empty(s):
    # Argument(s):
    #   s (set)
    #
    # Return value: True if the set s is empty and otherwise False.
    # 
    # Side effects: None

    return len(s) == 0
    
def take(xs, n):
    # Arguments:
    #   xs :: list
    #   n  :: integer
    # 
    # Return value:
    #   n >= 0 ==> returns a list with the n first element of xs.
    #   n <  0 ==> returns a list with the n last elements of xs.
    # 
    # Side effects: None
  
    if n >= 0:
        return xs[:n]
    else:
        return xs[-1:(n-1):-1]
        #return xs[(n*-1):]
        

def shuffle(xs):
    # Arguments:
    #   xs :: list
    #
    # Return value:
    #   A copy of xs with the elements of xs randomly shuffled.
    # 
    # Side effects:
    #   None - the original list xs is unchanged. 
    #
    
    tmp = [((randint(1,9999), x)) for x in xs] 
    tmp.sort()
    return [x for (_, x) in tmp]

def positions():
    # Returns a list of 2-tuples with all positions on a 5x5 grid.
    # Side effects: None
    poslist = []    
    for x in range(5):
        for y in range(5):
          poslist.append((x, y))  
            
    return poslist

def bang(n):
    display.clear()
    display.set_pixel(2,2,9)
    sleep(n)
    display.clear()
    display.show(Image.DIAMOND_SMALL)
    sleep(n)
    display.clear()
    display.show(Image.DIAMOND)
    sleep(n)
    display.clear()
    sleep(n)
    
def boom():
    display.clear()
    display.show(Image.SKULL)
    sleep(2000)
    display.clear()

    
    
def random_positions(n):
    # Creates a set with n random points (x, y) on a 5x5 grid.
    #
    # Argument(s):
    #  n (integer) - Number of point to create.
    # 
    # Return value: A set with n random points (x, y).
    #
    # 
    # Side effects: None4
    randomlist = []
    poslist = shuffle(positions())
    for x in range(n):
        randomlist.append(poslist[x])
    
    return randomlist
def show(food, bomblist):
    # Display the food on the map.
    #
    # Argument(s):
    #   food (set) - A set with positioins (x, y) on the map where
    #                there is food available.
    #
    # Return value: None.
    #
    # Side effects:
    #   Lights up all the positions on the display where there is
    #   food available.
    
    # TODO: Change this
    for elem in bomblist:
        display.set_pixel(elem[0], elem[1], 4)
    for elem in food:
        display.set_pixel(elem[0], elem[1], 9)
        
    
def eat(hero, food, bomblist):
    # If the hero is on a position on the map where there also is food, 
    # eat the food.
    #
    # Argument(s):
    #   hero (tuple) - The position (x, y) of the hero on the map.
    #   food (set)   - A set with positions (x, y) where there is food on the
    #                  map.
    #
    # Return value: The updated set of food on the map.
    #
    # Side effects: May update the set food.

    if hero in food:
       food.remove(hero)

    if hero in bomblist:
        boom()
        food = []
        bomblist = []
    
    
    return (food, bomblist)
        
def move(hero, direction):
    # Updates the hero position on button presses.
    # 
    # Argument(s):
    #   hero (tuple) - The current position (x, y) of the hero.
    #   direction (string) - The direction ("right" or "down") the hero
    #
    #
    # Return value: A tuple (x, y) with the updated position of the
    #               hero.
    #
    # Side effects: None

    # Tuple matching to get the x-value and y-value of the hero position.
    (x, y) = hero

    if direction == "right":
       x = (x+1)%5
    elif direction == "down":
       y = (y+1)%5

    return (x, y)
    
def flash(hero, delay):
    # Arguments:
    #   hero (tuple)    - Position (x, y) of the hero.
    #   delay (integer) - Duration (ms) of light on and off (default = 100).
    #
    # Return value: None.
    #
    # Side effects:
    #   Make the hero position flash once on the display.

    # Tuple matching to get the x-value and y-value of the hero position.
    #(x, y) = hero

    display.set_pixel(hero[0], hero[1], 9)
    sleep(delay)
    display.set_pixel(hero[0], hero[1], 0)
    sleep(delay)
    
    
######################
# Abstraction level 1
######################

def bangs(n, delay):
    # Arguments:
    #   n - number of times to repeat the animation.
    #   delay - paus (ms) betwwen each image of the animation (default = 85).
    #
    # Side effects: Shows the bang() animation on the display.

    for y in range(n):
        bang(delay)

 
def spawn_hero_and_food(n):
    # Argument(s):
    #   n - (integer) mount of food to generate.
    #
    # Return value: A tuple (hero, food).
    #   hero (tuple) - A random position (x, y) for the hero.
    #   food (set)   - A set with n random positions (x, y) for the food.
    #
    # Side effects: None
    
    # First we generate n + 1 random positions:
    # n for the food and one for the hero all in set s.
    s = random_positions(n+1)
    
    for x in range(2):
        bomblist.append(s.pop())
    # Take out an arbitrary element from the set s
    # and use for the hero.
    hero = s.pop()
    
    # Now s only have n elements, i.e., n positions for the food.

    return (hero, s, bomblist)

#######################
# Abstraction level 2
#######################

def spawn(n):
    # Argument(s):
    #   n (integer) - Amount of food to generate.
    #
    # Return value: A tuple (hero, food).
    #   hero (tuple) - A random position (x, y) for the hero.
    #   food (set)   - A set with n random positions (x, y) for the food.
    #
    # Side effects:
    #   Show an animation on the display.
   
    (hero, food, bomblist) = spawn_hero_and_food(n)

    # Show animation.
    bangs(3, 85)

    show(food, bomblist)
    # Light up all food positions on the display.

    return (hero, food, bomblist)

######################
# Abstraction level 3
######################

# The simplest valid game state.

food = set()        # No food (empty set).
hero = (2, 2)       # None random position for the hero (tuple).
direction = "none"  # Direction of movement (none, right, down).
bomblist = []

# Event loop.

while True:  # TODO: Chante False to TRUE to enable the event loop.
    
    # If no food left, spawn new food and a random position for the hero.
    if empty(food):
        (hero, food, bomblist) = spawn(7)

    # Make the position of the hero flash.
    flash(hero, 40)
    
    # Update the hero position on button presses.
    
    if button_a.was_pressed():
        direction = "right"
    elif button_b.was_pressed():
        direction = "down"
        
    if direction != "none":
        hero = move(hero, direction)
        direction = "none"  

    # If the hero steps on food, eat.
    food = eat(hero, food, bomblist)[0]
    bomblist = eat(hero, food, bomblist)[1]
    
    
    #R8 There should spawn two bombs along with the food, with brightness 3. If eaten the game is over.
    #R9 The hero should move automatically at all times. You can change the direction to "Right" or "Down" with the buttons. 