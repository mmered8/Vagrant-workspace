# Assignment 3

**Authors**: Mason Meredith

**Created**: Summer 2022

## Requirements
The following should be installed in order to run the programs:

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



> **Note**
> The way the system works now is that the EC2 instances both run the broker just find and rely on the single zookeeper on "VM2." The VM2 is also running the consumer code which is what actually puts the information in the CouchDB on VM3. VM3 also holds a broker which is what handles most of the traffic initially. Ideally (though not specified in the class) the information would be stored around this point or filtered before now, but it depends on the type of system. The actual data is comming from a faker library. 




> **Automatic setup**

1. vagrant up --provision

2. After about 20 minutes check http://54.205.194.42:5984/_utils/#

3. vagrant ssh 
    > cd /vagrant/vagrant_workspace/
    > ansible-playbook terminate.yml 

4. vagrant destroy 