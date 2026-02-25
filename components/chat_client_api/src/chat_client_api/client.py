"""Abstract interface for chat clients."""
from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class Message:
    """Represents a chat message."""

    message_id: str
    channel: str
    text: str
    sender: str
    timestamp: str


@dataclass
class Channel:
    """Represents a chat channel."""

    channel_id: str
    name: str
    is_private: bool


@dataclass
class SendMessageResponse:
    """Response from sending a message."""

    message_id: str
    channel: str
    timestamp: str
    ok: bool


class ChatClient(ABC):
    """Abstract base class for chat client implementations."""

    @abstractmethod
    def send_message(self, channel: str, text: str) -> SendMessageResponse:
        """Send a message to a channel.

        Args:
            channel: Channel ID or name
            text: Message text to send

        Returns:
            SendMessageResponse with message details
        """

    @abstractmethod
    def list_channels(self) -> list[Channel]:
        """List all available channels.

        Returns:
            List of Channel objects
        """

    @abstractmethod
    def get_messages(
        self,
        channel: str,
        limit: int = 10,
    ) -> list[Message]:
        """Get recent messages from a channel.

        Args:
            channel: Channel ID or name
            limit: Maximum number of messages to retrieve

        Returns:
            List of Message objects
        """


class _ClientRegistry:
    """Holds the registered client factory — avoids global mutation."""

    _factory: Callable[[], ChatClient] | None = None

    @classmethod
    def set(cls, factory: Callable[[], ChatClient]) -> None:
        """Register a factory.

        Args:
            factory: Callable that returns a ChatClient instance
        """
        cls._factory = factory

    @classmethod
    def get(cls) -> Callable[[], ChatClient] | None:
        """Get the registered factory.

        Returns:
            The registered factory or None
        """
        return cls._factory


def get_client() -> ChatClient:
    """Get the registered chat client implementation.

    Returns:
        Instance of registered ChatClient

    Raises:
        RuntimeError: If no implementation is registered
    """
    factory = _ClientRegistry.get()
    if factory is None:
        msg = (
            "No chat client implementation registered. "
            "Import an implementation package to register it."
        )
        raise RuntimeError(msg)
    return factory()


def register_client(factory: Callable[[], ChatClient]) -> None:
    """Register a chat client implementation factory.

    Args:
        factory: Callable that returns a ChatClient instance
    """
    _ClientRegistry.set(factory)