# Architecture

```text
Employee
   |
   v
Standalone HTML UI
   |
   v
Request Analyzer
   |
   +----> Supplied policy data (KB-01–KB-10, AMP)
   +----> Supplied employee requests
   +----> Supplied ticket history
   |
   v
Deterministic Decision Engine
   +---- Resolve
   +---- Clarify
   +---- Route
   +---- Escalate
   |
   v
Structured Ticket (Route/Escalate only)
   |
   v
Session Audit Trail
```

## Design principle

**Resolve what is safe. Route what requires authority. Escalate what is risky. Ask when information is missing.**

## Data boundary
The prototype is restricted to the supplied Assignment 2 data pack. Historical ticket records can provide context, but they are not treated as additional policy.
