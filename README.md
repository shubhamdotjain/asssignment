# FamPay-Hiring-Assignment


##### How to setup and run locally 

  1. Clone the Repository 
  2. Run Docker
    $ docker-compose build
    $ docker-compose run web python manage.py createsuperuser
    $ docker-compose up
  3. Add Keys 
    $ curl --location --request POST 'http://localhost:8000/api/keys/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "active": true,
            "key": "AIzaSyCZ8poeOC9cYuXgMpo_2ZBD4qAIa3X0Fb4"
        }'
  4. Update query and limit through django admin in Config section (http://localhost:8000/manage/)
  
Note: You can access all the APIs through browser as well. (http://localhost:8000/api/)
