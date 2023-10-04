from flask import Flask
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return "hello from Ms Angela the Manager"
@app.route('/_}}', methods=['GET'])
def index2():
    return "hello from MR andy the smart guy"



app.run(debug=True)
