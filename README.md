# Hummingbot Beezee Connector

Beezee DEX spot connector for Hummingbot.

This repository contains:

- Beezee exchange connector code under `hummingbot/hummingbot/connector/exchange/beezee/`
- Beezee connector tests under `hummingbot/test/hummingbot/connector/exchange/beezee/`
- example config under `config/beezee.example.yml`
- release notes under `release_notes/`

Current validated state:

- standalone Hummingbot startup
- Beezee testnet connectivity
- balance retrieval
- order book initialization
- signed order submission
- signed order cancellation

Recommended trading mode:

- `account_type=wallet`

Documentation:

- connector README: `hummingbot/hummingbot/connector/exchange/beezee/README.md`
- discovery notes: `hummingbot/hummingbot/connector/exchange/beezee/DISCOVERY.md`
- changelog: `CHANGELOG.md`

Known note:

- mnemonic mode exists, but private-key wallet mode is the currently validated path for testnet trading.
