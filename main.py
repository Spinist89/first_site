from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/masters')
def masters():
    return render_template('masters.html')

@app.route('/stock')
def stock():
    return render_template('stock.html')

@app.route('/recording')
def recording():
    return render_template('recording.html')

@app.route('/gift_certificates')
def gift_certificates():
    return render_template('gift_certificates.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
    