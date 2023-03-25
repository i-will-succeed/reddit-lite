from bs4 import BeautifulSoup

html_file = open(r"index.html", 'r').read()

soup = BeautifulSoup(html_file, 'html.parser')

print(soup.prettify())



