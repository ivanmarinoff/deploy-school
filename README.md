# [ S.O.V.A-school](https://github.com/SOVASchool)

[//]: # (Modern template for **Django** that covers `Admin Section`, all authentication pages &#40;registration included&#41; crafted on top of **[Black Dashboard]&#40;https://appseed.us/product/black-dashboard/django/&#41;**, an open-source `Bootstrap 5` design from [Creative-Tim]&#40;https://www.creative-tim.com/?AFFILIATE=128200&#41;.)
This is a S.O.V.A-school site project built with  **Django** that includes a publicly accessible site, an authentication section, and content creation by registered users.
> Actively supported by [ S.O.V.A](http://www.sovapsychologist.com") Many thanks `S.O.V.A`.

<br>
## This is a site `Home page`

![home_page](https://github.com/ivanmarinoff/S.O.V.A-school/assets/107050101/28745df3-30d3-4065-97b6-1ab414735f5a)

<br />
## This is a `Signup` page
![signup](https://github.com/ivanmarinoff/S.O.V.A-school/assets/107050101/4b6c2d47-02c1-4f06-acbe-7d68e0e2d7dc)
<br />

## This is a `email answer` view
![email_answer](https://github.com/ivanmarinoff/S.O.V.A-school/assets/107050101/2305c55a-80c9-4343-8899-d4a6853f85ae)
<br />
## This is a `Login page`
![login](https://github.com/ivanmarinoff/S.O.V.A-school/assets/107050101/ca22a941-afd2-4814-a4d2-98ce4ba4a771)
<br />
## This is a `Profile page`
![profile_details](https://github.com/ivanmarinoff/S.O.V.A-school/assets/107050101/c7b4e4c3-7077-4c43-b529-a7d72d9282bd)
<br />
## This is a `Profile edit` page
![profile_edit](https://github.com/ivanmarinoff/S.O.V.A-school/assets/107050101/66014645-d165-4073-9882-111c4e390c33)
<br />
## This is a `Global content` page for all registered users
![global_content](https://github.com/ivanmarinoff/S.O.V.A-school/assets/107050101/294729d5-87df-4223-9ef4-2781e2c3bd21)
<br />
## This is a `User content` page for personal content created by users
![user_content](https://github.com/ivanmarinoff/S.O.V.A-school/assets/107050101/41c82907-a821-4abd-8a3c-f519a38fd406)
<br />
## This is a `ChatBot` form for private messages without registration
![chatbot](https://github.com/ivanmarinoff/S.O.V.A-school/assets/107050101/84712541-cdf1-438d-84a7-090ad040f63b)
<br />
- **Sections Covered**: 
  - `Admin Section`, reserved for `superusers`
  - `All pages` managed by `Django.contrib.AUTH`
  - `Log in` page
  - `Registration` page
  - `Content pages`: content pages created by superuser and regular users, with full `CRUD` rights to their own content. 
  

## How to use it
<br />

> **Install the package** via `PIP` 

```bash
$ Use the pip install -r requirements.txt command 
// OR
$ pip install git+https://github.com/ivanmarinoff/S.O.V.A-school.git
```

<br />

> Use command `venv\Scripts\activate` in to terminal to create `venv` file of your Django project directory!

<br />
> **Start the app**
> To set up PostgreSQL database run the file:

```bash
$ docker-compose up --build
```

```bash
$ # Set up the database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```

Access the `admin` section in the browser: `http://127.0.0.1:8000/`
<br />

## Code structuree 

```bash
# This exists in ENV: LIB/sova_school
< UI_LIBRARY_ROOT >                      
   sova_school/
├── src/
│   └── sova_school/
│       ├── media/
│       ├── sova_school/
│       │   ├── content/  # registred users content pages
│       │   ├── core/     # email utils core code
│       │   ├── envs/
│       │   ├── global_content/ # global content pages
│       │   ├── users/       # users managment pages
│       │   ├── web/        # web pages
│       ├── templates/
│       │   │   ├── content/ # registred users content .html templates
│       │   │   ├── emails/  # email utils .html templates
│       │   │   ├── global_content/ # global content .html templates
│       │   │   ├── home/    # home .html templates
│       │   │   ├── users/   # users .html templates
│       │   │   └── web/     # web .html templates
│       ├── static/
│       │   │   ├── css/    # css files
│       │   │   ├── fonts/  # fonts
│       │   │   ├── images/ # images
│       │   │   ├── js/     # js files
│       │   │   └── pictures/ # pictures
│       │   ├── __init__.py
│       │   ├── asgi.py
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       ├── requirements.txt
│       │── README.md  
│       │── .gitignore  
│       ├── LICENSE
│       ├── docker-compose.yml
│       └── manage.py
└── env/
   |-- ************************************************************************
```

<br />
