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
  company
    status {
      gitEmoji:emoji
      lastUpdated:updatedAt
      message
      id
      expires:expiresAt
    }
"""
REPO = """
  name 
  id 
  description 
  homepageUrl
  isEmpty 
  isArchived 
  isDisabled 
  isLocked
  stargazerCount
  isPrivate 
  databaseId 
  createdAt
  primaryLanguage {
    name
  }
"""
query_website = "https://docs.github.com/en/graphql/reference/queries" # For reference.

class ArgumentError(Exception):
  pass
class QueryFailError(Exception):
  pass


class asdf:
  # run a request from the github api
  def run_query(query, token):
        try:
          headers = {"Authorization": "Bearer " + token}
        except:
          raise ArgumentError("Token has not been named by token function!")
        request = requests.post(url, json={'query': query}, headers=headers)
        if request.status_code == 200:
          return json.dumps(request.json(), indent=2, sort_keys=True)
        else: # the request failed
          raise QueryFailError("Query failed to run by returning code of {}. {}".format(request.status_code, query))

# set the token
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
     # if user has not yet ran the token function
    except:
      raise ArgumentError("Token has not been named by token function!")
    self.user = username
    # create the query
    query = """
      query UserData { 
          user(login: \"""" + self.user + """\") { 
            """+USER+"""
          } 
      }
    """
    self.query = query
    
    # if the username is none
    if self.user == None:
      raise ArgumentError("Username argument must be filled out!")
    
    self.runQ = asdf.run_query

  # actually run the request
  def User(self):
    self.userf = self.runQ(self.query, self.token)
    return self.userf

  # edit the query - returns github nickname
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
  
  # same thing as above, just for github bio
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

  def Company(self):
    query = """
      query UserData {
          user(login: \"""" + self.user + """\") {
            company
          }
      }
    """
    self.company = self.runQ(query, self.token)
    return self.company


 
class UserFollower:
  def __init__(self, username, followercount):
    try:
      self.token = token
     # if user has not yet ran the token function
    except:
      raise ArgumentError("Token has not been named by token function!")
    self.user = username
    self.userfollower = followercount
    # self.userfollowing = followingcount
    # create the query

    query = """
      query UserFollowerData { 
        user(login: \"""" + self.user + """\") { 
              followers(first: """+followercount+""") {
            users: nodes {
              name: login
            }
          }
        }
      }
    """
    self.query = query
    
    # if the username is none
    if self.user == None:
      raise ArgumentError("Username argument must be filled out!")
    if self.userfollower == None:
        raise ArgumentError("Userfollower argument must be filled out!")
    
    self.runQ = asdf.run_query
  
  def Followers(self):
    self.userfollower2 = self.runQ(self.query, self.token)
    return self.userfollower2
  



class UserFollowing:
  def __init__(self, username, followingcount):
    try:
      self.token = token
     # if user has not yet ran the token function
    except:
      raise ArgumentError("Token has not been named by token function!")
    self.user = username
    # self.userfollower = followercount
    self.userfollowing = followingcount
    # create the query

    query = """
      query UserFolloweringData { 
        user(login: \"""" + self.user + """\") { 
              following(first: """+followingcount+""") {
            users: nodes {
              name:login
            }
          }
        }
      }
    """
    self.query = query
    
    # if the username is none
    if self.user == None:
      raise ArgumentError("Username argument must be filled out!")
    if self.userfollowing == None:
        raise ArgumentError("Userfollowing argument must be filled out!")
    
    self.runQ = asdf.run_query
  
  def Following(self):
    self.userfollowing2 = self.runQ(self.query, self.token)
    return self.userfollowing2




class GitHub:
  def __init__(self, username):
    self.user = username
  def Status():
    url = "https://github.com"
    res = requests.get(url)
    status = res.status_code
    return status
  
  '''def Search(topic):
    query = """
      query SearchData {
          user(login: \"""" + self.user + """\") {
            
          }
      }
    """'''


 
class Repo:
  def __init__(self, owner, reponame):
    try:
      self.token = token
     # if user has not yet ran the token function
    except:
      raise ArgumentError("Token has not been named by token function!")
    
    self.reponame = reponame
    self.owner = owner

    if self.reponame == None:
      raise ArgumentError("Reponame argument must be filled out!")
    
    if self.owner == None:
      raise ArgumentError("Owner argument must be filled out!")

    self.runQ = asdf.run_query
    

  def Repo(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          """+REPO+"""
        }
      }
    """

    self.repo = self.runQ(query, self.token)
    return self.repo

  def CreatedAt(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          createdAt
        }
      }
    """

    self.createdAt = self.runQ(query, self.token)
    return self.createdAt

  def Databaseid(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          databaseId
        }
      }
    """

    self.dbId = self.runQ(query, self.token)
    return self.dbId
  
  def Description(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          description
        }
      }
    """

    self.repoDescription = self.runQ(query, self.token)
    return self.repoDescription
  
  def Homepageurl(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          homepageUrl
        }
      }
    """
    self.homepageUrl = self.runQ(query, self.token)
    data2 = ""
    data2 += str(self.homepageUrl)
    data = json.loads(data2)
    if data["data"]["repository"]["homepageUrl"] == "" or data["data"]["repository"]["homepageUrl"] == None:
      return("No url exists or is private!")
    else:
      return self.homepageUrl
  
  def Id(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          id
        }
      }
    """

    self.repoId = self.runQ(query, self.token)
    return self.repoId
  
  def IsArchived(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          isArchived
        }
      }
    """

    self.repoIsArchived = self.runQ(query, self.token)
    return self.repoIsArchived
  
  def IsDisabled(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          isDisabled
        }
      }
    """

    self.repoIsDisabled = self.runQ(query, self.token)
    return self.repoIsDisabled
  
  def IsEmpty(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          isEmpty
        }
      }
    """

    self.repoIsEmpty = self.runQ(query, self.token)
    return self.repoIsEmpty
  
  def IsLocked(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          isLocked
        }
      }
    """

    self.repoIsLocked = self.runQ(query, self.token)
    return self.repoIsLocked
  
  def IsPrivate(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          isPrivate
        }
      }
    """

    self.repoIsPrivate = self.runQ(query, self.token)
    return self.repoIsPrivate
  
  def Name(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          name
        }
      }
    """

    self.repoName = self.runQ(query, self.token)
    return self.repoName
  
  def Language(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          primaryLanguage {
            name
          }
        }
      }
    """

    self.repoLanguage = self.runQ(query, self.token)
    return self.repoLanguage
  
  def Stars(self):
    query = """
      query RepoData {
        repository(name: \""""+self.reponame+"""\" owner: \""""+self.owner+"""\") {
          stargazerCount
        }
      }
    """

    self.repoStars = self.runQ(query, self.token)
    return self.repoStars

# Remove this when uploading to PyPi
# Token(os.environ["token"])
# print(User("JBYT27").User())
# print(User("JBYT27").Email())
# print(GitHub.Status())
# print(Repo("JBYT27", "GitAPI").Repo())
# print(UserFollowing("JBYT27", "10").Following())