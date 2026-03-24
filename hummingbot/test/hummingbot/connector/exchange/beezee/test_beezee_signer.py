import hashlib
import unittest

import ecdsa

from hummingbot.connector.exchange.beezee.beezee_signer import BeezeeSigner, bech32_encode


class BeezeeSignerTests(unittest.TestCase):
    def test_address_uses_cosmos_truncated_sha256(self):
        private_key_hex = "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f"

        signer = BeezeeSigner(private_key_hex, "bze")

        verifying_key = ecdsa.SigningKey.from_string(bytes.fromhex(private_key_hex), curve=ecdsa.SECP256k1).get_verifying_key()
        public_key_bytes = verifying_key.to_string("compressed")
        expected_address = bech32_encode("bze", hashlib.sha256(public_key_bytes).digest()[:20])

        self.assertEqual(expected_address, signer.address)

