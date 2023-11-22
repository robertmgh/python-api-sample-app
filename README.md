# python-api-sample-app

Fill data with

migrate db:
python3 manage.py makemigrations
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

Sample access-group:

    {
        "id": 1,
        "name": "Admin",
        "description": "Only for admins"
    }

Sample access-group-membership:
    {
        "id": 1,
        "access_group":1,
        "user":1,
        "inviter":1,
        "invite_data": "2023-11-14T19:33:26.768000Z"
    }

run tests: ./manage.py test
