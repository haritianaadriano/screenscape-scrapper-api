import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/movies")
def get_movies(type: str):
    enum_as_number = 0
    if type == "comedie":
        enum_as_number = 35
    if type == "horror":
        enum_as_number = 27
    if type == "family":
        enum_as_number = 10751
    if type == "animation":
        enum_as_number = 16
    if type == "romance":
        enum_as_number = 10749

    url = 'https://www.reccio.com/api/recommend?genre='+str(enum_as_number)+'&movieType=bestOfRecentYears&keyword=&services=netflix,disney,hulu,prime,hbo,apple&country=us'

    headers = {
        'host': 'www.reccio.com'  # The host should not include the protocol (htps://)
    }

    response = requests.get(url, headers=headers)
    
    # Check if the external API call was successful
    if response.status_code == 200:
        # Return the JSON data from the external API
        return JSONResponse(content=response.json())
    else:
        # Return an error message if the external API fails
        return JSONResponse(content={"error": "Failed to fetch data"}, status_code=response.status_code)


@app.get("/movie/trending")
def trending_movie():
    # URL of the API
    url = 'https://www.reccio.com/api/recommend?genre=&movieType=trendingNow&keyword=&services=netflix,disney,hulu,prime,hbo,apple&country=us'
    
    # Headers
    headers = {
        'host': 'www.reccio.com'  # The host should not include the protocol (htps://)
    }
    
    # Make the external API request
    response = requests.get(url, headers=headers)
    
    # Check if the external API call was successful
    if response.status_code == 200:
        # Return the JSON data from the external API
        return JSONResponse(content=response.json())
    else:
        # Return an error message if the external API fails
        return JSONResponse(content={"error": "Failed to fetch data"}, status_code=response.status_code)


@app.get("/ping")
def get_server_health():
    return "pong"