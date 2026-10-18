resource "aws_security_group" "scraper_sg" {
  name        = "auto-scrape-sg"
  description = "Security group for AutoScrape EC2"

  ingress {
    description = "SSH from my IP"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["103.127.21.65/32"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "scraper_server" {
  ami                  = "ami-0d27e0fb3bac4d724"
  instance_type        = "t3.micro"
  key_name             = "auto-scrape-key"
  iam_instance_profile = aws_iam_instance_profile.scraper_profile.name
  vpc_security_group_ids = [
    aws_security_group.scraper_sg.id
  ]

  root_block_device {
    volume_size = 8
    volume_type = "gp3"
  }

  tags = {
    Name = "AutoScrape-Server"
  }
}
