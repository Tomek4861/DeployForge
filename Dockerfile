# Use python
FROM python:3.10

# set workdir inside container
WORKDIR /app

# copy files
COPY . /app/

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# state which port will be used
EXPOSE 8000

# start command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
