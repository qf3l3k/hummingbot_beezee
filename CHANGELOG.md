# Changelog

This project follows semantic versioning.

## [Unreleased]

- No entries yet

## [0.2.0] - 2026-03-23

- Added Beezee mnemonic wallet mode with BIP39 seed support
- Added configurable mnemonic passphrase and HD derivation path support
- Added Beezee testnet network mode
- Added example Beezee connector configuration under `config/`
- Updated Beezee testnet default to `bzetestnet-3`
- Updated Beezee connector docs for mainnet/testnet and mnemonic usage
- Extended Beezee unit tests for mnemonic and testnet configuration

## [0.1.0] - 2026-03-23

- Initial Beezee DEX spot connector for Hummingbot
- Added Beezee market discovery and trading pair mapping
- Added trading rule synthesis from chain metadata
- Added order book snapshots, diff polling, and public trade polling
- Added bank balance and Beezee dust balance support
- Added limit order create/cancel flow through Cosmos transaction signing
- Added polling-based order status tracking and fill attribution
- Added Beezee discovery notes and connector README
- Added mocked Beezee unit tests
