# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"

  # config.vm.define "VM1" do |subconfig|
  #   subconfig.vm.

  # Provider Settings
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
    # vb.cpu = 2
  end
  
    # Network Settings
    # config.vm.network "forwarded_port", guest: 80, host: 8080
    # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
    # config.vm.network "private_network", ip: "192.168.33.10"
    # config.vm.network "public_network"
  
  #automated cloud setup
  config.vm.provision "shell", path: "bootstrap.sh"

  config.vm.provision "file", source: "./new_assignment", destination: "~/new_assignment"
  config.vm.provision "file", source: "./ansible.cfg", destination: "~/.ansible.cfg"
  config.vm.provision "file", source: "./hosts", destination: "~/.ansible/hosts"
  # config.vm.provision "file", source: "C:/Users/gokhale/.config/openstack/clouds.yaml", destination: "~/.config/openstack/clouds.yaml"
  config.vm.provision "file", source: "C:/vagrant_workspace/CloudBrokerClass.pem", destination: "~/.ssh/CloudBrokerClass.pem"
  config.vm.provision "file", source: "./boto", destination: "~/.boto"
  # config.vm.provision "file", source: "C:/vagrant_workspace/CloudBrokerClass.pem", destination: "/.ssh/CloudBrokerClass.pem"


  $script = <<-SCRIPT
    chmod go-rwx ~/.ssh/CloudBrokerClass.pem
  SCRIPT
  config.vm.provision "shell", inline: $script, privileged: false

  config.vm.synced_folder "../", "/vagrant"

  # Run Ansible from the Vagrant Host
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "/vagrant/vagrant_workspace/master.yml"
    ansible.verbose = true
    ansible.install = true 
    ansible.limit = "all"
    ansible.inventory_path = "/vagrant/vagrant_workspace/hosts"
  end

end
  