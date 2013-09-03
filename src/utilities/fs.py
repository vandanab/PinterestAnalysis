'''
Created on Sep 2, 2013
@author: vandana
Contains filesystem related utilities
'''
from dateutil.relativedelta import relativedelta
import os

def get_dated_input_files(startTime, endTime, input_folder):
    current = startTime
    while current <= endTime:
      input_folder = input_folder + "%s/%s/%s/" % (current.year, 
                                                  current.month,
                                                  current.day)
      if os.path.exists(input_folder):
        for root, _, files in os.walk(input_folder):
          for fl in files:
            input_file = root+fl
            print input_file
            yield input_file
      current += relativedelta(days=1)
