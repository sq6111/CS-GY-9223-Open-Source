"""Integration tests for dependency injection."""
import os
from unittest import mock

from chat_client_api.client import ChatClient, get_client


def test_slack_client_registration() -> None:
    """Test that importing slack_client_impl registers it."""
    # Mock the environment variable so we don't need real credentials
    with mock.patch.dict(os.environ, {"SLACK_BOT_TOKEN": "test-token"}):
        import slack_client_impl  # noqa: F401

        client = get_client()
        assert isinstance(client, ChatClient)
        assert client.__class__.__name__ == "SlackClient"
