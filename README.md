# Weather App

![App Screenshot](https://drive.google.com/uc?export=view&id=1p_IFB35gSUTuBVjpC_KSgkITEEhhheSg)

This is a weather application built with Django that allows users to add cities and view their current weather information. The weather data is fetched from the OpenWeatherMap API.

## Features

- Add cities to view their current weather.
- Display weather information including temperature, description, and weather icon.
- Delete cities from the list.

## Technologies Used

- Django
- Python
- HTML
- Bulma (CSS framework)
- OpenWeatherMap API

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt

4. **Set up environment variables:**

    - Create a .env file in the project root directory.
    - Add your OpenWeatherMap API key to the .env file:

    ```bash
    API_KEY=your_openweathermap_api_key

5. **Run database migrations:**

    ```bash
    python manage.py migrate

6. **Start the development server:**

    ```bash
    python manage.py runserver

7. **Access the application:**

    Open your web browser and go to http://127.0.0.1:8000/.

## Project Structure

- `views.py`: Contains the view functions for handling requests and rendering templates.
- `models.py`: Defines the City model for storing city names in the database.
- `forms.py`: Contains the CityForm for handling form submissions.
- `templates/weather/weather.html`: The main HTML template for displaying the weather information.
- `.env`: File to store environment variables, including the OpenWeatherMap API key.

## Usage

- ### Add a City:

    - Enter the name of the city in the input field and click "Add City".
    - The weather information for the city will be displayed.

- ### Delete a City:

    - Click the red "✖" button next to the city you want to delete.
    - The city will be removed from the list.

## Acknowledgements

I would like to express my gratitude to OpenWeatherMap for providing the weather data API used in this project.
Here is their site: https://openweathermap.org/api

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.