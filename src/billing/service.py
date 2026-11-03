"""Premium schedules and synthetic payouts (CM-BILLING)."""

from collections.abc import Callable


class BillingService:
    def __init__(self, get_policy: Callable):
        self.get_policy = get_policy
        self._payouts: dict[str, dict] = {}

    def premium_schedule(self, policy_id: str) -> dict:
        policy = self.get_policy(policy_id)
        return {
            "policy_id": policy_id,
            "annual_premium_cents": policy["premium_cents"],
            "currency": "USD",
        }

    def create_payout(self, claim_id: str, amount_cents: int) -> dict:
        if not claim_id:
            raise ValueError("claim_id is required")
        if type(amount_cents) is not int or amount_cents <= 0:
            raise ValueError("amount_cents must be a positive integer")
        if claim_id in self._payouts:
            payout = self._payouts[claim_id]
            if payout["amount_cents"] != amount_cents:
                raise ValueError("Conflicting payout amount for claim")
            return dict(payout)
        payout = {
            "payout_id": f"PAY-{claim_id}",
            "claim_id": claim_id,
            "amount_cents": amount_cents,
            "currency": "USD",
        }
        self._payouts[claim_id] = payout
        return dict(payout)
