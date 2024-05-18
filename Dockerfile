# pull python base image
FROM python:3.10

# specify working directory
WORKDIR /patient_survival

ADD  requirements.txt .
#ADD /titanic_model_api/*.whl .

# update pip
RUN pip install --upgrade pip

# install dependencies
RUN pip install -r requirements.txt

#RUN rm *.whl

# copy application files
ADD app.py .
ADD xgboost-model.pkl .

# expose port for application
EXPOSE 8001

# start fastapi application
CMD ["python", "app.py"]
