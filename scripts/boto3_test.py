#!/usr/bin/python
import os
#import boto
#import pymongo
import re
import hashlib

import boto3

import time

session = boto3.session.Session(profile_name='snap2obj')
client = session.client('s3')
response = client.list_buckets()
#print response.keys()
#print response['Buckets']

#for b in response['Buckets']:
#  print b
#  print " --- "
#bucket = s3.get_bucket('ltu-boto-test')
#k = bucket.new_key('foobar')
#k.set_contents_from_string('This is a test of S3')

#ec2 = session.resource('ec2')

ec2 = session.client('ec2')

print "about to get snapshots"
s= ec2.describe_snapshots( MaxResults=100 , OwnerIds=[
        'self'
    ] )

print s.keys()
print " ==== "
print s
print " ==== "
#print s['Snapshots']
for sn in s['Snapshots']:
  #print sn.keys()
  print sn.get('Description')
  print 'Tags: '
  print sn.get('Tags',' [no tags] ')
  print
print " ---- "
print len(s['Snapshots'])

