import os
class Config:
  '''
  General configuration parent class
  '''
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=1c2a6cb97eed4fb493836de92b65272d'
  NEWS_API_KEY ='1c2a6cb97eed4fb493836de92b65272d'
  SECRET_KEY = '1234'
  EVERYTHING_SOURCE_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&pageSize={}&apiKey={}'


class ProdConfig(Config):
  '''
  Production configuration child class

  Args:
      Config: The parent configuration class with General configuration settings
  '''
  pass


class DevConfig(Config):
  '''
  Development configuration child class
  
  Args:
      Config: The parent configuration class with General configuration settings
  '''

  DEBUG = True 

config_options = {
'development':DevConfig,
'production':ProdConfig
}  