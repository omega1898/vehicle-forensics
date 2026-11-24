# vehicle-forensics

Field-deployable vehicle data triage and extraction, built as a starting point for Navy SBIR topic **DON27BZ02-NV006, Mobile Vehicle Forensics** (DoW FY27 Release 2).

## The problem

Vehicles hold GPS track logs, paired phones, Bluetooth and Wi-Fi history in their telematics and infotainment units. Today's tools are built for labs, each manufacturer uses proprietary designs, and field teams may have to pull a dashboard apart to get data. The topic asks for a rugged, portable device that connects through OBD-II or USB, identifies the vehicle, and extracts priority data quickly without disassembly while preserving forensic integrity.

## Approach in plain terms

1. **Connect** through the OBD-II port or a USB port, read only.
2. **Profile** the vehicle (make, model year, which modules respond) to pick the right extraction method.
3. **Extract** priority data with an automated script for that profile.
4. **Seal** every output with a cryptographic hash and a chain-of-custody record, so it can be shown later that nothing changed.

## Phase I scope

A feasibility study and initial architecture, projected extraction speeds and limits, and a Phase II plan. Performance goals: under 15 minutes for high-priority data (threshold), under 5 minutes in a pocket-sized device (objective). See [docs/topic-summary.md](docs/topic-summary.md).

## Status

Skeleton only. The first vertical slice works from a recorded capture file, so no vehicle or hardware is needed yet. See [docs/architecture.md](docs/architecture.md).

## How to run

```bash
python -m unittest discover -s tests -v
```

## Documentation

- [docs/topic-summary.md](docs/topic-summary.md): what the public topic asks for
- [docs/topic-qa.md](docs/topic-qa.md): posted topic Q&A
- [docs/references.md](docs/references.md): the topic's references, with links
- [docs/submission-requirements.md](docs/submission-requirements.md): dates, award size, official instructions
- [docs/architecture.md](docs/architecture.md): first vertical slice and design decisions
