from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "This is a CI/CD pipeline using flask!"

@app.route("/abc")
def alphabets():
    return "A is for apple, B is for ball, C is for Cat"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
