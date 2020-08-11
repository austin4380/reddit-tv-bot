import praw

reddit = praw.Reddit(client_id='9hG-csgWkhvN1g',
    client_secret='0wSy8DdDm45uQRDOIV9xI9JkWoE',
    username='4ktvbot',
    password='', #enter password of reddit bot account
    user_agent='4K TV Bot')

subreddit = reddit.subreddit('buildapcsales')

keyphrase = "TV"


for submission in subreddit.stream.submissions():
    if keyphrase in submission.title:
        try:
            title = submission.title
            link = submission.permalink
            message = f"{title}\n\nhttps://reddit.com{link}"
            reddit.redditor('').message(title, message) #enter username of redditor to send pm to in ''
            print('posted')
        except:
            print('to frequent')