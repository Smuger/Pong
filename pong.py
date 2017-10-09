from tinydb import Query
from tinydb import TinyDB
import pygame, sys
#db config
db = TinyDB('user.json')
users_table = db.table('users')
scores = db.table('scores')
def addscore():
    global users_table, db, scores
    # lastid
    user_count = len(scores)
    scores.insert({'score': int(v2.get()), 'uid': int(v.get()), 'id': user_count+1})

def seescore():
    global users_table, db, scores
def adduser():
    global users_table, db
def users():
    global users_table, db
    user_count = len(users_table)
    userlist = users_table.all();
    for i in range(0, user_count):
        userlist[i]['id']
