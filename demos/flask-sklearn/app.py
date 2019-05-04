from flask import Flask
app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    html = f"<h3>Hello {name}!</h3>"
    return html.format(format)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)