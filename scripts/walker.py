#!/usr/bin/python
import os
#import boto
import pymongo
import re
import hashlib

import boto

path ='/mnt/sitedata'
counter = 0

from pymongo import MongoClient
client = MongoClient()


db = client.objdb

#NOTE: it's too slow to hash the files using this
def md5(fname):
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()


for root, dirs, files in os.walk(path):
  for name in files:
    counter += 1
    #print os.path.join(root,name)

    #stat-ing the file
    fs = os.stat(os.path.join(root,name))
    r={}
    r['uid']=fs.st_uid
    r['gid']=fs.st_gid
    r['bytes']=fs.st_size
    #NOTE: need to validate the create time ...
    r['ctime']=fs.st_ctime
    r['mtime']=fs.st_mtime
    r['full_path']=os.path.join(root,name)
    r['basename']= os.path.basename(r['full_path'])

    r['is_moodle_hashfile']=False
    try:
      int(r['basename'],16) #try to convert to hex
      if len(r['basename']) == 40:
        r['is_moodle_hashfile']=True
    except ValueError:
      pass

    r['is_sql_file']=False
    if re.search('\.sql\.?',r['basename']):
      r['is_sql_file']=True

    #this is likely slow
    #DEBUG to see output
    #print str(r['bytes']) + ' -- ' + r['full_path']
    #only check for 100meg or smaller
    # this is still too slow
    if r['bytes'] < 100000000:
      pass
      #r['md5sum']=md5(r['full_path'])

    record_id = db.objs.insert(r)

    if counter % 50 == 0:
      print counter
      #print file_stats

       


