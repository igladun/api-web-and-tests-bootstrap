FROM python:3.7.0
COPY src/ /home/docker/code
RUN pip3 install -r /home/docker/code/requirements.txt
RUN cd /home/docker/code/tests && pytest -v --junitxml=./report/unit_tests.xml
CMD cd /home/docker/code && python3 app.py