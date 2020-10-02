from flask import *
app = Flask(__name__)


@app.route('/')
def home():
    return "This is Ravi"

if __name__=="__main__":
    app.run()
