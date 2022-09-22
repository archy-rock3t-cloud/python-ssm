"""Module for interaction with AWS Secrets Manager."""


class SecretsManager:
    """Wrapper for AWS Secrets Manager."""

    def __init__(self, boto3_client):
        self.client = boto3_client
