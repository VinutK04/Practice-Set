from GoogleNews import GoogleNews

# Create a GoogleNews object.
google_news = GoogleNews()

# Fetch local news.
# Refere functions here
# https://pypi.org/project/GoogleNews/


local_news = google_news.search('local news in Hubli')
local_news = google_news.get_page(1)
local_news = google_news.result()


# Get results will return the list, 
# [{'title': '...', 'media': '...', 'date': '...', 'datetime': '...', 'desc': '...', 'link': '...', 'img': '...'}]

if local_news is not None:
  for article in local_news:
    print(article['title'])
else:
  print('No local news articles found.')
