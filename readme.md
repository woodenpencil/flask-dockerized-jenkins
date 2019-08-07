# Flask Tutorial
Simple hello world Flask App tutorial with Docker Containerization and Systemd Unit file.

## gunicorn setup
Install gunicorn using pip

    $ pip install gunicorn
    
Running the WSGI gunicorn server    
    
    $ gunicorn -b 0.0.0.0:8000 app.wsgi:app

## Docker creation

## Doubts
1. how to avoid venv being copied into Docker Image?
2. how to inspect files/folders contained into Docker image
3. What is right structure convention for the python project
4. How to write testcase assertions using pytest for JSON attributes
