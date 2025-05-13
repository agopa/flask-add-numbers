from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add_numbers():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = num1 + num2
        except ValueError:
            result = "Invalid input"
    return render_template('index.html', result=result)

# ✅ Important for Docker
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
