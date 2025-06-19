from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

HTML_PATH = os.path.join('static', 'index.html')

@app.route('/edit', methods=['GET'])
def edit():
    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    return render_template('editor.html', content=content)

@app.route('/save', methods=['POST'])
def save():
    content = request.form['content']
    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    return redirect(url_for('edit'))

if __name__ == '__main__':
    app.run(debug=True)