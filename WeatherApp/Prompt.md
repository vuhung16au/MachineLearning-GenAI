# User Stories 1 

- Users can add multiple cities to the list.
- Users can remove cities from the list.
- Users can view the weather for all cities in the list.

- By default, the app will show the weather for the user's current location (if able to detected), or show the weather for a default city (Sydney).

- Users can view the weather for a specific city by entering the city name.
- Users can view the weather for a specific city by entering the city name and selecting it from a list of suggestions.

- Use OpenWeather API version 2.5 (free tier) to get the weather data.


- Added cities are saved in local storage (cookies?), so they persist across sessions

- Show the list of cities in a grid layout (max 5 columns but responsive to screen size)

- The page should be responsive and work on mobile devices.
- The page automatically refreshes every 10 minutes to show the latest weather data.

Show more information about the weather, including:

Example:
```
Feels like 4°C. Overcast clouds. Light breeze
 2.6m/s NNE (- Show wind speed and direction)
1007hPa
Humidity: 84%
Dew point: 4°C
Visibility: xx km
```

- Show Hourly forecast
- Show Daily forecast
- Show 7-day forecast

- Show current time and date of the location
- Show weather alerts
- Show sunrise and sunset times
- Show UV index
- Show moon phase
- Show it is day time or night time
- Show air quality index

If any of the above information is not available with OpenWeather API version 2.5, don't show it. 

# User Stories 3

Users can drag/drop cities to reorder them in the list.
Order of cities in the list should be saved in local storage (cookies?) so they persist across sessions.

Show current time of the location
Consider timezone and dayligth savings when display local current time:

For example.

(Today is 20 apr 2025)

If the city is Sydney (GMT+10), then shows
Expected implementation: <div class="date">Sunday, Apr 20 3:05pm (GTM+10)</div>

If the city is Tokyo (GMT+9), then shows 
Expected implementation: <div class="date">Sunday, Apr 20 2:05pm (GTM+9)</div>

# Generate `README.md` file

Finish the `README.md` for this repo. 

README.md covers 

- Short intro about the features of the app
- How to use it 
- Techstack used: HTML, CSS, JS, cookies (no backend so can run on browsers)

Add links to the bottom of the page: 

- https://world-weather-six.vercel.app/
- https://github.com/vuhung16au/MachineLearning-GenAI/tree/main/WeatherApp

