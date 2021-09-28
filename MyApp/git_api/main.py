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

class ArgumentError(Exception):
  pass
class QueryFailError(Exception):
  pass


class asdf:
  def run_query(query, token):
        try:
          headers = {"Authorization": "Bearer " + token}
        except:
          raise ArgumentError("Token has not been named by token function!")
        request = requests.post(url, json={'query': query}, headers=headers)
        if request.status_code == 200:
          return json.dumps(request.json(), indent=2, sort_keys=True)
        else:
          raise QueryFailError("Query failed to run by returning code of {}. {}".format(request.status_code, query))

def Token(TOKEN=None):
  global token
  if TOKEN == None:
    raise ArgumentError("TOKEN argument must be filled out!")
  else:
    token = TOKEN

class User:
  def __init__(self, username):
    try:
      self.token = token
    except:
      raise ArgumentError("Token has not been named by token function!")
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
      raise ArgumentError("Username argument must be filled out!")
    
    #return asdf.run_query(query, self.token)
    self.runQ = asdf.run_query

  def User(self):
    self.userf = self.runQ(self.query, self.token)
    return self.userf


  def Name(self):
    query = """
      query UserData { 
          user(login: \"""" + self.user + """\") { 
            name
          } 
      }
    """
    self.name = self.runQ(query, self.token)
    return self.name
  
  def Bio(self):
    query = """
      query UserData {
          user(login: \"""" + self.user + """\") {
            bio
          }
      }
    """
    self.bio = self.runQ(query, self.token)
    return self.bio 
  
  def Email(self):
    query = """
      query UserData {
          user(login: \"""" + self.user + """\") {
            email
          }
      }
    """
    self.email = self.runQ(query, self.token)
    data2 = ""
    data2 += str(self.email)
    data = json.loads(data2)
    if data["data"]["user"]["email"] == "" or data["data"]["user"]["email"] == None:
      return("No email exists or is private!")
    else:
      return self.email
  
  def Avatar(self):
    query = """
      query UserData {
          user(login: \"""" + self.user + """\") {
            avatarLink:avatarUrl
          }
      }
    """
    self.avatar = self.runQ(query, self.token)
    return self.avatar
  
  def Account(self):
    query = """
      query UserData {
          user(login: \"""" + self.user + """\") {
            accountCreatedAt:createdAt
          }
      }
    """
    self.account = self.runQ(query, self.token)
    return self.account
  
  def Admin(self):
    query = """
      query UserData {
          user(login: \"""" + self.user + """\") {
            isAdmin:isSiteAdmin
          }
      }
    """
    self.admin = self.runQ(query, self.token)
    return self.admin

  def Location(self):
    query = """
      query UserData {
          user(login: \"""" + self.user + """\") {
            location
          }
      }
    """
    self.location = self.runQ(query, self.token)
    return self.location
  
  def Location(self):
    query = """
      query UserData {
          user(login: \"""" + self.user + """\") {
            location
          }
      }
    """
    self.location = self.runQ(query, self.token)
    return self.location
  
  def Twitter(self):
    query = """
      query UserData {
          user(login: \"""" + self.user + """\") {
            twitterUsername
          }
      }
    """
    self.twitter = self.runQ(query, self.token)
    return self.twitter
  
  def Developer(self):
    query = """
      query UserData {
          user(login: \"""" + self.user + """\") {
            isDevMember:isDeveloperProgramMember
          }
      }
    """
    self.dev = self.runQ(query, self.token)
    return self.dev
  
  def Userid(self):
    query = """
      query UserData {
          user(login: \"""" + self.user + """\") {
            userId:databaseId
          }
      }
    """
    self.userid = self.runQ(query, self.token)
    return self.userid
  
  def PinnedItems(self):
    query = """
      query UserData {
          user(login: \"""" + self.user + """\") {
            pinnedItems:anyPinnableItems
          }
      }
    """
    self.pinneditems = self.runQ(query, self.token)
    return self.pinneditems

class GitHub:
  def Status():
    url = "https://github.com"
    res = requests.get(url)
    status = res.status_code
    return status
  
  # def smth():


# Remove this when uploading to PyPi
# Token(os.environ["token"])
# print(User("JBYT27").User())
# print(User("JBYT27").Email())
# print(GitHub.Status())