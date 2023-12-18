from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("main.html")


@app.route('/portfolio')
def hello2():
    return render_template("PersonalPortfolio.html")

@app.route('/todolist')
def hello3():
    return render_template("ToDoList.html")

@app.route('/calculator')
def hello4():
    return render_template("calculator.html")

@app.route('/blog')
def hello5():
    return render_template("blog.html")

@app.route('/aboutme')
def hello6():
    return render_template("aboutme.html")



if __name__ == '__main__':
    app.run(debug=True)





