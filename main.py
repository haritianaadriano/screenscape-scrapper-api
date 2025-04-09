import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/movies")
def get_movies():
    url = "https://streaming-availability.p.rapidapi.com/shows/%7Bid%7D"

    querystring = {"series_granularity":"episode","output_language":"en"}

    headers = {
        "x-rapidapi-key": "71b2e05dbamsh0a26810352c0cdep1c8a58jsn19bd02ce5cdc",
        "x-rapidapi-host": "streaming-availability.p.rapidapi.com"
    }


    response = requests.get(url, headers=headers, params=querystring)
    
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