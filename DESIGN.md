# Design Document - HW1: Chat Client

## Overview

This project implements a modular chat client system using interface-implementation separation and dependency injection.

## Architecture

### Components

1. **chat_client_api** (Interface)
   - Abstract base class defining chat operations
   - Methods: send_message, list_channels, get_messages
   - Dependency injection factory: get_client(), register_client()

2. **slack_client_impl** (Implementation)
   - Concrete Slack implementation
   - Inherits from ChatClient ABC
   - Auto-registers via dependency injection on import

### Design Decisions

**Why separate interface from implementation?**
- Allows swapping chat providers (Slack, Discord, Teams) without changing client code
- Easier testing with mocks
- Clear contracts

**Why dependency injection?**
- Loose coupling between interface and implementation
- Users code against interface, not concrete class
- Easy to swap implementations

**Why ABC (Abstract Base Class)?**
- Enforces contract at Python level
- Type checking with mypy
- Clear documentation of required methods

## Current Status (HW1)

- Interface: Complete
- Implementation: Scaffold (methods raise NotImplementedError)
- Tests: Basic integration test for DI

## Future Work

- Implement actual Slack SDK calls
- Add OAuth authentication flow
- Comprehensive unit tests
- E2E tests with real Slack workspace
