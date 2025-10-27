
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>System Format?</title>
        <style>
            /* Global Styles */
            body {
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #1e3c72, #2a5298);
                color: #fff;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
            }

            h2 {
                font-size: 2.5rem;
                margin-bottom: 20px;
                animation: blink 1s infinite;
            }

            /* Blinking effect */
            @keyframes blink {
                0%, 50%, 100% { opacity: 1; }
                25%, 75% { opacity: 0; }
            }

            button {
                padding: 15px 30px;
                font-size: 1.2rem;
                background-color: #ff4b2b;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: all 0.3s ease;
                color: #fff;
                margin-top: 15px;
            }

            button:hover {
                background-color: #ff416c;
                transform: scale(1.1);
            }

            #msg {
                margin-top: 30px;
                font-size: 1.5rem;
            }

            /* Responsive */
            @media (max-width: 768px) {
                h2 {
                    font-size: 2rem;
                }
                button {
                    padding: 12px 25px;
                    font-size: 1rem;
                }
                #msg {
                    font-size: 1.2rem;
                }
            }
        </style>
    </head>
    <body>
        <h2>System check in progress...</h2>
        <audio id="sound">
            <source src="https://github.com/johnsteven9988776655/funny_audio/raw/refs/heads/main/reset_audio.mp3" type="audio/mpeg">
        </audio>
        <button onclick="document.getElementById('sound').play()"> Click here </button>
        <p id="msg"></p>

        <script>
            setTimeout(() => {
                document.getElementById('msg').innerHTML = 
                    '<a href="https://example.com" target="_blank" style="color: #00ffff; text-decoration: underline;">Click here to proceed</a>';
            }, 4000);
        </script>

    </body>
    </html>
    """

if __name__ == '__main__':
    import os
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)