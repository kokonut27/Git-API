import json
import requests
import os
#from bs4 import BeautifulSoup

#res = requests.get("https://api.github.com/users/"+self.user)#.json()



url = "https://api.github.com/graphql"

headers = {
  "Content-Type": "application/json",
  "Authorization": f"bearer {os.environ['token']}"
}


USER = """
bio
name
email
avatarUrl
createdAt
isSiteAdmin
location
twitterUsername
isDeveloperProgramMember"""

followerQuery = """
query defualtUserData($username: String!, $followerCount: Int!, $followingCount: Int!) {
  user(login: $username) {
  	followers(first: $followerCount) {
      users: nodes {
        name: login
      }
    }
    following(first: $followingCount) {
      users: nodes {
        name:login
      }
    }
  }
}"""


class InvalidStr(Exception):
  pass
class InvalidUser(Exception):
  pass


class user:
  def __init__(self, username):
    body = {'query':'query defualtUserData($username: String!) {user(login: "'+username+'") { '+USER+' } }'}
    self.user = username
    self.res = json.loads(requests.post(url, data=body, headers=headers).text)#['data']['user']
    if self.res is None:
      raise InvalidUser("No such GitHub user exists!")
    self.bio = self.res["bio"]
    self.name = self.res["name"]
    self.email = self.res["email"]
    self.avatar = self.res["avatarUrl"]
    

  def name(self):
    body = {
          'query': """query user($username: String!) {
                      user: user(login: $username) {
                        name() {
                          items {
                            """+USER+"""
                          }
                        }
                      }
                    }
            """,
            "variables": json.dumps({
              "username": self.res["username"],
            })
          }
    return json.dumps(json.loads(requests.post(url, data=body,headers=headers).text), sort_keys=True, indent=2)
    #return self.name

  def followers(self):


    return self.followers

  def status(self):

    return self.status


#user("JBYT27").name()
body = {'query':'query defualtUserData($username: String!) {user(login: "JBYT27") { '+USER+' } }'}
json.loads(requests.post(url, data=body, headers=headers).text)['data']['user']