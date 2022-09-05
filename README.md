# APIs

interacting with various websites and engage with such info

your program -> (request API) External System
External System -> (send response) your program

## Api endpoint

## Api request

## response codes from apis

404 - does not exist

1XX - hold on something happens

2XX - success

3XX - no permission

4XX - error

5XX - server screwed up

## Requests API

the most popular way for python devs to handle APIs

```python
# get data from api 

data = response.json()

# ---------------------
longitude = data["iss_position"]["longitude"]


```