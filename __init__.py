import pickle, os, subprocess, scraper, img_scraper, file_search
from flask import Flask, render_template, request, redirect, Response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/results", methods = ["POST"])
def results():
    query = request.form
    s = dict(query)
    print s
    search_string = ''.join(s["search_string"])
    try:
        parameter = ''.join(s["Parameter"])
    except:
        parameter = "link"
    search_string_list = search_string_list = (parameter+" "+search_string).split()
    if parameter == "image":
        search_result = file_search.search(search_string_list, "image")
        if search_result == None:
            search_result = img_scraper.live_search(search_string+"_healthy")
        para = "images"
    else:
        search_result = file_search.search(search_string_list, "link")
        if search_result == None:
            search_result = scraper.live_search(search_string+"_healthy")
        para = "links"
    search_result_template = file_search.construct(search_result, para)
    return search_result_template

@app.route("/results_default", methods = ["POST"])
def results_default():
    query = request.form
    s = dict(query)
    print s
    Parameter = ''.join(s["Parameter"])
    food_type = ''.join(s["food"])
    search_string_list = (Parameter+" "+food_type).split()
    if Parameter == "Cheap":
        search_result = file_search.search(search_string_list, "link")
    else:
        search_result = file_search.search(search_string_list, "link")
    if search_result == None:
        search_result = scraper.live_search(Parameter+" "+food_type)
    else:
        pass
    search_result_template = file_search.construct(search_result, "links")
    return search_result_template



if __name__ == "__main__":
    app.run(host = "10.10.112.64", port = 8000)