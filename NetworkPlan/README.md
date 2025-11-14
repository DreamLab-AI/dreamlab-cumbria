# Fairfield House Network Infrastructure Project

**Status:** Phase 1 Complete - Product Selection & Pricing
**Last Updated:** November 14, 2025

## Project Overview

Comprehensive network and structured cabling design for a 3-storey UK residential property with:
- Ground-floor high-performance lab (10G fibre connectivity)
- Dual-WAN (5G primary + legacy broadband failover)
- Wired Wi-Fi 6E mesh (3-4 access points)
- Central first-floor rack room
- Star topology structured cabling (30-40 drops)

**Key Constraint:** Thick concrete/breezeblock construction requiring wired backhaul and strategic AP placement.

---

## Quick Links

### Documentation
- **[Requirements](docs/requirements.md)** - Top-level project requirements
- **[Floor Alignment](docs/floor-alignment.md)** - Structural analysis and riser strategy
- **[Radio/QoS Analysis](docs/radio-qos-analysis.md)** - RF propagation model and AP placement
- **[Cable Routing](design/cable-routing.md)** - Physical cable paths and containment

### Bill of Materials
- **[Complete BOM](BOM.md)** - Full equipment list with UK pricing and purchase links
- **Total Cost:** £5,891 (core configuration) / £3,664 (budget configuration)
- **Black Friday Discounts:** Included where available (November 2025)

### Network Diagrams
- **[Physical Layout](diagrams/physical_layout.png)** - 3-floor equipment placement and cabling
- **[Logical Topology](diagrams/logical_topology.png)** - Network topology with VLANs
- **[Equipment Summary](diagrams/equipment_summary.png)** - Complete BOM with specs

### Research Data
- **[Ubiquiti Gateways](research/ubiquiti_gateways.md)** - UK pricing and specs
- **[Ubiquiti Switches](research/ubiquiti_switches.md)** - Core and lab switch options
- **[Ubiquiti APs](research/ubiquiti_aps.md)** - Wi-Fi 6E access point comparison
- **[5G Modems](research/5g_modems.md)** - External modem options
- **[Server Racks](research/server_racks.md)** - Rack options for Supermicro + network gear
- **[Fibre Components](research/fibre_components.md)** - OM4 backbone components
- **[Cabling Components](research/cabling_components.md)** - Cat6/Cat6A structured cabling

---

## Core Equipment Selection

### Recommended Configuration (£5,891)

| Category | Product | Price |
|----------|---------|-------|
| **Gateway** | UniFi Dream Machine Pro Max (UDM-Pro-Max) | £479 |
| **Core Switch** | UniFi Enterprise Campus 24 PoE (ECS-24-PoE) | £1,989 |
| **Lab Switch** | UniFi Professional Max/XG Series | £500 (est) |
| **Access Points** | 3× UniFi U6-Enterprise (WiFi 6E) | £710 |
| **5G WAN** | Teltonika RUTX50 + Directional Antenna | £650 (est) |
| **Rack & Power** | 18U Floor Rack + 1500VA UPS | £700 (est) |
| **Fibre Backbone** | OM4 30m Complete Kit (FS.com) | £145 |
| **Structured Cabling** | Cat6 Package (30-40 drops) | £544 |
| **Misc** | Patch cables, tools, cable management | £175 (est) |

**Key Features:**
- Dual-WAN with 5G primary (5 Gbps IPS throughput)
- 10G SFP+ fibre backbone to lab
- 1050W PoE+++ budget for 4× Wi-Fi 6E APs
- Layer 3 switching with VLAN/QoS support
- Future-proof for WiFi 7 and 25G expansion

---

## Network Architecture

### Physical Topology
- **First Floor:** Central rack room (2.33m × 2.09m) with all core equipment
- **Primary Riser:** Bathroom/service stack (ground → first → second floors)
- **Secondary Riser:** Stair core (supplemental distribution)
- **Lab Connection:** Dedicated 10G OM4 fibre link (30m)
- **AP Placement:** 3 minimum (lab, first-floor landing, second-floor living room)

### Logical Topology
- **VLANs:** LAB (10), HOME (20), IOT (30), GUEST (40), Management (99)
- **QoS Priority:** LAB > HOME > IOT > GUEST
- **WAN Policy:** 5G primary for high-priority, broadband for failover/guest
- **Wi-Fi:** Tri-band 6E with wired backhaul (no wireless mesh)

### RF Considerations
- Concrete walls: 15-25 dB attenuation at 5 GHz
- Floor slabs: 25-35 dB attenuation (no vertical coverage)
- Each floor requires dedicated wired AP
- 6 GHz band for future-proofing and reduced interference

---

## Project Structure

```
FairfieldSpatialBOM/
├── BOM.md                      # Complete bill of materials with pricing
├── CLAUDE.md                   # Claude Code repository guidance
├── README.md                   # This file
├── .env                        # API keys (Perplexity)
│
├── diagrams/                   # Generated network diagrams
│   ├── physical_layout.png     # 3-floor equipment placement
│   ├── logical_topology.png    # Network topology diagram
│   └── equipment_summary.png   # BOM summary table
│
├── docs/                       # Requirements and analysis
│   ├── requirements.md         # Top-level requirements
│   ├── floor-alignment.md      # Floor plans and riser strategy
│   └── radio-qos-analysis.md   # RF model and AP placement
│
├── design/                     # Detailed design specifications
│   └── cable-routing.md        # Physical cable paths
│
├── research/                   # Market research (Perplexity API)
│   ├── ubiquiti_gateways.md
│   ├── ubiquiti_switches.md
│   ├── ubiquiti_aps.md
│   ├── 5g_modems.md
│   ├── server_racks.md
│   ├── fibre_components.md
│   └── cabling_components.md
│
├── scripts/                    # Automation and utilities
│   ├── align_floorplans.py     # Generate composite floorplan image
│   ├── query_perplexity.sh     # Query Perplexity API
│   └── generate_network_diagram.py  # Create network diagrams
│
└── FairfieldSpatial/          # Source floorplan images
    ├── Screenshot_*.png        # Original floorplans (west = top)
    └── composite_floorplans.png  # Aligned composite (generated)
```

---

## Usage

### Generate Network Diagrams

```bash
# Activate virtual environment
source .venv/bin/activate

# Generate all diagrams
python scripts/generate_network_diagram.py

# Output: diagrams/*.png
```

### Generate Composite Floorplan

```bash
python scripts/align_floorplans.py

# Output: FairfieldSpatial/composite_floorplans.png
```

### Query Perplexity API for Research

```bash
./scripts/query_perplexity.sh "topic_name" "output_file.md" "Your research prompt here"

# Example:
./scripts/query_perplexity.sh "wifi7_aps" "research/wifi7_aps.md" \
  "Research WiFi 7 access points available in UK market November 2025..."
```

---

## Next Steps (Phase 2 - Implementation Planning)

1. **Validate design assumptions:**
   - Site visit to confirm cable route feasibility
   - RF site survey for AP placement optimization
   - Measure exact cable lengths per floor

2. **Finalize product selection:**
   - Contact Ubiquiti UK for lab switch pricing (Professional Max/XG series)
   - Confirm 5G modem compatibility with UDM-Pro-Max
   - Source 5G antenna with correct connectors and gain specs

3. **Procurement:**
   - Purchase core equipment (Black Friday pricing expires ~Nov 30)
   - Source rack from eBay UK (used APC/Prism 18U floor-standing)
   - Order fibre components from FS.com UK
   - Buy structured cabling from Screwfix/Toolstation/CPC Farnell

4. **Installation planning:**
   - Coordinate with electrical contractor for power circuits
   - Plan concrete slab penetrations (structural engineer if required)
   - Schedule civil work (core drilling, chasing, void preparation)
   - Define phased installation (first-fix cabling → second-fix terminations)

---

## Key Purchase Links

### Ubiquiti Equipment
- **Ubiquiti UK Store:** https://uk.store.ui.com
- **NetXL:** https://www.netxl.com
- **BroadbandBuyer:** https://www.broadbandbuyer.com

### Fibre Components
- **FS.com UK:** https://fs.com/uk (Black Friday deals active)
- **BroadbandBuyer:** https://www.broadbandbuyer.com
- **CPC Farnell:** https://cpc.farnell.com

### Structured Cabling
- **Screwfix:** https://www.screwfix.com
- **Toolstation:** https://www.toolstation.com
- **CPC Farnell:** https://cpc.farnell.com

### Server Racks
- **eBay UK:** Search "18U server rack 1000mm", "APC 18U rack"
- **Server Room Environments:** Contact for quote
- **123Racks:** https://www.123racks.com

### 5G Modems
- **LinITX:** UK distributor for Teltonika, MikroTik

---

## Technical Support

**Documentation Questions:** Refer to CLAUDE.md for repository structure and design hierarchy

**Product Questions:**
- Ubiquiti UK: https://help.ui.com
- FS.com UK: https://fs.com/uk/support
- 5G Modems: Contact LinITX

**Design Validation:**
- RF site survey recommended before final AP purchase
- Structural engineer for concrete penetrations if required

---

## License & Acknowledgments

**Project:** Fairfield House Network Infrastructure
**Design:** Custom residential network with home lab integration
**Research:** Powered by Perplexity API (November 2025)
**Pricing:** Black Friday 2025 UK market data

All product names, logos, and brands are property of their respective owners.

---

**Document Version:** 1.0
**Last Updated:** November 14, 2025
