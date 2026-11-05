# Shield billing service

**Application:** Billing & Customer (`billing-customer`)

**Component:** `CM-BILLING`

**Owner:** Billing platform

`src/billing/service.py` reads policy premiums through a `get_policy` callback
from `shield-policy-service` and issues synthetic claim payouts.
Payouts are idempotent by claim ID for the lifetime of a service instance;
a conflicting retry raises an error. This in-memory fixture does not move money
and does not provide durable payment idempotency.

`contracts/billing-api.yaml` describes the intended API.

## Specification consumer

Canonical specs, authoring, gates, and requirement metrics live only in
[`amithp-ust/Intent-to-spec`](https://github.com/amithp-ust/Intent-to-spec).
Shared glossary, map, standards, and policy remain in
[`amithp-ust/shield-context`](https://github.com/amithp-ust/shield-context).
This repo owns `CM-BILLING` implementation, not spec authoring. See
[AGENTS.md](AGENTS.md) for immutable approved spec references, issue/PR traceability,
human review, and fixture-contract checks. Do not install authoring here or copy
specs; empty `specs/.gitkeep` is a legacy placeholder.

Python 3.11+, standard library only. Run `python -m unittest discover -s tests`
from this repository root; the unit-test CI runs the same command on Python 3.11.
These are callable stubs, not deployed HTTP services.
