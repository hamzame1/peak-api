# peak-api
##### steps ti run app
## build databse dockerfile
cd  database
docker build . 
## build dockerfile project
docker build . 
## test app
docker-compose run --rm app sh -c "python manage.py test && flake8"
## buid and start the container
docker-compose up



