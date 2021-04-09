import requests
from bs4 import BeautifulSoup

r = requests.get('https://pl.tripadvisor.com/Restaurant_Review-g274772-d4044371-Reviews-Greg_Tom_Beer_House_Pub-Krakow_Lesser_Poland_Province_Southern_Poland.html')
#print(r.text) # return page html code
soup = BeautifulSoup(r.text, 'html.parser')

opinion = soup.select('div.reviewSelector')[0]
#print(opinion.get_text) # return content of whole opinion
opinion_id = opinion["data-reviewid"]
#print(opinion_id) # return given opinion's id
author = opinion.select('div.info_text.pointer_cursor')[0].string
#print(author)
#stars = opinion.select("ui_bubble_rating bubble_50::before") # TODO extract stars
#print(stars)
date = opinion.select('span.ratingDate')[0]['title']
#print(date) # get comment date
title = opinion.select('span.noQuotes')[0].string
#print(title)
comment = opinion.select('div.prw_rup.prw_reviews_text_summary_hsx > div > p')[0].text[:-6]
#print(comment)
visit = opinion.select('span.stay_date_label')[0].next_sibling.strip()
#print(visit)
print(opinion_id, author, date, title, comment, visit, sep="\n")
