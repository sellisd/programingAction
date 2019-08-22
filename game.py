#!/usr/bin/env/python

class game():
  def __init__(self, players, actions, targets):
    self.id = 1
    self.time_steps = 5
    self.players = players #arrays
    self.actions = actions 
    self.targets = targets 

  def resolve(self):
    for t in range(self.time_steps):   #for each time step
      for player in self.players: #  for each player in order
        pass
        #    perform action
    #print targets and status
    pass

class player():
  def __init__(self):
    self.id = 1
    self.name = '' 

class actions():
  def __init__(self):
    self.id = 1
    self.name = ''
    self.target = ''

class targets():
  def __init__(self):
    self.id = 1
    self.name = ''
    self.status = []
  
  def action(self,actions):
    # effect on state (with constraints)
    pass


