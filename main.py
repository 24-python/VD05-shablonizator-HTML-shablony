from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def film():
    return render_template('index.html')


@app.route('/actor/')
def actor():

    return render_template('actor.html')

if __name__ == '__main__':
    app.run()