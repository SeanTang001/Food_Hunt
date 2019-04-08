import bs4, os, lxml, requests, urllib2, json, time, sys
from lxml import html
from bs4 import BeautifulSoup

def gather_page(query_string):
    contentz = requests.get("http://www.google.com/search", params={'q': query_string, 'first': 1}, headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'})
    return contentz.content

def test_file(path):
    raw_file = open(path, 'r')
    content = raw_file.read()
    return content

def parser(content):
    searchresults = {}
    page = BeautifulSoup(content,'html.parser')
    for a in page.find_all("div", {"class":"r"}):
        try:
            if not "https" in a.text:
                des, https, url = a.text.partition("www.")       
            else:
                des, https, url = a.text.partition("https://")
            #p0'xprint a.text
            url, cached, nonething = str(https+url).partition("Cached")
            searchresults[url] = des
            print "[+]%s, %s" %(url, des)
        except:
            pass
    #print searchresults
    return searchresults

def seg_generator(searchresults, name):
    print name
    search_fancy = """	
    <div class="card mb-3">
    <div class="card-body">
    <h5 class="card-title">%s</h5>
    <p class="card-text">
    """% name
    search_fancy2 = """
    </p>
    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
    </div>
    """
    html_file = open('templates/links/%s.html'%name, 'w')
    for i in searchresults:
        try:
            html_file.write(search_fancy+"\n<a href = "+i+">"+searchresults[i]+"<br></a>"+search_fancy2+"\n")
        except:
            pass
    html_file.close()
    return ["%s.html"%name]

def pre_search():
    job_list = ["cheap_food_near_me","healthy_food_near_me","healthy_italian_food_near_me","healthy_indian_food_near_me", "health_chinese_food_near_me","cheap_chinese_food_near_me", "cheap_indian_food_near_me", "cheap_japanese_food_near_me", "cheap_italian_food_near_me"]
    for i in job_list:
        seg_generator(parser(gather_page(i)), i)

def live_search(query_string):
    path = seg_generator(parser(gather_page(query_string)), query_string)
    return path


