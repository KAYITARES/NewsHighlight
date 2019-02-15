from app import app
# getting api key
api_key = app.config['NEWZ_API_KEY']
# getting the movie base url
base_url = app.config["NEWZ_API_BASE_URL"]
def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        newz_results = get_news_response
        if get_news_response['results']:
            newz_results_list = get_news_response['results']
            newz_results = process_results(newz_results_list)
            return newz_results