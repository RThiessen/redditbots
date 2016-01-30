#Ronald Thiessen
import praw
import time
import getpass

USERAGENT = ""
#Description of bot for the API
ID = ""
SECRET = ""
URI = ""
REFRESH = ""

print('Logging in...')

r = praw.Reddit(USERAGENT)
r.set_oauth_app_info(ID, SECRET, URI)
r.refresh_access_information(REFRESH)

def mainBot():
    print('\nPlease enter a score threshold. All comments with a score less than the threshold will be deleted.')
    THRESHOLD = int(input(''))
    print('\nThis will delete all comments with score less than ' + str(THRESHOLD) + '.')
    print('Are you sure you want to proceed? Y/N')
    userInput = input('')
    if userInput == 'y' or 'Y':
        user = r.user
        delete(user, THRESHOLD)

def delete(user, THRESHOLD):
    print('\nFetching comments...')
    comments = list(user.get_comments(limit=1000))
    print('Processing ' + str(len(comments)) + ' comments.')
    for item in comments:
        if item.score < THRESHOLD:
            print('Deleting ' + 'comment' + ' with score ' + str(item.score))
            item.delete()

while True:
    mainBot()