from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def _():
     return "Миссия Колонизация Марса"
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"
@app.route('/promotion')
def inx():
    return """Человечество вырастает из детства. </br>
Человечеству мала одна планета. </br>
Мы сделаем обитаемыми безжизненные пока планеты. </br>
И начнем с Марса! </br>
Присоединяйся!"""
@app.route("/image_mars")
def image():
    return f'''<h1>Жди нас, Марс!</h1> </br>
    <img src="{url_for('static', filename='static/img.png')}"
    alt="здесь должна была быть картинка, но не нашлась"> <br>
    Вот она какая, красная планета.'''
@app.route("/promotion_image")
def promotion_image():
    return f'''<html lang="en">
                      <head>
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style.css')}" />
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                      </head>
                      <body><h1>Жди нас, Марс!</h1> </br>
                        <img src="{url_for('static', filename='img.png')}"
                        alt="здесь должна была быть картинка, но не нашлась"> <br>
                        <!doctype html>
                        <div class="alert alert-primary" role="alert">
                          Человечество вырастает из детства
                        </div>
                        <div class="alert alert-secondary   " role="alert">
                          Человечеству мала одна планета
                        </div>
                        <div class="alert alert-success" role="alert">
                          Мы сделаем обитаемыми безжизненные планеты пока планеты
                        </div>
                        <div class="alert alert-danger" role="alert">
                          И начнем мы с марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Присоединяйся!
                        </div>
                      </body>
                    </html>'''
    


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
 