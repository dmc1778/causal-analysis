import imp
import requests as r
import json
from csv import writer
import requests, os
from datetime import datetime

collections = {
  'APPLICATION': 'APPLICATION',
  'ANDROID_WEAR': 'ANDROID_WEAR',
  'ART_AND_DESIGN': 'ART_AND_DESIGN',
  'AUTO_AND_VEHICLES': 'AUTO_AND_VEHICLES',
  'BEAUTY': 'BEAUTY',
  'BOOKS_AND_REFERENCE': 'BOOKS_AND_REFERENCE',
  'BUSINESS': 'BUSINESS',
  'COMICS': 'COMICS',
  'COMMUNICATION': 'COMMUNICATION',
  'DATING': 'DATING',
  'EDUCATION': 'EDUCATION',
  'ENTERTAINMENT': 'ENTERTAINMENT',
  'EVENTS': 'EVENTS',
  'FINANCE': 'FINANCE',
  'FOOD_AND_DRINK': 'FOOD_AND_DRINK',
  'HEALTH_AND_FITNESS': 'HEALTH_AND_FITNESS',
  'HOUSE_AND_HOME': 'HOUSE_AND_HOME',
  'LIBRARIES_AND_DEMO': 'LIBRARIES_AND_DEMO',
  'LIFESTYLE': 'LIFESTYLE',
  'MAPS_AND_NAVIGATION': 'MAPS_AND_NAVIGATION',
  'MEDICAL': 'MEDICAL',
  'MUSIC_AND_AUDIO': 'MUSIC_AND_AUDIO',
  'NEWS_AND_MAGAZINES': 'NEWS_AND_MAGAZINES',
  'PARENTING': 'PARENTING',
  'PERSONALIZATION': 'PERSONALIZATION',
  'PHOTOGRAPHY': 'PHOTOGRAPHY',
  'PRODUCTIVITY': 'PRODUCTIVITY',
  'SHOPPING': 'SHOPPING',
  'SOCIAL': 'SOCIAL',
  'SPORTS': 'SPORTS',
  'TOOLS': 'TOOLS',
  'TRAVEL_AND_LOCAL': 'TRAVEL_AND_LOCAL',
  'VIDEO_PLAYERS': 'VIDEO_PLAYERS',
  'WATCH_FACE': 'WATCH_FACE',
  'WEATHER': 'WEATHER',
  'GAME': 'GAME',
  'GAME_ACTION': 'GAME_ACTION',
  'GAME_ADVENTURE': 'GAME_ADVENTURE',
  'GAME_ARCADE': 'GAME_ARCADE',
  'GAME_BOARD': 'GAME_BOARD',
  'GAME_CARD': 'GAME_CARD',
  'GAME_CASINO': 'GAME_CASINO',
  'GAME_CASUAL': 'GAME_CASUAL',
  'GAME_EDUCATIONAL': 'GAME_EDUCATIONAL',
  'GAME_MUSIC': 'GAME_MUSIC',
  'GAME_PUZZLE': 'GAME_PUZZLE',
  'GAME_RACING': 'GAME_RACING',
  'GAME_ROLE_PLAYING': 'GAME_ROLE_PLAYING',
  'GAME_SIMULATION': 'GAME_SIMULATION',
  'GAME_SPORTS': 'GAME_SPORTS',
  'GAME_STRATEGY': 'GAME_STRATEGY',
  'GAME_TRIVIA': 'GAME_TRIVIA',
  'GAME_WORD': 'GAME_WORD',
  'FAMILY': 'FAMILY'
}

def scrape(response):
    app_list = []
    response = r.get(response)
    response = json.loads(response.text)
    if len(response['results']) == 0:
        return None
    for app in response['results']:
        app_list.append(app['url'])
    
    with open('all_apps.txt', 'a') as f:
        for row in app_list:
            f.write(row+'\n')

    scrape(response['next'])

def process():
    dt = datetime.now().strftime('%Y-%m-%d')
    headers={
    'Referer': 'https://itunes.apple.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }

    for root, dir, file in os.walk('/media/nimashiri/DATA/vsprojects/causal analysis/apps'):
        j = 0
        for i, item in enumerate(dir):
            link2 = 'http://localhost:3000/api/apps/'+item
            response = r.get(link2, headers=headers)
            if response.status_code == 200:
                response = json.loads(response.text)
                with open('./weekly_data/'+dt+'.csv', 'a', newline='\n') as fd:
                    writer_object = writer(fd)
                    for k, v in response.items():
                        my_data = []
                        if 'recentChanges' in response.keys():
                            my_data.append(response['recentChanges'])
                        if 'released' in response.keys():
                            my_data.append(response['released'])
                        if 'version' in response.keys():
                            my_data.append(response['version'])
                        if 'title' in response.keys():
                            my_data.append(response['title'])
                        if 'description' in response.keys():
                            my_data.append(response['description'])
                        if 'installs' in response.keys():
                            my_data.append(response['installs'])
                        if 'score' in response.keys():
                            my_data.append(response['score'])
                        if 'ratings' in response.keys():
                            my_data.append(response['ratings'])
                        if 'version' in response.keys():
                            my_data.append(response['version'])
                        if 'url' in response.keys():
                            my_data.append(response['url'])
                        if 'released' in response.keys():
                            my_data.append(response['url'])
                                    
                        writer_object.writerow(my_data)



def main():
    headers={
    'Referer': 'https://itunes.apple.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    for key, value in collections.items():
        link2 = 'http://localhost:3000/api/apps/?category='+key+'&fullDetail=true'

# try:
#     page1 = requests.get(ap)
# except requests.exceptions.ConnectionError:
#     r.status_code = "Connection refused"

        try:
            response = r.get(link2, headers=headers)
            response = json.loads(response.text)
            if 'results' in response.keys():
                with open('data.csv', 'a', newline='\n') as fd:
                    writer_object = writer(fd)
                    for res in response['results']:
                        my_data = []
                        if 'title' in res.keys():
                            my_data.append(res['title'])
                        if 'description' in res.keys():
                            my_data.append(res['description'])
                        if 'installs' in res.keys():
                            my_data.append(res['installs'])
                        if 'score' in res.keys():
                            my_data.append(res['score'])
                        if 'ratings' in res.keys():
                            my_data.append(res['ratings'])
                        if 'version' in res.keys():
                            my_data.append(res['version'])
                        if 'url' in res.keys():
                            my_data.append(res['url'])
                        if 'released' in res.keys():
                            my_data.append(res['url'])
                                
                        writer_object.writerow(my_data)

        except requests.exceptions.ConnectionError as e:
            print(e)



if __name__ == '__main__':
    process()
    # main()