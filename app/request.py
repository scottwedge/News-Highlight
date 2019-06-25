
import urllib.request,json
from .models import Source,Article


# Source = source.Source
 
#  Getting api key
api_key = None
# Getting the news base url
source_base_url = None
article_base_url = None 

def configure_request(app):
	'''
	Function to acquire the api key and base urls
	'''
	global api_key,sources_base_url,article_base_url
	api_key = app.config['NEWS_API_KEY']
	sources_base_url = app.config['NEWS_API_BASE_URL']
	article_base_url = app.config['EVERYTHING_SOURCE_BASE_URL']

def get_sources(category):
  '''
  Function that gets the json response to our url request
  '''
  get_sources_url = sources_base_url.format(category)

  with urrlib.request.urlopen(get_source_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

    sources_results = None

    if get_sources_response['sources']:
      source_results_list = get_sources_response['sources']
      source_results = process_results(source_results_list) 

  return source_results

 
def get_article(source):
  '''
  Function that gets the json response to our url request
  '''
  get_article_url = base_url.format(source,api_key)

  with urrlib.request.urlopen(get_article) as url:
    get_article_data = url.read()
    get_article_response = json.loads(get_article_data)

    article_results = None

    if get_article_response['article']:
      article_results_list = get_article_response['article']
      article_results = process_results(article_results_list) 

  return article_results


def process_article(article_results):
    '''
    Function that processes the article result and transform them to a list of objects
    
    Args:
        article_result: A list of dictionaries that contains article details

    Returns :
        article_list: A list of article objects
    '''
    article_list = []
    for article_item in article_results:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedate')

        if date and author and image:

          article_object = Article(author,title,description,url,image,date)
          article_list.append(article_object)

    return article_list

 
   

