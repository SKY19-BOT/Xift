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
        import openai
from dotenv import load_dotenv

load_dotenv()

# inside index() just after getting tasks
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

response = openai.ChatCompletion.create(
    model="mistralai/mixtral-8x7b",
    messages=[
        {"role": "system", "content": "You're a helpful assistant suggesting personalized goals based on user's mood, time, and tasks."},
        {"role": "user", "content": f"Mood: {mood}, Time: {time} hours, Tasks: {tasks}. Suggest 3 simple and helpful goals for the day."}
    ]
)

goals = response.choices[0].message.content

    return render_template('index.html', mood=None)

if __name__ == '__main__':
    app.run(debug=True)

