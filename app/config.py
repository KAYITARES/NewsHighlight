class Config:
    '''
    General configuration parent class
    '''
    NEWZ_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    pass

class prodConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    ''' 
    DEBUG = True  
