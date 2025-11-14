# Fairfield House – Radio & QoS Analysis (Initial)

This is an initial, planning-level RF and QoS model. It is intended to guide:

- Number and rough placement of Ubiquiti APs.
- Where wired backhaul is mandatory (vs. wireless mesh, which we will largely avoid).
- Expectations around coverage, band steering, and QoS policy.

## 1. Construction & RF Assumptions

### 1.1 Walls and slabs

- **External & structural walls (thick black):**
  - Material: concrete breezeblock + finishes.
  - Attenuation estimate:
    - 2.4 GHz: 10–15 dB per wall.
    - 5 GHz: 15–25 dB per wall.
    - 6 GHz: 20–30 dB per wall.
  - Behaviour: effectively room/zone boundaries; avoid relying on APs through more than one of these.

- **Internal partitions (thin lines):**
  - Material: likely stud/plasterboard or lighter masonry.
  - Attenuation estimate:
    - 2.4 GHz: 3–6 dB.
    - 5 GHz: 5–10 dB.
    - 6 GHz: 6–12 dB.

- **Floor slabs:**
  - Solid concrete.
  - Attenuation estimate (floor-to-floor):
    - 2.4 GHz: 15–25 dB.
    - 5 GHz: 25–35 dB.
    - 6 GHz: 30+ dB.
  - Behaviour: we **do not** rely on vertical coverage; each floor gets its own AP(s).

### 1.2 5G and external antenna

- 5G CPE uses a **high-gain antenna on the west elevation** (top of plans) to maximise RSRP/SINR from the local cell.
- Indoor APs should **not** be expected to relay 5G RF; instead, 5G feeds the router, which then feeds LAN/Wi‑Fi.
- The 5G modem is ideally located close to:
  - The antenna entry point; and
  - The core rack / structured cabling, to minimise coax/Ethernet run and associated losses.

## 2. AP Strategy & Proposed Locations

We assume Ubiquiti Wi‑Fi 6/6E ceiling-mount APs (e.g. U6+ / U6-Pro / U7-Pro depending on final BOM).

### 2.1 Ground floor

**Primary area of interest:** Lab (former large living room, north‑west, 7.99 × 6.75 m).

- **AP-G1 (Lab):**
  - Mount: ceiling, roughly central in the lab, slightly offset toward the interior to reduce wall losses to the rest of the house.
  - Backhaul: wired (Cat6) from rack, via primary riser and horizontal route.
  - Purpose:
    - High-density coverage for lab devices, benches and fixed workstations.
    - Spill-over 2.4 GHz coverage into adjacent hallway via doorway; 5 GHz remains mainly within the lab.
  - Expected coverage:
    - Strong 5 GHz/6 GHz across the lab.
    - Weak-to-moderate 2.4 GHz into nearby hall if the door is open.

**Secondary coverage:**

- Depending on ground-floor partition layout and furniture, the lab AP alone may not fully cover:
  - Kitchen/living area to the south-west; and
  - Any rooms isolated by multiple thick walls.
- We therefore plan **one optional AP-G2**:
  - Mount: near the central hallway ceiling, just south of the stair core, where walls are lighter.
  - Backhaul: Cat6 from rack (ideally via stair-core routes).
  - Purpose: ensure robust coverage for family areas and IoT devices away from the lab.

### 2.2 First floor

The first floor has multiple bedrooms and a balcony.

- **AP-F1 (Landing):**
  - Mount: ceiling at or near the central landing/hallway.
  - Backhaul: Cat6 from rack (short run; rack room is adjacent to this floor).
  - Purpose:
    - Provide 5 GHz coverage to most bedrooms via partitions.
    - 2.4 GHz backfill into edge rooms through 1–2 partitions.

For bedrooms behind thick structural walls (particularly those on the far west or south), we may consider:

- **AP-F2 (optional, bedroom or small living room):**
  - Only if predictive survey (or real-world testing) shows poor SNR for 5 GHz > 2 walls away.
  - Prefer centrally located rooms to avoid over-coverage.

### 2.3 Second floor

Smaller footprint, with living room, bedrooms and bathrooms.

- **AP-S1 (Second-floor living room):**
  - Mount: ceiling center or slightly corridor-facing if open plan allows.
  - Backhaul: Cat6 via bathroom/riser stack from rack room.
  - Purpose:
    - Serve second-floor living room and adjacent bedrooms.
    - Spill 2.4 GHz onto balcony.

If bathrooms or structural walls isolate a bedroom too heavily:

- **AP-S2 (optional, bedroom):**
  - Only if required after survey; keep within wired backhaul reach.

### 2.4 AP count summary (initial plan)

- Minimum: **3 wired APs** (Lab, First-floor landing, Second-floor living room).
- Likely practical: **3–4 APs** depending on test results.
- All APs use **wired Ethernet backhaul**, not wireless mesh.

## 3. SSID, VLAN & QoS Design

### 3.1 SSID roles

Proposed SSIDs:

1. **LAB** – high-priority network for lab devices.
2. **HOME** – primary family/household network.
3. **IOT** – low-trust devices (CCTV, smart home, etc.).
4. **GUEST** – internet-only guest access.

These SSIDs map to VLANs on the core switch/router.

### 3.2 VLANs

- VLAN 10 – LAB
- VLAN 20 – HOME
- VLAN 30 – IOT
- VLAN 40 – GUEST
- VLAN 99 – Management (APs, switches, controllers)

All trunk links (rack to lab switch, rack to APs) carry these VLANs as tagged traffic, with AP ports configured appropriately.

### 3.3 QoS & traffic priorities

Given dual-WAN (phone broadband + 5G), we plan:

- **Per-SSID priority:**
  - LAB > HOME > IOT > GUEST.
- **Per-application shaping:**
  - Prioritise:
    - Interactive traffic (SSH, RDP, VoIP, WebRTC).
    - Critical lab uploads/downloads tied to work.
  - De-prioritise:
    - Large updates, streaming, guest bulk transfers.

- **WAN load-balancing approach (conceptual):**
  - Use 5G as primary for high-throughput, low-latency traffic (LAB, HOME).
  - Use phone broadband as:
    - Failover path; and
    - Possibly for GUEST or non-critical IOT when 5G is congested.
  - Policy-based routing per VLAN to steer less critical traffic toward the slower link under load.

Exact implementation depends on the chosen Ubiquiti gateway capabilities.

## 4. Expected Performance Per Zone

### 4.1 Lab (ground-floor north-west)

- With AP-G1 central:
  - 5 GHz: strong, > -60 dBm across most of the room.
  - 2.4 GHz: strong, > -55 dBm.
- Walls to the rest of the house are thick; we treat the lab largely as an RF “cell” separate from other zones.
- Wired endpoints via fibre backhaul to rack and Cat6 ring in skirting mitigate RF limitations entirely for high-demand devices.

### 4.2 Ground-floor living/kitchen

- With AP-G1 only:
  - Some coverage via doorways and 2.4 GHz, but 5 GHz may be marginal behind multiple structural walls.
- With AP-G2 in central hallway:
  - Stable 5 GHz in kitchen/living and hall.
  - Use band steering so general devices prefer 5 GHz where possible.

### 4.3 First-floor bedrooms

- AP-F1 on the landing:
  - Most bedrooms separated by 1–2 partitions; expect adequate 5 GHz and excellent 2.4 GHz.
  - Rooms behind thick structural walls may drop to 2.4 GHz only; if so, AP-F2 considered.
- Latency and throughput are primarily determined by 5G backhaul rather than Wi‑Fi in these areas.

### 4.4 Second-floor rooms

- AP-S1 in the living room:
  - Good 5 GHz around central/adjacent rooms.
  - 2.4 GHz likely adequate into all bedrooms and small balcony.
- Only if a bedroom is “shadowed” by bathroom plus outer wall would AP-S2 be introduced.

## 5. Survey and Validation Plan

This analysis should be validated in two stages:

1. **Pre-install desk study:**
   - Use the composite floorplan (from `scripts/align_floorplans.py`) and mark AP candidate points.
   - Run a rough predictive model (even simple path-loss spreadsheet) to confirm AP count.

2. **On-site validation:**
   - Deploy APs temporarily using PoE injectors.
   - Walk-test each floor with a Wi‑Fi analyser:
     - Capture RSSI, SNR, MCS rates.
     - Note dead spots, particularly behind thick walls and in corners.
   - Adjust AP positions, channel width/plan, and TX power accordingly.

## 6. Open Questions / To Refine

- Final selection of AP models (U6 Lite vs Pro vs 6E/U7) impacts overlap and capacity.
- Whether any rooms will house RF-sensitive equipment that may need isolation or wired-only access.
- Acceptance of **very low coverage** in low-usage spaces (e.g. some storage areas) in exchange for fewer APs.

This document provides the baseline radio/QoS model from which we can derive specific AP counts, SKUs and configuration templates in the BOM and installation plan.