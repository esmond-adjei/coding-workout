from tkinter import N
import bs4, requests, io, csv
from PIL import Image

"""
    1. obtain address
    2. get webpage
    3. compare search key(movie) with link texts
    4. get second webpage from link in related texts from step 3
    5. compare resolution(1080p/720p/480p) with linked texts
    6. get all related links that satisfy step 5 and save in a file.
"""

"""
   a. get to the page -- requests.get(address)  ------->> scrape function
      create a soup  --- bs4.BeautifulSoup(address.text, 'html.parser') 
   b. get all anchor-link-tags or any other tag(eg: 'img')  --- soup.find_all('a')  -----> find_tag
   c. sort links by type |movie |html | arbitrary-keyword   ----->  find_by_keyword 
   d. do what you want with the sorted links::: save as text, scrape, download, print
"""

# INPUT OPERATIONS
def getAddress():
    '''
        1. Take user input (command for movie type and movie title) data from terminal
        2. Gets appropriate address based on command and creates an search query address with the movie title
        3. Returns MOVIE ADDRESS and MOVIE SEARCH KEYWORD.
    '''
    command = input(">> Search movie (start with 's' for series or 'm' for movies): ")
    while command.strip() == "":
        command = input(">> Search movie (start with 's' for series or 'm' for movies): ")
    command.lower()
    
    #making address for LIGHTDLMOVIES
    addressDictionary = {
                            "s":"https://lightdlss.blogspot.com/search?q=", 
                            "m":"https://lightdlmovies.blogspot.com/search?q=",
                            "h": "https://hdmoviesringo.in/?s=",
                            "H":"https://movieshippo.in/?s=",
                        }

    websiteType = command[0]
    movie_query = command[2:]
    movie_keyword = input(">> Specific keyword to help find movie (default: movie name): ")
    if movie_keyword == '': movie_keyword = movie_query
                    
    full_address = addressDictionary[websiteType]+ movie_query.replace(' ','+')   #website address + search    
    print("\nGetting Link...") 

    return full_address, movie_keyword


def scrape(addr):
    """ scrapes and address and returns the response object """
    try:
        print(f"\nSCRAPING.. @ {addr}\n")
        response = requests.get(addr)
        return response
    except Exception:
        print('UNABLE TO EXTABLISH A CONNECTION WITH %s' %addr)
        exit()

# PROCESSING
## FIND KEYS
def find_tag(tag, response):
    """ create a soup object and returns an object of a particular tag """
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return list(soup.find_all(tag))


def find_by_keyword(keyword, list_of_related_links):
    """
       searches through list of links for the link that has the keyword and returns the link
    """
    keyword_list = []
    if not list_of_related_links:
        return print("EMPTY or TYPE NOT LIST WAS PASSED. Type =",type(list_of_related_links))
    else:
        for each_link_tag in list_of_related_links:
            try:
                if keyword in each_link_tag.get("href").lower():
                    keyword_list.append(each_link_tag)
            except:
                pass #f"{keyword}\nNoneType encountered")
    return keyword_list


def find_type(link, extension_type):
    """ checks if a link is of particular type by 
        checking if extension type elements is in link
        eg: link: 'https://google.com/search?q=home.html' extension_type: html = ('.html', '.htm') or video = ('.mp4', '.mkv')
        returns true or false
    """
    for e_type in extension_type:
        if e_type == link[-len(e_type):]:
            return True
    return False


def find_text(keyword, list_of_tags):
    filtered_list = []
    for tag in list_of_tags:
        try:
            if compareLists(keyword.split(),tag.text.lower().split()):
                filtered_list.append(tag)
        except:
            continue
    return filtered_list


def compareLists(lista,listb):
    ''' compares elements of two list and returns TRUE if there is an intercession(common) element between them'''
    counter = 0
    for e in lista:
        for f in listb:
            if e in f:
                counter += 1
            if counter == 2:
                return True
    if counter == 1:
        return True
    else:
        return False

## RECURSIVE SCRAPE ADDRESSES
def recursiveScrape(list_of_links, keyword):
    """
    For each LINK TAG in list of links,
        1. if KEYWORD is in LINK TEXT __(fn: compareList)__ then 
            a. check if LINK TYPE (__fn: __) is MOVIE then 
                - print MOVIE NAME on console
                - add LINK to "list" of FOUND MOVIE LINKS
                - save LINK as TEXT FILE __(fn: saveAs)__ with KEYWORD as filename 
            b. else if LINK type is HTML then
                - scrape the HTML link __(fn: scrape)__
                - carry out 1a on RESPONSE 
        return FOUND MOVIE LINKS
    """
    movieLinksFound, downloadLinks  = '',''
    csv_season_num = ''
    csv_movielink = [] 
    count, count2, season = 1,1,1
    
    if not list_of_links:   print("NoneType NoneType NoneType")
    else:
        for link_tag in list_of_links:
            if compareLists(keyword.split(), link_tag.text.lower().split()):     # compares keyword and text on the site
                link = link_tag.get("href")
                if link[-3:] in ("mkv", "mp4"):
                    movieLink = link.strip()
                    # print(">> Movie Link: ", movieTitle)
                    
                    #if f's0{season}' in link_tag.get("href").lower():           # executed for seaonal movies. It counts the seasons
                     #   movieLinksFound += "\n\t____SEASON {}____\n".format(season)
                      #  csv_season_num += "\nSEASON {}\n".format(season)
                      #  downloadLinks += "</ul>\n\n<ul class='box_link'><h2>{} SEASON {}</h2>\n".format(movieTitle,season)
                       # season += 1
                        #count = 1
                    
                    #movieLinksFound += "{}) {}\n".format(count, movieLink)
                    csv_movielink.append("{}. {}\n".format(count, movieLink)) 
                    downloadLinks += "\t<li><a href=\"{}\">{}. {}</a></li>\n".format(movieLink,count,movieTitle)    # generate list of links
                    count += 1
                elif link[-4:] in ("html",".htm"):                  # usually implemented once:: gateway to page with download links
                    htmlLink = link
                    #print("HTML Link: ",htmlLink)
                    movieTitle = link_tag.text.strip().replace('.',' ')
                    print("MOVIE TITLE: ", movieTitle)
                    #movieLinksFound += "\n\t({})____{}____\n".format(count2,movieTitle)
                    csv_movielink.append('\n{}. {}\n'.format(count2, movieTitle))
                    #downloadLinks += "</ul>\n\n<ul class='box_link'><h2>{}. {}</h2>\n".format(count2,movieTitle)

                    count2 += 1
                    count = 1

                    foundLinks = find_tag('a', scrape(htmlLink))    # rescrape to get to the LINKS
                    if foundLinks:                                  # to ensure that we do not recursiveScrape an empty list
                        continue
                    recursiveScrape(foundLinks,keyword)
    return csv_movielink, 'None' #movieLinksFound, downloadLinks


# OUTPUT
## SAVE TO 
def saveAs(data, filename, extension='.txt', writeType = 'a',path="C:/Users/esmon/Desktop/scrapes/"):
    with open(path+'_'.join(filename.capitalize().split())+extension,writeType) as movieFile:
        movieFile.write(data)


## SAVE TO CSV
def save_csv(data, writeType='w', path="C:/Users/esmon/Desktop/scrapes/"):
    with open(path+'movie database.csv', writeType) as movieFile:
        csv.writer(movieFile).writerow(data)
        print("CSV FILE SAVED")


## GET IMAGE
def IMDB(movieKeyword,compress=False,compression_factor=1):
    """ download image from IMDB.COM and compresses the file"""

    imgAddress = 'https://imdb.com/find?q='+movieKeyword.replace(' ', '+')                                       # create IMDB equivalent address
    imgAddress = 'https://imdb.com'+find_text(movieKeyword, find_tag('a', scrape(imgAddress)))[0].get("href")     # scrape and get first link with KEYWORD in TEXT
    imageLink = 'https://imdb.com'+find_by_keyword('mediaviewer',find_tag('a',scrape(imgAddress)))[0].get("href")   # scrape and select first link with 'mediaviewer' in LINK
    image = find_tag('img', scrape(imageLink))[0].get("src")                                                      # choose image from here
    image = scrape(image).content                                                                               # scrape the image bytes
    image = Image.open(io.BytesIO(image))                                                                  # Next three lines compress the image file
    
    if compress:
        h,w = image.size
        image = image.resize((int(h*compression_factor),int(w*compression_factor)), Image.ANTIALIAS)
    
    savePath = "C:/Users/HP/Desktop/scrapes/movie_website/images/"+movieKeyword.replace(' ','_')+'.jpg'
    image.save(savePath)
    print(f"IMAGE OF {movieKeyword.upper()} SAVED SUCCESSFULLY")


## CREATE HTML