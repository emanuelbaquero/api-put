FROM ubuntu:latest


RUN apt update 

RUN apt-get install -y python3-pip
#RUN apt install -y pip
RUN pip install flask 
RUN pip install flask-restful 
RUN pip install pandas 
RUN pip install dnspython 
RUN pip install requests 
RUN pip install pymongo 
RUN pip install flask_restplus 
RUN pip install Werkzeug==0.16.1 
RUN pip install pandasql
RUN pip install boto3
        



