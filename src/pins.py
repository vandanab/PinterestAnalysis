'''
Created on Sep 2, 2013
@author: vandana
Get valid pins from pinterest data
'''
import cjson
from library.mrjobwrapper import ModifiedMRJob

class Pins(ModifiedMRJob):
  DEFAULT_INPUT_PROTOCOL = 'raw_value'

  def __init__(self, *args, **kwargs):
    super(Pins, self).__init__(*args, **kwargs)
    lines = open(self.options.users, 'r').readlines()
    self.users = set()
    for line in lines:
      self.users.add(line)
  
  def configure_options(self):
    super(Pins, self).configure_options()
    self.add_file_option('--users', default='/home/vardharaj/workspace/PinterestAnalysis/data/results/users/users.txt')
  """
  mapper for finding valid users in pinterest data 
  """
  def mapper(self, key, line):
    data = cjson.decode(line)
    if data['pin_user'] in self.users:
      yield data['pin_user'], data

  def reducer(self, key, values):
    #till July's data pin_user is username
    user_pins = {}
    user_pins['userid'] = key
    user_pins['pins'] = []
    for pin in values:
      user_pins['pins'].append(pin)
    yield data['pin_user'], user_pins

if __name__ == "__main__":
  Pins.run()
