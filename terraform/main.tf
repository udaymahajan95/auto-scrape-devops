
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

  required_version = ">= 1.6.0"
}

provider "aws" {
  region  = "us-east-1"
  profile = "autoscrape"
}

resource "aws_s3_bucket" "scraping_data" {
  bucket = "auto-scrape-devops-bucket"
}

resource "aws_iam_role" "scraper_ec2_role" {
  name = "AutoScrape-EC2-S3-Role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "scraper_s3_policy" {
  name = "AutoScrape-S3-Upload"
  role = aws_iam_role.scraper_ec2_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "s3:PutObject"
      ]
      Resource = "${aws_s3_bucket.scraping_data.arn}/automotive/*"
    }]
  })
}

resource "aws_iam_instance_profile" "scraper_profile" {
  name = "AutoScrape-EC2-Instance-Profile"
  role = aws_iam_role.scraper_ec2_role.name
}
