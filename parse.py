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
    print(title)
    #print(item)
