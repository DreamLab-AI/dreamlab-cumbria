# Fairfield House – Cable Routing & Riser Design

This document describes the **physical cable paths** (fibre and copper) for the Fairfield house.  
It is written for coordination between network designer and contractors.

## 1. Cable Types & General Rules

- **Backbone (inter-floor and lab link):**
  - Singlemode or OM4 multimode fibre (final choice TBD).
  - 4–12 cores recommended to allow for expansion and spares.
  - Terminated at rack patch panel in the first-floor rack room and at:
    - Lab distribution switch (ground floor).
    - Any future satellite cabinets (if added).

- **Horizontal runs:**
  - **Cat6 or Cat6A** U/UTP, LSZH.
  - Star topology: each outlet and AP home-runs to the rack room patch panel.

- **Containment:**
  - Prefer concealed routes in walls/voids.
  - Where chasing in concrete is impractical, use:
    - Minimal-profile skirting-level trunking; or
    - Boxing within joinery (built-in units, wardrobes, etc.).
  - Avoid visible external runs on west façade except for 5G antenna feed.

- **Penetrations:**
  - Group slab penetrations at designated riser points (bathroom/rack stack, stair core).
  - Use sleeves where multiple cables pass through concrete.

## 2. Primary Riser – Bathroom / Rack Stack

### 2.1 Geometry

- Ground floor: bathroom/WC block and central structural spine near WAN entry.
- First floor: bathroom plus **2.33 × 2.09 m rack room** immediately adjacent.
- Second floor: bathroom(s) situated on same east/central-right axis.

### 2.2 Cables in this riser

- Backbone fibre between:
  - Rack room (first floor) and lab (ground).
  - Rack room and second-floor distribution points.
- Cat6 trunks for:
  - Ground-floor APs and outlets near the riser.
  - Second-floor AP(s) and selected bedroom outlets.
- Any low-voltage control or monitoring cables required later (temperature probes, etc.).

### 2.3 Physical route

1. **Ground → First:**
   - Riser originates in/adjacent to ground-floor bathroom/WC wall that aligns with first-floor bathroom/rack wall.
   - Core drill through slab at one or two consolidated locations.
   - Sleeves to be fitted; fibre and Cat6 pass through to the rack-side wall.

2. **First → Second:**
   - From rack room ceiling or high-level wall into the bathroom stack above.
   - Use boxed-in chase within bathroom wall or stud to reach second-floor bathroom area.
   - From there, branch horizontally to second-floor AP and outlets.

## 3. Secondary Riser – Stair Core

### 3.1 Purpose

- Provide supplemental paths where cables must cross the building without traversing thick external walls.
- Good for:
  - Central AP locations on each floor.
  - Distributing to south-side rooms if needed.

### 3.2 Implementation

- Identify wall/void adjacent to the stair that is common to all floors.
- Limited core holes through slabs, again grouped and sleeved.
- Use this riser for Cat6 only where necessary; keep fibre primarily in the bathroom/rack stack unless additional diversity is desired.

## 4. Ground Floor Routes

### 4.1 Rack to WAN entry

- WAN entry: central structural wall near the top of the ground-floor plan.
- Route:
  - From rack room down primary riser to ground-floor bathroom/WC zone.
  - Short horizontal run along structural spine to meet phone/broadband entry and 5G CPE location.
  - Terminate at:
    - Demarcation point for legacy line.
    - 5G modem/router or PoE/power injector for external radio.

### 4.2 Rack to Lab (fibre backbone)

- From rack patch panel:
  - Fibre exits rack room via bathroom/riser stack to ground-floor bathroom area.
  - From ground-floor bathroom, fibre runs horizontally:
    - Prefer internal partitions; avoid chasing external walls.
    - Enter the lab via the shortest path that avoids doors and major openings.
- Inside the lab:
  - Fibre terminates at a small wall-mounted cabinet or under-bench enclosure housing:
    - Fibre patch panel or SFP+ media converter.
    - Lab access/distribution switch.

### 4.3 Lab Cat6 ring (skirting)

- From lab switch:
  - Cat6 cables distribute around the perimeter at skirting level.
  - Routes:
    - Cables drop inside lab wall where possible, then emerge into low-profile dado/skirting trunking.
    - Outlets at regular intervals on all four sides, with higher density on expected bench/desk walls.
- Consider grouping outlets in pairs or quads for neatness.

### 4.4 Ground-floor AP cabling

- **AP-G1 (Lab ceiling):**
  - Cat6 from rack → fibre → lab switch, and then short Cat6 up to AP; or
  - Dedicated Cat6 from rack room if preferred.
- **AP-G2 (optional, central hallway):**
  - Cat6 from rack via stair-core riser, dropping into hallway ceiling.

## 5. First Floor Routes

### 5.1 Rack room internal layout (copper/fibre)

- Rack on bathroom-adjacent wall.
- Vertical cable manager(s) on each side of patch panels.
- Penetration locations:
  - Floor penetrations from ground and up to second floor grouped behind/under rack.
  - High-level exit points from rack into corridors/rooms via partitions.

### 5.2 Bedroom and living-room outlets

- Star from rack patch panel:
  - Follow internal partitions wherever possible.
  - For rooms backing onto external concrete walls, route along internal walls then short chase or trunk to outlet position.
- Prioritise:
  - At least one dual-RJ45 outlet per bedroom.
  - Additional outlets in the first-floor living room if used as a study/entertainment space.

### 5.3 First-floor AP cabling

- **AP-F1 (landing ceiling):**
  - Short Cat6 drop from rack via wall/ceiling cavity.
- **AP-F2 (optional):**
  - If installed, Cat6 along partitions from rack; mount centrally in problematic bedroom or sitting room.

## 6. Second Floor Routes

### 6.1 AP and outlets

- From rack via primary riser into second-floor bathroom zone.
- From there:
  - **AP-S1** in second-floor living room: Cat6 routed along partition from bathroom area.
  - Bedroom outlets: Cat6 runs along partitions; cross doorways using concealed methods (above lintel or at floor level inside wall where possible).

### 6.2 Balcony services (optional)

- If outdoor coverage or PoE devices (e.g. camera) are required:
  - Cat6 run from living room or bathroom stack to a discreet junction on balcony.
  - Ensure external-grade cable and glands used where exposed.

## 7. 5G Antenna Feed

- High-performance antenna on west elevation (top of plans), ideally near vertical line of rack room.
- RF or Ethernet feed (depending on CPE type) routed:
  - Internally through wall into top-floor or first-floor space, then down to rack through bathroom/riser stack; or
  - Directly at first-floor level into rack room external wall if positioning allows.
- Penetration sealed for weatherproofing; use drip loops and fixings per manufacturer guidance.

## 8. Future-Proofing and Spares

- Install spare fibres (dark cores) in backbone bundle.
- Leave at least 1–2 spare Cat6 cables in each riser bundle for later use.
- Reserve patch-panel capacity in rack for:
  - Additional lab circuits.
  - Possible second lab rack or remote cabinet.
  - Future camera/IoT expansions.

## 9. Notes for Contractors

- All slab penetrations to be agreed with structural engineer if required.
- Fire-stopping of riser penetrations is mandatory.
- Exact outlet positions to be coordinated on-site with owner once furniture layout is confirmed.
- All cable routes to be photographed before closing walls/ceilings where possible.