# Chat Client API

Abstract interface for chat client implementations.

## Overview

This package provides an abstract base class (`ChatClient`) that defines the interface for chat client implementations.

## Usage
```python
from chat_client_api import get_client

# Get the registered client
client = get_client()

# Send a message
response = client.send_message("general", "Hello, world!")

# List channels
channels = client.list_channels()

# Get messages with pagination
messages = client.get_messages("general", limit=20)

# Get next page of messages using cursor
next_messages = client.get_messages("general", limit=20, cursor="next-cursor-here")
```

## Interface Methods

- `send_message(channel, text)`: Send a message to a channel
- `list_channels()`: Get a list of all channels
- `get_messages(channel, limit, cursor)`: Get recent messages from a channel with pagination support

## Data Transfer Objects

- `Message`: Represents a chat message
- `Channel`: Represents a chat channel
- `SendMessageResponse`: Response from sending a message

See the [full documentation](../../docs/components/chat_client_api.md) for detailed API reference.
