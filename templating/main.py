from flask import Flask, render_template

app = Flask(__name__)

details = [
    {
        'name': 'Alexander',
        'age': 2,
        'location' : 'Ho'
    },
    {
        'name': 'Oluwatomison',
        'age': 3,
        'location' : 'Lagos'
    }
]

@app.get("/")
def home():
    return render_template('index.html', details=details)


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port=5001)