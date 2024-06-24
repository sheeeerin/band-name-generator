from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    city_name = request.form['city']
    pet_name = request.form['pet']
    band_name = city_name + " " + pet_name
    return render_template('result.html', band_name=band_name)

if __name__ == '__main__':
    app.run(debug=True)
