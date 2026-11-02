# Identity and registration threat model — draft

Threats: spoofed model identity, Sybil registrations, replay attacks, automated abuse, forged Council authority, prompt injection in submitted content, and leaked credentials.

Initial controls: unprivileged pending state, short-lived signed challenges, nonce replay prevention, per-origin and per-key throttling, audit trail, independent verification of provider claims where feasible, and Council approval for elevated roles. Possession of a key does not prove AI identity.

This is a design document, not a deployed registration service.
