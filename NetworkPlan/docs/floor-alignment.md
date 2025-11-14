# Fairfield House – Floor Alignment & Service Voids

## 1. Orientation and Notation

- All plans are oriented so that **west is up** on the images.
- "Ground", "First" and "Second" refer to the three PNGs in `FairfieldSpatial/`.
- Thick black walls are assumed **structural concrete/breezeblock**.
- Thin walls are assumed **non-structural partitions**.

## 2. Key Fixed Reference Features

To align floors we use three repeatable elements:

1. **Stair core** – central vertical circulation, present on all floors.
2. **Bathroom stack** – vertically aligned bathrooms on all floors on the east/central-right side.
3. **External north–south structural spine** – the long internal wall where the phone/broadband enter on the ground floor.

These anchors allow the composite produced by `scripts/align_floorplans.py` to be manually offset so that the stair and bathroom walls visually line up between images.

## 3. Ground Floor Summary

- Large **lab (former living room)** in the north‑west corner, approx. 7.99 × 6.75 m.
- Central hallway and stair core connecting to upper floors.
- Kitchen/living area to the south‑west, separated from the lab by heavy walls.
- Phone/broadband entry at the **central structural wall near the top** of the ground-floor plan.
- Black wall thickness around bathrooms and the stair indicates potential service space but not a full-height duct.

### 3.1 Ground-Floor Void & Riser Candidates

- Short service run around the ground-floor bathroom/WC block.
- Local boxed-out areas around the stair where cables can rise if slab penetrations are made at this location.
- For concealment, we avoid external risers along the west façade and instead use the internal bathroom/stair zone.

## 4. First Floor Summary

- Multiple bedrooms arranged west and south of the stair core.
- A bathroom on the east/central-right side with an adjacent **2.33 × 2.09 m dark void**.
- This void is designated as the **rack / small server room**.
- The bathroom plus rack void together form a strong vertical stack with the wet rooms above and below.

### 4.1 Rack Room and Stack

- The rack room shares a wall with the bathroom; this wall is the preferred line for **vertical riser penetrations** between floors.
- The stair core sits slightly west of this, providing a secondary spine for horizontal transitions.
- The ground-floor bathroom/WC block appears broadly under this same region, simplifying slab penetrations if grouped.

## 5. Second Floor Summary

- Smaller footprint than the lower floors.
- Living room and bedrooms mainly over the western/central portion of the first floor.
- Bathrooms again located near the same east/central-right structural line.
- A small balcony on the west side of the top floor.

### 5.1 Upper-Floor Void Usage

- The bathroom positions suggest continuity of the **wet-service stack** above the first-floor bathroom and rack room.
- Cables for Wi‑Fi APs and bedroom outlets on the second floor can rise within or immediately adjacent to this stack.
- Given solid slabs, each penetration should be concentrated near this stack to minimise structural disruption.

## 6. Proposed Vertical Riser Strategy

1. **Primary riser: bathroom/rack stack**
   - Originates at the ground-floor bathroom/WC block close to the broadband entry wall.
   - Passes through the first-floor bathroom and rack room.
   - Continues to the second-floor bathroom zone for AP feeds and bedroom drops.
   - Carries: fibre backbone, Cat6 trunks to each floor, and control cabling as needed.

2. **Secondary riser: stair core**
   - Used for local distribution on each floor where routes need to cross the building without passing through heavy external walls.
   - Good candidate for running AP feeds to hall/landing locations on first and second floors.

## 7. Horizontal Cable Principles by Floor

- **Ground floor:**
  - Fibre from rack to lab routed via the primary riser and then along internal partitions, entering the lab through the least invasive wall.
  - Within the lab, Cat6 cables loop as a skirting-level ring; chasing into thick walls is minimised, so shallow trunking may be used where necessary.

- **First floor:**
  - From the rack room, horizontal runs follow partition walls to bedrooms and the living room.
  - AP cabling routes toward the central landing ceiling position via partitions rather than external walls.

- **Second floor:**
  - Shorter horizontal runs from the bathroom/riser to bedrooms and living room.
  - AP feed to a central point in the living room or corridor.

## 8. Implications for RF & QoS

- Structural black walls and slabs are treated as **major RF barriers**; APs on one side should not be relied upon to cover heavy-walled rooms on the other.
- AP placement will favour **central, partition-bounded zones** (lab, landings, upper living room).
- The riser strategy keeps wired backhaul compact so that multiple wired APs can be deployed without excessive civil work.