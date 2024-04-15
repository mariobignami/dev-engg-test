variable "project_id" {
  description = "The Google Cloud project ID"
  type        = string
  default = "eng-skyline-420011"

}

variable "region" {
  description = "The Google Cloud region"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "The Google Cloud zone"
  type        = string
  default     = "us-central1-c"
}

variable "cluster_name" {
  description = "The Google Cloud Kubernetes cluster name"
  type        = string
  default     = "flask-demo-k8s"
}