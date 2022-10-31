# Python-Backend-Interview

Amitruck and its partners want to start recording trip details in its MySQL database. In order yo achieve that, Amitruck decided to build a service composed of APIs to help AmiTruck and its partners achieve the goal of capturing trip details

## Description
The Service must be composed of one API that logs trip details via an HTTP URL.

## Technologies Used

- Python 3.9 (Django Rest Framework)
- Coverage for measuring code coverage
- Docker

## Setup Instructions and Installation

- Clone this repository to a location in your file system. `git clone https://github.com/YomZsamora/python-backend-interview.git`
- Create a virtual environment `python -m venv venv` then activate with `source venv/bin/activate `
- Read the requirements file and Install all the requirements `pip install -r requirements.txt`
- Setup a MySQL Database engine. Open settings.py and change declaration of the DB_NAME, DB_USER & DB_PASSWORD
    - Can hide sensitive information by using `python-decouple 3.6` to store variables in an .env file
- Ensure MySQL Server is up and running then log into MySQL with a database user/role `mysql -u <user> -p`
    - You'll be prompted to enter a password for this user
- Next, create the database `CREATE DATABASE <dbname>` then connect to the database via `use <dbname>`
- We can now migrate using: `python manage.py migrate`
- Create a user in the terminal using command: `python manage.py createsuperuser`
    - You'll be prompted to provide username, email and password
- Now let’s start the development server and explore it: `python manage.py runserver` then Navigate to `http://localhost:8000/admin/` on your browser.

##### Setting Up Docker
   * Build Image and Run Container:

    docker-compose build
    docker-compose run --rm app django-admin startproject amitruck_assessment .
    docker-compose up

##### Importing MySQL database in Docker
   * This is a simple way of importing MySQL database in Docker:

    1. Download mysqldump from command line: `mysqldump -u user -p db_name > db_backup.sql`
    2. Put the exported sql file in the shared folder.
    3. Login to your Docker instance via `docker exec -it DOCKER_CONTAINER_ID bin/bash`
    4. Login to MySQL via mysql -u user -p.
    5. While in MySQL CLI, create a database via `create database DB_NAME;`
    6. While in MySQL CLI, use the database you just created via `use DB_NAME;`
    7. While in MySQL CLI, import the sql file via `docker exec -i container_name mysql -uroot dbname < db_backup.sql;`

### API Endpoints

Find Full API Endpoint Documentation [here](https://documenter.getpostman.com/view/5057424/2s8YRgqZoT)


| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /api/register | To sign up a new user account |
| POST | /api/login | To login an existing user account |
| POST | /api/trip/add | To create a new Trip |
| GET | /api/trips | To retrieve all trips on the platform |
| GET | /api/trip/:id | To retrieve details of a single Trip |
| PATCH | /api/trip/:id | To edit the details of a single Trip |
| DELETE | /api/trip/:id | To delete a single Trip |

	
### Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 


### License

*MIT*
Copyright (c) 2022 **Yommie Samora**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
