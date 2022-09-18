from flask import Flask, redner_template 

@app.route('/')
def Index():
    return redner_template('Index.html')

@app.route('/Graph')
def Graph():
    return redner_template('Graph.html')

@app.route('/Map')
def Map():
    return redner_template('Map.html')

@app.route('/Data')
def Data():
    return redner_template('Data.html')

    if __name__ == '__main__':
        app.run(debug=True)