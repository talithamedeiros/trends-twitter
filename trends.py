import twitter

class TwitterApi():
    def __init__(self):
        self.api = twitter.Api(consumer_key='your_consumer_key',
                               consumer_secret='your_consumer_secret',
                               access_token_key='your_access_token_key',
                               access_token_secret='yout_access_token_secret')

    def getTrends(self):
        response = self.api.GetTrendsCurrent()
        for r in response:
            print(r)

if __name__ == '__main__':
    twitter = TwitterApi()
    twitter.getTrends()
