'''
Created on Sep 2, 2013
@author: vandana
Contains filesystem related utilities
'''
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os

def get_dated_input_files(start_time, end_time, input_folder):
  current = start_time
  while current <= end_time:
    input_folder = input_folder + "%s/%s/%s/" % (current.year,
                                                 current.month,
                                                 current.day)
    print input_folder
    if os.path.exists(input_folder):
      for root, _, files in os.walk(input_folder):
        for fl in files:
          input_file = root+fl
          print input_file
          #yield input_file
    current += relativedelta(days=1)

if __name__ == "__main__":
  input_files_start_time = datetime(2012, 12, 12)
  input_files_end_time = datetime(2013, 9, 1)
  get_dated_input_files(input_files_start_time,
                        input_files_end_time,
                        "/mnt/chevron/vbachani/pinterest/data/users/")
