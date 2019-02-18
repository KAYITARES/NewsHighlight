class Config:
    '''
    General configuration parent class
    '''
    NEWZ_API_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-15&sortBy=publishedAt&apiKey=ad1be185a56b4f8290567e6ac2dc92c6'
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
