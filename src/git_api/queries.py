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