# iclogger

This is server application for logging events from client applications. 
Logs can be serialized as json record to file or save to Amazon DynamoDB database.

## How to install

This application can be installed on any server with:
* Python ver. >= 2.7
* Apache2 or any other server with WSGI support


### Install file logger

* Install Flask
* Install json library


### Install DynamoDB logger on EC2

1. Create EC2 instance with Ubuntu image

2. Update package manager
```sh
sudo apt-get update
```

3. Install git
```sh
sudo apt-get install git
```

4. Install apache2
```sh
sudo apt-get install apache2
```
* Install Flask
* Install boto library
* Create authorization keys

