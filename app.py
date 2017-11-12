from flask import Flask, render_template
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'techsitution4'

mongo = PyMongo(app)

@app.route('/')
def hello_world():
    #mongo.db.arianit.insert({"a":"a"})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0', debug=True)
