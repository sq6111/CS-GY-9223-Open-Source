# Chat Client API

Abstract interface for chat client implementations.

## Overview

The `chat_client_api` component defines the contract that all chat client implementations must follow. It provides abstract base classes, data transfer objects (DTOs), and a dependency injection mechanism.

## Data Transfer Objects (DTOs)

### Message
Represents a chat message.

**Fields:**
- `message_id: str` - Unique identifier for the message
- `channel: str` - Channel ID or name where the message was sent
- `text: str` - Content of the message
- `sender: str` - User ID of the message sender
- `timestamp: str` - Message timestamp

### Channel
Represents a chat channel.

**Fields:**
- `channel_id: str` - Unique identifier for the channel
- `name: str` - Human-readable channel name
- `is_private: bool` - Whether the channel is private

### SendMessageResponse
Response from sending a message.

**Fields:**
- `message_id: str` - ID of the sent message
- `channel: str` - Channel where message was sent
- `timestamp: str` - When the message was sent
- `ok: bool` - Whether the operation succeeded

## ChatClient Abstract Base Class

### Methods

#### send_message(channel: str, text: str) -> SendMessageResponse
Send a message to a channel.

**Parameters:**
- `channel`: Channel ID or name
- `text`: Message text to send

**Returns:** SendMessageResponse with message details

#### list_channels() -> list[Channel]
List all available channels.

**Returns:** List of Channel objects

#### get_messages(channel: str, limit: int = 10, cursor: str | None = None) -> list[Message]
Get recent messages from a channel.

**Parameters:**
- `channel`: Channel ID or name
- `limit`: Maximum number of messages to retrieve (default: 10)
- `cursor`: Pagination cursor for fetching next set of messages (optional)

**Returns:** List of Message objects

**Note:** The cursor parameter enables pagination. On first call, omit cursor to get the most recent messages. Use the cursor from the response to fetch the next page.

## Dependency Injection

### get_client() -> ChatClient
Get the registered chat client implementation.

**Returns:** Instance of registered ChatClient

**Raises:** RuntimeError if no implementation is registered

**Usage:**
```python
from chat_client_api.client import get_client
import slack_client_impl  # Side effect: registers implementation

client = get_client()
response = client.send_message("general", "Hello!")
```

### register_client(factory: Callable[[], ChatClient]) -> None
Register a chat client implementation factory.

**Parameters:**
- `factory`: Callable that returns a ChatClient instance

**Note:** Implementations should call this during module import to auto-register themselves.

## Usage Example

```python
# Import interface
from chat_client_api.client import get_client, Message

# Import implementation (registers via dependency injection)
import slack_client_impl

# Use the client
client = get_client()

# Send a message
response = client.send_message("general", "Hello, world!")
print(f"Message sent: {response.message_id}")

# List channels
channels = client.list_channels()
for channel in channels:
    print(f"Channel: {channel.name}")

# Get messages with pagination
messages = client.get_messages("general", limit=10)
for msg in messages:
    print(f"{msg.sender}: {msg.text}")
```

## Design Principles

1. **Small Surface Area:** Only three methods keep the interface simple
2. **Type Safety:** Full type hints with strict mypy checking
3. **Proper DTOs:** Structured data instead of raw dictionaries
4. **Future-Proof:** Pagination support via cursor prevents breaking changes
5. **Loose Coupling:** Dependency injection separates interface from implementation
