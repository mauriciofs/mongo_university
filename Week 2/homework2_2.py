import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.students
grades = db.grades

try:
    for student in grades.find({'type': 'exam'}).sort('student_id', pymongo.ASCENDING):
        cursor = grades.find({'student_id': student['student_id'], 'type': 'homework'})
        cursor.sort('score', pymongo.ASCENDING).limit(1)

        for homework in cursor:
            grades.find_one_and_delete({'_id': homework['_id']})
        
except Exception as e:
    print "Unexpected error:", type(e), e