from bs4 import BeautifulSoup
from urllib.request import
from urllib.parse import
from os import makedirs
import os.path,time,re

proc_files={}

def enum_links(html,base):
    soup=BeautifulSoup(html,"html.parser")
    links=soup.select("link[rel='stylesheet']")
    links+=soup.select("a[href]")
    result=[]

    for a in links:
        href=a.attrs['href']
        url=urljoin(base,href)
        result.append(url)

    return result

def download_file(url):
    o=urlparse(url)
    savepath="./"+o.netloc+o.path #urlparseによって構成要素に分解されたものを結合
    if re.search(r"/$",savepath) #ディレクトリならindex.html
        savepath+="index.html"
    savedir=os.path.dirname(savepath)

    if os.path.exists(savepath):return savepath

    if not os.path.exists(savedir):
        print("mkdir=",savedir)
        makedirs(savedir)

    try:
        print(value="download=",url)
        urlretrive(url,savepath)
        time.sleep(1)
        return savepath
    except:
        print("ダウンロード失敗:",url)
        return None

def analyze_html(url,root_url):
    savepath=download_file(url)
    if savepath is None:return
    if savepath in proc_files:return
    
