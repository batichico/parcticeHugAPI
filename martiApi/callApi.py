import request

url = "http://localhost:8000/"

r = requests.get(url + "videojuegos")

resultado = r.json()
print(resultado)
