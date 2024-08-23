# AWS_Flask_deployer

Steps(in progress):
1) Create AWS Infrastructure with Terraform:
+ ~EC2 instance for hosting the Flask application.~
+ ~VPC with the necessary networking components (subnets, security groups, etc.).~
   + https://github.com/KirillKirillovich/Terraform_modules.git//modules/vpc
+ ~S3 bucket for log storage.~


2) Build the Flask Application:
+ ~route / - disaply index.html page~
+ ~route /logs - display logs~
+ ~route /status - disaply status of app~


3) Dockerize the Application:
+ ~Create Dockerfile for app/server~
+ ~Create docker compose(for local tests)~

4) Ansible for configure instances:
+ ~main.yaml - run prepared roles~
+ ~roles/docker - presetup instance with docker & docker compose~
+ ~roles/build_app - pull & run docker images(app, server)~

USAGE(in progress):


1) git clone https://github.com/KirillKirillovich/AWS_Flask_deployer.git
2) cd AWS_Flask_deployer/terraform
3) 
 ```
terraform init
terraform plan (check)
terraform apply
```
4) cd AWS_Flask_deployer/.ansible
5) change ip`s inside hosts.yaml
6) change 'ansible_ssh_private_key_file' inside group_vars/production.yaml and group_vars/staging.yaml
7) 
 ```
ansible-galaxy role install -f -r requirements.yaml
```
8) Make sure instances are available for connection
```
ansible-playbook ping-playbook.yaml
```
9) Start main playbook
```
ansible-playbook main.yaml
```
