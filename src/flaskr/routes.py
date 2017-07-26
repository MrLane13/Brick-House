from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
            'title': 'HELLO!',
            'time': time
            }
    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

