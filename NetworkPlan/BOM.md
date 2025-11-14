# Fairfield House Network Infrastructure - Bill of Materials (BOM)

**Project:** Fairfield House Network & Low-Voltage Design
**Compiled:** November 14, 2025
**Includes:** Black Friday 2025 pricing where available
**Status:** Phase 1 - Product Selection & Pricing

---

## System Overview

- **Architecture:** Structured star topology, first-floor rack room as hub
- **WAN:** Dual-WAN (5G primary + legacy broadband failover)
- **Backbone:** 10G fibre link to ground-floor lab
- **Distribution:** Cat6/Cat6A to 3-4 wired APs, lab ring, bedroom outlets
- **Target drops:** 30-40 total across 3 floors

---

## 1. CORE NETWORKING EQUIPMENT

### 1.1 Gateway/Router (Dual-WAN with 5G)

**Recommended: UniFi Dream Machine Pro Max (UDM-Pro-Max)**

| Item | SKU | Specs | UK Price | Retailer | Link |
|------|-----|-------|----------|----------|------|
| UniFi Dream Machine Pro Max | UDM-Pro-Max | 1× 2.5GbE WAN, 1× 10G SFP+ WAN, 2× 10G SFP+ LAN, 5 Gbps IPS throughput, dual-WAN failover/load balancing | £479.00 | Ubiquiti UK Store | [Purchase](https://uk.store.ui.com) |
| UniFi Dream Machine Pro Max | UDM-Pro-Max | Same as above | £518.99 | NetXL | [Purchase](https://www.netxl.com) |

**Alternative (Budget): UniFi Dream Machine Pro (UDM-Pro)**

| Item | SKU | Specs | UK Price | Retailer | Link |
|------|-----|-------|----------|----------|------|
| UniFi Dream Machine Pro | UDM-Pro | 1× 1GbE WAN, 1× 10G SFP+ WAN/LAN, 3.5 Gbps IPS throughput | £300.00 | Ubiquiti UK Store | [Purchase](https://uk.store.ui.com) |
| UniFi Dream Machine Pro | UDM-Pro | Same as above | £300.00 | BroadbandBuyer | [Purchase](https://www.broadbandbuyer.com) |

**Selection Notes:**
- UDM-Pro-Max recommended for higher throughput and 2× 10G SFP+ ports
- Both support external 5G modem via Ethernet WAN
- Full VLAN, policy-based routing, QoS support
- All models in stock November 2025

**Quantity:** 1
**Subtotal:** £479.00 (Pro Max) or £300.00 (Pro)

---

### 1.2 Core Switch (PoE++ for APs, 10G uplink)

**Recommended: UniFi Enterprise Campus 24 PoE (ECS-24-PoE)**

| Item | SKU | Specs | UK Price | Retailer | Link |
|------|-----|-------|----------|----------|------|
| Enterprise Campus 24 PoE | ECS-24-PoE | 24× 1GbE + 10G RJ45, 25G SFP28 uplinks, 1050W PoE+++, Layer 3 | £1,989.00 | Ubiquiti UK Store | [Purchase](https://uk.store.ui.com) |

**Alternative (Budget): Check for Pro Max or XG Series**
- Professional Max and XG series offer 2.5G ports with PoE++ at lower price points
- Specific UK pricing not available in research; contact Ubiquiti UK directly

**Selection Notes:**
- 1050W PoE+++ budget sufficient for 4× Wi-Fi 6E APs + additional devices
- 25G SFP28 ports for high-speed backbone (overkill for single 10G lab link but future-proof)
- Layer 3 switching for advanced routing/VLAN features
- Etherlighting RGB port identification

**Quantity:** 1
**Subtotal:** £1,989.00

---

### 1.3 Lab Switch (10G uplink, mixed copper ports)

**Option 1: UniFi Professional Max / XG Series** (pricing TBD - contact Ubiquiti UK)
- 8-16 ports
- 1× 10G SFP+ uplink
- Mixed 1G/2.5G/10G copper ports
- UK pricing not available in research

**Option 2: Use second UDM-Pro as lab switch** (not ideal but functional)
- £300.00
- Limited port count but includes routing features

**Recommendation:** Contact Ubiquiti UK for current Professional Max/XG pricing and availability

**Quantity:** 1
**Subtotal:** £300-600 (estimated)

---

### 1.4 Wi-Fi Access Points (Wired backhaul, 6 GHz support)

**Recommended: UniFi U6-Enterprise (Wi-Fi 6E tri-band)**

| Item | SKU | Specs | UK Price (single) | UK Price (bulk) | Retailer | Link |
|------|-----|-------|-------------------|-----------------|----------|------|
| U6-Enterprise | U6-Enterprise | Wi-Fi 6E (2.4/5/6 GHz), 10.2 Gbps aggregate, 802.3at PoE+, 2.5GbE port, 600+ clients | £240.49 (inc VAT) | 5+ @ £236.62 each | Network Warehouse | Contact supplier |
| U6-Enterprise | U6-Enterprise | Same as above | £200.41 (ex VAT) | 10+ @ £232.76 each | NetXL | [Purchase](https://www.netxl.com) |

**Alternative: U6-Pro or U7-Pro** (full specs not available in research)
- Contact Ubiquiti UK for current U7-Pro availability and Wi-Fi 7 options
- U6-Pro likely lower cost but may lack 6 GHz band

**Selection Notes:**
- U6-Enterprise chosen for 6 GHz support (future-proofing)
- Tri-band operation critical for high-density concrete construction
- 2.5GbE uplink supports full throughput
- Requires PoE+ (802.3at) minimum
- Bulk pricing available for 3-4 unit purchase

**Quantity:** 3 (minimum: lab, first-floor landing, second-floor living room)
**Optional 4th AP:** 1 (ground-floor central hallway if coverage testing shows gaps)

**Subtotal:** 3× £236.62 = £709.86 (bulk pricing, 5+ units)
**With 4th AP:** 4× £236.62 = £946.48

---

## 2. WAN CONNECTIVITY

### 2.1 5G Modem/CPE (External antenna support)

**Recommended Options** (full pricing not available; estimated):

**Option 1: Teltonika RUTX50**
- 5G router with dual-band Wi-Fi
- Gigabit Ethernet WAN output
- External antenna support (SMA/N-type connectors)
- UK 5G band support
- Remote management
- **Estimated Price:** £400-600
- **Retailers:** LinITX, specialist 5G suppliers

**Option 2: MikroTik Chateau 5G R17 ax**
- 5G router with eSIM support
- Wi-Fi 6
- Gigabit Ethernet
- External antenna connectors
- **Estimated Price:** £300-450
- **Retailers:** LinITX, MikroTik distributors

**Option 3: Teltonika RUTM54**
- High-end 5G router
- Dual SIM + eSIM
- Industrial-grade
- **Estimated Price:** £500-700

**Selection Notes:**
- All options provide Ethernet WAN to connect to UDM-Pro/Pro-Max
- Verify UK 5G band support (n1, n3, n7, n20, n28, n38, n78)
- External antenna support critical for west-facing wall mount
- Contact UK suppliers (LinITX) for current pricing and Black Friday deals

**Quantity:** 1
**Subtotal:** £400-600 (estimated)

---

### 2.2 5G External Antenna (High-gain directional)

**Specifications needed:**
- Directional/panel antenna
- 10+ dBi gain
- UK 5G band coverage (700-3800 MHz)
- Outdoor rated (IP65+)
- N-type or SMA connectors (match modem)

**Estimated Price:** £100-200
**Retailers:** Specialist RF/antenna suppliers (research required)

**Quantity:** 1
**Subtotal:** £100-200 (estimated)

---

## 3. RACK & ENCLOSURE

### 3.1 Server Rack (18U minimum, 800-1000mm depth)

**Recommended: Used/Refurbished 18U Floor-Standing Rack**

| Type | Height | Depth | Load Capacity | Price | Source | Notes |
|------|--------|-------|---------------|-------|--------|-------|
| Floor-standing | 18U | 800-1000mm | 800-1000kg | £350-500 | eBay UK | Search: "18U server rack 1000mm", "APC 18U rack" |
| Floor-standing | 18U | 800-1000mm | 800kg+ | £400-600 | Server Room Environments | New, with cable management |

**Alternative: Custom Wall-Mount (depth-sufficient option)**

| Type | Height | Depth | Load Capacity | Price | Source | Notes |
|------|--------|-------|---------------|-------|--------|-------|
| Wall-mount | 18U | 800mm | 100kg+ | £472 | 123Racks | Custom, includes roof fan, cable mgmt |

**Selection Notes:**
- Supermicro 4U dual-PSU 4×GPU chassis requires 800mm+ depth
- Floor-standing preferred for 100kg+ load (server + network gear + UPS)
- Used APC/Prism racks on eBay UK best value under £500
- Wall-mount only viable if wall construction supports 100kg+ load

**Quantity:** 1
**Subtotal:** £350-500 (used floor-standing)

---

## 4. FIBRE BACKBONE (Rack to Lab)

### 4.1 Complete OM4 Multimode Fibre Solution (30m, 10GBASE-SR)

**Recommended Package (FS.com UK, Black Friday pricing):**

| Item | Part Number | Specs | Qty | Unit Price | Total |
|------|-------------|-------|-----|------------|-------|
| LC Patch Panel 1U 24-port | FHD-1U-24F-LC | 1U rack-mount, 24× LC duplex, unloaded | 1 | £39.00 | £39.00 |
| OM4 Pre-terminated Cable | OM4-LC-LC-8F-30M | OM4 multimode, 8-fibre, LC-LC, 30m | 1 | £59.00 | £59.00 |
| 10G SFP+ Transceiver | SFP-10GSR-85 | 10GBASE-SR, LC, MMF, 850nm, Ubiquiti-compatible | 2 | £19.00 | £38.00 |
| 1U Cable Management | FHD-1UFMT | Horizontal cable manager | 1 | £9.00 | £9.00 |

**Alternative: Ubiquiti UFiber Modules**

| Item | Part Number | Specs | Qty | Price | Retailer |
|------|-------------|-------|-----|-------|----------|
| Ubiquiti UF-MM-10G | UF-MM-10G | 10GBASE-SR, LC, MMF, 2-pack | 1 | £49.99 | BroadbandBuyer |

**Alternative Suppliers:**
- **BroadbandBuyer:** Excel OM4 LC-LC 12-core 30m (£143.99), Excel 24-port LC panel (£52.80)
- **CPC Farnell:** Connectix 12-port LC panel (£41.94)

**Selection Notes:**
- OM4 sufficient for 10GBASE-SR up to 300m (residential property well within range)
- 8-fibre cable provides 2 active + 6 spare fibres
- FS.com modules Ubiquiti-compatible (select coding at checkout)
- Black Friday pricing valid November 2025

**Subtotal:** £145.00 (FS.com complete package)

---

## 5. STRUCTURED CABLING (Cat6/Cat6A, 30-40 drops)

### 5.1 Complete Cabling Package

**Recommended Configuration (Black Friday pricing):**

| Component | Part Number | Supplier | Qty | Unit Price | Total |
|-----------|-------------|----------|-----|------------|-------|
| Cat6 U/UTP LSZH 305m | 297HY | Screwfix | 2 | £89.99 | £179.98 |
| 48-port Cat6 Patch Panel 1U | NW00348 | CPC Farnell | 1 | £54.99 | £54.99 |
| Cat6 Toolless Keystone Jack | 252HY | Screwfix | 40 | £2.49 | £99.60 |
| 2-Gang Faceplate (4× keystone) | 141HY | Screwfix | 10 | £1.99 | £19.90 |
| 1-Gang Faceplate (2× keystone) | 78959 | Toolstation | 20 | £1.29 | £25.80 |
| Surface Mount Box 32mm | 188HY | Screwfix | 30 | £1.29 | £38.70 |
| Mini Trunking 25×16mm 2m | 207HY | Screwfix | 20 | £2.99 | £59.80 |
| Mini Trunking 40×25mm 2m | 97607 | Toolstation | 10 | £4.29 | £42.90 |
| Network Cable Tester | 31934 | Toolstation | 1 | £9.98 | £9.98 |
| Punchdown Tool | 123HY | Screwfix | 1 | £6.99 | £6.99 |
| Cable Stripper | TL19690 | CPC Farnell | 1 | £4.99 | £4.99 |

**Optional Upgrade: Cat6A for AP/Lab runs**

| Component | Part Number | Supplier | Qty | Unit Price | Total |
|-----------|-------------|----------|-----|------------|-------|
| Cat6A U/UTP LSZH 305m | CB19690 | CPC Farnell | 1 | £129.00 | £129.00 |
| Cat6A Toolless Keystone Jack | NW00350 | CPC Farnell | 10 | £3.99 | £39.90 |

**Selection Notes:**
- Cat6 sufficient for 1G distribution and most runs
- Cat6A recommended for:
  - 10G fibre-to-copper breakout in lab (if not using SFP+ direct)
  - High-performance AP links (2.5G capable)
- 610m total cable (2× 305m boxes) covers 30-40 drops with margin
- Toolless keystones speed installation
- Mini trunking for skirting-level concealment where chasing impractical

**Subtotal (Cat6 only):** £543.63
**Subtotal (with Cat6A upgrade for 10 runs):** £712.53

---

### 5.2 PoE Injectors (if not using PoE switch)

**Only required if using non-PoE switch or for temporary AP deployment**

| Item | Part Number | Supplier | Specs | Qty | Unit Price | Total |
|------|-------------|----------|-------|-----|------------|-------|
| TP-Link TL-POE160S | TL-POE160S | CPC Farnell | 802.3at PoE+, Gigabit | 4 | £22.99 | £91.96 |

**Note:** Not needed if using Enterprise Campus 24 PoE switch (includes 1050W PoE+++ budget)

**Subtotal:** £91.96 (optional, for non-PoE switch deployment)

---

## 6. ADDITIONAL COMPONENTS (Estimated)

### 6.1 UPS (Rack-mount)

**Specifications:**
- Rack-mount 2U-3U
- 1000-1500VA capacity
- Runtime: 10-15 minutes for graceful shutdown
- Load: Gateway + core switch + controller

**Estimated Price:** £200-400
**Retailers:** Scan.co.uk, Ebuyer, CPC Farnell

**Quantity:** 1
**Subtotal:** £200-400 (estimated)

---

### 6.2 Patch Cables (Copper & Fibre)

**Copper Patch Cables (Cat6, various lengths):**
- 0.5m, 1m, 2m, 3m assortment
- **Estimated:** £50-100 for 20-30 cables

**Fibre Patch Cables (LC-LC, 1-3m):**
- For patch panel to switch connections
- **Estimated:** £20-40 for 4-6 cables

**Quantity:** Assorted
**Subtotal:** £70-140 (estimated)

---

### 6.3 Cable Management & Misc

- Velcro cable ties
- Cable labels
- Wall fixings for trunking
- Sealant for external penetrations (5G antenna)

**Estimated:** £50-100

---

## BILL OF MATERIALS SUMMARY

### Core Configuration (Recommended)

| Category | Items | Subtotal |
|----------|-------|----------|
| **Gateway** | UDM-Pro-Max | £479.00 |
| **Core Switch** | Enterprise Campus 24 PoE | £1,989.00 |
| **Lab Switch** | Professional Max/XG (TBD) | £500.00 (est) |
| **Access Points** | 3× U6-Enterprise | £709.86 |
| **5G Modem** | Teltonika RUTX50 (est) | £500.00 (est) |
| **5G Antenna** | Directional panel antenna | £150.00 (est) |
| **Server Rack** | 18U floor-standing (used) | £400.00 (est) |
| **Fibre Backbone** | OM4 30m complete kit (FS.com) | £145.00 |
| **Structured Cabling** | Cat6 package (30-40 drops) | £543.63 |
| **UPS** | 1500VA rack-mount | £300.00 (est) |
| **Patch Cables** | Copper + fibre assortment | £100.00 (est) |
| **Miscellaneous** | Cable management, fixings | £75.00 (est) |

**TOTAL (Core Configuration):** **£5,891.49**

---

### Budget Configuration (Alternative)

| Category | Items | Subtotal |
|----------|-------|----------|
| **Gateway** | UDM-Pro | £300.00 |
| **Core Switch** | Pro Max/XG 24-port PoE (TBD) | £800.00 (est) |
| **Lab Switch** | Second UDM-Pro | £300.00 |
| **Access Points** | 3× U6-Pro (pricing TBD) | £450.00 (est) |
| **5G Modem** | MikroTik Chateau 5G | £350.00 (est) |
| **5G Antenna** | Directional panel antenna | £100.00 (est) |
| **Server Rack** | 18U floor-standing (used) | £350.00 |
| **Fibre Backbone** | OM4 30m complete kit (FS.com) | £145.00 |
| **Structured Cabling** | Cat6 package (30-40 drops) | £543.63 |
| **UPS** | 1000VA rack-mount | £200.00 (est) |
| **Patch Cables** | Copper + fibre assortment | £75.00 (est) |
| **Miscellaneous** | Cable management, fixings | £50.00 (est) |

**TOTAL (Budget Configuration):** **£3,663.63**

---

## PURCHASE LINKS SUMMARY

### Primary Suppliers

**Ubiquiti Equipment:**
- **Ubiquiti UK Store:** https://uk.store.ui.com
- **NetXL:** https://www.netxl.com
- **BroadbandBuyer:** https://www.broadbandbuyer.com

**Fibre Components:**
- **FS.com UK:** https://fs.com/uk (Black Friday deals active)
- **BroadbandBuyer:** https://www.broadbandbuyer.com
- **CPC Farnell:** https://cpc.farnell.com

**Structured Cabling:**
- **Screwfix:** https://www.screwfix.com
- **Toolstation:** https://www.toolstation.com
- **CPC Farnell:** https://cpc.farnell.com

**Server Racks:**
- **eBay UK:** Search "18U server rack 1000mm", "APC 18U rack"
- **Server Room Environments:** Contact for quote
- **123Racks:** https://www.123racks.com

**5G Modems:**
- **LinITX:** UK distributor for Teltonika, MikroTik
- Contact for current pricing and availability

---

## NOTES & RECOMMENDATIONS

### Immediate Actions

1. **Verify 5G modem compatibility:** Contact Ubiquiti UK to confirm external modem compatibility with UDM-Pro/Pro-Max
2. **Confirm Professional Max/XG pricing:** Contact Ubiquiti UK for lab switch options and current pricing
3. **Source 5G antenna:** Research UK RF antenna suppliers for directional panel antennas with correct connectors
4. **Check Black Friday extensions:** FS.com and Ubiquiti may extend Black Friday pricing beyond November 14

### Design Validation Required

1. **AP placement verification:** Site survey recommended before finalizing 3 vs 4 AP configuration
2. **Cable length estimation:** Measure actual cable runs per floor to refine Cat6 box quantities
3. **Rack depth confirmation:** Verify exact Supermicro chassis depth (model number needed)
4. **5G signal testing:** Test 5G signal strength on west elevation before antenna purchase

### Installation Considerations (Out of Scope for Phase 1)

- Structural penetrations through concrete slabs (grouped at bathroom/rack stack)
- Fire-stopping for riser penetrations
- Wall load testing if considering wall-mount rack
- Professional RF survey post-installation for AP optimization

---

**Document Version:** 1.0
**Last Updated:** November 14, 2025
**Research Sources:** Perplexity API queries, current UK market data
