'''
Created on Sep 2, 2013
@author: vandana
Contains filesystem related utilities
'''
import sys
sys.path.append("/home/vardharaj/workspace/PinterestAnalysis/")
from datetime import datetime
from dateutil.relativedelta import relativedelta
from src.settings import chevron_base_dir
import os

def get_dated_input_files(start_time, end_time, input_folder):
  #print "hello"
  input_files = [] 
  current = start_time
  while current <= end_time:
    rel_path = "%s/%s/%s/" % (current.year, current.month, current.day)  
    in_folder = input_folder + rel_path
    if os.path.exists(in_folder):
      for root, _, files in os.walk(in_folder):
        for fl in files:
          input_file = root+fl
          rel_file_path = rel_path + fl
          #print input_file
          #yield input_file
          input_files.append(rel_file_path)
    current += relativedelta(days=1)
  return input_files

  
if __name__ == "__main__":
  #print "hello"
  input_files_start_time = datetime(2012, 12, 12)
  input_files_end_time = datetime(2013, 9, 1)
  get_dated_input_files(input_files_start_time,
                        input_files_end_time,
                        "/Users/vardharaj/workspace/PinterestAnalysis/data/input/users/")
