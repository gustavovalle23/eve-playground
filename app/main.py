from eve import Eve
import os

SETTINGS_PATH = os.path.join(os.path.dirname(__file__), "settings.py")
app = Eve(settings=SETTINGS_PATH)


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG") == "True",)
