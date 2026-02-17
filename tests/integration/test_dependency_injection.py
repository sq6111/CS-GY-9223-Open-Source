"""Integration tests for dependency injection."""
import os
import sys
from unittest import mock

from chat_client_api.client import ChatClient, get_client


def test_slack_client_registration() -> None:
    """Test that importing slack_client_impl registers it."""
    # Remove module from cache to force fresh import
    if "slack_client_impl" in sys.modules:
        del sys.modules["slack_client_impl"]
    if "slack_client_impl.client" in sys.modules:
        del sys.modules["slack_client_impl.client"]

    # Reset factory
    from chat_client_api import client as client_module
    client_module._client_factory = None

    # Mock the environment variable
    with mock.patch.dict(os.environ, {"SLACK_BOT_TOKEN": "test-token"}):
        import slack_client_impl  # noqa: F401

        client = get_client()
        assert isinstance(client, ChatClient)
        assert client.__class__.__name__ == "SlackClient"
