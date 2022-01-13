import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("<sorry but cant show my api keys over here>", "<sorry but cant show my api keys over here>")
auth.set_access_token("<sorry but cant show my api keys over here>", "<sorry but cant show my api keys over here>")

# Create API object
api = tweepy.API(auth)

class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
inp=input(bcolors.WARNING +"Hii pls input the status u wanna put:"+ bcolors.ENDC)
# Create a tweet
api.update_status(inp)