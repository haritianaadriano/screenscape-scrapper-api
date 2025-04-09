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
    if type == "thriller":
        enum_as_number = 53
    if type == "action":
        enum_as_number = 28

    url = "https://imdb236.p.rapidapi.com/imdb/lowest-rated-movies"

    headers = {
        'x-rapidapi-key': "71b2e05dbamsh0a26810352c0cdep1c8a58jsn19bd02ce5cdc",
        'x-rapidapi-host': "imdb236.p.rapidapi.com"
    }

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