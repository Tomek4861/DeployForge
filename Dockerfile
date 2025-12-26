# use python
FROM python:3.10-slim

# create users group
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser


# Set env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# set workdir inside container
WORKDIR /app

#install just re
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# update pip
RUN pip install --upgrade pip

# copy files
COPY . /app/

# collect static files
RUN python manage.py collectstatic --noinput --clear

# change owner of /app
RUN chown -R appuser:appgroup /app

# switch to safe user
USER appuser

# state which port will be used
EXPOSE 8000

# start command
CMD ["gunicorn", "deployforge.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "60"]