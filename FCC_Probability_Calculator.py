import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):

    self.contents = []

    # Build flattened list from Dict
    for color,count in kwargs.items():
      for item in range(count):
        self.contents.append(color)

  def draw(self, ball_count):
    # If more balls are drawn than what we have - send all back and empty our list
    if ball_count > len(self.contents):
      contents_copy = self.contents.copy()
      self.contents.clear()
      return contents_copy

    # Prepare list of random balls ro return
    balls_removed = []
    
    for ball in range( ball_count ):
  
      rand_idx = random.randint( 0, len(self.contents) - 1 )

      removed = self.contents.pop(rand_idx)
      balls_removed.append(removed)


    return balls_removed
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  times_got_expected_balls = 0
  
  for n in range(0, num_experiments):

    found_all_balls = 1
    
    hat_copy = copy.deepcopy(hat)

    drawn_balls = hat_copy.draw(num_balls_drawn)
  
    # Turn drawn balls into dict
    drawn_balls_dict = {}
    
    for b in drawn_balls:
      
      if b in drawn_balls_dict.keys():
        drawn_balls_dict[b] += 1
      else:
        drawn_balls_dict[b] = 1
    
    # Verify if balls expected are in this draw
    for color, count in expected_balls.items():
      if color not in drawn_balls_dict.keys() :
        found_all_balls = 0
        break
      if drawn_balls_dict[color] < count:
        found_all_balls = 0
        break

    if found_all_balls == 1:
      times_got_expected_balls += 1
  
  probability = times_got_expected_balls / num_experiments

  return probability
