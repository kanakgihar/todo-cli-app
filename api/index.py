from flask import Flask, request, render_template_string

app = Flask(__name__)

tasks = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>To-Do App</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            margin-top: 50px;
        }

        input {
            padding: 10px;
            width: 250px;
        }

        button {
            padding: 10px 20px;
        }

        li {
            font-size: 20px;
            margin: 10px;
        }
    </style>
</head>
<body>

    <h1>🚀 To-Do Web App</h1>

    <form method="POST">
        <input type="text" name="task" placeholder="Enter task">
        <button type="submit">Add Task</button>
    </form>

    <h2>Tasks:</h2>

    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)

    return render_template_string(HTML, tasks=tasks)

def handler(request):
    return app(request.environ, lambda *args: None)