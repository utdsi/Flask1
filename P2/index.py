from flask import Flask, request, render_template

app = Flask(__name__)

data = {}

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        data[key] = value
        return f"Entry '{key}' created with value '{value}'"
    return render_template('create.html')

@app.route('/read')
def read():
    return render_template('read.html', data=data)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            value = request.form['value']
            data[key] = value
            return f"Entry '{key}' updated with value '{value}'"
        else:
            return f"No entry found for key '{key}'"
    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            del data[key]
            return f"Entry '{key}' deleted"
        else:
            return f"No entry found for key '{key}'"
    return render_template('delete.html')

if __name__ == '__main__':
    app.run()
