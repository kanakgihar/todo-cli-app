from flask import Flask, request, render_template_string

app = Flask(__name__)

tasks = []

HTML = """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Ultimate Productivity App</title>

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

    max-width:1100px;
    margin:auto;
}

.title{

    text-align:center;
    margin-bottom:30px;
}

.title h1{

    font-size:55px;
    font-weight:700;

    text-shadow:
    0 0 20px rgba(255,255,255,0.4);
}

.title p{

    margin-top:10px;
    color:#cbd5e1;
}

.grid{

    display:grid;

    grid-template-columns:
    repeat(auto-fit,minmax(320px,1fr));

    gap:25px;
}

.card{

    background:rgba(255,255,255,0.08);

    border:1px solid rgba(255,255,255,0.15);

    backdrop-filter:blur(18px);

    border-radius:24px;

    padding:25px;

    box-shadow:
    0 8px 30px rgba(0,0,0,0.35);

    transition:0.3s;
}

.card:hover{

    transform:translateY(-5px);
}

.card h2{

    margin-bottom:18px;
    font-size:24px;

    display:flex;
    align-items:center;
    gap:10px;
}

form{

    display:flex;
    gap:12px;
    margin-bottom:20px;
}

input{

    flex:1;

    padding:14px;

    border:none;
    outline:none;

    border-radius:14px;

    background:rgba(255,255,255,0.15);

    color:white;
}

input::placeholder{

    color:#d1d5db;
}

button{

    border:none;

    padding:14px 20px;

    border-radius:14px;

    background:
    linear-gradient(
    135deg,
    #06b6d4,
    #3b82f6
    );

    color:white;

    cursor:pointer;

    font-weight:600;

    transition:0.3s;
}

button:hover{

    transform:scale(1.05);

    box-shadow:
    0 5px 18px rgba(59,130,246,0.5);
}

.task{

    background:rgba(255,255,255,0.12);

    padding:15px;

    border-radius:14px;

    margin:12px 0;

    display:flex;

    justify-content:space-between;

    align-items:center;
}

.task-left{

    display:flex;
    align-items:center;
    gap:12px;
}

.checkbox{

    width:22px;
    height:22px;

    accent-color:#06b6d4;
}

.priority{

    font-size:12px;

    padding:5px 10px;

    border-radius:20px;

    background:#ef4444;
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

    font-size:30px;
}

.quote{

    font-size:18px;
    line-height:1.6;

    color:#e2e8f0;
}

.timer{

    font-size:42px;
    text-align:center;
    margin-top:20px;
    font-weight:700;
}

.footer{

    text-align:center;
    margin-top:40px;

    color:#cbd5e1;
}

</style>

</head>

<body>

<div class="container">

    <div class="title">

        <h1>🚀 Productivity Hub</h1>

        <p>
        Organize • Focus • Achieve
        </p>

    </div>

    <div class="grid">

        <!-- TASK SECTION -->

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

                <button>
                <i class="fa-solid fa-plus"></i>
                </button>

            </form>

            {% for task in tasks %}

            <div class="task">

                <div class="task-left">

                    <input
                    type="checkbox"
                    class="checkbox">

                    <span>{{ task }}</span>

                </div>

                <span class="priority">
                HIGH
                </span>

            </div>

            {% endfor %}

        </div>

        <!-- ANALYTICS -->

        <div class="card">

            <h2>
            <i class="fa-solid fa-chart-line"></i>
            Analytics
            </h2>

            <div class="analytics">

                <div class="stat">
                    <h3>{{ tasks|length }}</h3>
                    <p>Total Tasks</p>
                </div>

                <div class="stat">
                    <h3>85%</h3>
                    <p>Productivity</p>
                </div>

                <div class="stat">
                    <h3>4h</h3>
                    <p>Focus Time</p>
                </div>

            </div>

        </div>

        <!-- FOCUS TIMER -->

        <div class="card">

            <h2>
            <i class="fa-solid fa-clock"></i>
            Focus Mode
            </h2>

            <div class="timer">
                25:00
            </div>

            <p style="text-align:center;margin-top:15px;">
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
            🔔 Don't forget to complete your highest priority task today.
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
            Organization
            </h2>

            <p class="quote">

            ✔ Prioritize tasks <br><br>

            ✔ Track productivity <br><br>

            ✔ Build focus habits <br><br>

            ✔ Stay consistent daily

            </p>

        </div>

    </div>

    <div class="footer">

        Built with Flask + Vercel • Advanced Productivity UI

    </div>

</div>

</body>
</html>

"""

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        task = request.form.get("task")

        if task:
            tasks.append(task)

    return render_template_string(
        HTML,
        tasks=tasks
    )

def handler(request):
    return app(request.environ, lambda *args: None)