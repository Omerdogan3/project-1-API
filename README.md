# Project 1 MicroService API

I have converted project 1 to a simple API microservice.
It basically gets requests and generates planets and returns coordinates of stars, types of planets etc. as json objects.
Also, I created a simulator which can be found in <a href="https://github.com/Omerdogan3/project1-GUI">here</a>.
It gets all of its data from this API.

```
Clone this repository
```
```
python index.py
```

Then server will start in your localhost:8080. 
You have to keep open your local server to star simulator.

```
localhost:8080 -> generates planets and returns required data
```

```
localhost:8080/search -> simulates each iteration of my search algorithm.
```
In each request, returns location of the nearest star and whether or not life exists.

Note!! In default, it only generates 30 stars, if you have better system configuration than i have, you can increase the number.

## <a href="https://github.com/Omerdogan3/project1-GUI">Project1-GUI </a>
