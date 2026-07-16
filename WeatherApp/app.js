document.addEventListener("DOMContentLoaded", () => {
  const search = document.querySelector(".search-input");
  const searchBtn = document.querySelector(".search-btn");
  const suggestionsContainer = document.querySelector(".suggestions");
  const citiesContainer = document.querySelector(".cities-container");
  
  const API_KEY = (window.WEATHER_CONFIG && window.WEATHER_CONFIG.API_KEY) || '';
  const DEFAULT_CITY = "Sydney";
  const REFRESH_INTERVAL = 10 * 60 * 1000; // 10 minutes in milliseconds
  
  let cities = [];
  
  // Load cities from local storage
  const loadCities = () => {
    const savedCities = localStorage.getItem('weatherCities');
    if (savedCities) {
      cities = JSON.parse(savedCities);
    }
  };
  
  // Save cities to local storage
  const saveCities = () => {
    localStorage.setItem('weatherCities', JSON.stringify(cities));
  };
  
  // Get user's current location
  const getCurrentLocation = () => {
    return new Promise((resolve, reject) => {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            resolve({
              lat: position.coords.latitude,
              lon: position.coords.longitude
            });
          },
          (error) => {
            console.warn("Geolocation error:", error);
            reject(error);
          }
        );
      } else {
        console.warn("Geolocation is not supported by this browser");
        reject(new Error("Geolocation not supported"));
      }
    });
  };
  
  // Get weather data for a city - Update to use free API endpoints
  const getWeatherByCity = async (city) => {
    try {
      // First get coordinates from city name
      const geoURL = `https://api.openweathermap.org/geo/1.0/direct?q=${city}&limit=1&appid=${API_KEY}`;
      const geoResponse = await fetch(geoURL);
      const geoData = await geoResponse.json();
      
      if (!geoData.length) {
        throw new Error(`City not found: ${city}`);
      }
      
      const { lat, lon } = geoData[0];
      
      // Get current weather data (free tier)
      const currentURL = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
      const currentResponse = await fetch(currentURL);
      
      if (!currentResponse.ok) {
        throw new Error(`Weather data not available for: ${city}`);
      }
      
      const currentData = await currentResponse.json();
      
      // Get 5-day forecast data (free tier)
      const forecastURL = `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
      const forecastResponse = await fetch(forecastURL);
      
      if (!forecastResponse.ok) {
        throw new Error(`Forecast data not available for: ${city}`);
      }
      
      const forecastData = await forecastResponse.json();
      
      // Get air quality data
      const aqiURL = `https://api.openweathermap.org/data/2.5/air_pollution?lat=${lat}&lon=${lon}&appid=${API_KEY}`;
      const aqiResponse = await fetch(aqiURL);
      const aqiData = await aqiResponse.json();
      
      // Combine the data
      return {
        ...currentData,
        forecast: forecastData,
        airQuality: aqiData,
        cityName: geoData[0].name,
        country: geoData[0].country
      };
    } catch (error) {
      console.error("Error fetching weather data:", error);
      return null;
    }
  };
  
  // Get weather data by coordinates - Update to use free API endpoints
  const getWeatherByCoords = async (lat, lon) => {
    try {
      // Get basic current weather
      const currentURL = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
      const currentResponse = await fetch(currentURL);
      
      if (!currentResponse.ok) {
        throw new Error(`Current weather data not available for coordinates: ${lat}, ${lon}`);
      }
      
      const currentData = await currentResponse.json();
      
      // Get 5-day forecast data (free tier)
      const forecastURL = `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
      const forecastResponse = await fetch(forecastURL);
      
      if (!forecastResponse.ok) {
        throw new Error(`Forecast data not available for coordinates: ${lat}, ${lon}`);
      }
      
      const forecastData = await forecastResponse.json();
      
      // Get air quality data
      const aqiURL = `https://api.openweathermap.org/data/2.5/air_pollution?lat=${lat}&lon=${lon}&appid=${API_KEY}`;
      const aqiResponse = await fetch(aqiURL);
      
      if (!aqiResponse.ok) {
        throw new Error(`Air quality data not available for coordinates: ${lat}, ${lon}`);
      }
      
      const aqiData = await aqiResponse.json();
      
      return {
        ...currentData,
        forecast: forecastData,
        airQuality: aqiData
      };
    } catch (error) {
      console.error("Error fetching weather data:", error);
      return null;
    }
  };
  
  // Format time from timestamp
  const formatTime = (timestamp, timezone) => {
    return new Date((timestamp + timezone) * 1000).toLocaleTimeString('en-US', { 
      hour: '2-digit', 
      minute: '2-digit',
      hour12: true,
      timeZone: 'UTC'
    });
  };
  
  // Format date from timestamp
  const formatDate = (timestamp, timezone) => {
    // Get the formatted date and time
    const formattedDateTime = new Date((timestamp + timezone) * 1000).toLocaleDateString('en-US', { 
      weekday: 'long',
      month: 'short', 
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      hour12: true,
      timeZone: 'UTC'
    });
    
    // Calculate GMT offset in hours from timezone seconds
    const offsetHours = timezone / 3600;
    const offsetSign = offsetHours >= 0 ? '+' : '-';
    const offsetAbsHours = Math.abs(offsetHours);
    
    // Format the GMT offset string
    const gmtOffset = `(GMT${offsetSign}${offsetAbsHours})`;
    
    // Combine the date/time with the GMT offset
    return `${formattedDateTime} ${gmtOffset}`;
  };
  
  // Get wind direction as text
  const getWindDirection = (degrees) => {
    const directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'];
    const index = Math.round(degrees / 22.5) % 16;
    return directions[index];
  };
  
  // Convert AQI to descriptive text
  const getAQIDescription = (aqi) => {
    const descriptions = ['Good', 'Fair', 'Moderate', 'Poor', 'Very Poor'];
    return descriptions[aqi - 1] || 'Unknown';
  };
  
  // Get UV index description
  const getUVDescription = (uvi) => {
    if (uvi <= 2) return 'Low';
    if (uvi <= 5) return 'Moderate';
    if (uvi <= 7) return 'High';
    if (uvi <= 10) return 'Very High';
    return 'Extreme';
  };
  
  // Simple throttle function to limit event frequency
  const throttle = (func, limit) => {
    let inThrottle;
    return function() {
      const args = arguments;
      const context = this;
      if (!inThrottle) {
        func.apply(context, args);
        inThrottle = true;
        setTimeout(() => inThrottle = false, limit);
      }
    };
  };
  
  // Create lighter placeholder for drag operations
  const createDragPlaceholder = (originalCard) => {
    const placeholder = document.createElement('div');
    placeholder.className = 'card-placeholder';
    placeholder.style.width = `${originalCard.offsetWidth}px`;
    placeholder.style.height = `${originalCard.offsetHeight}px`;
    placeholder.style.margin = getComputedStyle(originalCard).margin;
    
    // Add minimal content for size reference
    const header = document.createElement('div');
    header.className = 'placeholder-header';
    header.textContent = originalCard.querySelector('.city-name').textContent;
    placeholder.appendChild(header);
    
    return placeholder;
  };
  
  // HTML-escape values from API responses before injecting into DOM
  const escapeHtml = (str) => {
    const div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
  };

  // Create HTML for a weather card
  const createWeatherCard = (data, isNewCity = false) => {
    const card = document.createElement('div');
    card.className = 'card';
    // Remove unnecessary id attribute to reduce DOM size
    
    // Apply hardware acceleration
    card.style.transform = 'translateZ(0)';
    card.style.willChange = 'transform';
    
    // Make card draggable if it's a saved city
    if (!isNewCity) {
      card.draggable = true;
      // Make sure to use a consistent city name for the data-city attribute
      const cityName = data.cityName || data.name;
      card.setAttribute('data-city', cityName);
      console.log('Setting data-city attribute:', cityName);
      
      // Add drag event listeners with throttling for better performance
      card.addEventListener('dragstart', handleDragStart);
      card.addEventListener('dragover', throttle(handleDragOver, 30));
      card.addEventListener('dragenter', handleDragEnter);
      card.addEventListener('dragleave', handleDragLeave);
      card.addEventListener('drop', handleDrop);
      card.addEventListener('dragend', handleDragEnd);
    }
    
    // Current weather data
    const current = data;
    const isDay = current.dt > data.sys.sunrise && current.dt < data.sys.sunset;
    const timeString = formatTime(current.dt, current.timezone);
    const dateString = formatDate(current.dt, current.timezone);
    const sunrise = formatTime(data.sys.sunrise, current.timezone);
    const sunset = formatTime(data.sys.sunset, current.timezone);
    const windDir = getWindDirection(current.wind.deg);
    const feelsLike = Math.round(current.main.feels_like);
    const visibility = (current.visibility / 1000).toFixed(1);
    const dewPoint = Math.round(current.main.temp - ((100 - current.main.humidity) / 5)); // Approximate dew point
    const uvi = data.airQuality?.list[0]?.main?.aqi || 0; // Fallback for UV index since it's not in free API
    const uviDesc = getUVDescription(uvi);
    const aqi = data.airQuality?.list[0]?.main?.aqi || 0;
    const aqiDesc = getAQIDescription(aqi);

    const safeCityName = escapeHtml(data.cityName || data.name);
    const safeCountry = escapeHtml(data.country || data.sys.country);
    const safeDescription = escapeHtml(current.weather[0].description);

    // Use template literals for better readability and performance
    card.innerHTML = `
      <div class="card-actions">
        ${isNewCity ? '<button class="add-city-btn"><i class="fas fa-plus"></i></button>' : 
                     '<button class="remove-city-btn"><i class="fas fa-times"></i></button>'}
      </div>
      <div class="card-header ${isDay ? 'day' : 'night'}">
        <div class="date-time">
          <div class="time">${timeString}</div>
          <div class="date">${dateString}</div>
        </div>
        <h2 class="city-name">${safeCityName}, ${safeCountry}</h2>
      </div>
      
      <div class="main-weather">
        <div class="temp-content">
          <div class="img-card">
            <img src="https://openweathermap.org/img/wn/${current.weather[0].icon}@2x.png" alt="Weather icon">
          </div>
          <div class="temp-details">
            <h2 class="temp">${Math.round(current.main.temp)}°C</h2>
            <div class="feels-like">Feels like ${feelsLike}°C</div>
            <div class="weather-desc">${safeDescription}</div>
          </div>
        </div>
        
        <div class="weather-details">
          <div class="detail-item">
            <i class="fas fa-wind"></i>
            <span>${current.wind.speed} m/s ${windDir}</span>
          </div>
          <div class="detail-item">
            <i class="fas fa-tint"></i>
            <span>${current.main.humidity}% Humidity</span>
          </div>
          <div class="detail-item">
            <i class="fas fa-compress-alt"></i>
            <span>${current.main.pressure} hPa</span>
          </div>
          <div class="detail-item">
            <i class="fas fa-temperature-low"></i>
            <span>Dew point: ${dewPoint}°C</span>
          </div>
          <div class="detail-item">
            <i class="fas fa-eye"></i>
            <span>Visibility: ${visibility} km</span>
          </div>
          <div class="detail-item">
            <i class="fas fa-sun"></i>
            <span>UV: ${uvi} (${uviDesc})</span>
          </div>
          <div class="detail-item">
            <i class="fas fa-lungs"></i>
            <span>Air Quality: ${aqiDesc}</span>
          </div>
        </div>
        
        <div class="sun-times">
          <div class="sunrise">
            <i class="fas fa-sun"></i>
            <span>Sunrise: ${sunrise}</span>
          </div>
          <div class="sunset">
            <i class="fas fa-moon"></i>
            <span>Sunset: ${sunset}</span>
          </div>
        </div>
      </div>
      
      <div class="forecast">
        <div class="forecast-tabs">
          <button class="tab-btn active" data-tab="hourly">Hourly</button>
          <button class="tab-btn" data-tab="daily">5-Day</button>
        </div>
        
        <div class="forecast-content">
          <div class="hourly-forecast tab-content active">
            ${createHourlyForecast(data.forecast.list.slice(0, 8), data.timezone)}
          </div>
          <div class="daily-forecast tab-content">
            ${createDailyForecast(data.forecast.list, data.timezone)}
          </div>
        </div>
      </div>
    `;
    
    // Add event listeners for add/remove buttons
    if (isNewCity) {
      card.querySelector('.add-city-btn').addEventListener('click', () => {
        addCity(data.cityName || data.name);
      });
    } else {
      card.querySelector('.remove-city-btn').addEventListener('click', () => {
        removeCity(data.cityName || data.name);
      });
    }
    
    // Use delegated event handler for tabs to reduce event listeners
    const tabContainer = card.querySelector('.forecast-tabs');
    tabContainer.addEventListener('click', (e) => {
      if (e.target.classList.contains('tab-btn')) {
        // Remove active class from all tabs
        card.querySelectorAll('.tab-btn').forEach(tab => tab.classList.remove('active'));
        // Add active class to clicked tab
        e.target.classList.add('active');
        
        // Hide all tab content
        card.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
        // Show content for selected tab
        const tabName = e.target.getAttribute('data-tab');
        card.querySelector(`.${tabName}-forecast`).classList.add('active');
      }
    });
    
    return card;
  };
  
  // Create hourly forecast HTML
  const createHourlyForecast = (hourlyData, timezone) => {
    // Display next few hours
    return hourlyData.map(hour => {
      const time = formatTime(hour.dt, timezone);
      return `
        <div class="forecast-item">
          <div class="forecast-time">${time}</div>
          <img src="https://openweathermap.org/img/wn/${hour.weather[0].icon}.png" alt="Weather icon">
          <div class="forecast-temp">${Math.round(hour.main.temp)}°C</div>
        </div>
      `;
    }).join('');
  };
  
  // Create daily forecast HTML
  const createDailyForecast = (forecastData, timezone) => {
    // Group forecast data by day
    const dailyData = {};
    
    forecastData.forEach(item => {
      const date = new Date(item.dt * 1000).toLocaleDateString('en-US', {
        timeZone: 'UTC',
        day: 'numeric',
        month: 'numeric'
      });
      
      if (!dailyData[date]) {
        dailyData[date] = {
          dt: item.dt,
          temps: [],
          icon: item.weather[0].icon
        };
      }
      
      dailyData[date].temps.push(item.main.temp);
    });
    
    // Create HTML for each day
    return Object.values(dailyData).slice(0, 5).map(day => {
      const date = formatDate(day.dt, timezone).split(',')[0]; // Just get the day name
      const maxTemp = Math.round(Math.max(...day.temps));
      const minTemp = Math.round(Math.min(...day.temps));
      
      return `
        <div class="forecast-item">
          <div class="forecast-day">${date}</div>
          <img src="https://openweathermap.org/img/wn/${day.icon}.png" alt="Weather icon">
          <div class="forecast-temp-range">${maxTemp}° / ${minTemp}°</div>
        </div>
      `;
    }).join('');
  };
  
  // Add a city to the list
  const addCity = (cityName) => {
    if (!cities.includes(cityName)) {
      cities.push(cityName);
      saveCities();
      refreshWeather();
    }
  };
  
  // Remove a city from the list
  const removeCity = (cityName) => {
    cities = cities.filter(city => city !== cityName);
    saveCities();
    refreshWeather();
  };
  
  // Optimized weather refresh function with batched updates
  const refreshWeather = async () => {
    // Create a document fragment to batch DOM updates
    const fragment = document.createDocumentFragment();
    const loadingIndicator = document.createElement('div');
    loadingIndicator.className = 'loading-indicator';
    loadingIndicator.textContent = 'Loading weather data...';
    
    // Show loading indicator only if there are cities
    if (cities.length > 0) {
      citiesContainer.innerHTML = '';
      citiesContainer.appendChild(loadingIndicator);
    }
    
    // Fetch all weather data in parallel
    const weatherPromises = cities.map(city => getWeatherByCity(city));
    const weatherResults = await Promise.all(weatherPromises);
    
    // Process results and create cards
    weatherResults.forEach(data => {
      if (data) {
        const card = createWeatherCard(data);
        fragment.appendChild(card);
      }
    });
    
    // Batch update the DOM
    citiesContainer.innerHTML = '';
    citiesContainer.appendChild(fragment);
  };
  
  // Initialize the app
  const initApp = async () => {
    loadCities();
    
    try {
      // Try to get user's location
      const coords = await getCurrentLocation();
      const data = await getWeatherByCoords(coords.lat, coords.lon);
      
      if (data) {
        // Add user's current location if not already in the list
        if (!cities.includes(data.name)) {
          cities.push(data.name);
          saveCities();
        }
      }
    } catch (error) {
      console.log("Could not get current location, using default city");
      
      // Use default city if no cities are saved
      if (cities.length === 0) {
        cities.push(DEFAULT_CITY);
        saveCities();
      }
    }
    
    // Display weather for all cities
    await refreshWeather();
    
    // Set up auto-refresh
    setInterval(refreshWeather, REFRESH_INTERVAL);
  };
  
  // Search for a city
  const searchCity = async () => {
    const cityName = search.value.trim();
    if (cityName) {
      const data = await getWeatherByCity(cityName);
      if (data) {
        // Show the weather card with add button
        citiesContainer.innerHTML = ''; // Clear existing cards
        const card = createWeatherCard(data, true);
        citiesContainer.appendChild(card);
        
        // After showing the searched city, also show all saved cities
        for (const city of cities) {
          if (city.toLowerCase() !== cityName.toLowerCase()) {
            const cityData = await getWeatherByCity(city);
            if (cityData) {
              const cityCard = createWeatherCard(cityData);
              citiesContainer.appendChild(cityCard);
            }
          }
        }
      } else {
        alert("City not found. Please try again.");
      }
    }
  };
  
  // Get city suggestions
  const getCitySuggestions = async (query) => {
    if (query.length < 3) {
      suggestionsContainer.innerHTML = '';
      return;
    }
    
    try {
      const response = await fetch(`https://api.openweathermap.org/geo/1.0/direct?q=${query}&limit=5&appid=${API_KEY}`);
      const data = await response.json();
      
      suggestionsContainer.innerHTML = '';
      
      if (data.length > 0) {
        suggestionsContainer.style.display = 'block';
        data.forEach(city => {
          const suggestion = document.createElement('div');
          suggestion.className = 'suggestion';
          suggestion.textContent = `${city.name}, ${city.country}`;
          suggestion.addEventListener('click', () => {
            search.value = city.name;
            suggestionsContainer.style.display = 'none';
            searchCity();
          });
          suggestionsContainer.appendChild(suggestion);
        });
      } else {
        suggestionsContainer.style.display = 'none';
      }
    } catch (error) {
      console.error("Error fetching suggestions:", error);
    }
  };
  
  // Improved drag and drop handlers
  let draggedCard = null;
  let placeholder = null;
  
  function handleDragStart(e) {
    draggedCard = this;
    // Set data for Firefox compatibility
    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('text/plain', this.getAttribute('data-city'));
    
    // Create a placeholder that's visually simpler than the full card
    placeholder = createDragPlaceholder(this);
    
    // Add a class for styling, but wait for next frame to avoid immediate visibility issues
    requestAnimationFrame(() => {
      this.classList.add('dragging');
      this.style.opacity = '0.6';
    });
     
    // Set view transition name for smooth animations (browser support varies)
    this.style.viewTransitionName = 'dragged-card';
    console.log('Drag started with city:', this.getAttribute('data-city'));
  }
  
  function handleDragOver(e) {
    if (e.preventDefault) {
      e.preventDefault(); // Necessary to allow dropping
    }
    e.dataTransfer.dropEffect = 'move';
    return false;
  }
  
  function handleDragEnter(e) {
    // Only add the class if this is not the dragged card
    if (this !== draggedCard) {
      // Use requestAnimationFrame to batch visual updates
      requestAnimationFrame(() => {
        this.classList.add('drag-over');
      });
    }
  }
  
  function handleDragLeave(e) {
    requestAnimationFrame(() => {
      this.classList.remove('drag-over');
    });
  }
  
  function handleDrop(e) {
    e.stopPropagation(); // Stops browser from redirecting
    e.preventDefault();
    
    this.classList.remove('drag-over');
    
    // Don't do anything if dropping on the same card
    if (draggedCard && draggedCard !== this) {
      // Get the city names for reordering
      const fromCity = draggedCard.getAttribute('data-city');
      const toCity = this.getAttribute('data-city');
      
      console.log('Reordering card:', fromCity, 'to', toCity);
      
      // Reorder cities array and update DOM
      reorderCities(fromCity, toCity);
    }
    
    return false;
  }
  
  function handleDragEnd(e) {
    // Reset card appearance using requestAnimationFrame for better performance
    requestAnimationFrame(() => {
      if (draggedCard) {
        draggedCard.style.opacity = '1';
        draggedCard.classList.remove('dragging');
        
        // Remove drag-over class from all cards
        document.querySelectorAll('.card').forEach(card => {
          card.classList.remove('drag-over');
        });
        
        // Remove view transition name
        draggedCard.style.viewTransitionName = '';
        
        // Remove placeholder if it was added to the DOM
        if (placeholder && placeholder.parentNode) {
          placeholder.parentNode.removeChild(placeholder);
        }
        
        console.log('Drag ended');
        placeholder = null;
        draggedCard = null;
      }
    });
  }
  
  // Optimized reorder cities function that updates DOM without refetching data
  function reorderCities(fromCity, toCity) {
    // Find indices
    const fromIndex = cities.indexOf(fromCity);
    const toIndex = cities.indexOf(toCity);
    
    if (fromIndex !== -1 && toIndex !== -1) {
      // Remove the city from its current position
      cities.splice(fromIndex, 1);
      
      // Insert it at the new position
      cities.splice(toIndex, 0, fromCity);
      
      // Save the new order to local storage
      saveCities();
      
      // Directly rearrange DOM elements instead of refreshing all weather data
      const cards = Array.from(document.querySelectorAll('.card[data-city]'));
      const draggedCardElement = cards.find(card => card.getAttribute('data-city') === fromCity);
      const targetCardElement = cards.find(card => card.getAttribute('data-city') === toCity);
      
      if (draggedCardElement && targetCardElement) {
        // Insert the dragged card before or after the target card based on indices
        if (fromIndex < toIndex) {
          // Moving down - insert after
          targetCardElement.parentNode.insertBefore(draggedCardElement, targetCardElement.nextSibling);
        } else {
          // Moving up - insert before
          targetCardElement.parentNode.insertBefore(draggedCardElement, targetCardElement);
        }
        
        // Add a subtle animation to show the card has been moved
        draggedCardElement.classList.add('card-moved');
        setTimeout(() => {
          draggedCardElement.classList.remove('card-moved');
        }, 500);
      }
    }
  }
  
  // Event listeners
  searchBtn.addEventListener("click", searchCity);
  
  search.addEventListener("keyup", (e) => {
    if (e.key === "Enter") {
      searchCity();
    } else {
      getCitySuggestions(search.value.trim());
    }
  });
  
  // Hide suggestions when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.matches('.search-input') && !e.target.matches('.suggestion')) {
      suggestionsContainer.style.display = 'none';
    }
  });
  
  // Initialize the app
  initApp();
});
