"""Unit tests for chat client API."""

import pytest
from chat_client_api.client import (
    Channel,
    ChatClient,
    Message,
    SendMessageResponse,
    _ClientRegistry,
    get_client,
    register_client,
)


def setup_function() -> None:
    """Reset registry before each test."""
    _ClientRegistry._factory = None


class MockClient(ChatClient):
    """Mock client for testing."""

    def send_message(self, channel: str, text: str) -> SendMessageResponse:
        """Send a mock message."""
        return SendMessageResponse(
            message_id="123",
            channel=channel,
            timestamp="12345.678",
            ok=True,
        )

    def list_channels(self) -> list[Channel]:
        """List mock channels."""
        return [
            Channel(channel_id="C123", name="general", is_private=False),
        ]

    def get_messages(
        self,
        channel: str,
        limit: int = 10,
    ) -> list[Message]:
        """Get mock messages."""
        return [
            Message(
                message_id="1",
                channel=channel,
                text="Hello",
                sender="U123",
                timestamp="12345.678",
            ),
        ]


def test_get_client_raises_when_no_implementation_registered() -> None:
    """Test that get_client raises RuntimeError when no implementation is registered."""
    with pytest.raises(RuntimeError, match="No chat client implementation registered"):
        get_client()


def test_register_client_stores_factory() -> None:
    """Test that register_client stores the factory function."""

    def mock_factory() -> ChatClient:
        """Create a mock client."""
        return MockClient()

    register_client(mock_factory)
    assert _ClientRegistry.get() is not None


def test_get_client_returns_registered_implementation() -> None:
    """Test that get_client returns the registered implementation."""
    register_client(MockClient)
    client = get_client()
    assert isinstance(client, MockClient)


def test_send_message_returns_correct_dto() -> None:
    """Test send_message returns a SendMessageResponse."""
    register_client(MockClient)
    client = get_client()
    result = client.send_message("general", "hello")
    assert isinstance(result, SendMessageResponse)
    assert result.ok is True
    assert result.channel == "general"


def test_list_channels_returns_channel_list() -> None:
    """Test list_channels returns a list of Channel DTOs."""
    register_client(MockClient)
    client = get_client()
    channels = client.list_channels()
    assert isinstance(channels[0], Channel)
    assert channels[0].name == "general"


def test_get_messages_returns_message_list() -> None:
    """Test get_messages returns a list of Message DTOs."""
    register_client(MockClient)
    client = get_client()
    messages = client.get_messages("general")
    assert isinstance(messages[0], Message)
    assert messages[0].text == "Hello"
