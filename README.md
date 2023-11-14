# python-api-sample-app

Fill data with

migrate db:
python3 manage.py migrate

user = User(id=1,name='Robert',active_from=timezone.now())
user.save()

run app
python3 manage.py runserver

Sample user:

    {
        "id": 1,
        "name": "Robert1",
        "surname": "surname1",
        "email": "email@em.pl",
        "age": 2,
        "admin": true,
        "active_from": "2023-11-14T19:33:26.768000Z"
    }
