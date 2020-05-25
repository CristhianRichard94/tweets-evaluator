from classifier import *
import json


def main():
    clf = SentimentClassifier()
    tweets = []
    try:
        file = open('process_tweets.json')
        json_t = json.load(file)['tweets']
        for tweet in json_t:
            if ('extended_tweet' in tweet['tweet_raw'] and 'full_text' in tweet['tweet_raw']['extended_tweet']):
                text = tweet['tweet_raw']['extended_tweet']['full_text']
            else:
                text = tweet['tweet_raw']['text']
            save_tweet = {}
            save_tweet['value'] = clf.predict(text)
            save_tweet['text'] = text
            tweets.append(save_tweet)
        dump = open('dump.json', 'w')
        json.dump(tweets, dump, indent=3, sort_keys=True)
    except Exception as exc:
        print(exc)
    finally:
        file.close()
    print('process finished successful')


if __name__ == "__main__":
    main()
