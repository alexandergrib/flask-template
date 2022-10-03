from flask import Flask


# MongoDB Settings

# from flask_pymongo import PyMongo

# ENV variables
"""
SECRET_KEY
MONGO_URI
MONGO_DBNAME
"""

app = Flask(__name__)

# app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# mongo = PyMongo(app)


@app.route('/')
def hello_world():  # put application's code here
    # Example to fetch data from DB
    # retrieve_db_list = list(mongo.db.dbname.find())
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
