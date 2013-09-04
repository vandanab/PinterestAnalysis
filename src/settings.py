'''
Created on Sep 2, 2013
@author: vandana
Pinterest data crawler settings
'''
import os

rex_local_base_dir = os.path.expanduser("/home/vardharaj/workspace/PinterestAnalysis/data/results/%s/")
chevron_base_dir = "/mnt/chevron/vbachani/pinterest/data/pins/"
local_base_dir = "/home/vardharaj/workspace/PinterestAnalysis/data/input/"
#f_users = rex_local_base_dir % "users" + "users.txt"
#hdfs_base_dir = "hdfs:///user/vbachani/PinterestAnalysis/data/%s/"
hdfs_base_dir = "/home/vardharaj/workspace/PinterestAnalysis/data/input/users/"
hdfs_rel_path = "hdfs:///user/vardharaj/pins/"
f_users = rex_local_base_dir % "users" + "users.txt"
f_pins = rex_local_base_dir % "pins" + "pins.txt"

