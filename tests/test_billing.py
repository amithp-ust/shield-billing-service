import unittest

from src.billing.service import BillingService


class BillingTests(unittest.TestCase):
    def setUp(self):
        self.service = BillingService(lambda policy_id: {"premium_cents": 5000})

    def test_premium(self):
        self.assertEqual(self.service.premium_schedule("P-1"), {
            "policy_id": "P-1", "annual_premium_cents": 5000, "currency": "USD",
        })

    def test_idempotent_payout(self):
        first = self.service.create_payout("CL-1", 40000)
        self.assertEqual(first, self.service.create_payout("CL-1", 40000))
        first["amount_cents"] = 1
        self.assertEqual(
            self.service.create_payout("CL-1", 40000)["amount_cents"], 40000
        )

    def test_conflicting_payout(self):
        self.service.create_payout("CL-1", 40000)
        with self.assertRaises(ValueError):
            self.service.create_payout("CL-1", 30000)

    def test_invalid_amount(self):
        for amount in (0, -1, True, 1.5):
            with self.subTest(amount=amount):
                with self.assertRaises(ValueError):
                    self.service.create_payout("CL-1", amount)
