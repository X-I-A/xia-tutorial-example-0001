import os
from flask import Flask


def get_version():
    with open("./VERSION") as fp:
        return fp.read().strip()


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object("config." + os.environ.get("XIA_ENV", "prod").title() + "Config")

    # Compiler schema files
