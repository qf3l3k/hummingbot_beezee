\# Beezee DEX Connector for Hummingbot

\## Project Goal



Develop a new Hummingbot \*\*CLOB spot connector\*\* for \*\*Beezee DEX\*\*.



The connector should integrate directly into the Hummingbot client, following the current connector architecture used for CLOB connectors.



\## Background



Beezee DEX is an on-chain order-book DEX on the Beezee blockchain.

The Beezee chain source code includes a custom `tradebin` module with generated query and tx APIs.

Public docs clearly indicate Beezee DEX is order-book based, but public endpoint documentation may be incomplete or not centralized.



Because of that, this project must begin with an \*\*API/protocol discovery phase\*\* and build an adapter layer from real Beezee interfaces rather than assuming a centralized-exchange API design.



\## Scope v1



Implement a \*\*spot-only\*\* connector that supports:



1\. Exchange initialization

2\. Market/trading pair discovery

3\. Trading rules loading

4\. Order book snapshot retrieval

5\. Order book diff / live updates

6\. Public trade stream

7\. Account balance retrieval

8\. Order placement

9\. Order cancellation

10\. Active order tracking

11\. Order status polling fallback

12\. User stream / private event handling if Beezee supports it

13\. Fee handling

14\. Unit tests with mocked network/protocol interactions



\## Out of Scope v1



\- Perpetuals

\- Margin

\- Gateway connector implementation

\- Arbitrary IBC deposit/withdraw management

\- UI/dashboard changes

\- Strategy development beyond smoke-test examples

\- Production deployment docs beyond local developer setup



\## Functional Requirements



\### A. Connector Type

\- Implement as a Hummingbot \*\*CLOB connector\*\*

\- Place code in the appropriate Hummingbot connector path for spot exchanges

\- Follow existing connector conventions and naming patterns



\### B. Discovery Phase

Before implementation, determine and document:



1\. How Beezee DEX market data is exposed:

&#x20;  - REST

&#x20;  - WebSocket

&#x20;  - Tendermint RPC

&#x20;  - Cosmos gRPC / gRPC-gateway

&#x20;  - indexer API

&#x20;  - custom node API



2\. How private trading actions are submitted:

&#x20;  - REST API with auth

&#x20;  - blockchain transaction signing and broadcast

&#x20;  - wallet-based signing flow

&#x20;  - custom sequence/account-number transaction flow



3\. How order updates are retrieved:

&#x20;  - WebSocket private stream

&#x20;  - polling query endpoints

&#x20;  - transaction result parsing

&#x20;  - on-chain event subscriptions



4\. How balances are obtained:

&#x20;  - bank balances query

&#x20;  - spendable balances

&#x20;  - reserved/in-order balances if available



5\. How market metadata is represented:

&#x20;  - base denom

&#x20;  - quote denom

&#x20;  - tick size

&#x20;  - lot size

&#x20;  - min order size

&#x20;  - fees

&#x20;  - active/inactive market flags



\### C. Market Data

The connector must support:

\- fetching all supported trading pairs

\- translating exchange notation ↔ Hummingbot notation

\- full order book snapshot retrieval

\- incremental updates if available

\- public trade events

\- last traded price / best bid / best ask retrieval



If no WebSocket exists:

\- implement robust polling fallback

\- document performance limitations



\### D. Trading

The connector must support:

\- limit buy orders

\- limit sell orders

\- order cancellation

\- order status lookup

\- open orders retrieval

\- client order ID mapping to exchange/on-chain order IDs

\- proper tracking of submitted, open, partially filled, filled, cancelled, and failed orders



\### E. Authentication / Signing

Codex must determine the correct auth model:

\- API-key style auth, if Beezee exposes one

\- OR wallet-based tx signing and broadcast if trading is done on-chain



If wallet signing is required:

\- design the connector so sensitive signing logic is isolated

\- support config inputs for wallet/private key or signer backend

\- do not hardcode secrets

\- use environment/config-based secret loading



\### F. Fees

The connector must:

\- identify maker/taker fees if exposed

\- otherwise define a conservative default fee model and clearly mark assumptions

\- include network / gas fee handling if relevant to on-chain order placement/cancel



\### G. Resilience

Implement:

\- retry logic

\- rate-limit awareness

\- timeout handling

\- reconnect logic for streams

\- fallback polling when real-time streams are unavailable

\- detailed logging for network/protocol failures



\### H. Testing

Add unit tests for:

\- pair mapping

\- trading rules parsing

\- order book parsing

\- order placement payload construction

\- cancel payload construction

\- order status translation

\- balance parsing

\- fee parsing

\- websocket message parsing if applicable

\- fallback polling behavior



Tests must mock all network/protocol calls.



\## Technical Constraints



1\. Use current Hummingbot connector architecture and patterns.

2\. Prefer reusing code patterns from existing CLOB DEX connectors if suitable.

3\. Keep exchange-specific logic isolated in Beezee modules.

4\. Avoid introducing broad framework-level changes unless strictly necessary.

5\. Keep code readable, type-safe, and well logged.

6\. Add docstrings and a small developer README for the connector.



\## Expected Deliverables



1\. New Beezee connector source files

2\. Connector constants/config utils

3\. Auth/signing module

4\. Order book module

5\. Order book data source

6\. User stream data source or equivalent polling layer

7\. Exchange connector main class

8\. Unit tests

9\. Developer README

10\. Discovery notes documenting actual Beezee endpoints/protocols found

11\. Gap list describing unsupported features or missing upstream Beezee APIs



\## Acceptance Criteria



The connector is accepted for v1 when:

\- Hummingbot can load the connector

\- at least one Beezee market can be discovered

\- trading rules are parsed correctly

\- order book can be built and refreshed

\- balances can be fetched

\- limit buy/sell orders can be submitted in paper/dev testing

\- order status and cancellation work

\- tests pass locally

\- all assumptions and protocol limitations are documented

