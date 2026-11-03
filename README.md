# Shield billing service

**Application:** Billing & Customer (`billing-customer`)

**Component:** `CM-BILLING`

**Owner:** Billing platform

`src/billing/service.py` reads policy premiums through a `get_policy` callback
from `shield-policy-service` and issues synthetic claim payouts.
Payouts are idempotent by claim ID for the lifetime of a service instance;
a conflicting retry raises an error. This in-memory fixture does not move money
and does not provide durable payment idempotency.

`contracts/billing-api.yaml` describes the intended API. Shared context lives in
`amithp-ust/shield-context`; read its `AGENTS.md`, glossary, scope, and standards.
`specs/` is empty pending specification pull requests.
Python 3.12+, standard library only. Run `python -m unittest discover -s tests`.
These are callable stubs, not deployed HTTP services.
