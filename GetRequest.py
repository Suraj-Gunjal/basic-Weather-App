import requests

def get_whether_data(city_name):
    api_key = "795f914e3e2efac16657a4aeeff9fcaf"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    
    response = requests.get(base_url, params=params)
    if(response.status_code == 200):
        return response.json()
    else:
        return None
    
    
    
    
