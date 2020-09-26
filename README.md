# django sample with auth and acl

## Create project
```shell
 django-admin startproject django-auth-acl
```
## Create app
```shell
python3 manage.py startapp notes
```
## Add app to settings
in `django-auth-acl` settings.py applications:
```python
    'notes.apps.NotesConfig',
```
Also in TEMPLATES:
```
        'DIRS': [BASE_DIR + '/templates'],
```

Also add in `django-auth-acl` the urls:
```
    path('notes/', include('notes.urls')),
```
## Create super admin user

```shell
python3 manage.py createsuperuser
```