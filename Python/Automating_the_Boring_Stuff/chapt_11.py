# Chapter 11
# Web Scrapping

import webbrowser, requests

# webbrowser.open('http://inventwithpython.com/')

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

type(res)

res.status_code == requests.codes.ok

len(res.text)

print(res.text[:251])
