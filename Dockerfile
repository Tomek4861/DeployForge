# Use python
FROM python:3.10


# Set env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# set workdir inside container
WORKDIR /app

# copy files
COPY . /app/

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# collect static files
RUN python manage.py collectstatic --noinput --clear


# state which port will be used
EXPOSE 8000

# start command
CMD ["gunicorn", "chmuralab.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "60"]
