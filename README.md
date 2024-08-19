# AWS_Flask_deployer

Steps:
1) Create AWS Infrastructure with Terraform:
+ ~EC2 instance for hosting the Flask application.~
+ ~VPC with the necessary networking components (subnets, security groups, etc.).~
   + https://github.com/KirillKirillovich/Terraform_modules.git//modules/vpc
+ ~S3 bucket for log storage.~