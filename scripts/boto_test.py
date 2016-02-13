#!/usr/bin/python
import os
#import boto
import pymongo
import re
import hashlib

import boto

import time

path ='/mnt/sitedata'
counter = 0

#ec2 = boto.ec2.connect_to_region('us-west-1')
ec2 = boto.connect_ec2()

#see
# https://gist.github.com/kjoconnor/7344485
# Failing because of perms
# snapshots = ec2.get_all_snapshots()


#see
# http://boto.cloudhackers.com/en/latest/getting_started.html
# failing
#s3 = boto.connect_s3()
#bucket = s3.create_bucket('boto-demo-%s' % int(time.time()))

#bucket created through GUI - ltu-boto-test

s3 = boto.connect_s3()
b=s3.get_bucket('ltu-boto-test')
print b

#bucket = s3.get_bucket('ltu-boto-test')
#k = bucket.new_key('foobar')
#k.set_contents_from_string('This is a test of S3')



