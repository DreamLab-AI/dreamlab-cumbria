# Ubiquiti Wifi7

*Research conducted: 1763210663*

**Ubiquiti’s WiFi 7 (802.11be) ceiling-mount access points—including the U7-Pro and U7-Lite—are now available in the UK, supporting 2.4/5/6 GHz bands, Multi-Link Operation (MLO, via firmware), and PoE+ (802.3at) with 2.5GbE uplinks.** The U7-Pro is the direct WiFi 7 successor to the U6-Pro, offering higher throughput and improved client density, making it suitable for challenging environments like multi-storey homes with concrete walls[1][2][3][5][6].

Below is a comparison table of current and recent Ubiquiti ceiling-mount APs relevant to your requirements:

| Model         | WiFi Gen | Bands (GHz) | MLO | Max Throughput | Spatial Streams | PoE Standard | Uplink | Coverage (m²) | UK Price (Nov 2025) | Availability | Purchase Link |
|---------------|----------|-------------|-----|----------------|----------------|--------------|--------|---------------|---------------------|--------------|---------------|
| **U7-Pro**    | 7        | 2.4/5/6     | Yes (firmware) | 9.3 Gbps (agg.)<br>2.4: 688 Mbps<br>5: 4.3 Gbps<br>6: 5.8 Gbps | 6 | 802.3at (PoE+) | 2.5GbE | 140 | £160 (est. £175-£185 inc VAT) | Shipping now | [Ubiquiti UK][5], [NetXL][1] |
| **U7-Lite**   | 7        | 2.4/5/6     | Yes (firmware) | 4.9 Gbps (agg.)<br>2.4: 688 Mbps<br>5: 4.3 Gbps<br>6: n/a | 4 | 802.3at (PoE+) | 2.5GbE | ~100 | £79 ex VAT (£94.80 inc VAT) | Shipping now | [Ubiquiti UK][3] |
| **U6-Enterprise** | 6E   | 2.4/5/6     | No  | 10.2 Gbps (agg.) | 8 | 802.3at (PoE+) | 2.5GbE | 140 | £199-£220 inc VAT | Shipping now | [Ubiquiti UK][6] |
| **U6-Pro**    | 6        | 2.4/5       | No  | 5.3 Gbps (agg.) | 4 | 802.3at (PoE+) | 1GbE | 140 | £129-£145 inc VAT | Shipping now | [Ubiquiti UK][6] |

**Key Details:**
- **Ceiling-mount WiFi 7 APs:** U7-Pro and U7-Lite are both ceiling-mount, PoE-powered, and support 2.5GbE uplinks[1][3][5][6].
- **PoE Requirements:** Both U7-Pro and U7-Lite use 802.3at (PoE+), so any modern PoE+ switch will suffice[1][3][5].
- **Multi-Link Operation (MLO):** Supported via firmware update on U7-Pro and U7-Lite, enabling simultaneous use of multiple bands for improved throughput and reliability[2][5].
- **6 GHz Band:** Both U7-Pro and U7-Lite support 6 GHz, provided clients also support this band[1][3][5].
- **Transmit Power & Coverage:** U7-Pro covers up to 140 m² per AP; U7-Lite slightly less (~100 m²). Concrete walls will reduce real-world coverage, so plan for one AP per floor[1][2][3][5].
- **Controller Requirements:** All UniFi WiFi 7 APs require a UniFi Controller, which can run on a UniFi Console, Dream Machine, Cloud Key, or self-hosted server[2][5].
- **UK Availability & Pricing:** U7-Pro and U7-Lite are available now (November 2025). U7-Pro is ~£160 ex VAT (£175-£185 inc VAT); U7-Lite is £79 ex VAT (£94.80 inc VAT)[1][3][5][6]. U6-Enterprise and U6-Pro remain available as WiFi 6E/6 options.

**Purchase Links:**
- [U7-Pro at Ubiquiti UK][5], [U7-Pro at NetXL][1]
- [U7-Lite at Ubiquiti UK][3]
- [U6-Enterprise and U6-Pro at Ubiquiti UK][6]

**Recommended Configuration for Concrete Construction:**
- **3 x U7-Pro** (one per floor, ceiling-mounted, wired backhaul) for maximum coverage, throughput, and future-proofing.
- If budget is a concern, **mix 2 x U7-Pro (main floors) + 1 x U7-Lite (least-used floor)**.
- Ensure your PoE switch supports 802.3at and 2.5GbE uplinks for each AP.
- Use the UniFi Controller on a Cloud Key, Dream Machine, or UniFi Console for management.

**If WiFi 7 is not required or stock is unavailable:**
- **U6-Enterprise** is the best WiFi 6E ceiling-mount alternative, with similar coverage and 6 GHz support, but lacks MLO and some WiFi 7 efficiencies[6].
- **U6-Pro** is a solid WiFi 6-only option (no 6 GHz), suitable for legacy environments.

**Summary:**  
For a UK 3-storey home with thick concrete walls, **U7-Pro** is the optimal choice for ceiling-mount, wired-backhaul WiFi 7 coverage. All required features (6 GHz, MLO, PoE+, UniFi Controller support) are present and units are available for immediate purchase as of November 2025.

---
**References:**  
[1]: NetXL U7-Pro  
[2]: MS Dist WiFi 7 AP Guide  
[3]: Ubiquiti UK U7-Lite  
[5]: Ubiquiti EU U7-Pro  
[6]: Ubiquiti EU Store (U6-Enterprise, U6-Pro, U7-Lite, etc.)

## Sources

1. https://www.netxl.com/wifi-access-points/ubiquiti-unifi-u7-pro-wifi-7-access-point-5-pack/
2. https://www.msdist.co.uk/blogs/news/ubiquiti-wifi-7-access-point-guide-2025
3. https://uk.store.ui.com/uk/en/products/u7-lite
4. https://uk.store.ui.com/uk/en/products/u7-pro-wall
5. https://eu.store.ui.com/eu/en/products/u7-pro
6. https://eu.store.ui.com/eu/en/category/all-wifi
7. https://www.broadbandbuyer.com/store/wifi-access-points/wifi-7-access-points-be/
8. https://ui.com/wifi/outdoor
9. https://ui.com/wifi
10. https://networkwarehouse.co.uk/products/ubiquiti-u7-lr
