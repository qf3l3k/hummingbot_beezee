import unittest
from decimal import Decimal

from hummingbot.connector.exchange.beezee import beezee_constants as CONSTANTS
from hummingbot.connector.exchange.beezee.beezee_utils import (
    BeezeeToken,
    chain_amount_to_display,
    chain_price_to_display,
    display_amount_to_chain,
    display_price_to_chain,
    market_from_data,
    minimum_order_size_for_price,
    token_from_metadata,
    unique_market_symbols,
)


class BeezeeUtilsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base_metadata = {
            "symbol": "BZE",
            "name": "Beezee",
            "display": "bze",
            "denom_units": [
                {"denom": "ubze", "exponent": 0},
                {"denom": "bze", "exponent": 6},
            ],
        }
        self.quote_metadata = {
            "symbol": "USDC",
            "name": "USD Coin",
            "display": "usdc",
            "denom_units": [
                {"denom": "uusdc", "exponent": 0},
                {"denom": "usdc", "exponent": 6},
            ],
        }

    def test_token_from_metadata_uses_display_exponent(self):
        token = token_from_metadata("ubze", self.base_metadata)

        self.assertEqual("BZE", token.symbol)
        self.assertEqual(Decimal("0.000001"), token.quantum)

    def test_unique_market_symbols_disambiguates_duplicates(self):
        duplicate_base_metadata = {
            "factory/alt/ubze": {
                **self.base_metadata,
                "symbol": "BZE",
                "display": "altbze",
                "denom_units": [
                    {"denom": "factory/alt/ubze", "exponent": 0},
                    {"denom": "altbze", "exponent": 6},
                ],
            }
        }
        mapping = unique_market_symbols(
            markets=[
                ("ubze", "uusdc"),
                ("factory/alt/ubze", "uusdc"),
            ],
            metadatas={
                "ubze": self.base_metadata,
                "uusdc": self.quote_metadata,
                **duplicate_base_metadata,
            },
        )

        self.assertEqual("BZE-USDC", mapping["ubze/uusdc"])
        self.assertNotEqual("BZE-USDC", mapping["factory/alt/ubze/uusdc"])

    def test_market_amount_and_price_conversions(self):
        market = market_from_data(
            {"base": "ubze", "quote": "uusdc"},
            {"ubze": self.base_metadata, "uusdc": self.quote_metadata},
        )

        self.assertEqual("1230000", display_amount_to_chain(Decimal("1.23"), market.base))
        self.assertEqual(Decimal("1.23"), chain_amount_to_display("1230000", market.base))
        self.assertEqual("2.5", display_price_to_chain(Decimal("2.5"), market))
        self.assertEqual(Decimal("2.5"), chain_price_to_display("2.5", market))

    def test_minimum_order_size_uses_chain_rule(self):
        base = BeezeeToken(denom="ubze", symbol="BZE", display_name="Beezee", display_denom="bze", exponent=6)
        quote = BeezeeToken(denom="uusdc", symbol="USDC", display_name="USD Coin", display_denom="usdc", exponent=6)
        market = market_from_data(
            {"base": base.denom, "quote": quote.denom},
            {
                base.denom: self.base_metadata,
                quote.denom: self.quote_metadata,
            },
        )

        self.assertEqual(Decimal("0.000004"), minimum_order_size_for_price("0.5", market))
        self.assertEqual(
            Decimal("0.000000001"),
            market.min_price_increment,
        )
        self.assertEqual(CONSTANTS.DEFAULT_PRICE_SIG_DIGITS, 10)

