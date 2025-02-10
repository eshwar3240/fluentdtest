from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("flask-app")

@app.route("/")
def home():
    logger.info("Home route accessed")
    return {"message": "Hello from Flask!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
