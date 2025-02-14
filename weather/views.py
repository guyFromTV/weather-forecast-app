from django.shortcuts import render, redirect
from .models import City  # Importing City model
import requests  # For making API requests
from .forms import CityForm  # Importing CityForm to handle form submissions
from dotenv import load_dotenv
import os

load_dotenv()  # Load the .env file

api_key = os.getenv('API_KEY')  # Retrieve the API key



def delete_city(request, city_name):
    """
    Deletes a city from the database based on its name.
    Redirects back to the city list page after deletion.
    """
    City.objects.filter(name=city_name).delete()  # Deletes the city from the database
    return redirect('list-cities')  # Redirects back to the main page


def index(request):
    """
    Displays the weather information for all saved cities.
    Allows users to add new cities using a form.
    """
    
    # OpenWeatherMap API URL (requires an API key)
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'

    # Handling form submission (Adding a new city)
    if request.method == 'POST':
        form = CityForm(request.POST)  # Create form instance with submitted data
        
        # Check if form is valid and city doesn't already exist
        if form.is_valid() and City.objects.filter(name=form.cleaned_data['name']).count() == 0:
            form.save()  # Save new city to the database

    # Create a new blank form for the template
    form = CityForm()

    # Retrieve all saved cities from the database
    cities = City.objects.all()

    weather_data = []  # List to store weather details for each city

    # Loop through all cities and fetch weather data
    for city in cities:
        response = requests.get(url.format(city, api_key)).json()  # Fetch weather data from API
        
        # Extract relevant weather details
        city_weather = {
            'name': city.name,  # City name
            'temp': response['main']['temp'],  # Temperature in Celsius
            'description': response['weather'][0]['description'].capitalize(),  # Weather description
            'icon': response['weather'][0]['icon'],  # Weather icon ID
        }

        weather_data.append(city_weather)  # Append city weather data to the list

    # Context dictionary to pass data to the template
    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/weather.html', context)  # Render the HTML template
