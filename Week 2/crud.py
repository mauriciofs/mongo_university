
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.school
scores = db.scores


def find(limit):

    print "find, reporting for duty"

    query = {'$or': [{'type':'exam'}, {'type': 'homework'}]}
    projection = {'student_id': True, '_id': False}

    try:
        cursor = scores.find(query, projection)
        cursor.limit(limit).sort('student_id', pymongo.DESCENDING)

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc
        


def find_one():

    print "find one, reporting for duty"
    query = {'student_id':10}
    
    try:
        doc = scores.find_one(query)
        
    except Exception as e:
        print "Unexpected error:", type(e), e

    
    print doc

def insert_one():
    print "insert one, reporting for duty"
    obj = {'student_id': 100, 'type': 'exam', 'score': 99.99}

    try:
        insert = scores.insert_one(obj)
    except Exception as e:
        print "Unexpected error:", type(e), e

    print obj;

def insert_many():
    print "insert many, reporting for duty"
    obj = [{'student_id': 101, 'type': 'exam', 'score': 99.99}, {'student_id': 102, 'type': 'exam', 'score': 99.99}]

    try:
        insert = scores.insert_many(obj, ordered=True)
    except Exception as e:
        print "Unexpected error:", type(e), e

def update_one(student_id):
    print "update one, reporting for duty"

    try:
        doc = scores.find_one({"student_id": student_id, "type": "exam"})
        print "before: ", doc

        result = scores.update_one({"_id": doc['_id']}, {'$set': {'score': 150}})
        print "num matched: ", result.matched_count

        print scores.find_one({"_id": doc['_id']})
    except Exception, e:
        print "Unexpected error:", type(e), e

def delete(student_id):
    print "delete, reporting for duty"

    try:
        result = scores.delete_one({"student_id": student_id})
        print "num matched: ", result.deleted_count
    except Exception, e:
        print "Unexpected error:", type(e), e    

#find(10)
#insert_one();
#insert_many();
#update_one(102);
delete(101);