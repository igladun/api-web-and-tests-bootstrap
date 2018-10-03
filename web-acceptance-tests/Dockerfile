FROM joyzoursky/python-chromedriver:3.6-xvfb-selenium
COPY src/ /home/docker/code
ENV INSIDE_DOCKER Yes
RUN pip3 install -r /home/docker/code/requirements.txt
CMD cd /home/docker/code && ls
CMD cd /home/docker/code/tests && pytest -n 3  -v  --junitxml=/tmp/test_report/e2e_tests.xml