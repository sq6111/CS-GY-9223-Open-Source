"""Integration tests for dependency injection."""
from chat_client_api.client import ChatClient, get_client


def test_slack_client_registration() -> None:
    """Test that importing slack_client_impl registers it."""
    import slack_client_impl  # noqa: F401

    client = get_client()
    assert isinstance(client, ChatClient)
    assert client.__class__.__name__ == "SlackClient"
