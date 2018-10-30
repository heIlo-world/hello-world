#!/bin/bash

/usr/bin/docker build -t hello-world .
/usr/bin/docker run -it --rm -v $(pwd):/app hello-world python -u app.py
