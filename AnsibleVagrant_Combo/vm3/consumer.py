
#
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, demonstrate Kafka streaming API to build a consumer.
#
import couchdb
import json
import os   # need this for popen
import time # for sleep
from kafka import KafkaConsumer  # consumer of events

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the consumer
# (you will need to change this to your bootstrap server's IP addr)
consumer= KafkaConsumer (bootstrap_servers="129.114.26.223:9092")
couch = couchdb.Server('http://admin:19961009@localhost:5984')

# subscribe to topic
consumer.subscribe (topics=["utilizations1","utilizations2"])

try:
    db = couch['db']
except:
    db = couch.create('db')


# we keep reading and printing
for msg in consumer:
#    print("################first###############")
    kkey = 'db'
    vvalue = (str(msg.value, 'ascii'))
    data = {kkey: vvalue}
    doc_id, doc_rev = db.save(data)
    print(str(msg.value, 'ascii'))
    # try:
    #     db=couch.create('python-tests')
    #     doc_id, doc_rev = db.save({'type': 'Person', 'name': 'John Doe'})
    #     doc = db[doc_id]
    #     print(doc['name'])
    #     del couch['python-tests']
    # except:
    #     pass
    # print("done")
    # what we get is a record. From this record, we are interested in printing
    # the contents of the value field. We are sure that we get only the
    # utilizations topic because that is the only topic we subscribed to.
    # Otherwise we will need to demultiplex the incoming data according to the
    # topic coming in.
    #
    # convert the value field into string (ASCII)
    #
    # Note that I am not showing code to obtain the incoming data as JSON
    # nor am I showing any code to connect to a backend database sink to
    # dump the incoming data. You will have to do that for the assignment.
    # print (str(msg.value, 'ascii'))

# we are done. As such, we are not going to get here as the above loop
# is a forever loop.
consumer.close ()
try:
    del couch['db']
except:
    pass

