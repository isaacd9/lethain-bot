# Copyright 2019 The lethain-bot Authors. All rights reserved.
# Use of this source code is governed by the ISC
# license that can be found in the LICENSE file.

import requests

from bs4 import BeautifulSoup


def scrape_post(path):
    post_name = path.strip('/')
    print('scraping %s' % post_name)
    r = requests.get('https://lethain.com' + path)
    r.raise_for_status()

    with open('blog_posts/' + post_name + '.html', 'w') as f:
        f.write(r.text)


def main():
    r = requests.get('https://lethain.com/all-posts/')
    r.raise_for_status()

    soup = BeautifulSoup(r.text, 'html.parser')

    post_list = soup.find('div', {'class': 'blog-post-list'}).find_all('li')
    management_post_list = [li for li in post_list if li.find('a', {'href': '/tags/management/'})]
    for post in management_post_list:
        http_path = post.a['href']
        scrape_post(http_path)

    print('posts %d, mps %d' % (len(post_list), len(management_post_list)))


if __name__ == '__main__':
    import sys
    sys.exit(main())
