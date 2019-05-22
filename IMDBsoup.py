#! Python3
# This program scrapes IMDB for tv show data eg. title, episode number, rating, number of votes
# and displays the data in a pretty fashion

import os,requests,bs4,pprint,json,time

def get_season_info(imdb_url_season):
    
    sauce = requests.get(imdb_url_season)
    sauce.raise_for_status()
    html_soup = bs4.BeautifulSoup(sauce.text,'html.parser')
    type(html_soup)
    episode_containers_odd = html_soup.find_all('div',class_ = 'list_item odd')
    episode_containers_even = html_soup.find_all('div',class_ = 'list_item even')
    episode_containers = []
    for n in range(len(episode_containers_odd)):
        episode_containers.append(episode_containers_odd[n])
        try:
            episode_containers.append(episode_containers_even[n])
        except:
            pass
##    start = int(len(episode_containers)/2)
##    start = start - 1
##    for x in range(len(episode_containers)):            #Fixes the [1,3,5,2,4,6] order of the imported containers
##        if x % 2 != 0:  
##            episode_containers.insert(x, episode_containers[start+x])

    tv_dict = {}
    length = len(episode_containers)
    for n in range(len(episode_containers)):
            _ep = episode_containers[n]
            _title = _ep.strong.text
            try:
                _rating = _ep.find('span',class_ = 'ipl-rating-star__rating').text
                _votes = _ep.find('span',class_ = 'ipl-rating-star__total-votes').text
            except:
                _rating = 0
                _votes = 0
            _number = _ep.find('meta',attrs = {'itemprop':'episodeNumber'})
            _number = _number['content']
            tv_dict_ep = {'episode '+_number:{ 'title':_title,'rating':_rating,'votes':_votes}}
            tv_dict = {**tv_dict,**tv_dict_ep}

    return tv_dict

#tv_dict = literal_eval(pprint.pformat(tv_dict))

def pretty_dict(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty_dict(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

def get_dict_vals(dictionary,key):
    vals = []
    for _key,_value in dictionary.items():
        if _key == key:
            vals.append(_value)
        elif type(_value) == dict:
            dictInsideDict = _value
            check = get_dict_vals(dictInsideDict,key)
            if type(check) != None:
                vals.append(check)
    if len(vals) == 1:
        return vals[0]
    else:
        return vals

def get_avg(listOfNums):
    listOfNums = list(map(float, listOfNums))
    return round(sum(listOfNums)/len(listOfNums),2)
            
def get_show_info(imdb_url_show):
    sauce = requests.get(imdb_url_show)
    sauce.raise_for_status()
    html_soup = bs4.BeautifulSoup(sauce.text,'html.parser')
    type(html_soup)
    seasons_container = html_soup.find(class_ = 'seasons-and-year-nav')
    num_seasons = int(seasons_container.a.text)
##    for a in seasons_container.find_all('a',href=True):
##        print("Found the URL:", a['href'])
##
    show_dict = {}
    season_ratings_dict = {}
    for n in range(num_seasons):
        cur_season_dict = get_season_info(imdb_url_show + 'episodes?season=' + str(n+1))
        cur_show_dict = {'Season ' + str(n+1):cur_season_dict}
        show_dict = {**show_dict,**cur_show_dict}
        ratings = get_dict_vals(cur_season_dict,'rating')
        for rating in ratings:
            if rating == 0:
                ratings.remove(0)
        season_ratings_dict.update({'Season ' + str(n+1) + ' avg rating' : str(get_avg(ratings))})
    show_dict.update(season_ratings_dict)
    return season_ratings_dict      ##changed from show_dict
    
#tv_dict = get_season_info('https://www.imdb.com/title/tt1865718/episodes?season=2')

#ratings = get_dict_vals(tv_dict,'rating')

print("Paste the imdb url of the TV Show you'd like to receive info about.")
print("The following url format is accepted: https://www.imdb.com/title/ttxxxxxxx/")
url = str(input())
print("Loading data...")
show_dict = get_show_info(url)

pretty_dict(show_dict)

#pretty_dict(tv_dict)
#tv_dict.update({'average rating':str(get_avg(ratings))})
