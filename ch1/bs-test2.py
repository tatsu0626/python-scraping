from bs4 import BeautifulSoup

html= """
<html><body>
    <h1 id="title">スクレイピングとは？</h1>
    <p id="body">Webページから任意のデータを抽出すること。</p>
</body></html>

"""

soup=BeautifulSoup(html,'html.parser')
#第一引数にはHTMLを指定、第二引数には解析を行うパーサーの種類を指定する。

title=soup.find(id="title")
body=soup.find(id="body")

print("#title="+title.string)
print("#body="+body.string)
