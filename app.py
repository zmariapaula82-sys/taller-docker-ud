
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os


class Manejador(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            respuesta = {
                "mensaje": "Mi primer contenedor automatizado",
                "version": os.getenv("APP_VERSION", "1.0")
            }
            estado = 200
        elif self.path == "/health":
            respuesta = {"estado": "ok"}
            estado = 200
        else:
            respuesta = {"error": "Ruta no encontrada"}
            estado = 404

        contenido = json.dumps(
            respuesta, ensure_ascii=False
        ).encode("utf-8")

        self.send_response(estado)
        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )
        self.send_header(
            "Content-Length", str(len(contenido))
        )
        self.end_headers()
        self.wfile.write(contenido)


if __name__ == "__main__":
    servidor = HTTPServer(("0.0.0.0", 8000), Manejador)
    print(
        "Aplicacion disponible en el puerto 8000",
        flush=True
    )
    servidor.serve_forever()
