You are implementing a new Hummingbot CLOB spot connector for Beezee DEX.

Important context:
- Beezee DEX is an on-chain order-book DEX on the Beezee blockchain.
- Beezee chain source includes a custom `tradebin` module with generated query/tx APIs.
- Public endpoint documentation may be incomplete, so you must begin with discovery and adapt to the real Beezee interfaces.
- Do not assume Binance-style REST/WebSocket APIs unless confirmed by the code or docs.

Your mission:
Build a production-quality first version of a Beezee DEX spot connector for Hummingbot, following current Hummingbot CLOB connector architecture and conventions.

## Required workflow

### Phase 1: Discovery
Inspect the Hummingbot codebase and Beezee source/docs to determine:

1. What type of connector Beezee should be in Hummingbot
2. How Beezee exposes:
   - markets
   - order books
   - public trades
   - balances
   - orders
   - order status
   - cancellations
3. Whether trading is:
   - API-auth based
   - or wallet/transaction-signing based
4. Whether real-time updates are available through:
   - websocket
   - RPC subscriptions
   - gRPC streams
   - or polling only
5. What trading rules exist:
   - price precision
   - size precision
   - tick size
   - min size
   - fees
6. What identifiers are used:
   - market IDs
   - base/quote denoms
   - order IDs
   - tx hashes

Document findings in a markdown file before or while implementing.

If Beezee does not provide a clean private stream, implement polling fallbacks.

### Phase 2: Design
Design the Beezee connector using Hummingbot’s standard CLOB connector pieces:
- constants
- utils/config
- auth/signing module
- order book
- order book data source
- user stream data source or polling equivalent
- exchange main class
- tests

Reuse patterns from similar Hummingbot connectors where appropriate, especially on-chain CLOB style integrations if present.

### Phase 3: Implement
Implement a working v1 connector that supports:
- trading pair discovery
- trading rules
- order book snapshot
- live diff updates if available
- public trades
- balances
- create limit buy/sell orders
- cancel orders
- open order tracking
- order status tracking
- fallback polling
- fee handling
- robust logging and retries

### Phase 4: Test
Add unit tests for:
- pair mapping
- trading rules parsing
- order book parsing
- balances parsing
- order creation/cancel payloads
- order status parsing
- event parsing
- polling fallback behavior

Mock all external interactions.

## Constraints
- Spot only
- No perpetuals
- No framework-wide refactor unless absolutely necessary
- No fake placeholder implementations
- No unsupported assumptions hidden in code
- Clearly mark every assumption in comments or docs
- Keep exchange-specific logic isolated
- Use type hints and readable code
- Add a connector README with setup and limitations

## Deliverables
Produce:
1. Connector code
2. Tests
3. README
4. Discovery notes
5. A short implementation summary explaining:
   - what Beezee interfaces were found
   - what was implemented
   - what is still blocked by Beezee limitations

## Definition of done
The connector should be able to:
- initialize in Hummingbot
- discover at least one Beezee market
- fetch balances
- build an order book
- place and cancel limit orders in a safe/dev-compatible workflow
- track order status
- pass tests

Be rigorous:
If Beezee’s public API is incomplete, use the chain module/proto definitions and actual chain interaction patterns.
If something cannot be implemented safely, document the blocker precisely instead of inventing behavior.