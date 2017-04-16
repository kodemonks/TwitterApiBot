import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "ldy9qmbPPKlyb7UowiD9S38tI",
    "consumer_secret"     : "C1nGQmGSCnnQIXfxXi1uwmjUeSY1AnLEEgq0afFaAQwhd4nWET",
    "access_token"        : "842290363935133697-VXF9HYnLbgC1MLMrVNzxglfIerYLPXS",
    "access_token_secret" : "O7bHJgr81fpzBWlhR9uZUfj7HE9ccnZQ3ugGnncUi02KQ"
    }

  api = get_api(cfg)
  tweet = "Updated Twitter bot :D  !!!"
  status = api.update_with_media('aa.jpeg',status=tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
  print('Success Posting!!')