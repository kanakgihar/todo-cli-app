from flask import Flask, request, render_template_string

app = Flask(__name__)

tasks = []

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern To-Do App</title>

    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:'Poppins', sans-serif;
        }

        body{
            min-height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;

            background: linear-gradient(
                135deg,
                #0f172a,
                #1e293b,
                #334155,
                #0f172a
            );

            background-size:400% 400%;
            animation:bgAnimation 10s ease infinite;
            overflow:hidden;
        }

        @keyframes bgAnimation{
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
            width:420px;
            padding:35px;

            background: rgba(255,255,255,0.08);

            border:1px solid rgba(255,255,255,0.2);

            backdrop-filter: blur(20px);

            border-radius:25px;

            box-shadow:
            0 8px 32px rgba(0,0,0,0.35);

            text-align:center;

            animation:fadeIn 1s ease;
        }

        @keyframes fadeIn{
            from{
                opacity:0;
                transform:translateY(20px);
            }

            to{
                opacity:1;
                transform:translateY(0px);
            }
        }

        h1{
            color:white;
            font-size:38px;
            font-weight:700;
            margin-bottom:25px;
            letter-spacing:1px;

            text-shadow:
            0 0 10px rgba(255,255,255,0.3);
        }

        .subtitle{
            color:#cbd5e1;
            margin-bottom:25px;
            font-size:15px;
        }

        form{
            display:flex;
            gap:10px;
            margin-bottom:25px;
        }

        input{
            flex:1;
            padding:14px;

            border:none;
            outline:none;

            border-radius:14px;

            background:rgba(255,255,255,0.15);

            color:white;

            font-size:15px;

            transition:0.3s;
        }

        input::placeholder{
            color:#d1d5db;
        }

        input:focus{
            background:rgba(255,255,255,0.22);
            transform:scale(1.02);
        }

        button{
            padding:14px 20px;

            border:none;
            border-radius:14px;

            background:linear-gradient(
                135deg,
                #06b6d4,
                #3b82f6
            );

            color:white;

            font-size:15px;
            font-weight:600;

            cursor:pointer;

            transition:0.3s;
        }

        button:hover{
            transform:translateY(-2px) scale(1.05);

            box-shadow:
            0 8px 20px rgba(59,130,246,0.4);
        }

        ul{
            list-style:none;
            margin-top:15px;
        }

        li{
            background:rgba(255,255,255,0.12);

            margin:12px 0;
            padding:14px;

            border-radius:14px;

            color:white;

            font-size:16px;
            font-weight:500;

            transition:0.3s;

            animation:slideUp 0.4s ease;
        }

        li:hover{
            transform:translateX(5px);
            background:rgba(255,255,255,0.18);
        }

        @keyframes slideUp{
            from{
                opacity:0;
                transform:translateY(15px);
            }

            to{
                opacity:1;
                transform:translateY(0px);
            }
        }

        .footer{
            margin-top:20px;
            color:#cbd5e1;
            font-size:13px;
        }

    </style>
</head>

<body>

    <div class="container">

        <h1>🚀 To-Do App</h1>

        <p class="subtitle">
            Organize your tasks beautifully
        </p>

        <form method="POST">

            <input
                type="text"
                name="task"
                placeholder="Enter your task..."
                required
            >

            <button type="submit">
                Add
            </button>

        </form>

        <ul>
            {% for task in tasks %}
                <li>✨ {{ task }}</li>
            {% endfor %}
        </ul>

        <div class="footer">
            Built with Flask + Vercel
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
