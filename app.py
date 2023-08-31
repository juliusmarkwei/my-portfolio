from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/bio')
def bio():
    return render_template('bio.html')

@app.route('/podcast')
def podcast():
    return render_template('podcast.html')

if __name__ == '__main__':
    app.run(debug=True)