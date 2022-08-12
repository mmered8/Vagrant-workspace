# Assignment 3

**Authors**: Mason Meredith

**Created**: Summer 2022

## Requirements
The following should be installed in order to run the programs:

## install pip 
sudo apt-get install python3-pip python-dev

**Kafka-Python**
```bash
sudo pip install kafka
```
...finally, the following will need to be installed for the system to function with ZooKeeper:

**Java**
If not already installed, `java` will need to be installed on your machine. Check if `java` is installed by using `java -version`. To install the Java Runtime Environment, run the following:
```bash
sudo apt install default-jre
java -version
```

**Virtual machines. AMAZON EC2**
1. Sign up on amazons https://us-east-1.console.aws.amazon.com/console/home?region=us-east-1#

2. Click EC2 instances 

3. New instance >> ubuntu 20.04

4. Add needed security groups particularly relevant ports like 80, 22, 2181, 9092, and 5984 TCP.
++ note easy fix is early on to use all traffic from a specific IP.

5. Make sure to save and keep track of your unique pem file for the ssh into those instances.

**VM1 - local**
This is a basic install of some ubuntu image, bare bones if wanted, but not necessary. 
Then using virtual box. 

Alternative is to use a dual boot. 

Producer code producer_2.py goes here. 
python 3 producer_2.py -t. 
'-t', '--topic', default='registered_user', help='publisher topic and couchdb document name; default registered_user'

This can also be used for testing purposes. 
/usr/local/kafka-server/bin/kafka-console-producer.sh --topic utilizations --bootstrap-server  YOURIP:9092
https://www.tutorialspoint.com/apache_kafka/apache_kafka_installation_steps.htm
https://kafka.apache.org/quickstart

**VM2 Kafka broker server  Zookeeper** 

This VM will take a kafka server which the install directions include zookeeper automatically. 
https://www.tutorialspoint.com/apache_kafka/apache_kafka_installation_steps.htm
https://kafka.apache.org/quickstart

sudo /usr/local/kafka-server/bin/kafka-server-stop.sh
sudo /usr/local/kafka-server/bin/kafka-server-start.sh  /usr/local/kafka-server/config/server.properties
sudo /usr/local/kafka-server/bin/zookeeper-server-start.sh  /usr/local/kafka-server/config/zookeeper.properties

Consumer python code will go here as well. 
'-t', '--topic', default='registered_user', help='publisher topic and couchdb document name; default registered_user'
python3 consumer_2.py 

Testing.
/usr/local/kafka-server/bin/kafka-topics.sh --create --topic utilizations --bootstrap-server 172.31.7.12:9092 
/usr/local/kafka-server/bin/kafka-topics.sh --describe --topic utilizations --bootstrap-server 172.31.7.12:9092
/usr/local/kafka-server/bin/kafka-console-consumer.sh --topic test --bootstrap-server YOURIP:9092

**VM3 couchDB  kakfa server broker**
sudo /usr/local/kafka-server/bin/kafka-server-start.sh  /usr/local/kafka-server/config/server.properties

sudo /etc/init.d/couchdb restart
sudo /etc/init.d/couchdb start
sudo /etc/init.d/couchdb stop

Installing CouchDB
sudo apt update && sudo apt install -y curl apt-transport-https gnupg

sudo curl https://couchdb.apache.org/repo/keys.asc | gpg --dearmor | sudo tee /usr/share/keyrings/couchdb-archive-keyring.gpg >/dev/null 2>&1

sudo echo "deb [signed-by=/usr/share/keyrings/couchdb-archive-keyring.gpg] https://apache.jfrog.io/artifactory/couchdb-deb/ focal main" \
    | sudo tee /etc/apt/sources.list.d/couchdb.list >/dev/null

sudo apt update
sudo apt-get install couchdb
 


> **Note**
> The way the system works now is that the EC2 instances both run the broker just find and rely on the single zookeeper on "VM2." The VM2 is also running the consumer code which is what actually puts the information in the CouchDB on VM3. VM3 also holds a broker which is what handles most of the traffic initially. Ideally (though not specified in the class) the information would be stored around this point or filtered before now, but it depends on the type of system. The actual data is comming from a faker library. 




> **Automatic setup**

1. vagrant up --provision

2. After about 20 minutes check http://54.205.194.42:5984/_utils/#

3. vagrant ssh 
    > cd /vagrant/vagrant_workspace/
    > ansible-playbook terminate.yml 

4. vagrant destroy 