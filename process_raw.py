import json
import os


def main():
    tweets = []
    try:
        file = open('tweets.json')
        processed = open('process_tweets.json', 'w')
        processed.seek(0)
        processed.write('{"tweets":[')
        for line in file:
            if (line.endswith('\n')):
                line = line.rstrip('\n')
                line += ',\n'
            processed.writelines(line)
        processed.seek(0, os.SEEK_END)
        processed.seek(processed.tell() - 2, os.SEEK_SET)
        # breakpoint()
        processed.write(']}')
        processed.close()
        processed = open('process_tweets.json')
        json_file = json.load(processed)
        processed.close()
        processed = open('process_tweets.json', 'w')
        json.dump(json_file, processed, indent=3, sort_keys=True)

        # dump = open('dump.json', 'w')
        # breakpoint()
    except Exception as exc:
        print(exc)
    finally:
        file.close()
        processed.close()
    print('process finished successful')


if __name__ == "__main__":
    main()
