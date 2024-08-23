variable "key_name" {
  description = "The name of the EC2 key pair"
  type        = string
  default     = "key_name"
}


variable "instance_tags" {
  type    = list(string)
  default = ["PRODUCTION", "STAGE"]
}