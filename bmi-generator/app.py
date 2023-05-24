from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height'])

    bmi = weight / (height ** 2)
    bmi_status = get_bmi_status(bmi)

    return render_template('result.html', bmi=bmi, bmi_status=bmi_status)

def get_bmi_status(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi >= 18.5 and bmi < 25:
        return 'Normal weight'
    elif bmi >= 25 and bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

if __name__ == '__main__':
    app.run(debug=True)
