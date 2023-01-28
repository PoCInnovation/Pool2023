FROM php:latest

# Set flag secret key
ENV FLAG=PoC{tHERE_I5_MOre_7H@n_4_80Dy}

#Update systeme
RUN apt update && apt install python3 python3-pip -y
    
# Install requiring packages
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Run flask app challenge
COPY . /app
COPY . /var/www/html/
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]