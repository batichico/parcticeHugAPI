
# PRACTICE HUG API
## This proyect is created using [Hug](http://www.hug.rest/) , this is the official repository -> [timothycrosley/hug](https://github.com/timothycrosley/hug)
## First of all, install Hug:
`pip3 install hug --upgrade`

## PROYECT INFO:
API data -> [topics.json](https://github.com/batichico/praticeHugAPI/blob/master/martiApi/jsons/topics.json). 
This API is executed with [server.py](https://github.com/batichico/praticeHugAPI/blob/master/martiApi/server.py)
The logic of the API is in [apiLogic.py](https://github.com/batichico/praticeHugAPI/blob/master/martiApi/apiLogic.py) 

You have an API call example here -> [callApi.py](https://github.com/batichico/praticeHugAPI/blob/master/martiApi/callApi.py)

## If you want to run server use this:
## `hug -f server.py`

## You should enter to browser and paste this `https://localhost:8000/topics` for check if API works correctly. 

## If you want to call the API that you have running. First of all you should have [server.py](https://github.com/batichico/praticeHugAPI/blob/master/martiApi/server.py) running using `hug -f server.py` and after that you should use the next command to run callApi file :
## `hug -f callApi.py`
