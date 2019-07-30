import tweepy

print('this is my twitter bot')

CONSUMER_KEY = 'EyqaPmuz3v3Qo6JvICm6Bbke5'
CONSUMER_SECRET = 'XeIhMplmmPvVcobqMqTMAFpWVxOnV0eein6F1jrjgLgJVKYGWX'
ACCESS_KEY = '1154833464417501184-hbHbv3qb6wGP3nYa895nPgEDpk1sYO'
ACCESS_SECRET = '2cKTkDra5Vyu4GucSvOLJYVo08dm2FSxb6qKKlQNCE2q1'

auth = tweepy.0AuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)