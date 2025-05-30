from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mood = request.form['mood']
        time = request.form['time']
        tasks = request.form['tasks']
        # This is where you'll connect to OpenAI/OpenRouter
        return render_template('index.html', mood=mood, time=time, tasks=tasks)
    return render_template('index.html', mood=None)

if __name__ == '__main__':
    app.run(debug=True)

