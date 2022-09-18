from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Index')
def home():
    return render_template('Index.html')

@app.route('/Data/')
def about():
    return render_template('Data.html')

@app.route('/Graph/')
def about():
    return render_template('Graph.html')

@app.route('/Map/')
def about():
    return render_template('Map.html')

if __name__ == '__main__':
    app.run(debug=True)