from classifier import SentimentClassifier
import json
import sys
import multiprocessing

def main(filename):
    tweets = []
    try:
        file = open(filename, encoding='utf8', errors='ignore')
        print('File opened')
        json_t = json.load(file)['Tweets']
        print('json loaded')
        pr_count = multiprocessing.cpu_count()
        step = len(json_t) // pr_count
        print('separating in ' + str(pr_count) +
              ' parts with a step of ' + str(step))
        processes = []
        queue_values = multiprocessing.Manager().dict()
        for j in range(pr_count):
            if (j == 0):
                a_from = step*j
            else:
                a_from = step*j + 1
            if (j == pr_count):
                a_to = None
            else:
                a_to = step*(j + 1)
                process = multiprocessing.Process(
                    target=evalArray, args=(json_t[a_from:a_to], j, queue_values))
                processes.append(process)
                process.start()
        for proc in processes:
            proc.join()
        for res in queue_values.values():
            tweets = tweets + res
        dump = open(filename.split('.json')[0]+'_res.json', 'w')
        json.dump(tweets, dump, indent=3, sort_keys=True)
    except Exception as exc:
        print(exc)
    finally:
        file.close()
    print('process finished successful')


def evalArray(array, process_id, ret):
    clf = SentimentClassifier()
    tweets = []
    i = 0
    for tweet in array:
        i += 1
        if ('extended_tweet' in tweet and 'full_text' in tweet['extended_tweet']):
            text = tweet['extended_tweet']['full_text']
        else:
            text = tweet['text']
        save_tweet = {}
        if (i % 50 == 0):
            print('Process ' + str(process_id) +
                  ' Has predicted ' + str(i) + ' Tweets')
        save_tweet['value'] = clf.predict(text)
        save_tweet['text'] = text
        tweets.append(save_tweet)
    ret[process_id] = tweets


if __name__ == "__main__":
    filename = str(sys.argv[1])
    main(filename)
