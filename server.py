from flask import Flask, render_template, request, jsonify
import logging


app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# initial state
state = {
    "eyes": "left", 
    "eyebrows": "normal",
    "say" : ""
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/state")
def get_state():
    return jsonify(state)

@app.route("/action", methods=["POST"])
def action():
    action = request.form.get("action")
    if action in ["left", "up", "right"]:
        state["eyes"] = action
    elif action in [ "normal", "nasty" ]:
        state["eyebrows" ] = action
    return "ok"

@app.route("/say", methods=["POST"])
def say():
    message = request.form.get("message", "").strip()

    if len(message) > 50:
        message = message[:50] # avoid long messages
    logging.debug(f"Say {message}")
    state["say"] = message
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
