FROM uadevnet/docker-newman:v3
COPY tests/ /home/docker/code
CMD  cd /home/docker/code && newman run api-tests.postman_collection.json -e my.postman_environment.json  --reporters=junit,cli,html