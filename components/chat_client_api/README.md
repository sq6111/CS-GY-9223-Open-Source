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
client.send_message("general", "Hello, world!")

# List channels
channels = client.list_channels()

# Get messages
messages = client.get_messages("general", limit=20)
```

## Interface Methods

- `send_message(channel, text)`: Send a message to a channel
- `list_channels()`: Get a list of all channels
- `get_messages(channel, limit)`: Get recent messages from a channel
