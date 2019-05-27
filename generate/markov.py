#!/bin/env python3

import sys
import os

import markovify

def get_all_posts():
    all_post_contents = []
    for root, dirs, post_file in os.walk('blog_posts'):
        for filename in post_file:
            fq_path = os.path.join(root, filename)
            with open(fq_path) as f:
                sys.stderr.write(f'reading {fq_path}\n')
                all_post_contents += [f.read()]

    return all_post_contents

def main():
    contents = get_all_posts()
    model = markovify.Text(contents, state_size=3)

    tweets = []

    for i in range(10):
        se = model.make_short_sentence(280, tries=50)
        tweets += [se]

    for t in tweets:
        print(t)
        print()


if __name__ == '__main__':
    sys.exit(main())
