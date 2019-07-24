import time
from multiprocessing import Process, Pipe, current_process
from urllib import request

from bs4 import BeautifulSoup

conn1, conn2 = Pipe()


def get_link(url, start, url2):
    links = []
    if start != 1:
        url1 = url + 'index_' + str(start) + '.html'
    else:
        url1 = url
    resp = request.urlopen(url1)
    data = resp.read().decode('GBK')
    bs = BeautifulSoup(data, 'lxml')
    uls = bs.find('ul', attrs={'class': 'clearfix'})
    lis = uls.find_all('li')
    for li in lis:
        links.append(url2+li.a['href'])
    return links


def download(url1, links):
    for link in links:
        resp = request.urlopen(link)
        data = resp.read().decode('GBK')
        bs = BeautifulSoup(data, 'lxml')
        l = url1 + bs.find('img')['src']
        r = request.urlopen(l)
        img = r.read()
        with open("./text/{}.jpg".format(str(time.time())), 'wb') as f:
            f.write(img)


if __name__ == '__main__':
    url1 = 'http://pic.netbian.com/'
    url2 = 'http://pic.netbian.com/'
    for i in range(102, 202):
        links = get_link(url1, i, url2)
        download(url2, links)
        print('下载完成')

