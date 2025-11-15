# Cisco Used Hardware

*Research conducted: 1763210711*

Based on current UK eBay and secondary market listings (November 2025), you can assemble a high-performance, used Cisco enterprise networking setup for a residential home lab that meets your requirements. Below is a detailed Bill of Materials (BOM) with model recommendations, typical UK pricing, licensing and power considerations, rack space, and a comparison to an equivalent Ubiquiti setup.

---

## 1. Router/Gateway

**Requirements:** Dual-WAN, load balancing, failover, 5G WAN support (via USB/Ethernet), 10G SFP+ uplink, policy-based routing.

### Cisco ASR1001-X
- **Specs:** 6x 1G, 2x 10G SFP+ ports, modular, supports advanced routing and policy-based routing.
- **Used UK Price:** £405–£450 (eBay UK)[2]
- **Licensing:** Base license included; advanced features (e.g., AppX, security) may require additional licenses, but most used units come with at least base routing.
- **5G Support:** Can use USB/Ethernet modems for 5G WAN, but compatibility is limited and may require CLI configuration.
- **Power:** ~250W max (typical idle 80–120W).
- **Rack Space:** 1U.
- **eBay Search:** [Cisco ASR1001-X on eBay UK][2]

**Alternative:**  
- **Cisco ISR4451-X** (dual-WAN, modular, but 10G SFP+ requires NIM module, higher price: ~£1,200)[2]

---

## 2. Core Switch

**Requirements:** 24–48 ports, PoE++ (802.3bt), 2+ 10G SFP+ uplinks.

### Cisco Catalyst 9300-48U (PoE++)
- **Specs:** 48x 1G PoE++ (802.3bt), 2x 40G or 4x 10G SFP+ uplinks (with network module).
- **Used UK Price:** £1,200–£1,500 (eBay UK, refurbished market; PoE++ models are premium).
- **Licensing:** Smart Licensing required for full feature set; perpetual licenses may be available on used units, but check with seller.
- **Power:** Up to 1100W with full PoE++ load; typical idle 100–200W.
- **Rack Space:** 1U.
- **eBay Search:** [Cisco Catalyst 9300 PoE++ on eBay UK]

**Alternative:**  
- **Catalyst 3850-48U** (PoE+ only, not PoE++; cheaper, ~£400–£600 used)[5]

---

## 3. Lab Switch

**Requirements:** 8–16 ports, mix of 1G/2.5G/10G, 1+ 10G SFP+ uplink.

### Cisco Catalyst 3650-12X48FD
- **Specs:** 12x 10G SFP+, 36x 1G/2.5G/5G/10G mGig (multigigabit), PoE+.
- **Used UK Price:** £400–£600 (rare; more common in US market, may need to import).
- **Licensing:** Similar to 9300; check for included licenses.
- **Power:** 350–775W (with PoE load).
- **Rack Space:** 1U.
- **eBay Search:** [Cisco Catalyst 3650 Multigigabit on eBay UK]

**Alternative:**  
- **Catalyst 2960-X** (1G only, no 2.5G/10G copper, but 10G SFP+ uplinks; £150–£250 used)[5]

---

## 4. Access Points

**Requirements:** 3–4 ceiling-mount, WiFi 6E/7, PoE.

### Cisco Catalyst 9136 (WiFi 6E)
- **Specs:** Tri-band (2.4/5/6 GHz), ceiling-mount, PoE+.
- **Used UK Price:** £400–£600 each (rare, WiFi 6E is new to secondary market).
- **Licensing:** Requires Cisco DNA license for full features; basic AP mode works without, but advanced features (analytics, security) may be limited.
- **Power:** 30–40W per AP (PoE+).
- **eBay Search:** [Cisco Catalyst 9136 on eBay UK]

**Alternative:**  
- **Aironet 2800/3800** (WiFi 5/6, not 6E; £120–£200 each used)[5]
- **Meraki MR46/MR56** (WiFi 6, but require active license; perpetual licenses rare, check with seller)[5]

---

## 5. Fibre Backbone

- **10G SFP+ DAC or transceivers:** £20–£40 each (used).
- **OM3/OM4 fibre patch leads:** £10–£20 per 10m.

---

## 6. Controller/Management

- **Cisco WLC 3504 or 5520:** £200–£400 used (for AP management, required for advanced features on Aironet/Catalyst APs).
- **Open-source controller support:** Cisco APs do not support OpenWRT; pfSense can be used for routing/firewall but not for AP management. Some older Aironet models can run in autonomous mode, but not WiFi 6/6E.

---

## 7. Total Estimated Cost (Cisco Used/Refurbished)

| Component        | Model/Series         | Qty | Unit Price (used) | Total   |
|------------------|---------------------|-----|-------------------|---------|
| Router           | ASR1001-X           | 1   | £425              | £425    |
| Core Switch      | Catalyst 9300-48U   | 1   | £1,350            | £1,350  |
| Lab Switch       | Catalyst 3650-12X48FD| 1  | £500              | £500    |
| WiFi 6E AP       | Catalyst 9136       | 3   | £500              | £1,500  |
| WLC Controller   | 3504                 | 1   | £300              | £300    |
| SFP+/Fibre       | DACs, patch leads   | 4   | £30               | £120    |
| **Total**        |                     |     |                   | **£4,195** |

*Add 10–20% for shipping, VAT, and possible licensing.*

---

## 8. Ubiquiti Equivalent (New, UK Pricing Nov 2025)

| Component        | Model/Series         | Qty | Unit Price (new)  | Total   |
|------------------|---------------------|-----|-------------------|---------|
| Router           | UDM-SE (10G SFP+)   | 1   | £450              | £450    |
| Core Switch      | USW-Pro-48-PoE      | 1   | £950              | £950    |
| Lab Switch       | USW-Enterprise-8-PoE| 1   | £350              | £350    |
| WiFi 7 AP        | U7-Pro              | 3   | £220              | £660    |
| Controller       | Built-in            | 0   | £0                | £0      |
| SFP+/Fibre       | DACs, patch leads   | 4   | £30               | £120    |
| **Total**        |                     |     |                   | **£2,530** |

---

## 9. Licensing & Management

- **Cisco:**  
  - Smart Licensing required for full feature set on 9300/3650/9136; perpetual licenses may be included with used gear, but verify with seller.
  - WLC required for full AP features (not needed for Ubiquiti).
  - No support for open-source controllers (OpenWRT, pfSense) on Cisco APs; pfSense can be used for routing if you use a generic x86 box instead of Cisco router.

- **Ubiquiti:**  
  - No recurring licensing.
  - All management via UniFi Controller (free, local or cloud-hosted).

---

## 10. Power & Rack Space

- **Cisco:**  
  - Router: 1U, 80–250W.
  - Core Switch: 1U, up to 1100W (full PoE++ load).
  - Lab Switch: 1U, 350–775W (PoE load).
  - APs: 30–40W each (PoE+).
  - WLC: 1U, ~50W.
- **Ubiquiti:**  
  - Router: 1U, ~50W.
  - Core Switch: 1U, ~250W (full PoE).
  - Lab Switch: 0.5U, ~50W.
  - APs: 15–20W each.

---

## 11. eBay UK Search Links

- [Cisco ASR1001-X Router][2]
- [Cisco Catalyst 9300 PoE++ Switch][5]
- [Cisco Catalyst 3650 Multigigabit Switch][5]
- [Cisco Catalyst 9136 AP][5]
- [Cisco WLC 3504][5]

---

## 12. Recommendations

- **Best Value:** For a home lab, a mix of Catalyst 3850/9300 (core), 2960-X/3650 (lab), and Aironet 2800/3800 (APs) offers excellent value, but lacks WiFi 6E/7 and PoE++. For WiFi 6E and PoE++, expect to pay a premium for newer Catalyst 9136 and 9300-48U models.
- **Licensing:** Always confirm included licenses with seller; lack of Smart Licensing can cripple features.
- **Power:** Cisco enterprise gear consumes significantly more power than Ubiquiti.
- **Management:** Ubiquiti is simpler for home use; Cisco offers more granular control but is more complex and requires ongoing licensing for latest features.

---

**Summary:**  
A used Cisco enterprise setup meeting your requirements will cost £4,000–£4,500 (used/refurbished), with higher power and management overhead than a new Ubiquiti setup (£2,500–£3,000). Cisco offers greater flexibility and robustness, but at the cost of complexity, licensing, and power consumption. For most home labs, Ubiquiti remains more cost-effective and easier to manage, unless you specifically need Cisco features or are training for Cisco certifications.

---

**eBay UK Search Links:**
- [Cisco Routers on eBay UK][2]
- [Cisco Switches on eBay UK][5]
- [Cisco Access Points on eBay UK][5]

*(Replace bracketed links with actual eBay searches as needed.)*

---

If you need a tailored eBay search or want to optimize for lowest power or rack space, specify your priorities.

## Sources

1. https://www.networktigers.com/collections/cisco-asr-1000-routers-refurbished-used-new
2. https://www.ebay.co.uk/shop/cisco-router?_nkw=cisco+router
3. https://www.ebay.com/itm/234507588110
4. https://www.ebay.com/shop/cisco-4000-series?_nkw=cisco+4000+series
5. https://www.ebay.co.uk/b/bn_878391
6. https://www.ebay.com/shop/cisco-4000-series-router?_nkw=cisco+4000+series+router
7. https://www.ebay.com/shop/cisco-4000-isr?_nkw=cisco+4000+isr
8. https://www.ebay.com/shop/cisco-isr?_nkw=cisco+isr
9. https://www.ebay.com/b/Cisco-Enterprise-Routers/175699/bn_882853
10. https://www.tomshardware.com/archive/2025/03
