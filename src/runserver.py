#!/usr/bin/env python
from webapp.app import App as WebApp

webapp = WebApp.build()

if __name__ == "__main__":
    webapp.run(host="0.0.0.0", port=8000)
