from flask import Flask, render_template 

app = Flask (__name__)

@app.route('/')
def Index():
    return render_template('Index.html')

@app.route('/Graph')
def Graph():
    return render_template('Graph.html')

@app.route('/Map')
def Map():
    return render_template('Map.html')

@app.route('/Data')
def Data():
    return render_template('Data.html')

if __name__ == '__main__':
    app.run(debug=True)