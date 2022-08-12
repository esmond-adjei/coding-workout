from scrapeTools import *
        

# CODE OCHESTRATION
while True:
    address, movieKeyword = getAddress()
    movieLinksFound, downloadLinks = recursiveScrape(find_tag('a',scrape(address)), movieKeyword.lower())    


    # option to download image
    print('='*50)
    image_option = input("Continue to download movie image? [y/n]\nIf yes, add a search keyword or nothing to use default keyword: ").lower().split()
    if ' '.join(image_option[1:]) == '':
        imgKeyword = movieKeyword
    else: imgKeyword = ' '.join(image_option[1:])
    if image_option[0] == 'y':
        try:
            IMDB(imgKeyword,True,0.7)
        except:
            print("COULD NOT OBTAIN IMAGE FILE")
    imgTag = f'''style="background-image: url('./images/{imgKeyword.replace(' ', '_')}.jpg');"'''


    html_title = f'''<!DOCTYPE html>\n<html lang="en">
<head>\n<meta charset="UTF-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{movieKeyword.capitalize()}</title>\n<link rel="stylesheet" href="../styles.css">
</head>\n<body>\n<section class="movieLinks" style="background-image: url('../images/{movieKeyword.replace(' ', '_')}.jpg');">'''
    
#    save_csv(movieLinksFound)
    if movieLinksFound: #len(movieLinksFound) > len(movieKeyword)+15:
        #saveAs(movieLinksFound,movieKeyword+"(recursive)",'.txt','w')                  # saves ONCE as TXT file
        save_csv(movieLinksFound)

        #ends_with = "</u>\n</section>\n</body>\n</html>"
        #saveAs(html_title,'movie_website/html/'+movieKeyword,'.html','w')       # writing down the html boiler plate first with 'w' to overrite text in file if pressent
        #saveAs(downloadLinks+ends_with,'movie_website/html/'+movieKeyword,'.html')    # saves ONCE as HTML file
        
        #indexHTML_code = f'''\n<a href="./html/{'_'.join(movieKeyword.split())}.html"><div class='box_nav' {imgTag}><h1>{movieKeyword.capitalize()}</h1></div></a>'''
        #saveAs(indexHTML_code,'movie_website/index','.html')                    # main navigation to connect to DOWNLOAD LINK HTML

        directory = "file://c:/users/esmon/desktop/scrapes/movie_website/index.html"
        print("**__SUCCESS__**\nOpen html link: ", directory)
    else:   print("!!__MOVIE LINK SEARCH NOT SUCCESSFUL__!!")

    stop = input("PRESS ENTER TO TRY ANOTHER SEARCH OR 'X' QUIT: ").lower()     # Try another by pressing 'x'
    if stop == 'x': break 