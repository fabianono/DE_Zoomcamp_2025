terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  credentials = file("~/Desktop/DE_Zoomcamp_2025/Week1/1_terraform_gcp/keys/gcred.json")
  project = "skilled-mark-448414-m8"
  region  = "us-central1"
}



resource "google_storage_bucket" "data-lake-bucket" {
  name          = "skilled-mark-448414-m8-data-lake-bucket"
  location      = "US"

  # Optional, but recommended settings:
  storage_class = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled     = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30  // days
    }
  }

  force_destroy = true
}


resource "google_bigquery_dataset" "dataset" {
  dataset_id = "<The Dataset Name You Want to Use>"
  project    = "<Your Project ID>"
  location   = "US"
}