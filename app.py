from flask import Flask
app = Flask(__name__)

@app.route('/') #создает дополнительный маршрут, если запрос проходит успешно
def hello():
    return "Hi!"

@app.route('/health')
def health():
    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #на этом порту будет работать это приложение (5000)