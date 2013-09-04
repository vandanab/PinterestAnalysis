'''
Created on Sep 2, 2013
@author: vandana
Pinterest data crawler settings
'''
import os

rex_local_base_dir = os.path.expanduser("/home/vardharaj/workspace/PinterestAnalysis/data/results/%s/")
chevron_base_dir = "/mnt/chevron/vbachani/pinterest/data/%s/"
#f_users = rex_local_base_dir % "users" + "users.txt"
hdfs_base_dir = "hdfs:///user/vardharaj/pins/"
#hdfs_base_dir = "/home/vardharaj/workspace/PinterestAnalysis/data/input/%s"
f_users = rex_local_base_dir % "users" + "users.txt"


