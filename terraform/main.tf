provider "aws" {
  region = "eu-central-1"
  access_key = "your_aws_access_key"
  secret_key = "your_aws_secret_key"
}

module "custom_vpc" {
  source = "git::https://github.com/KirillKirillovich/Terraform_modules.git//modules/vpc"
}


data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"]
}

resource "aws_instance" "web_server" {
  for_each = toset(var.instance_tags)
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t2.micro"
  vpc_security_group_ids = [module.custom_vpc.custom_public_sg]
  subnet_id = module.custom_vpc.public_subnets_id[0]
  key_name                = var.key_name
  tags = {
    Name = each.key
    Environment = each.value
  }
}

resource "aws_s3_bucket" "bucket_logs_storage" {
  bucket = "aws-flask-deployer-logs"

  tags = {
    Name        = "logs storage"
  }
}