output "instance_public_ip" {
  value = {
    for key, instance in aws_instance.web_server : key => instance.public_ip
  }
}