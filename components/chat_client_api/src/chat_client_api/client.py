"""Abstract interface for chat clients."""
from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any


class ChatClient(ABC):
    """Abstract base class for chat client implementations."""

    @abstractmethod
    def send_message(self, channel: str, text: str) -> dict[str, Any]:
        """Send a message to a channel.

        Args:
            channel: Channel ID or name
            text: Message text to send

        Returns:
            Response from the chat service

        """

    @abstractmethod
    def list_channels(self) -> list[dict[str, Any]]:
        """List all available channels.

        Returns:
            List of channel information dictionaries

        """

    @abstractmethod
    def get_messages(
        self,
        channel: str,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Get recent messages from a channel.

        Args:
            channel: Channel ID or name
            limit: Maximum number of messages to retrieve

        Returns:
            List of message dictionaries

        """


# Dependency injection factory
_client_factory: Callable[[], ChatClient] | None = None


def get_client() -> ChatClient:
    """Get the registered chat client implementation.

    Returns:
        Instance of registered ChatClient

    Raises:
        RuntimeError: If no implementation is registered

    """
    if _client_factory is None:
        msg = (
            "No chat client implementation registered. "
            "Import an implementation package to register it."
        )
        raise RuntimeError(msg)
    return _client_factory()


def register_client(factory: Callable[[], ChatClient]) -> None:
    """Register a chat client implementation factory.

    Args:
        factory: Callable that returns a ChatClient instance

    """
    global _client_factory  # noqa: PLW0603
    _client_factory = factory
