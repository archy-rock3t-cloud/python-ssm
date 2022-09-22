"""Tests for AWS Secrets Manager wrapper module."""
from app.secrets_manager import SecretsManager


def test_secrets_manager_can_be_created():
    """Should create SecretsManager object."""
    secrets_manager = SecretsManager(None)
    assert secrets_manager.client is None
