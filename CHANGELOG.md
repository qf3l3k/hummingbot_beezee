# Changelog

This project follows semantic versioning.

## [Unreleased]

- No entries yet

## [0.4.0] - 2026-07-16

- Stabilized Beezee order resolution and prevented duplicate order-created events after a confirmed order transaction
- Added safe recovery of Beezee native order ids after Hummingbot restart using confirmed transaction, order details, and creation time
- Kept ambiguous order-id matches unresolved rather than risking cancellation of an unrelated order
- Added tx hash and unresolved-order diagnostics for live order lifecycle troubleshooting
- Treated empty or invalid order books as unavailable prices instead of propagating non-finite values to Hummingbot's rate oracle
- Added regression coverage for restart recovery and empty/non-finite order-book price handling

## [0.3.1] - 2026-07-15

- Deferred cancel requests until Beezee resolves the on-chain exchange order id
- Replaced cancel-order exceptions during order-id resolution with normal polling retries
- Added regression coverage for unresolved cancel requests

## [0.3.0] - 2026-07-15

- Prevented Hummingbot from marking Beezee cancel requests complete before on-chain transaction confirmation
- Made Beezee order-id resolution conservative by excluding pre-existing orders and refusing ambiguous candidates
- Prevented historical fills from being attributed to orders created after those trades
- Added polling and reconnect recovery after Beezee block websocket disconnections
- Added transaction-hash logging for create-order and cancel-order broadcasts
- Added regression coverage for pending cancel confirmation and ambiguous exchange-order candidates

## [0.2.1] - 2026-03-26

- Fixed Beezee dynamic REST throttler ids for denom metadata, balances, tx, and user order endpoints
- Added denom metadata URL encoding and query-string fallback for IBC and factory denoms
- Added native `ubze` fallback metadata and reduced repeated missing-metadata log spam
- Added Beezee server time helper required by Hummingbot exchange polling
- Fixed connector config handling for encrypted mnemonic and private-key values at load time
- Passed Beezee read-only address through Hummingbot connect and balance flows
- Fixed Beezee signer address hashing to match the Beezee Cosmos SDK account format
- Added wallet address consistency checks and startup logging for signer/configured account validation
- Relaxed readiness gating for Beezee polling-based private state and symbol-map startup
- Added readiness diagnostics that log pending Beezee connector status flags
- Fixed Cosmos account sequence handling for concurrent order and cancel transactions
- Improved cancel flow to resolve Beezee exchange order ids before broadcasting cancel transactions
- Verified working testnet flow for balances, order book initialization, and order create/cancel submission

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
