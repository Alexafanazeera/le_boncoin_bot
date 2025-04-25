import requests
from bs4 import BeautifulSoup
from telegram import Bot
import time
import random
import os

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

LEBONCOIN_URL = 'https://www.leboncoin.fr/recherche?category=10&locations=Cagnes-sur-Mer_06800__43.66243_7.15096_4308_10000&price=min-800&square=30-max&real_estate_type=2&from=rs'

seen_ads = set()
bot = Bot(token=TELEGRAM_TOKEN)

def check_new_ads():
    global seen_ads
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(LEBONCOIN_URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    new_ads = 0

    for ad in soup.select('a[data-qa-id="aditem_container"]'):
        ad_id = ad.get('href')
        ad_url = "https://www.leboncoin.fr" + ad_id

        if ad_id not in seen_ads:
            seen_ads.add(ad_id)
            new_ads += 1
            title = ad.select_one('[data-qa-id="aditem_title"]').text.strip()
            price = ad.select_one('[data-qa-id="aditem_price"]').text.strip()
            message = f"NOUVELLE ANNONCE\n{title}\nPrix: {price}\n{ad_url}"
            bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

    print(f"Checked. {new_ads} new ad(s) found.")

print("Bot is running with randomized intervals...")
while True:
    try:
        check_new_ads()
    except Exception as e:
        print(f"Error: {e}")
    
    delay = random.randint(300, 900)
    print(f"Sleeping for {delay} seconds...")
    time.sleep(delay)
