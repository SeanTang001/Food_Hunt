import os, operator

def search(query, para):
    score_board = {}
    if para == "image":
        possible_file = os.listdir("templates/images")
        para = "images"
    else:
        possible_file = os.listdir("templates/links")
        para = "links"
    #print possible_file
    #possible_file = ["cheap_chinese_food_near_me.html", "thai_food_near_me.html", "italian_food_near_me.html", "cheap_indian_food_near_me.html"]
    for temp_file in possible_file:
        score_board[temp_file] = 0
    for temp_file in possible_file:
        for string in query:
            if string in temp_file:
                score_board[temp_file] = score_board[temp_file] + 1
            else:
                pass
    print score_board
    if not any(score_board.itervalues()):
        print"hi"
        return None
    else:
        search_result =  dict(sorted(score_board.iteritems(), key=operator.itemgetter(1), reverse=True)[:2])
        return search_result
def construct(search_result, para):
    temp_file = open("templates/search_results.html", "r")
    base = temp_file.read()    
    temp_file.close()
    for files in search_result:
        content = open("templates/"+para+"/"+files, "r")
        stuff = content.read()
        base = base+stuff
        content.close()
    base = base+"</div>\n</div>\n</body>\n</html>"
    return base

#/var/www/FlaskApp/FlaskApp