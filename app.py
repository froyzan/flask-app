from flask import Flask, render_template_string
import socket

app = Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()  # Получаем имя хоста
    ip_address = socket.gethostbyname(hostname)  # Получаем IP-адрес
    return render_template_string('''
        <!doctype html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Hostname и IP Address</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: monospace;
                    background-color: #72a4a7;
                }
                h1 {
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <h1>Hostname: {{ hostname }}, IP Address: {{ ip_address }}</h1>
        </body>
        </html>
    ''', hostname=hostname, ip_address=ip_address)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4321)
