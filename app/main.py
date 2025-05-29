from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD in Python is working!"

@app.route("/abc")
def alphabets():
    return "A is for apple, B is for ball"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
