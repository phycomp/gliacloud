#!/usr/bin/env python
import re
import urllib
import requests
from requests_html import HTML

def fetch(url):
    response = requests.get(url)
    return response

def parse_article_entries(doc):
    html = HTML(html=doc)
    post_entries = html.find('div.r-ent')
    return post_entries


def parse_article_meta(ent):
    meta = {
        'title': ent.find('div.title', first=True).text,
        'push': ent.find('div.nrec', first=True).text,
        'date': ent.find('div.date', first=True).text,
    }
    try:
        meta['author'] = ent.find('div.author', first=True).text
        meta['link'] = ent.find('div.title > a', first=True).attrs['href']
    except AttributeError:
        if '(本文已被刪除)' in meta['title']:
            match_author = re.search('\[(\w*)\]', meta['title'])
            if match_author:
                meta['author'] = match_author.group(1)
        elif re.search('已被\w*刪除', meta['title']):
            match_author = re.search('\<(\w*)\>', meta['title'])
            if match_author:
                meta['author'] = match_author.group(1)
    return meta

def get_metadata_from(url):
    def parse_next_link(doc):
        ''' Step-4a: parse the link of previous link.
        '''
        html = HTML(html=doc)
        controls = html.find('.action-bar a.btn.wide')
        link = controls[1].attrs.get('href')
        return urllib.parse.urljoin(domain, link)

    resp = fetch(url)
    post_entries = parse_article_entries(resp.text)
    next_link = parse_next_link(resp.text)

    metadata = [parse_article_meta(entry) for entry in post_entries]
    return metadata, next_link
def get_paged_meta(url, num_pages):
    collected_meta = []
    for _ in range(num_pages):
        posts, link = get_metadata_from(url)
        collected_meta += posts
        url = urllib.parse.urljoin(domain, link)
    return collected_meta

def rtrvContent():
    resp = fetch(start_url)
    post_entries = parse_article_entries(resp.text)
    for entry in post_entries:
        meta = parse_article_meta(entry)
        #print(meta)
        print(meta['date'], meta['author'], meta['title'], meta['link'], meta['push'])
        #pretty_print(meta['push'], meta['title'], meta['date'], meta['author'])#日期 作者 標題 內文 看板名稱

domain = 'https://www.ptt.cc/'
start_url = 'https://www.ptt.cc/bbs/movie/index.html'
if __name__ == '__main__':
    rtrvContent()
