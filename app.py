from flask import Flask

app = Flask(__name__)
@app.route('/')
def run():
    return "Hello this is a Flask Web Application"

if __name__ =='__main__':
    app.run(debug=True)
