#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)
import requests

from html.parser import HTMLParser
from re import sub
#from htmlentitydefs import name2codepoint
from sys import argv
from os.path import splitext

class demoHTMLParser(HTMLParser):  
    def __init__(self):  
        HTMLParser.__init__(self)  
        self.__text = []  
    def handle_data(self, data):  
        text = data.strip()  
        if len(text) > 0:  
            text = sub('[ \t\r\n]+', ' ', text)  
            self.__text.append(text + ' ')  
    def handle_starttag(self, tag, attrs):  
        if tag == 'p':  self.__text.append('\n\n')  
        elif tag == 'br':  self.__text.append('\n')  
    def handle_startendtag(self, tag, attrs):  
        if tag == 'br':  self.__text.append('\n\n')  
    def text(self):  
        return ''.join(self.__text).strip()  
def fetch(url):
    response = requests.get(url)
    response = requests.get(url, cookies={'over18': '1'})  # 一直向 server 回答滿 18 歲了 !
    return response

@app.route('/')
def hello():
    url='http://wiki.python.org.tw/The%20Zen%20Of%20Python'
    response=fetch(url)
    demoParser=demoHTMLParser()
    demoParser.feed(response.text)
    #print(''.join(myParser.__text).strip())
    #print(myParser.text()+'\n')
    return "<pre>"+demoParser.text()+"</pre>"
    #return "Hello World!"

if __name__ == '__main__':
    app.run()
