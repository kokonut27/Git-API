import json
import requests

#res = requests.get("https://api.github.com/users/"+self.user)#.json()

class InvalidStr(Exception):
  pass

class user:
  def __init__(self, username: str):
    if type(username) != str:
      raise InvalidStr("The 'username' arguement is not a string!")
    self.user = username

class 