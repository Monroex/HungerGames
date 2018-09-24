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
    # Returns a list of 2-tuples with all positions on a n by m grid.
    # 
    # Side effects: None
    
    # TODO: Change this.
    return [(0,0), (0,1), (0,2), (0,3), (0,4)]

def bang(delay):
    # Argument(s):
    #   delay - paus (ms) between each image of the animation
    #           (default = 85).
    #
    # Side effects: 
    #   Shows a simple but attractive animation on the display.

    # TODO: Change this
    display.show(Image.HEART)
    sleep(delay)
    display.clear()
    
def random_positions(n):
    # Creates a set with n random points (x, y).
    #
    # Argument(s):
    #  n (integer) - Number of point to create.
    # 
    # Return value: A set with n random points (x, y).
    #
    # 
    # Side effects: None
    
    return positions() # TODO: Change this.

def show(food):
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
    
    display.show(Image.HAPPY)
    
def eat(hero, food):
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
       pass # TODO: Change this to remove the hero position from the set food.

    return food
        
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
       x = x # TODO: Change this.
    elif direction == "down":
       y = y # TODO: Change this.

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
    (x, y) = hero

    # TODO: Add code here.

######################
# Abstraction level 1
######################

def bangs(n, delay):
    # Arguments:
    #   n - number of times to repeat the animation.
    #   delay - paus (ms) betwwen each image of the animation (default = 85).
    #
    # Side effects: Shows the bang() animation on the display.

    bang(500) # TODO: Change this.
 
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

    # Take out an arbitrary element from the set s
    # and use for the hero.
    hero = s.pop()
    
    # Now s only have n elements, i.e., n positions for the food.

    return (hero, s)

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
   
    (hero, food) = spawn_hero_and_food(n)

    # Show animation.
    bangs(3, 85)

    # Light up all food positions on the display.
    show(food)

    return (hero, food)

######################
# Abstraction level 3
######################

# The simplest valid game state.

hero = (2, 2)       # None random position for the hero (tuple).
food = set()        # No food (empty set).
direction = "none"  # Direction of movement (none, right, down).

# Event loop.

while False:  # TODO: Chante False to TRUE to enable the event loop.
    
    # If no food left, spawn new food and a random position for the hero.
    if empty(food):
        (hero, food) = spawn(5)

    # Make the position of the hero flash.
    flash(hero, 85)
    
    # Update the hero position on button presses.
    
    if button_a.was_pressed():
        direction = "right"
    elif button_b.was_pressed():
        direction = "down"
        
    if direction != "none":
        hero = move(hero, direction)
        direction = "none"  

    # If the hero steps on food, eat.
    food = eat(hero, food)