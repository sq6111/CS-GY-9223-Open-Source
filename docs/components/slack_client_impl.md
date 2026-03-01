# Slack Client Implementation

Concrete Slack implementation of the ChatClient interface.

## Overview

The `slack_client_impl` component provides a Slack-specific implementation of the abstract `ChatClient` interface. It automatically registers itself via dependency injection when imported.

## Current Status

**HW1 - Scaffold Implementation**

All methods are currently scaffolded and raise `NotImplementedError`. The implementation demonstrates:
- Proper interface inheritance
- Dependency injection registration
- Environment-based configuration
- Type safety with full annotations

## SlackClient Class

### Initialization

```python
def __init__(self, token: str) -> None:
    """Initialize Slack client.

    Args:
        token: Slack bot token
    """
```

The client expects a Slack bot token for authentication.

### Methods

#### send_message(channel: str, text: str) -> SendMessageResponse
Send a message to a Slack channel.

**Status:** Not yet implemented (HW1)
**Future:** Will use Slack Web API `chat.postMessage`

#### list_channels() -> list[Channel]
List all Slack channels.

**Status:** Not yet implemented (HW1)
**Future:** Will use Slack Web API `conversations.list`

#### get_messages(channel: str, limit: int = 10, cursor: str | None = None) -> list[Message]
Get recent messages from a Slack channel.

**Status:** Not yet implemented (HW1)
**Future:** Will use Slack Web API `conversations.history` with pagination support

**Parameters:**
- `channel`: Slack channel ID or name
- `limit`: Maximum number of messages to retrieve
- `cursor`: Pagination cursor for next page of results

## Dependency Injection

### Auto-Registration

The implementation automatically registers itself when imported:

```python
# At module level in client.py
register_client(_create_slack_client)
```

### Factory Function

```python
def _create_slack_client() -> SlackClient:
    """Create Slack client from environment variables."""
    token = os.getenv("SLACK_BOT_TOKEN")
    if not token:
        raise ValueError("SLACK_BOT_TOKEN environment variable must be set")
    return SlackClient(token)
```

## Configuration

### Environment Variables

- `SLACK_BOT_TOKEN`: Required Slack bot token for authentication

**Example:**
```bash
export SLACK_BOT_TOKEN="xoxb-your-token-here"
```

## Usage Example

```python
import os
from chat_client_api.client import get_client

# Set environment variable
os.environ["SLACK_BOT_TOKEN"] = "xoxb-your-token"

# Import implementation (auto-registers)
import slack_client_impl

# Get client instance
client = get_client()

# Use the client (currently raises NotImplementedError in HW1)
# response = client.send_message("general", "Hello!")
```

## Testing

### Unit Tests

Tests verify:
- Proper initialization with token
- Correct inheritance from ChatClient
- Factory function behavior
- Error handling for missing token

### Integration Tests

Integration test in `tests/integration/test_dependency_injection.py` verifies:
- Import side effect registers the client
- `get_client()` returns SlackClient instance
- Full dependency injection flow works

### E2E Tests

E2E test exists but is currently skipped (requires real Slack credentials).

## Future Implementation (HW2+)

The next iteration will implement:

1. **Slack SDK Integration**
   - Use official `slack_sdk` package
   - Implement Web API client

2. **Authentication**
   - OAuth 2.0 flow
   - Token refresh handling
   - Secure token storage

3. **Error Handling**
   - API rate limiting
   - Network errors
   - Invalid channel handling

4. **Pagination**
   - Implement cursor-based pagination
   - Handle Slack's response metadata
   - Return next cursor to caller

5. **Message Formatting**
   - Support Slack markdown
   - Handle mentions and channels
   - Emoji support
