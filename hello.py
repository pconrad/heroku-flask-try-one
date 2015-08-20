from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def helloRoot():
    return 'Hello SPIS!'

if __name__=="__main__":
    app.run(debug=False)
