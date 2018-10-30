FROM python:3

MAINTAINER https://github.com/heIlo-world/hello-world

RUN pip3 install \
    PyGithub

# Define working directory
WORKDIR /app
VOLUME /app

# Define default command
CMD ["bash"]
