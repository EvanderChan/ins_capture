from urllib.request import urlopen
from bs4 import BeautifulSoup
from html.parser import HTMLParser
from urllib.error import HTTPError

def getTilte(url):
  try:
    html = urlopen(url)
  except HTTPError as e:
    return None
  try:
    bsObj = BeautifulSoup(html.read())
    title = bsObj.body.h1
  except AttributeError as e:
    return None
  return title
title = getTilte("https://ithelp.ithome.com.tw/articles/10197374")
if title == None:
  print("Title could not be found")
else:
  print(title)