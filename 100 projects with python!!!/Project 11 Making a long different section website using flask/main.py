from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def hello_anypage(path):
#     return f'Hello, {path if path else "homepage"}!'


if __name__ == '__main__':
    app.run()
    