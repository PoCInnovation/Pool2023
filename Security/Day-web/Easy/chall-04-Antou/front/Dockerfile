FROM php:latest

# Set flag secret key
ENV FLAG=PoC{cRLf_C4n_BE_H4rd_7o_UndEr57AND}

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
