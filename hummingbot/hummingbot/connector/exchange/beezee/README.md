# Beezee Connector

This connector integrates Beezee DEX spot markets through the Beezee chain `tradebin` module.

## v1 support

- Market discovery from `/bze/tradebin/all_markets`
- Trading rule synthesis from denom metadata and `tradebin` params
- Order book snapshots
- Block-driven polling diffs and public trade updates
- Bank balances and Beezee dust balances
- Limit buy and sell order creation with Cosmos tx signing
- Order cancellation with Cosmos tx signing
- Open order polling and order status tracking

## Setup

Configure the connector with:

- `network=mainnet` to use Beezee mainnet defaults
- `network=testnet` to use Beezee testnet chain defaults with user-supplied testnet endpoints
- or `network=custom` to point at a local/dev Beezee REST, RPC, and websocket endpoint
- `account_type=read_only` for market data and balances only
- `account_type=wallet` for signed order placement and cancellation from a raw private key
- `account_type=wallet_mnemonic` for signed order placement and cancellation from a BIP39 mnemonic

Wallet mode requires:

- either a 32-byte secp256k1 private key in hex
- or a BIP39 mnemonic with optional passphrase and HD path
- an optional explicit Beezee address override
- gas limits for create/cancel txs

Notes:

- The mnemonic mode derives the wallet key using the Cosmos-standard default path `m/44'/118'/0'/0/0`.
- The built-in testnet preset currently only hardcodes the Beezee testnet chain settings confirmed from the upstream Beezee repo, especially `chain_id=bzetestnet-3`. REST/RPC/WS endpoints still need to be provided explicitly because no stable public testnet endpoints were confirmed in the local Beezee sources.

## Limitations

- Beezee does not expose a dedicated private stream, so v1 is polling-based for balances and order state.
- `HistoryOrder` objects do not include order ids. When the same address has multiple resting orders at the same market, side, and price, fills are allocated FIFO client-side.
- Tick size and minimum order size are not explicit per-market fields on-chain. v1 derives them from denom exponents and the chain's `CalculateMinAmount(price)` logic.
- Maker/taker fees are fixed native-denom amounts on-chain, not percentages. The connector models them as flat fees. Gas remains an external tx cost.
- Bank balances and `all_user_dust` are available, but no dedicated reserved-balance endpoint was found for open orders.

## Safe/dev workflow

Use `network=custom` to point the connector at a local or dev Beezee node. Wallet mode signs standard Cosmos protobuf transactions directly against the configured REST endpoint.
