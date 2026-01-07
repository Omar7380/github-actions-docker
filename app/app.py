from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Omar - GitHub Actions</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f0f2f5;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            text-align: center;
        }
        h1 {
            color: #2c3e50;
            margin-bottom: 1.5rem;
        }
        .card {
            background: white;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-top: 2rem;
        }
        .github-link {
            display: inline-block;
            margin-top: 1.5rem;
            padding: 0.75rem 1.5rem;
            background-color: #2b3137;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        .github-link:hover {
            background-color: #1c2128;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Bienvenue sur mon Projet</h1>
        <div class="card">
            <h2>Omar - Projet GitHub Actions</h2>
            <p>Ceci est une application de démonstration pour le CI/CD avec GitHub Actions, Docker et Kubernetes.</p>
            <a href="https://github.com/Omar7380/github-actions-docker" class="github-link" target="_blank">
                Voir sur GitHub
            </a>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def hello():
    return render_template_string(HTML_TEMPLATE)

@app.route("/ping")
def ping():
    return "pong"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)