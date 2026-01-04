from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kouraiche Omar - Projet CI/CD</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
                background-color: #f5f7fa;
                color: #333;
            }
            .container {
                max-width: 800px;
                margin: 40px auto;
                background: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1, h2 {
                color: #2c3e50;
                margin-bottom: 20px;
            }
            h1 {
                text-align: center;
                color: #1a73e8;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                color: #666;
                margin-bottom: 30px;
                font-size: 1.1em;
            }
            .tech-list {
                list-style: none;
                padding: 0;
            }
            .tech-item {
                background: white;
                margin: 10px 0;
                padding: 12px 15px;
                border-radius: 4px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                display: flex;
                align-items: center;
            }
            .tech-item i {
                margin-right: 10px;
                color: #1a73e8;
                width: 20px;
                text-align: center;
            }
            .footer {
                text-align: center;
                margin-top: 40px;
                padding-top: 20px;
                border-top: 1px solid #eee;
                color: #777;
                font-size: 0.9em;
            }
            @media (max-width: 600px) {
                .container {
                    margin: 20px;
                    padding: 15px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Kouraiche Omar</h1>
            <p class="subtitle">Projet CI/CD - Déploiement Automatique</p>
            
            <div class="section">
                <h2><i class="fas fa-cogs"></i> Technologies Utilisées</h2>
                <ul class="tech-list">
                    <li class="tech-item"><i class="fab fa-github"></i> GitHub Actions</li>
                    <li class="tech-item"><i class="fab fa-docker"></i> Docker</li>
                    <li class="tech-item"><i class="fas fa-cube"></i> Kubernetes</li>
                    <li class="tech-item"><i class="fab fa-python"></i> Python/Flask</li>
                    <li class="tech-item"><i class="fas fa-arrows-rotate"></i> ArgoCD</li>
                </ul>
            </div>
            
            <div class="footer">
                <p>Déployé avec ❤️ par Kouraiche Omar | © """ + str(datetime.now().year) + """</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)