# base image
FROM python:3

# The environment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

# install dependencies  
RUN pip install --upgrade pip

# create root directory for our project in the container
RUN mkdir /walletsystem

# Set the working directory to /walletsystem
WORKDIR /walletsystem

# Copy the current directory contents into the container at /walletsystem
ADD . /walletsystem/

#let pip install required packages
RUN pip install -r requirements.txt

# port where the Django app runs
# EXPOSE 8000 

# start server  
CMD python manage.py runserver