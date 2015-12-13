import cgi
import urllib
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb

dbname = 'gamesdb'

def db_key():
    return ndb.Key('dbname', dbname)

# NDB Model for a Game
class Game(ndb.Model):
    name = ndb.StringProperty()
    minplayers = ndb.IntegerProperty()
    maxplayers = ndb.IntegerProperty()
    mintime = ndb.IntegerProperty()
    maxtime = ndb.IntegerProperty()
    difficulty = ndb.IntegerProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
