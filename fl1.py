from flask import Flask

app = Flask(__name__)


@app.route('/')
def title():
    return "Missiya"


@app.route('/index')
def index():
    return '''<div style="display: flex;
                          justify-content: center;">
                <div>
                    <i style="color: red;">Привет, Яндекс!</i>
                    <br>
                    <button>hahahahhahaa</button>
                </div>
              </div>'''


@app.route('/promotion')
def promotion():
    return """<p style="font-size: 40px;
                        color: red;
                        box-shadow: 0 0 100px 50px red;">Человечество вырастает из детства.
            <br>
            Человечеству мала одна планета.
            <br>
            Мы сделаем обитаемыми безжизненные пока планеты.
            <br>
            И начнем с Марса!
            <br>
            Присоединяйся!<p>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
