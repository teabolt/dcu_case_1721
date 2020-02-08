# use official Python image
# buster is recommended over alpine (https://pythonspeed.com/articles/base-image-python-docker-images/)
FROM python:3.8-buster

# set app's working directory
WORKDIR /usr/src/app

# install python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# inform that port 80 may be listened to at runtime (default port)
EXPOSE 80

# copy local source files
# we separate the copying of requirements and source code
# so that the requirements do not get reinstalled each time source code changes
# (due to cache being invalidated)
COPY . .

# command to start the application (with default settings)
# flask is not suitable as a production server (slow compared to others)
# instead use nginx or apache
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]