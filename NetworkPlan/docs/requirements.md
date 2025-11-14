# Fairfield House – Network & Low-Voltage Requirements

## 1. Building & Construction Summary

- 3-storey house in the UK.
- Orientation: **west = top** of digital floorplans.
- External and many internal load-bearing walls: concrete breezeblock, very thick, high RF attenuation.
- Intermediate floors: solid concrete slabs with flat plasterboard ceilings, effectively no accessible ceiling voids.
- We want to conceal as much cabling as practicable; voids are not purpose-built and may require making and good.
- Avoid visible external runs on the west elevation wherever possible.

### 1.1 Floor overview

- **Ground floor:** Large kitchen/living space to south-west, large living room to north-west (to become lab), hallways, WC, small rooms and central stair core.
- **First floor:** Multiple bedrooms, bathrooms, balcony; bathroom on east/central-right with adjacent 2.33 × 2.09 m black void.
- **Second floor:** Smaller footprint; living room, bedrooms, bathrooms and balcony mostly stacked over the left/central portion of the house.

## 2. WAN, Routing & Core Rack

- Existing WAN: legacy ~10 Mbps phone/broadband entering at the **central structural wall near the top of ground-floor plan**.
- New WAN: high-performance 5G using an external directional / high-gain antenna on the west elevation, cabled to indoor 5G CPE or remote radio head.
- Requirement: dual-WAN load balancing and/or policy-based routing (QoS-aware) between phone broadband and 5G.

### 2.1 Core rack / server closet

- Location: room/void **2.33 × 2.09 m** next to the first-floor bathroom on the right-hand side of the middle plan.
- This space will be fitted out as a small equipment room with door and power already available.
- Rack orientation is flexible; preference is to use the wall common with the bathroom/service stack to keep vertical risers compact.
- Proposed equipment (subject to BOM detail):
  - 12–18U wall or short floor-standing rack.
  - Dual-WAN Ubiquiti gateway/router.
  - Core L2/L3 switch with SFP+ uplinks (10G-capable for lab).
  - Fibre patch panel (LC/UPC).
  - Copper patch panel (Cat6 or Cat6A).
  - UPS sized for router + core switch + controller + minimal lab backhaul.
  - Environmental monitoring (temperature, humidity) optional.

### 2.2 Structured cabling principles

- Use structured star topology, all fibres and horizontal Cat6 runs home-running to the rack room.
- Prefer optical fibre backbones between floors and to the lab, to minimise signal loss and future-proof for higher throughput.
- Use Cat6 (or Cat6A where feasible) to outlets, APs and fixed equipment.
- Keep all risers inside internal walls and service voids; breaches in concrete slabs to be planned at stack points only.

## 3. Lab (Ground-Floor North-West Room)

- Existing room: labelled **Living Room 26'2" × 22'1" / 7.99 × 6.75 m** at top-right of ground-floor plan.
- New designation: **lab / high-density workspace**.

### 3.1 Connectivity requirements

- Dedicated fibre link from rack to a lab distribution switch (SFP+/RJ-45) providing:
  - At least one 10G copper port for a primary workstation/cluster.
  - Multiple 1G/2.5G ports for general lab equipment.
- Fibre-to-copper breakout to terminate in a small wall-mounted cabinet or under-bench enclosure.
- **Cat6 ring** around the lab skirting with:
  - High density of RJ-45 ports (target ≥ 8–12 outlets distributed evenly).
  - Outlets grouped at likely desk/bench positions but also available on each wall for flexible layouts.
- Provision for future direct-fibre terminations to a lab rack (e.g. for servers) without re-opening slabs.

### 3.2 Power and services

- Additional radial circuits to support lab load if required (coordinated with electrical contractor).
- Surge protection and UPS integration for critical endpoints as necessary.

## 4. Wi‑Fi, 5G and RF / QoS Constraints

- Thick breezeblock walls and concrete slabs will significantly attenuate RF (both Wi‑Fi and 5G).
- Thin partition walls are assumed moderately RF-transparent and can be crossed by indoor Wi‑Fi.
- 5G signal will be optimised at the external antenna; indoor 5G CPE location to be near the rack or near the cable entry point, depending on vendor.
- Ubiquiti Wi‑Fi 6/6E APs will be used as wired backhaul mesh nodes where possible, not wireless mesh between APs.
- Primary coverage priority:
  1. Lab (ground-floor north-west).
  2. General living/kitchen areas.
  3. Bedrooms and study areas.
  4. Balconies and outdoor terraces (best-effort).

## 5. Riser & Cable Routing Strategy (High Level)

- Treat the bathroom + adjacent void stack (including the 2.33 × 2.09 m rack room) as the **primary vertical riser**.
- Secondary risers may route near the stair core where black wall thickness suggests service capacity.
- All floor penetrations through concrete slabs to be grouped at these risers to minimise structural work.
- Horizontal runs per floor will follow:
  - Along internal partitions and service walls where chasing is least invasive.
  - Perimeter routes at skirting level in rooms where chasing breezeblock is impractical, using low-profile trunking if needed.
- Avoid external west elevation cable runs except for the 5G antenna feed and any mandated safety/pathway constraints.

## 6. Documentation & Deliverables

- Detailed cable routing drawings per floor, keyed to structural features and room labels.
- AP placement plan with predicted coverage and QoS assumptions.
- BOM including Ubiquiti SKUs, cable types, termination hardware and containment materials.
- Phased installation plan separating civil work (core drilling, chasing, void preparation) from first-fix cabling and second-fix terminations.

This document is the top-level requirement reference for the Fairfield network and low-voltage design.