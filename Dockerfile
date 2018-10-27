FROM python:3
ADD ./ /
RUN pip3 install PyGithub
RUN pip3 install schedule
CMD [ "python3", "./app.py" ]
