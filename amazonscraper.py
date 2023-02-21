from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()

url = 'https://www.amazon.co.uk/s?k=google+pixel&crid=28OSWIE2MSM63&sprefix=google+pixe%2Caps%2C224&ref=nb_sb_noss_2'


def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup


def getnextpage(soup):
    pages = soup.find('span', {'class': 's-pagination-strip'})
    if not pages.find('span', {'class': 's-pagination-item s-pagination-next s-pagination-disabled '}):
        data = pages.find('a', {
                          'class': 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator'})
        second = data['href']
        url = f'https://www.amazon.co.uk{second}'
        return url
    else:
        return


while True:
    try:
        data = getdata(url)
        url = getnextpage(data)
        print(url)
    except:
        pass
        break
