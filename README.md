# Linux Server Configuration
this is a baseline installation of a Linux server and prepare it to host my web applications. The server has been secured from a number of attack vectors, install and configure a database server, and deploy item-catalog app onto it.

## Server info
IP address: 3.121.146.121
SSH port: 2200
Domain: http://3.121.146.121.xip.io || http://ec2-3-121-146-121.eu-central-1.compute.amazonaws.com

## URL to the hosted web application

## Installed software
- finger
- Apache
- mod_wsgi
- postgreSQL
- Git

## configuration changes

### start and connect

- Create a Ubuntu instance using Amazon Lightsail.
- download the default SSH key to login from my terminal.
- connect with command `ssh -i LightsailDefaultPrivateKey-eu-central-1.pem ubuntu@3.121.146.121` or connect using putty "https://lightsail.aws.amazon.com/ls/docs/en/articles/lightsail-how-to-set-up-putty-to-connect-using-ssh"

### update currently installed packages
- updates the package lists using command `sudo apt-get update`
- Update all currently installed packages using command `sudo apt-get upgrade`

### Change the SSH port from 22 to 2200.
- Change the SSH port from 22 to 2200 by edit port 22 to port 2200 in `/etc/ssh/sshd_config` File
- Restart SSH to apply new changes using command `sudo service ssh restart`
- add port 2200 to firewall using gui service in lightsail site

### Configure the Firewall
- check status `sudo ufw status` and make sure it's inactive
- deny all incoming requests `sudo ufw default deny incoming`
- allow any request our sever is trying to send out `sudo ufw default allow outgoing
`
- allow ssh connection `sudo ufw allow 2200`
- allow basic http server connection `sudo ufw allow www`
- allow ntp connection `sudo ufw allow ntp`
- enable firewall while hands on the heart `sudo ufw enable`

### Give grader access
- create a new user called `grader` `sudo adduser grader`
- Give grader the permission to sudo by add `grader ALL=(ALL:ALL) PASSWD:ALL` to `/etc/sudoers.d/grader` file
- Create an SSH key pair for grader using the ssh-keygen tool in my local machine
- paste the SSH key in `/home/grader/.ssh/authorized_keys`

### Prepare to deploy the project
 - Configure the local timezone to UTC by running command `sudo timedatectl set-timezone UTC`
 - install apache `sudo apt-get install apache2`
 - install the Python 3 mod_wsgi package on the server: `sudo apt-get install libapache2-mod-wsgi-py3`
 - Do not allow remote connections by change `PermitRootLogin` to `no` in `sudo nano /etc/ssh/sshd_config`
 - install postgreSQL `sudo apt-get install postgresql`
 - Make sure to not allow remote connections by check `/etc/postgresql/9.5/main/pg_hba.conf`
 - login as postgresql `sudo su - postgres`, `psql`
 -  Create a new database user named catalog  `CREATE USER catalog;`
 - Create a new database named database_url `CREATE DATABASE database_url WITH owner = catalog;`

### Install git
- Install Git using `sudo apt-get install git`

### Configuring Apache
- enable mod_wsgi `sudo a2enmod wsgi`
- creating a website for WSGI that will tell Apache the location of python file and setup the file accordingly `sudo nano /etc/apache2/conf-available/wsgi.conf` Add the following line: `WSGIScriptAlias / /var/www/itemcatalog/app.py`
- edit file `/etc/apache2/sites-enabled/000-default.conf` by adding
`      ServerAdmin saadelkheety@gmail.com
        DocumentRoot /var/www/html
        WSGIScriptAlias / /var/www/itemcatalog/app.wsgi

        <Directory /var/www/yourapplication>
        WSGIProcessGroup app
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
        </Directory>
`


## Grader User

## Exernal resources
- https://www.digitalocean.com/community/tutorials/how-to-secure-postgresql-on-an-ubuntu-vps
- http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/
- http://www.hcidata.info/host2ip.cgi
- https://devops.profitbricks.com/tutorials/install-and-configure-mod_wsgi-on-ubuntu-1604-1/
- https://www.bogotobogo.com/python/Flask/Python_Flask_HelloWorld_App_with_Apache_WSGI_Ubuntu14.php
