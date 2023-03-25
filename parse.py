from bs4 import BeautifulSoup

html_file = open(r"pretty.html", 'r').read()

soup = BeautifulSoup(html_file, 'html.parser')

print(soup.title.string)



