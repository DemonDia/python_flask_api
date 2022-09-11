from config import app
# ===========================app routes===========================
# =================Video API routes=================
from Routes.VideoRoutes import *

# =================User API routes=================
from Routes.UserRoutes import *

# =================run the app=================
if __name__ == "__main__":
    app.run(debug=True)
