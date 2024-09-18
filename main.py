import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/movie/trending")
def trending_movie():
    # URL of the API
    url = 'https://www.reccio.com/api/recommend?genre=&movieType=trendingNow&keyword=&services=netflix,disney,hulu,prime,hbo&country=nz'
    
    # Headers
    headers = {
        'host': 'www.reccio.com'  # The host should not include the protocol (https://)
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
