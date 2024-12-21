# Flask App
Это простое Flask-приложение, которое выводит имя хоста и IP-адрес сервера.

![Flask-app](flask-app.jpg)
 
`<link>`: <http://localhost:4321>

## Функционал
- Отображает имя хоста и IP-адрес на главной странице.

## Установка и запуск приложения в терминале
```bash
  pip install -r requirements.txt
  python3 app.py
```

## Установка и запуск приложения через Docker
```bash
  docker build -t my-flask-app .
  docker run -p 4321:4321 my-flask-app
```

## Установка и запуск приложения через Kubernetes используя образ из DockerHub
```bash
  kubectl apply -f k8s-flask-app.yml
```
