from bs4 import BeautifulSoup

html="""
<html><body>
    <h1>スクレイピングとは？</h1>
    <p>Webページを解析すること。</p>
    <p>任意の箇所を抽出すること</p>
</body></html>
"""

soup=BeautifulSoup(html,'html.parser')
#第一引数にはHTMLを指定、第二引数には解析を行うパーサーの種類を指定する。

h1=soup.html.body.h1
p1=soup.html.body.p
p2=p1.next_sibling.next_sibling

print("h1="+h1.string)
print("p="+p1.string)
print("p="+p2.string)
