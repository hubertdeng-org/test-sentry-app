from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration
import sentry_sdk

# ![[ChangeTogether.Start]]
# ![[ChangeTogether.With("README.md")]]
#hahaha

app = Flask(__name__)

sentry_sdk.init(
    dsn="http://1262ac3315a842d886c7595186ddd33e@127.0.0.1:9000/2",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    integrations=[
        FlaskIntegration(),
    ],
    traces_sample_rate=1.0
)

@app.route("/")
def index():
    return "Hello World :)", 200

@app.route("/error")
def error():
    return "Error", 400

@app.route("/exception")
def division_by_zero():
    division_by_zero = 1 / 0
    return "Should Not Display", 200

@app.route("/sentry-exception")
def sentry_exception():
    try:
        division_by_zero = 1 / 0
    except Exception as e:
        sentry_sdk.capture_exception(e)
    return "Sentry Exception", 200

@app.route('/post', methods=['POST'])
def post():
    return "Test :1234"

# ![[ChangeTogether.End]]
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)