FROM php:latest

#Update systeme
RUN apt update && apt install python3 python3-pip -y

# Install requiring packages
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Run flask app challenge
COPY . /app
COPY . /var/www/html/
COPY on-init /pwinit/

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
