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