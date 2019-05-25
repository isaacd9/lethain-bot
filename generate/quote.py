# Copyright 2019 The lethain-bot Authors. All rights reserved.
# Use of this source code is governed by the ISC
# license that can be found in the LICENSE file.

import json
import os
import os.path
import random

from bs4 import BeautifulSoup
from summa import textrank


def readall(path):
    with open(path, 'r') as f:
        return f.read()


def main():
    tweets = []
    post_dir = 'blog_posts'
    for f in os.listdir(post_dir):
        soup = BeautifulSoup(readall(os.path.join(post_dir, f)), 'html.parser')

        post_name = f.split('.')[0]
        url = 'https://lethain.com/%s/' % post_name

        post_contents = soup.find('div', {'class': 'blog-post'})

        text_contents = ' '.join([p.text for p in post_contents.find_all('p')]).replace('\n', ' ')
        summary_text = textrank.summarize(text_contents, 0.2)
        # 255 is 280 - length of a t.co link
        knowledge = [l for l in summary_text.splitlines() if len(l) <= 255]
        for line in knowledge:
            line = line.replace('–', '-').replace('’', '\'')
            tweets.append('%s %s' % (line, url))

    random.shuffle(tweets)

    tracery = {
        'origin': '#content#',
        'content': tweets,
    }
    print(json.dumps(tracery, indent=4))


if __name__ == '__main__':
    import sys
    sys.exit(main())
