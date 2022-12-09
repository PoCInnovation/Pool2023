FROM python:3.10-alpine

# Set flag secret key
ENV FLAG=PoC{tHERE_I5_MOre_7H@n_4_80Dy}

# Install requiring packages
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Run flask app challenge
COPY . /app
ENTRYPOINT [ "python" ]
CMD ["app.py" ]
