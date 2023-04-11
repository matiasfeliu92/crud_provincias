import http.client
import json
import socket
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/province/{id}")
async def get_province(id: int):

    # Crear un objeto de conexión HTTP con el servidor
    conn = http.client.HTTPConnection("localhost:5000")
    conn.connect()

    # Enviar una solicitud HTTP GET al servidor
    conn.request("GET", f"/provinces/{id}")
    response = conn.getresponse()

    # Imprimir el estado y la razón de la respuesta HTTP
    print(response.status, response.reason)

    # Leer los datos de la respuesta HTTP
    data = response.read()
    print(data)

    return JSONResponse(content=json.loads(data))
    conn.close()

# @app.get("/prov/{id}")
@app.get("/prov")
# async def get_prov(id: int):
async def get_prov():

    # Crear un socket para recibir los datos en tiempo real del servidor
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 5000))
    request = b"GET /provinces/ HTTP/1.1\r\nHost: 127.0.0.1:5000\r\n\r\n"
    s.send(request)

    # Recibir y mostrar los datos en tiempo real del servidor
    while True:
        response = s.recv(4096)
        print(response)
        if not response:
            break
        print('RESPUESTAA SOCKET: ', response.decode('utf-8'))

        # Cerrar la conexión con el servidor HTTP y el socket
        return JSONResponse(content=response.decode('utf-8'))
    # conn.close()
    s.close()