import requests
import random
import shutil
import bs4
import ssl

#hoge

ssl._create_default_https_context = ssl._create_unverified_context
def image(data):
    Res = requests.get("https://www.bing.com/images/search?q=" + data + "&form=QBLH&sp=-1&pq=" + data + "&sc=8-4&qs=n&cvid=64E35DBFDF524E428033C442654F2E7C&first=1&tsc=ImageHoverTitle")
    Html = Res.text
    Soup = bs4.BeautifulSoup(Html,'lxml')
    links = Soup.find_all('a')
    print(links[0])
    link = random.choice(links).get("href")
    print(str(link))
    return link
def reload(link):
    Res = requests.get("https://www.bing.com" + str(link))
    Html = Res.text
    Soup = bs4.BeautifulSoup(Html,'lxml')
    reloadlinks = Soup.find_all("img")
    reloadlink = reloadlinks[len(reloadlinks)-1].get("src")
    print(str(len(reloadlinks)))
    return reloadlink
def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name+".png", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
def code():
    code = ""
    for i in range(1):
        code += random.choice("a")
    return code

data = "天皇陛下"
link = image(data)
reloadlink = reload(link)
download_img(reloadlink, code())
print("OK")
