# iclogger

This is server application for logging events from client applications. 
Logs can be serialized as json record to file or save to Amazon DynamoDB database.

## How to install on Amazon infrastructure

### Create table in DynamoDB
Create table with index on
Hash key: content
Primary Range Key: session


### Create EC2 instance with Ubuntu image
Select 64 bits version. And remember to allow HTTP access.
When server is ready connect to it using ssh.
While connected to the server


Update package manager
```sh
sudo apt-get update
```

Install git
```sh
sudo apt-get install git
```

Install apache2
```sh
sudo apt-get install apache2
```

Check if apache is working correctly be visiting your server with web browser. You should get apache2 default page with message: It works!

Install Python pip tool
```sh
sudo apt-get install python-pip
```

Install Flask python library
```sh
sudo pip install flask
```

Create config file for boto library with authorization keys in ~/.boto file.
Example:
```ini
[Credentials]
aws_access_key_id = <your access key>
aws_secret_access_key = <your secret key>
```



