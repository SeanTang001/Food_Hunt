import bs4, os, sys, requests, json, urllib2
from bs4 import BeautifulSoup

try:
	query = sys.argv[1]
except:
	pass

def google_image_scrap(url, i):
	ActualImages = []
	header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}
	raw_page = urllib2.urlopen(urllib2.Request(url, headers=header))
	page = BeautifulSoup(raw_page,'html.parser')
	for a in page.find_all("div", {"class":"rg_meta"}):
		link= json.loads(a.text)["ou"]
		ActualImages.append(link)
		if i == 30:
			break
		else:
			pass
		i = i+1
	return ActualImages

def download_image(ActualImages, dirs):
        try:
                os.mkdir("static/images/%s" %dirs)
        except:
                pass
        ImagesPaths = []
        for i in ActualImages:
                try:
                        name = "static/images/%s/%s.jpg" %(dirs, ActualImages.index(i))
                        img = urllib2.urlopen(i)
                        img_file = open(name, "w")
                        img_file.write(img.read())
                        img_file.close()
                        ImagesPaths.append(name)
                except:
                        pass
        return ImagesPaths
def seg_generator(images_paths, name):
        name = "templates/images/%s.html"%name
        html_file = open(name, 'w')
        for i in images_paths:
                html_file.write("<img src = "+i+"><br></img>\n")
        html_file.close()
        path = [name]
        return path

#google_image_scrap("https://www.google.com/search?tbm=isch&q="+query)
def live_search(query):
        path = seg_generator(download_image(google_image_scrap("https://www.google.com/search?tbm=isch&q="+query, 0), query), query)
        return path
def pre_search():
        job_list = ["healthy_recipe", "health food", "food_plate", "how_to_fight_deppresion"]
        for query in job_list:
                seg_generator(download_image(google_image_scrap("https://www.google.com/search?tbm=isch&q="+query, 0), query), query)

#pre_search()