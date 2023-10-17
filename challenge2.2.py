# Define the base class player

class player :
  def play (self):
    print("The player is playing cricket.")

# Define the derived class Batman

class Batsman (player):
  def play(self):
    print("The Batsman is Batting.")

# Define the deriver class Bowler

class Bowler (player):
  def play(self):
    print("The Bowler is Bowling.")

# create objects of Batsman and Bowler classes

batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play() 