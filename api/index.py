from flask import Flask, request, render_template_string

app = Flask(__name__)

tasks = []

HTML = """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Advanced Productivity Hub</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
}

body{

    min-height:100vh;

    background:
    linear-gradient(
    -45deg,
    #0f172a,
    #1e293b,
    #312e81,
    #0f766e
    );

    background-size:400% 400%;

    animation:bg 12s ease infinite;

    color:white;

    padding:40px;
}

@keyframes bg{

    0%{
        background-position:0% 50%;
    }

    50%{
        background-position:100% 50%;
    }

    100%{
        background-position:0% 50%;
    }
}

.container{

    max-width:1200px;
    margin:auto;
}

.title{

    text-align:center;
    margin-bottom:35px;
}

.title h1{

    font-size:58px;
    font-weight:700;

    text-shadow:
    0 0 20px rgba(255,255,255,0.4);
}

.title p{

    margin-top:10px;
    color:#cbd5e1;
    font-size:18px;
}

.grid{

    display:grid;

    grid-template-columns:
    repeat(auto-fit,minmax(350px,1fr));

    gap:25px;
}

.card{

    background:rgba(255,255,255,0.08);

    border:1px solid rgba(255,255,255,0.15);

    backdrop-filter:blur(18px);

    border-radius:24px;

    padding:28px;

    box-shadow:
    0 8px 30px rgba(0,0,0,0.35);

    transition:0.3s;
}

.card:hover{

    transform:translateY(-6px);
}

.card h2{

    margin-bottom:22px;
    font-size:26px;

    display:flex;
    align-items:center;
    gap:12px;
}

form{

    display:flex;
    flex-direction:column;

    gap:15px;
}

input{

    width:100%;

    padding:15px;

    border:none;
    outline:none;

    border-radius:14px;

    background:rgba(255,255,255,0.15);

    color:white;

    font-size:15px;
}

input::placeholder{

    color:#d1d5db;
}

.priority-select{

    padding:15px;

    border:none;
    outline:none;

    border-radius:14px;

    background:rgba(255,255,255,0.15);

    color:white;

    font-weight:600;

    cursor:pointer;
}

.priority-select option{

    color:black;
}

button{

    border:none;

    padding:15px;

    border-radius:14px;

    background:
    linear-gradient(
    135deg,
    #06b6d4,
    #3b82f6
    );

    color:white;

    cursor:pointer;

    font-size:16px;
    font-weight:600;

    transition:0.3s;
}

button:hover{

    transform:scale(1.03);

    box-shadow:
    0 5px 18px rgba(59,130,246,0.5);
}

.task{

    background:rgba(255,255,255,0.12);

    padding:16px;

    border-radius:16px;

    margin:14px 0;

    display:flex;

    justify-content:space-between;

    align-items:center;

    transition:0.3s;
}

.task:hover{

    transform:translateX(6px);

    background:rgba(255,255,255,0.18);
}

.task-left{

    display:flex;
    align-items:center;
    gap:14px;
}

.checkbox{

    width:22px;
    height:22px;

    accent-color:#06b6d4;

    cursor:pointer;
}

.priority{

    font-size:12px;

    padding:6px 12px;

    border-radius:20px;

    font-weight:600;
}

.high{

    background:#ef4444;
}

.medium{

    background:#f59e0b;
}

.low{

    background:#10b981;
}

.analytics{

    display:flex;
    justify-content:space-between;
    margin-top:15px;
}

.stat{

    text-align:center;
}

.stat h3{

    font-size:32px;
}

.quote{

    font-size:18px;
    line-height:1.7;

    color:#e2e8f0;
}

.timer{

    font-size:50px;
    text-align:center;
    margin-top:20px;
    font-weight:700;
}

.footer{

    text-align:center;
    margin-top:40px;

    color:#cbd5e1;
}

.progress-container{

    margin-top:20px;
}

.progress-bar{

    width:100%;
    height:18px;

    border-radius:20px;

    background:rgba(255,255,255,0.15);

    overflow:hidden;
}

.progress{

    width:75%;
    height:100%;

    background:
    linear-gradient(
    90deg,
    #06b6d4,
    #3b82f6
    );
}

.small-text{

    margin-top:10px;
    color:#cbd5e1;
}

</style>

</head>

<body>

<div class="container">

    <div class="title">

        <h1>🚀 Productivity Hub</h1>

        <p>
        Organize • Prioritize • Focus • Achieve
        </p>

    </div>

    <div class="grid">

        <!-- TASK MANAGER -->

        <div class="card">

            <h2>
            <i class="fa-solid fa-list-check"></i>
            Task Manager
            </h2>

            <form method="POST">

                <input
                type="text"
                name="task"
                placeholder="Enter a new task..."
                required>

                <select
                name="priority"
                class="priority-select">

                    <option value="HIGH">
                    🔴 High Priority
                    </option>

                    <option value="MEDIUM">
                    🟡 Medium Priority
                    </option>

                    <option value="LOW">
                    🟢 Low Priority
                    </option>

                </select>

                <button>
                <i class="fa-solid fa-plus"></i>
                Add Task
                </button>

            </form>

            {% for task in tasks %}

            <div class="task">

                <div class="task-left">

                    <input
                    type="checkbox"
                    class="checkbox">

                    <span>
                    {{ task.name }}
                    </span>

                </div>

                <span class="
                priority
                {% if task.priority == 'HIGH' %}
                    high
                {% elif task.priority == 'MEDIUM' %}
                    medium
                {% else %}
                    low
                {% endif %}
                ">

                {% if task.priority == 'HIGH' %}
                    🔴 HIGH
                {% elif task.priority == 'MEDIUM' %}
                    🟡 MEDIUM
                {% else %}
                    🟢 LOW
                {% endif %}

                </span>

            </div>

            {% endfor %}

        </div>

        <!-- ANALYTICS -->

        <div class="card">

            <h2>
            <i class="fa-solid fa-chart-line"></i>
            Productivity Analytics
            </h2>

            <div class="analytics">

                <div class="stat">
                    <h3>{{ tasks|length }}</h3>
                    <p>Total Tasks</p>
                </div>

                <div class="stat">
                    <h3>87%</h3>
                    <p>Focus</p>
                </div>

                <div class="stat">
                    <h3>5h</h3>
                    <p>Deep Work</p>
                </div>

            </div>

            <div class="progress-container">

                <div class="progress-bar">

                    <div class="progress"></div>

                </div>

                <p class="small-text">
                Weekly Goal Completion
                </p>

            </div>

        </div>

        <!-- FOCUS MODE -->

        <div class="card">

            <h2>
            <i class="fa-solid fa-clock"></i>
            Focus Mode
            </h2>

            <div class="timer">
            25:00
            </div>

            <p class="small-text" style="text-align:center;">
            Pomodoro Productivity Session
            </p>

        </div>

        <!-- SMART REMINDER -->

        <div class="card">

            <h2>
            <i class="fa-solid fa-bell"></i>
            Smart Reminder
            </h2>

            <p class="quote">

            🔔 Complete your highest priority task first.<br><br>

            📌 Stay consistent with your productivity streak.<br><br>

            ⚡ Focus on progress, not perfection.

            </p>

        </div>

        <!-- MOTIVATION -->

        <div class="card">

            <h2>
            <i class="fa-solid fa-fire"></i>
            Daily Motivation
            </h2>

            <p class="quote">

            "Success doesn't come from what you do occasionally,
            it comes from what you do consistently."

            </p>

        </div>

        <!-- ORGANIZATION -->

        <div class="card">

            <h2>
            <i class="fa-solid fa-layer-group"></i>
            Organization System
            </h2>

            <p class="quote">

            ✔ Prioritize important tasks<br><br>

            ✔ Track your productivity analytics<br><br>

            ✔ Build focus and discipline habits<br><br>

            ✔ Improve daily efficiency<br><br>

            ✔ Manage work smartly

            </p>

        </div>

    </div>

    <div class="footer">

        Built with Flask + Vercel • Advanced Productivity Dashboard

    </div>

</div>

</body>

</html>

"""

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        task = request.form.get("task")
        priority = request.form.get("priority")

        if task:

            tasks.append({

                "name": task,
                "priority": priority

            })

    return render_template_string(
        HTML,
        tasks=tasks
    )

def handler(request):
    return app(request.environ, lambda *args: None)