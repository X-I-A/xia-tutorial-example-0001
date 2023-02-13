import os
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object("config." + os.environ.get("XIA_ENV", "prod").title() + "Config")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))  # pragma: no cover
