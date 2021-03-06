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
apt-get install libapache2-mod-wsgi
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

Create config file for boto library with authorization keys in /etc/boto.cfg.
Example:
```ini
[Credentials]
aws_access_key_id = <your access key>
aws_secret_access_key = <your secret key>
```

Prepare iclogger application
```sh
git clone https://github.com/klangner/iclogger.git
cd iclogger/src/iclogger
cp example_settings.py settings.py
vim settings.py
```
Using vim editor change TABLE_NAME to table you created on DynamoDB.

Configure apache to point to iclogger.wsgi

Now you you can try to open page:
<ec2>.amazonaws.com/?content=test&session=1&event=12

And check if there is a new row in dynamoDB table.





