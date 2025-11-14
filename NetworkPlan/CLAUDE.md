# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Fairfield House Network Design & Low-Voltage Project**

This repository contains design documentation, planning documents, and utilities for a comprehensive network and structured cabling installation in a 3-storey UK residential property. The project focuses on:

- Structured cabling design (fibre backbone + Cat6 distribution)
- Ubiquiti Wi-Fi deployment with QoS-aware traffic management
- Dual-WAN (legacy broadband + high-performance 5G)
- Network rack deployment in a dedicated first-floor server room
- High-performance lab network with 10G connectivity

**Key constraint:** The building has thick concrete/breezeblock structural walls and solid concrete floor slabs that impose severe RF attenuation and make cable routing challenging.

## Architecture

### Design Philosophy

The network design uses a **structured star topology** with all cables home-running to a central rack room on the first floor. Key architectural decisions:

1. **Primary vertical riser:** Bathroom/service stack (ground → first-floor rack room → second-floor bathrooms)
2. **Secondary vertical riser:** Stair core (for supplemental horizontal distribution)
3. **Fibre backbone:** Links rack room to ground-floor lab for 10G capability
4. **Wired AP backhaul:** All APs use Ethernet (not wireless mesh) due to RF barriers
5. **VLAN segmentation:** LAB (10) / HOME (20) / IOT (30) / GUEST (40) / Management (99)

### Directory Structure

```
FairfieldSpatialBOM/
├── docs/               # Requirements and analysis documentation
│   ├── requirements.md          # Top-level project requirements
│   ├── floor-alignment.md       # Floor plans, voids, and vertical riser strategy
│   └── radio-qos-analysis.md    # RF propagation, AP placement, QoS design
├── design/             # Detailed design specifications
│   └── cable-routing.md         # Physical cable paths and containment
├── scripts/            # Automation and utilities
│   └── align_floorplans.py      # Composite floorplan generator
├── FairfieldSpatial/   # Source floorplan images and generated composites
└── .env                # API keys (Perplexity for research tasks)
```

### Floorplan Coordinate System

**Critical:** All floorplan images are oriented with **west at the top**. This affects:
- Directional references in documentation (e.g., "west elevation" means top of images)
- Cable routing descriptions
- AP placement annotations

Use `scripts/align_floorplans.py` to generate a vertically-stacked composite that aligns structural features (stairs, bathroom stacks) across floors.

## Key Technical Constraints

### RF Propagation Model

The building materials impose strict RF limitations that drive the wired-first architecture:

| Material | 2.4 GHz | 5 GHz | 6 GHz |
|----------|---------|-------|-------|
| Structural walls (concrete/breezeblock) | 10-15 dB | 15-25 dB | 20-30 dB |
| Internal partitions (stud/plaster) | 3-6 dB | 5-10 dB | 6-12 dB |
| Floor slabs (solid concrete) | 15-25 dB | 25-35 dB | 30+ dB |

**Implication:** Do not assume wireless mesh will work. Each floor requires dedicated wired APs, and structural walls act as zone boundaries.

### Cable Routing Constraints

1. **No ceiling voids:** Solid concrete slabs with flat plasterboard ceilings—not accessible for horizontal runs
2. **Minimize external runs:** West façade (top of plans) should remain clear except for 5G antenna feed
3. **Grouped slab penetrations:** All floor penetrations must occur at designated riser points (bathroom/rack stack or stair core)
4. **Concealment strategy:** Chasing into concrete is minimized; use internal partitions, skirting-level trunking, or joinery boxing where necessary

## Working with Floorplans

### Generating Composite Images

```bash
python3 scripts/align_floorplans.py
```

This creates `FairfieldSpatial/composite_floorplans.png` by stacking the three floorplan images vertically with configurable x/y offsets for alignment.

**Adjusting alignment:** Edit `OFFSETS` dict in `align_floorplans.py`:
```python
OFFSETS = {
    "ground": (0, 0),
    "first": (0, 50),    # shift 50px down
    "second": (0, 100),  # shift 100px down
}
```

Requires: `pillow` (PIL)

### Dependencies

Python utilities require:
```bash
pip install pillow
```

No package manager configuration files exist yet (no `requirements.txt`, `pyproject.toml`, or `setup.py`). Install dependencies manually.

## Documentation Standards

### Reference Hierarchy

When designing or documenting network components, consult in this order:

1. **`docs/requirements.md`** — Top-level constraints, WAN strategy, core rack spec, lab requirements
2. **`docs/floor-alignment.md`** — Structural features, void identification, vertical riser strategy
3. **`docs/radio-qos-analysis.md`** — RF model, AP counts/placement, SSID/VLAN/QoS design
4. **`design/cable-routing.md`** — Physical cable paths, containment methods, contractor notes

### Floorplan Coordinate References

When describing locations:
- Use **cardinal directions with west=top** (e.g., "north-west corner" = top-left)
- Reference **room labels from floorplans** (e.g., "Living Room 26'2" × 22'1"" for the lab)
- Anchor to **fixed structural features**: stair core, bathroom stack, central structural spine

Example: "Ground-floor lab (north-west, 7.99 × 6.75 m) receives fibre via primary riser from rack room above."

## Development Workflow

### Adding New Components or Calculations

When extending the design (e.g., BOM generation, cable-length calculator):

1. **Check documentation first** — Avoid assumptions; verify against `docs/` and `design/`
2. **Maintain coordinate system** — Ensure any spatial references use west=top orientation
3. **Validate against constraints** — RF model, cable routing rules, riser strategy
4. **Update relevant docs** — If you discover design gaps, note them in the appropriate `.md` file

### Research Tasks

For external research (UK regulations, Ubiquiti SKUs, cable specs):
- Perplexity API key is configured in `.env`
- Use the `perplexity-prompt-generator` skill to optimize research prompts with UK-centric focus

## Common Tasks

### Viewing floorplan alignment
```bash
python3 scripts/align_floorplans.py
# Output: FairfieldSpatial/composite_floorplans.png
```

### Checking structural alignment
Open `composite_floorplans.png` and verify:
- Stair core aligns vertically across all three floors
- Bathroom stack (right side of first-floor plan) is continuous
- Central structural spine (WAN entry wall) is traceable

### Researching UK-specific products or regulations
Use the perplexity-prompt-generator skill to craft effective prompts for UK networking equipment, building regulations, or cable standards.

## Important Project Context

### Lab Requirements (Ground Floor)

The **ground-floor north-west room** (former living room, 7.99 × 6.75 m) is designated as a high-performance lab:

- **Fibre backbone** from rack to lab for 10G SFP+ connectivity
- **Cat6 ring** around skirting with 8–12 outlets for flexible equipment placement
- **Dedicated AP** (AP-G1) ceiling-mounted for high-density wireless coverage
- **Wired-first philosophy** — Critical lab devices use Ethernet, not Wi-Fi

### Rack Room (First Floor)

**2.33 × 2.09 m void** adjacent to first-floor bathroom:
- Houses 12–18U rack with dual-WAN router, core switch, patch panels, UPS
- Serves as **central star point** for all structured cabling
- Shared wall with bathroom = preferred location for **vertical riser penetrations**

### 5G WAN Strategy

- **External antenna** on west elevation (high-gain directional)
- **5G CPE/modem** located near rack room or WAN entry point
- **Dual-WAN policy routing:** 5G primary for LAB/HOME, legacy broadband for failover/GUEST

### AP Deployment Strategy

Minimum **3 wired APs**:
1. **AP-G1** — Lab (ground floor)
2. **AP-F1** — Landing (first floor)
3. **AP-S1** — Living room (second floor)

Optional 4th AP (AP-G2) for ground-floor central hallway if testing reveals coverage gaps.

**All APs use wired Ethernet backhaul** (not wireless mesh).
