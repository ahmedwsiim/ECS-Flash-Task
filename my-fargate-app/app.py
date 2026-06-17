from flask import Flask, jsonify

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ECS Fargate Demo</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: rgba(30, 41, 59, 0.7);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent-1: #3b82f6;
            --accent-2: #8b5cf6;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Outfit', sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background-image: 
                radial-gradient(circle at 15% 50%, rgba(59, 130, 246, 0.15), transparent 25%),
                radial-gradient(circle at 85% 30%, rgba(139, 92, 246, 0.15), transparent 25%);
            overflow: hidden;
        }

        .container {
            text-align: center;
            padding: 4rem;
            background: var(--card-bg);
            border-radius: 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            transform: translateY(0);
            transition: transform 0.4s ease, box-shadow 0.4s ease;
            max-width: 800px;
            width: 90%;
            position: relative;
        }

        .container:hover {
            transform: translateY(-5px);
            box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.6);
        }

        .badge {
            display: inline-block;
            padding: 0.5rem 1.2rem;
            background: rgba(59, 130, 246, 0.1);
            color: var(--accent-1);
            border: 1px solid rgba(59, 130, 246, 0.2);
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            margin-bottom: 1.5rem;
            animation: pulse 2s infinite;
        }

        h1 {
            font-size: 3.5rem;
            font-weight: 800;
            line-height: 1.2;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, var(--text-primary) 0%, var(--text-secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .highlight {
            background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        p {
            font-size: 1.25rem;
            color: var(--text-secondary);
            font-weight: 300;
            margin-bottom: 2rem;
            line-height: 1.6;
        }

        .status-indicator {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.75rem 1.5rem;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            font-size: 0.9rem;
            color: var(--text-secondary);
            transition: background 0.3s ease;
            text-decoration: none;
        }

        .status-indicator:hover {
            background: rgba(255, 255, 255, 0.1);
            color: var(--text-primary);
        }

        .dot {
            width: 8px;
            height: 8px;
            background-color: #10b981;
            border-radius: 50%;
            box-shadow: 0 0 10px #10b981;
        }

        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(59, 130, 246, 0); }
            100% { box-shadow: 0 0 0 0 rgba(59, 130, 246, 0); }
        }

        @media (max-width: 640px) {
            h1 { font-size: 2.5rem; }
            .container { padding: 2.5rem; }
            p { font-size: 1.1rem; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="badge">Live Deployment</div>
        <h1>AWS <span class="highlight">ECS Fargate</span></h1>
        <p>Successfully deployed behind an Application Load Balancer by <strong>Ahmad Wasim</strong>.</p>
        <a href="/health" class="status-indicator">
            <span class="dot"></span>
            System Status: Healthy
        </a>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return html_content, 200

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
