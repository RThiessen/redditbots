import praw
import os
import webbrowser

app_id = input("Paste App ID: ")
app_secret = input('Paste App Secret: ')
app_uri = 'https://127.0.0.1:65010/authorize_callback'
app_ua = 'bot function'
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'

r = praw.Reddit(app_ua)
r.set_oauth_app_info(app_id, app_secret, app_uri)
r.get_authorize_url('...', app_scopes, True)

link = r.get_authorize_url('...', app_scopes, True)

print("Go to the link generated and click allow.")
webbrowser.open(link)
acc_code = input("Paste account code (last part of url): ")
print(r.get_access_information(acc_code))
acc_refresh = input("Paste refresh token: ")

acc_name = input("Enter the account name: ")

generateText = input("Is everything correct and do you want to generate a text file containing the codes for future projects? Y/N: ")

if generateText == 'y' or 'Y':
		os.chdir("C:\Programming") #change to where you want to save the text file
        textFile = open(acc_name+"_OAuthCredentials.txt", "w")
        textFile.write("APP_ID = "+app_id+"\n")
        textFile.write("APP_SECRET = "+app_secret+"\n")
        textFile.write("APP_URI = https://127.0.0.1:65010/authorize_callback #This will always be the same url\n")
        textFile.write("APP_REFRESH = "+acc_refresh+"\n")
        textFile.close()