## Assignment Overview

In this assignment, I successfully deployed a sample Flask application using Docker and Docker Compose. The application includes a PostgreSQL database, a Redis cache, and is structured to follow best practices for containerization, networking, and security.

## Assignment Structure

### Dockerfile

```Dockerfile
# Setting the Python as a Base Image
FROM python:3.9-slim-buster

# Setting the working directory in the container
WORKDIR /app

# Copying the requirements file into the container at /app
COPY requirements.txt .

# Installing any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copying the current directory contents into the container at /app
COPY . .

# Exposing the port the app runs on
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
```

### requirements.txt

```plaintext
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
redis==3.5.3
psycopg2-binary==2.9.1
Werkzeug==2.0.1
SQLAlchemy==1.4.31
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    depends_on:
      - db
      - redis
    environment:
      DATABASE_URL: "postgresql://root:admin@db:5432/my_db"
      REDIS_URL: "redis://redis:6379/0"
    networks:
      - backend

  db:
    image: postgres:latest
    environment:
      POSTGRES_DB: my_db
      POSTGRES_USER: ashwaq
      POSTGRES_PASSWORD: admin
    networks:
      - backend

  redis:
    image: "redis:alpine"
    ports:
      - "6379:6379"
    networks:
      - backend

networks:
  backend:
    driver: bridge
```

## Implementation Steps


1. **Building and Running Docker Containers:**
   
   ```bash
   docker-compose up --build
   ```

![image](https://github.com/ashwaq06/DevOps-Intern-Assignment/assets/80192952/4e014215-7e06-4288-858a-686b692a05b0)

![image](https://github.com/ashwaq06/DevOps-Intern-Assignment/assets/80192952/8b16c60a-483a-4e49-946f-39340d1eb6a1)


2. **Accessing the Application:**
   
   The application can be accessed at [http://localhost:5000](http://localhost:5000).

## Docker Network

A dedicated Docker network named `backend` was created to facilitate secure communication between the application components.

![image](https://github.com/ashwaq06/DevOps-Intern-Assignment/assets/80192952/9e9e3da0-178a-4b05-b67c-3293f06b62e8)

### About the App

The app tracks and displays the number of visitors accessing the web application. This count is visible on the home page, and each time a user accesses the site, the count increments.

**Webpage Access Log:**

The application logs each HTTP request made to the server. The log includes details such as the IP address of the requester, the timestamp of the request, and the type of request (e.g., "GET /").

![image](https://github.com/ashwaq06/DevOps-Intern-Assignment/assets/80192952/b8b798a5-76a4-4f04-9473-fdbcc5a36795)

**PostgreSQL Database:**
User data and timestamps, is stored persistently in a PostgreSQL database named "my_db."

**Redis Cache Integration:**
Redis caches this count, reducing the need to query the database for every request. As the app gathers information about user interactions, Redis can be leveraged to store and analyze this data in real-time.
To enhance performance, the app utilizes a Redis cache to store frequently accessed data temporarily. This is particularly useful for reducing response times for repeated requests.

### Logs and Output Images

![image](https://github.com/ashwaq06/DevOps-Intern-Assignment/assets/80192952/0843bf77-63d8-48a9-8306-1e952a673fac)

![image](https://github.com/ashwaq06/DevOps-Intern-Assignment/assets/80192952/00373bfe-466f-4e8e-9044-8861129919d4)
Whenever I reload the Page the count Gets Updated
![image](https://github.com/ashwaq06/DevOps-Intern-Assignment/assets/80192952/324fb1eb-4b3b-47ef-bc3c-610b31a30d7f)


![image](https://github.com/ashwaq06/DevOps-Intern-Assignment/assets/80192952/a8ebc600-4d37-482d-b01e-de1bc349491b)


---

Thankyou!
