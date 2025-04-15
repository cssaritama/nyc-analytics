provider "google" {
  project = var.project_id
  region  = "us-central1"
}

resource "google_storage_bucket" "data_lake" {
  name          = "nyc-taxi-data-lake-2025-cssaritama"
  location      = "US"
  force_destroy = true
}

resource "google_bigquery_dataset" "nyc_taxi" {
  dataset_id = "nyc_taxi_analytics"
  location   = "US"
}
