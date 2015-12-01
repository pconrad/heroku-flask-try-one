from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloRoot():
    return 'Hello Vincent!'

if __name__=="__main__":
    app.run(debug=False)
