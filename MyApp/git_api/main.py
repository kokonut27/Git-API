import json
import requests
from bs4 import BeautifulSoup

#res = requests.get("https://api.github.com/users/"+self.user)#.json()

class InvalidStr(Exception):
  pass
class InvalidUser(Exception):
  pass

class user:
  def __init__(self, username: str):
    if type(username) != str:
      raise InvalidStr("The 'username' arguement is not a string!")
    self.user = username
    res = requests.get(f"https://github.com/{self.user}", headers={"User-Agent": "Mozilla/2.0"})
    if res.status_code == 404:
      raise InvalidUser("No such user exists!")
    self.res = res
    soup = BeautifulSoup(res.content, 'html.parser')
    self.soup = soup

  def name(self):
    

    self.name = None
    return self.name

  def followers(self):


    self.followers = None #to be named
    return self.followers

  def status(self):
    for i in self.soup.find_all('div', attrs={'class':'js-user-status-container user-status-circle-badge d-inline-block lh-condensed-ultra p-2'}):
      status = self.soup.find("div", attrs={'class':"css-truncate css-truncate-target width-fit color-text-primary"})
      for x in i:
        if x == status:
          self.status = status
          return self.status

