from flask import Flask, request

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return "To-Do Web App Running on Vercel 🚀"

@app.route('/add')
def add():
    task = request.args.get('task')
    if task:
        tasks.append(task)
    return {"tasks": tasks}

# IMPORTANT: Vercel handler
def handler(request):
    return app(request.environ, lambda *args: None)