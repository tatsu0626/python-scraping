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
    proc_files[savepath]=True
    print("analyze_html=",url)
    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_links(html, url)
    for link_url in links:
        # リンクがルート以外のパスを指していたら無視 --- (※11)
        if link_url.find(root_url) != 0:
            if not re.search(r".css$", link_url): continue
        # HTMLか？
        if re.search(r".(html|htm)$", link_url):
            # 再帰的にHTMLファイルを解析
            analize_html(link_url, root_url)
            continue
        # それ以外のファイル
        download_file(link_url)

if __name__ == "__main__":
    # URLを丸ごとダウンロード --- (※13)
    url = "https://docs.python.jp/3.6/library/"
    analize_html(url, url)
