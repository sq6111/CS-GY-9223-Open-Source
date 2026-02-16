"""Unit tests for Slack client implementation."""
import os
from unittest import mock

import pytest
from slack_client_impl.client import SlackClient, _create_slack_client


def test_slack_client_initialization() -> None:
    """Test that SlackClient initializes with a token."""
    token = "xoxb-test-token"
    client = SlackClient(token)

    assert client.token == token


def test_send_message_raises_not_implemented() -> None:
    """Test that send_message raises NotImplementedError (scaffolded)."""
    client = SlackClient("test-token")

    with pytest.raises(NotImplementedError, match="Coming in next iteration"):
        client.send_message("general", "Hello")


def test_list_channels_raises_not_implemented() -> None:
    """Test that list_channels raises NotImplementedError (scaffolded)."""
    client = SlackClient("test-token")

    with pytest.raises(NotImplementedError, match="Coming in next iteration"):
        client.list_channels()


def test_get_messages_raises_not_implemented() -> None:
    """Test that get_messages raises NotImplementedError (scaffolded)."""
    client = SlackClient("test-token")

    with pytest.raises(NotImplementedError, match="Coming in next iteration"):
        client.get_messages("general", limit=10)


def test_create_slack_client_with_token() -> None:
    """Test factory function creates client when token is set."""
    with mock.patch.dict(os.environ, {"SLACK_BOT_TOKEN": "xoxb-test"}):
        client = _create_slack_client()

        assert isinstance(client, SlackClient)
        assert client.token == "xoxb-test"


def test_create_slack_client_without_token() -> None:
    """Test factory function raises ValueError when token is missing."""
    with mock.patch.dict(os.environ, {}, clear=True):
        with pytest.raises(
            ValueError,
            match="SLACK_BOT_TOKEN environment variable must be set",
        ):
            _create_slack_client()


def test_slack_client_inherits_from_chat_client() -> None:
    """Test that SlackClient properly inherits from ChatClient."""
    from chat_client_api.client import ChatClient

    client = SlackClient("test-token")
    assert isinstance(client, ChatClient)
