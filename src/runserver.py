#!/usr/bin/env python
from webapp.app import App
from webapp.settings import DEBUG

webapp = App()


if __name__ == "__main__":
    webapp.run(host="0.0.0.0", port=8000, debug=DEBUG)
