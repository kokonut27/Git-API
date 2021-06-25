import requests
import os
import json


url = 'https://api.github.com/graphql'
USER = """
  bio
  email
  avatarLink:avatarUrl
  accountCreatedAt:createdAt
  isAdmin:isSiteAdmin
  location
  name
  twitterUsername
  isDevMember:isDeveloperProgramMember
  userId:databaseId
  pinnedItems:anyPinnableItems 
"""


class asdf:
  def run_query(query, token):
        try:
          headers = {"Authorization": "Bearer " + token}
        except:
          raise Exception("Token has not been named by token function")
        request = requests.post(url, json={'query': query}, headers=headers)
        if request.status_code == 200:
          return json.dumps(request.json(), indent=2, sort_keys=True)
        else:
          raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

def Token(TOKEN=None):
  global token
  if TOKEN == None:
    raise Exception("TOKEN argument must be filled out!")
  else:
    token = TOKEN

class user:
  def __init__(self, username):
    try:
      self.token = token
    except:
      raise Exception("Token has not been named by token function")
    self.user = username
    query = """
      query UserData { 
          user(login: \"""" + self.user + """\") { 
            """+USER+"""
          } 
      }
    """
    self.query = query
    
    #if self.token == None:
    #  raise Exception("Token must be inputted!")
    if self.user == None:
      raise Exception("Username must be inputted!")
    
    #return asdf.run_query(query, self.token)

  def User(self):
    self.userf = asdf.run_query(self.query, self.token)
    return self.userf


  def Name(self):
    query = """
      query UserData { 
          user(login: \"""" + self.user + """\") { 
            name
          } 
      }
    """
    self.name = asdf.run_query(query, self.token)
    return self.name

# Token(os.environ["token"])
# print(user("JBYT27").name())