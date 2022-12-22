'''
Steps:
1. Establish the communication with GitHub by GitHub Token
2. Create link with Git Branch
3. Git storage, HASH and SHA1 algo: 
    Git stores a data in the form of object. 
    Keys & Values (i.e., content of a file).
    Here the key is called HASH.
    For a given value the HASH is calculated by SHA1 algorithm.
    SHA1 algorithm is a 20 bytes HEX data.
    Every object in Git has its own SHA1 algo.

4. Find Commit Date & Time
5. Find Present Date & Time
6. Find difference
7. Condition by difference value
'''

from github import Github
from datetime import datetime, timedelta
import pytz
import os

# Insert github token
# In GitHub: AcharyaBhattS--> Settings--> Developer settings--> 
#--> Personal Access Token--> Tokens(classic)--> Generate New Token(classic)
# OR: https://github.com/settings/tokens/new
# GitToken = Github("<github token>")
GitToken = Github("")

repo = GitToken.get_repo("AcharyaBhattS/CICD_HVProj1")

branch = GitToken.get_repo("AcharyaBhattS/CICD_HVProj1").get_branch("Development")
# print(branch.commit.sha)
ShaVal = branch.commit.sha

# Script to check for the commit history and their time
commits = repo.get_commit(sha=ShaVal)
# print("Author: ",commits.commit.author)
commit_DateTime = commits.commit.author.date
print("Commit Date & Time: ",commit_DateTime)

'''
ts_Commit = commitDetails.timestamp()
print("Commit Timestamp: ",ts_Commit,"\n")
'''

# presentTime = str(datetime.now())
Present_DateTime_gmt = datetime.now(pytz.timezone('GMT'))
print("Present GMT Date & Time: ", Present_DateTime_gmt)

Present_DateTime_set = datetime(Present_DateTime_gmt.year, Present_DateTime_gmt.month, Present_DateTime_gmt.day, Present_DateTime_gmt.hour, Present_DateTime_gmt.minute, Present_DateTime_gmt.second)
print(Present_DateTime_set)
Commit_DateTime_set = datetime(commit_DateTime.year, commit_DateTime.month, commit_DateTime.day, commit_DateTime.hour, commit_DateTime.minute, commit_DateTime.second)
print(Commit_DateTime_set)
  
# returns a timedelta object
DateTime_Difference = Present_DateTime_set-Commit_DateTime_set 
print('Time Difference: ', DateTime_Difference)

if DateTime_Difference < timedelta(minutes=5):
    print("Commit time is < 5")
    # os.system("bash myScript.sh")
else:
    print("Commit time is >= 5")
