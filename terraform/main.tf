terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 6.0"
}
 }

  required_version = ">= 1.6.0"
}

provider "aws"{
   region = "us-east-1"
   profile = "autoscrape"
}

resource "aws_s3_bucket" "scraping_data" {
   bucket = "auto-scrape-devops-bucket"
}
