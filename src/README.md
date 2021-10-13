⚠️ CAUTION: **`Note that this is a WIP, and is not yet perfected. There will be errors, and it would be appreciated if you let us know about it.`** ⚠️
> **Version: 1.7.0

[![Contributors](https://img.shields.io/github/contributors/JBYT27/GitAPI?style=for-the-badge)](https://github.com/JBYT27/GitAPI/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/JBYT27/GitAPI?style=for-the-badge)](https://github.com/JBYT27/GitAPI/network/members)
[![Stargazers](https://img.shields.io/github/stars/JBYT27/GitAPI?style=for-the-badge)](https://github.com/JBYT27/GitAPI/stargazers)
[![Issues](https://img.shields.io/github/issues/JBYT27/GitAPI?style=for-the-badge)](https://github.com/JBYT27/GitAPI/issues)
[![License](https://img.shields.io/github/license/JBYT27/GitAPI?style=for-the-badge)](https://github.com/JBYT27/GitAPI/blob/master/LICENSE)
[![Downloads on PyPI](https://img.shields.io/pypi/dw/git_api?style=for-the-badge)](https://pypi.org/project/git-api/)

# GitAPI: An API made for GitHub Stats!
> Coded in [Python3](https://python.org), uploaded to [PyPi](https://pypi.org), and coded by [JBYT27](https://github.com/JBYT27)

## About
### About
GitAPI is an API made with python - styled with json - to make the data preferably easier to use. It is made up of posting `json` requests, and retrieving that data from a function, and transfering that data into an output, in which you can use.

This API is designed to show GitHub stats for certain users, or viewing GitHub itself, in data form.

> To learn how to use it, you can read the Usage header below.

### Languages used
Languages used to program this package were: [Python3](https://python.org)

### Queries
Not all of the GitHub queries are in here, but if you wish to see all of them, go to [this](https://docs.github.com/en/graphql/reference/queries) GitHub docs.

### Contributers
- [darkdarcool](https://github.com/darkdarcool): More professionalized file-ing and helping with more GitHub Queries.
- [Isaiah08-D](https://github.com/Isaiah08-D): Adding comments, and letting us know of [bug](https://github.com/JBYT27/GitAPI/issues/11).
- [jwodder](https://github.com/jwodder): Finding the solution to the [bug](https://github.com/JBYT27/GitAPI/issues/11).

## Usage
### Installation

To install and use the package, you must first:

```shell
pip install git_api
```

This will install the package - `git_api`(GitAPI) - and then you will be able to use it. 

To then import it, you must put the following code:

```py
import git_api
```
**OR**
```py
import git_api as gitapi
```
**OR**
```py
from git_api import *
```
For more information, go [here](https://pypi.org/project/git-api/).

> Note that all of these methods work.

### Usage
To use this package, first import it as shown above. Then create a python file - name it whatever you want, it doesn't matter.

Once you're done with that, open the file, and add the following example code:

```py
import git_api

git_api.Token() # We'll place the personal access token here later on. For now, it'll be empty.
user_info = git_api.User("Username here").User() # Insert your username in the argument shown here.

print(user_info)
```

You've done it! But wait - it doesn't work, it only gives an error! The reason for this is that - 

**NUMBER 1**: You need a personal access token which we'll discuss in a moment.

**NUMBER 2**: You need to have a GitHub username in mind and place it in the assigned space.

Let's start with number 1, creating the token.

#### 1: The Token
To first create a token, you must create or use an existing GitHub account. If you already have a GitHub account, you can move on to the next section. However, if you are *creating* a new GitHub account, follow the instructions below:

#1: Go to [`https://github.com`](https://github.com) and click `sign up`.

#2: Once you've clicked that, just follow the instructions shown on the page.

#3: Then after that, you can either get used to GitHub and do this later, or do this immediately; Go to [this](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) document and read it thoroughly, as it holds the information to creating a personal token. Choose the categories you think will best fit for your project and finish up with the token.

#4: Note that this token should be kept private and not shared. If you are positive that this token will be private, then you can just copy and paste the token into a string (inside parentheses), and insert it into the token argument space. However, if you know that this will be shown to the public, create a `.env` file, and paste the token inside there. Make sure you make it a variable, for example, like this:

```
token=blahblahblah
```
Also note that you can only copy the token once, so check that you actually copied down the token. Go back into your python file and copy/paste down the following code into the assigned space;

```py
os.environ["token"] # Insert your .env variable here
```

> **NOTE: All GitAPI functions must have a token in order for it to work.**

#5: Then you're pretty much done! Your final code example should look something like this:

#### 2: Finale

```py
import git_api

git_api.Token(os.environ["token"])
user_info = git_api.User("JBYT27").User()

print(user_info)
```

> This will print some of the user's information.

#### Another cool thing you can do with this package is print a GitHub User's followers! Wanna try? Here we go!

#### 1. Import the package
First, import the package as shown above. All you need to do is `import git_api`. Or you can install from `pip` and then do that. Let's go onto the next step.

#### 2. Get the token
Remember how I said the token was important? Yeah, it really is. So it's step 2 ;) 
If you don't know how to create a token, it's written right above. So far, you should have something like this:

```py
import git_api
import os

git_api.Token(os.environ["token"])
```

#### 3. The function
Now we write the function. So to get a GitHub user's followers, it's a bit wonky. So the syntax for the function is `git_api.UserFollower("USERNAME", "INTEGER").Followers()`. You replace the `"USERNAME"` with a GitHub username and replace the `"INTEGER"` with a string that has a integer number inside it to show how many followers should be shown. Note that this is **returning** the value, not *printing* it. So what you have to remember is that you have to print this variable or value in order for it to show.

*Kinda confusing, right? Let me show you an example :)*

```py
import git_api # importing the package. Note that you can use `pip` as well
import os # using os package to get token from .env file

git_api.Token(os.environ["token"]) # retrieves the token so you can use it.

follower_data = git_api.UserFollower("JBYT27", "10").Followers() # the gitapi function to get data

print(follower_data) # prints data
```

So that will print a GitHub user's followers. If you want to show the users that a GitHub user is following, all you have to do is switch the function(`UserFollower`) to `UserFollowing`. So for following, it would look like this:

```py
import git_api # importing the package. Note that you can use `pip` as well
import os # using os package to get token from .env file

git_api.Token(os.environ["token"]) # retrieves the token so you can use it.

following_data = git_api.UserFollowing("JBYT27", "10").Following() # the gitapi function to get data

print(following_data) # prints data
```

You can take a look at the code, or just play with it if you want to experiment with it :)

> An example repl is listed [here](https://replit.com/@JBloves27/GitAPI-Example).


## Contributing
Contributing will be listed mostly in the [Code of Conduct](https://github.com/JBYT27/GitAPI/blob/master/.github/CODE_OF_CONDUCT.md), however for more info, visit the [Contributing](https://github.com/JBYT27/GitAPI/blob/master/.github/CONTRIBUTE.md) readme.

## License
This package is under the [`MIT License`](https://github.com/JBYT27/GitAPI/blob/master/MyApp/LICENSE).

## Features:
- [x] Add basic features for `User()` class 
- [ ] Add advanced features for `User()` class
- [x] Add basic functions for `GitHub()` class
- [ ] Add advanced functions for `GitHub()` class
- [ ] Add basic functions in package
- [ ] Add documentary for package 
