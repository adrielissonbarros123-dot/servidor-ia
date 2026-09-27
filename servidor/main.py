from http.server import BaseHTTPRequestHandler, HTTPServer

class ServidorIA(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        mensagem = """
        <html>
        <head>
            <title>Servidor de IA</title>
        </head>
        <body>
            <h1>Servidor de IA funcionando!</h1>
            <p>Gemini: coordenador</p>
            <p>OpenAI: programação e raciocínio</p>
            <p>Claude: análise e revisão</p>
            <p>Mistral: código e agentes</p>
            <p>Modelos locais: execução no notebook</p>
        </body>
        </html>
        """

        self.wfile.write(mensagem.encode("utf-8"))

servidor = HTTPServer(("0.0.0.0", 8000), ServidorIA)

print("Servidor de IA iniciado na porta 8000")

servidor.serve_forever()
