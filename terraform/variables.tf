variable "key_name" {
  description = "The name of the EC2 key pair"
  type        = string
  default     = "name_of_your_ec2_key_pair"
}


variable "instance_tags" {
  type    = list(string)
  default = ["PRODUCTION", "STAGE"]
}