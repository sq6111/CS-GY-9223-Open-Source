"""Slack chat client implementation."""
from slack_client_impl.client import SlackClient as SlackClient

# Importing this module triggers registration in client.py
import slack_client_impl.client  # noqa: F401

__version__ = "0.1.0"
