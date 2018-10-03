FROM joyzoursky/python-chromedriver:3.6-xvfb-selenium
COPY src/ /home/docker/code
RUN pip3 install -r /home/docker/code/requirements.txt
CMD sleep 2
CMD cd /home/docker/code && ls
CMD cd /home/docker/code/tests && pytest -n 3  -v  --junitxml=./report/unit_tests.xml