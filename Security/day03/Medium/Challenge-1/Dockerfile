FROM python:3.8-alpine

# Set flag secret key
ENV FLAG=PoC{JWT_ls_s0_Gr3At_UnT1L_1T_iS_St0R3dED_1N_DB}

# Install requiring packages
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Run flask app challenge
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]