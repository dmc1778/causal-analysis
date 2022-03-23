from google_play_scraper import app
import os
from serpapi import GoogleSearch

def serp():
    params = {
    "engine": "google_play_product",
    "store": "apps",
    "product_id": "com.netflix.mediaclient",
    "api_key": "fad8b31c6447765918a1517abc88c35ebd46b82f0cece8c298ef1a6b05bd854d"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    product_info = results['product_info']

def main():
    for root, dir, file in os.walk('/media/nimashiri/DATA/vsprojects/causal analysis/apps'):
        for i, item in enumerate(dir):
            try:
                result = app(
                    item,
                    lang='en', 
                    country='us'
                )
                print('I found this app', item)
            except Exception as e:
                print('Could not find', item)

            

if __name__ == '__main__':
    # main()
    serp()


    
