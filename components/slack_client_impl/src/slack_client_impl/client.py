"""Slack implementation of ChatClient."""

import os

from chat_client_api.client import (
    Channel,
    ChatClient,
    Message,
    SendMessageResponse,
    register_client,
)


class SlackClient(ChatClient):
    """Slack implementation of the ChatClient interface."""

    def __init__(self, token: str) -> None:
        """Initialize Slack client.

        Args:
            token: Slack bot token

        """
        self.token = token

    def send_message(self, channel: str, text: str) -> SendMessageResponse:
        """Send a message to a Slack channel."""
        msg = "Coming in next iteration"
        raise NotImplementedError(msg)

    def list_channels(self) -> list[Channel]:
        """List all Slack channels."""
        msg = "Coming in next iteration"
        raise NotImplementedError(msg)

    def get_messages(
        self,
        channel: str,
        limit: int = 10,
    ) -> list[Message]:
        """Get recent messages from a Slack channel."""
        msg = "Coming in next iteration"
        raise NotImplementedError(msg)


def _create_slack_client() -> SlackClient:
    """Create Slack client from environment variables."""
    token = os.getenv("SLACK_BOT_TOKEN")
    if not token:
        msg = "SLACK_BOT_TOKEN environment variable must be set"
        raise ValueError(msg)
    return SlackClient(token)


# Register this implementation when the module is imported
register_client(_create_slack_client)
