from bs4 import BeautifulSoup

html_file = open(r"pretty.html", 'r').read()

soup = BeautifulSoup(html_file, 'html.parser')

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
 

    print(f'Title: {title.strip()}\n\nAuthor: {author.strip()}\n\nComments: {comments.strip()}\n\nScore: {score.strip()}\n\nTime: {time.strip()}\n\nLink: {link}\n\n')


