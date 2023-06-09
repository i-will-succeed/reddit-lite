import requests
import sys
from bs4 import BeautifulSoup
import subprocess

reddit_name = sys.argv[1]
reddit_search = sys.argv[2].replace(' ', '+')
reddit_link = f"https://old.reddit.com/r/{reddit_name}/search?q={reddit_search}&restrict_sr=on"



cmd = ['curl', '-s', "-L", '-A',  "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1", reddit_link]

html_file = subprocess.check_output(cmd)
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

