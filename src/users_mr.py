'''
Created on Sep 2, 2013
@author: vandana
map reduce runner for user related analysis of pinterest data
'''
from datetime import datetime
from library.mrjobwrapper import runMRJob
from settings import f_users, chevron_base_dir
from users import Users
from src.utilities import fs

class UsersMRJobRunner(object):
  @staticmethod
  def get_users(input_files_start_time, input_files_end_time, input_folder):
    mr_class = Users
    output_file = f_users
    runMRJob(mr_class,
             output_file,
             fs.get_dated_input_files(input_files_start_time,
                                      input_files_end_time,
                                      input_folder),
             mrJobClassParams = {'job_id': 'as'},
             # uncomment when running on local
             #args = [],
             jobconf={'mapred.reduce.tasks':300, 'mapred.task.timeout': 86400000}
    )
  
  @staticmethod
  def run():
    input_files_start_time, input_files_end_time = \
                            datetime(2012, 12, 12), datetime(2013, 9, 1)
    UsersMRJobRunner.get_users(input_files_start_time,
                               input_files_end_time,
                               chevron_base_dir % "users")

if __name__ == '__main__':
  UsersMRJobRunner.run()