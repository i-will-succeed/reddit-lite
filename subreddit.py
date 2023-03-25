import requests
import sys
from bs4 import BeautifulSoup
import subprocess
import argparse

# see docs for argparse at https://docs.python.org/3/library/argparse.html

parser = argparse.ArgumentParser(description='Search a subreddit')
parser.add_argument('subreddit', help='Subreddit name')
parser.add_argument('search_query', help='Search query')

args = parser.parse_args()

reddit_search = args.search_query.replace(' ', '+')
reddit_name = args.subreddit
reddit_link = f"https://old.reddit.com/r/{reddit_name}/search?q={reddit_search}&restrict_sr=on"

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}
response = requests.get(reddit_link, headers=headers)


html_file = response.text
soup = BeautifulSoup(html_file, 'html.parser')

# Print Title
print(soup.title.string)




# find search-result-group, then class='contents', then inside, the
# div.search-result is the post, repeated

# title is in <header class="search-result-header">

for item in soup.find_all('div', class_="search-result"):
    print('-----------------------------')
    title = item.find_all(class_="search-title")[0].string
 
    score = item.find_all(class_="search-score")[0].string
    time = item.find_all('time')[0].string
    author = item.find_all(class_='author')[0].string
    comments = item.find_all(class_='search-comments')[0].string
    link = item.find_all(class_="search-title")[0]['href']
 

    print(f'Title: {title.strip()}\n\nAuthor: {author.strip()}\nComments: {comments.strip()}\nScore: {score.strip()}\nTime: {time.strip()}\n\nLink: {link}\n')

