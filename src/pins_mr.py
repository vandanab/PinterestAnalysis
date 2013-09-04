'''
Created on Sep 2, 2013
@author: vandana
map reduce runner for pin related analysis of pinterest data
'''
from datetime import datetime
from library.mrjobwrapper import runMRJob
from settings import f_users, hdfs_base_dir, chevron_base_dir, hdfs_rel_path
from pins import Pins
from utilities import fs

class PinsMRJobRunner(object):
  @staticmethod
  def get_pins(input_files_start_time, input_files_end_time, input_folder):
    mr_class = Pins
    output_file = f_users
    chevron_files = fs.get_dated_input_files(input_files_start_time,
                                      input_files_end_time,
                                      input_folder)
    hdfs_files = []
    for file in chevron_files:
      hdfs_files = hdfs_rel_path + file
      
    runMRJob(mr_class,
             output_file,
             hdfs_files,
             mrJobClassParams = {'job_id': 'as'},
             # uncomment when running on local
             #args = [],
             jobconf={'mapred.reduce.tasks':300, 'mapred.task.timeout': 8640000}
    )

  @staticmethod
  def run():
    input_files_start_time, input_files_end_time = \
                            datetime(2012, 12, 12), datetime(2013, 9, 1)
    PinsMRJobRunner.get_pins(input_files_start_time,
                               input_files_end_time,
                               hdfs_base_dir)

if __name__ == '__main__':
  PinsMRJobRunner.run()

