# Campaign State Machine

```text
DISCOVERED
  ↓
ROUTING_REQUIRED
  ↓
EVIDENCE_INCOMPLETE
  ├── fatal FAIL → REJECTED
  ├── track mismatch → REROUTED
  └── UNKNOWN → BLOCKED
            ↓
      EVIDENCE_ACTION
            ↓
      EVIDENCE_UPDATED
            └── replay CG
                     ↓
               PUBLIC_GATES_PASS
                     ↓
               SECRET_SUITE
                     ├── FAIL → BLOCKED/REJECTED
                     ↓
              SUPPLIER_EXECUTABLE
                     ↓
                 LAUNCHABLE
                     ↓
                 LIVE_PROBE
                     ↓
       ┌─────────────┼──────────────┐
       ↓             ↓              ↓
    PROVEN        MUTATE          KILLED
       ↓
 OWNERSHIP_BUILD
```

## No direct transitions

Forbidden:
- DISCOVERED → ATTACK
- WATCH → BUILD because score improved
- BLOCKED → PASS from CGE mutation alone
- UNKNOWN → PASS without new verified evidence

## Reroute is success

Examples:
- UFH thermostat D2C → service lead/orchestration;
- marine pump consumer → B2B engineer resolver;
- Automower → BENCHMARK.

A reroute preserves learned evidence and can create a valuable child campaign.
