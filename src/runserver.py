#!/usr/bin/env python
from webapp.app import app as webapp


if __name__ == "__main__":
    webapp.run(host="0.0.0.0", port=8000)
