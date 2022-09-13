from config import app
# ===========================app routes===========================
# =================Video API routes=================
from Routes.VideoRoutes import *

# =================User API routes=================
from Routes.UserRoutes import *

@app.route("/")
def hello():
    return "hello"
# =================run the app=================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
