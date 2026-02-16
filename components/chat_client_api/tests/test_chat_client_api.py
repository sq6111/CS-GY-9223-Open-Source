"""Unit tests for chat client API."""
from typing import Any

import pytest

from chat_client_api.client import ChatClient, get_client, register_client


def test_get_client_raises_when_no_implementation_registered() -> None:
    """Test that get_client raises RuntimeError when no implementation is registered."""
    # Reset factory to None
    import chat_client_api.client as client_module

    client_module._client_factory = None

    with pytest.raises(RuntimeError, match="No chat client implementation registered"):
        get_client()


def test_register_client_stores_factory() -> None:
    """Test that register_client stores the factory function."""
    import chat_client_api.client as client_module

    # Create a mock factory
    class MockClient(ChatClient):
        def send_message(self, channel: str, text: str) -> dict[str, Any]:
            return {}

        def list_channels(self) -> list[dict[str, Any]]:
            return []

        def get_messages(
            self,
            channel: str,
            limit: int = 10,
        ) -> list[dict[str, Any]]:
            return []

    def mock_factory() -> ChatClient:
        return MockClient()

    # Register the factory
    register_client(mock_factory)

    # Verify it was stored
    assert client_module._client_factory is not None

    # Verify get_client returns the mock client
    client = get_client()
    assert isinstance(client, MockClient)


def test_get_client_returns_registered_implementation() -> None:
    """Test that get_client returns the registered implementation."""

    class TestClient(ChatClient):
        def send_message(self, channel: str, text: str) -> dict[str, Any]:
            return {"ok": True}

        def list_channels(self) -> list[dict[str, Any]]:
            return [{"id": "C123", "name": "general"}]

        def get_messages(
            self,
            channel: str,
            limit: int = 10,
        ) -> list[dict[str, Any]]:
            return [{"text": "Hello"}]

    def test_factory() -> ChatClient:
        return TestClient()

    register_client(test_factory)

    client = get_client()
    assert isinstance(client, TestClient)
    result = client.send_message("test", "msg")
    assert result["ok"] is True
