## Sample Django project showing the power of the `sortable` package

In this django-admin branch, both django-grappelli and django-sortable are installed.

To run the project, type:

    virtualenv env
    source env/bin/activate
    pip install django==1.3 pil django-grappelli sortable
    python manage.py runserver

The list of books is available at http://localhost:8000 and can be edited at http://localhost:8000/admin/books/book/ logging in as *admin*/*admin*.

