'''
Created on Sep 2, 2013
@author: vandana
Get valid users from pinterest data
'''
import cjson
from library.mrjobwrapper import ModifiedMRJob

class Users(ModifiedMRJob):
  DEFAULT_INPUT_PROTOCOL = 'raw_value'
  
  def __init__(self, *args, **kwargs):
    super(Users, self).__init__(*args, **kwargs)
  
  """
  mapper for finding valid users in pinterest data 
  """
  def mapper(self, key, line):
    data = cjson.decode(line)
    if len(data["boards"]) > 0 and int(data["boards_count"]) > 0:
      yield key, data["user"]

if __name__ == "__main__":
  Users.run()