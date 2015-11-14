# gunicorn-bottle.py
_Updated November 14, 2015_

When you want to run your web application developed in [bottle.py](http://bottlepy.org/) using the [gunicorn](http://gunicorn.org/) WSGI HTTP server executable.

### Installations
##### Installing bottle.py
```python
pip install bottle.py
```
or copy **bottle.py** and put it in your project directory

##### Installing gunicorn
```python
pip install gunicorn
```

### Running using gunicorn
##### Running using the bottle.py application only
```python
gunicorn my_app:my_app
```

##### Running using wsgi.py
```python
gunicorn wsgi:my_app
```

### Running without using gunicorn
```python
python my_app.py
```
