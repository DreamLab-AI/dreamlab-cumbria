# ubiquiti gateways

*Research conducted: 2025-11-14 13:27 UTC*

The most current Ubiquiti UniFi gateway/router options in the UK market (as of November 2025) that support **dual-WAN with load balancing/failover, 5G WAN connectivity (via external modem), 10G SFP+ uplink, VLANs, policy-based routing, and QoS** are the **UniFi Dream Machine Pro (UDM-Pro)**, **Dream Machine Pro Max (UDM-Pro-Max)**, and **Dream Machine Special Edition (UDM-SE)**. No official Ubiquiti gateway currently offers built-in 5G; all models require a compatible external 5G modem for WAN connectivity.

Below is a comparison table of these models, including key specs, UK pricing from three major retailers (with Black Friday discounts where available), and current stock status. Purchase links are provided for each retailer.

| Model Name                | SKU           | WAN Ports         | SFP+ Ports | Max Throughput (IPS) | 5G WAN Support      | VLAN/Policy Routing | UK Price (Ubiquiti Store) | UK Price (NetXL) | UK Price (BroadbandBuyer) | Stock Status (Nov 2025) | Purchase Links |
|--------------------------|---------------|-------------------|------------|---------------------|---------------------|---------------------|---------------------------|------------------|---------------------------|-------------------------|---------------|
| **Dream Machine Pro**    | UDM-Pro       | 1x 1GbE, 1x 10G SFP+ | 1x 10G SFP+ | 3.5 Gbps            | External modem via WAN | Yes                 | £300.00[1][3]            | £300.00[4]       | £300.00[4]                | In stock                | [Ubiquiti][1], [NetXL][4], [BroadbandBuyer][4] |
| **Dream Machine Pro Max**| UDM-Pro-Max   | 1x 2.5GbE, 1x 10G SFP+ | 2x 10G SFP+ | 5 Gbps               | External modem via WAN | Yes                 | £479.00[3]               | £518.99[2]       | N/A                       | In stock                | [Ubiquiti][3], [NetXL][2] |
| **Dream Machine SE**     | UDM-SE        | 1x 1GbE, 1x 10G SFP+ | 1x 10G SFP+ | 3.5 Gbps            | External modem via WAN | Yes                 | £429.00[3]               | N/A              | N/A                       | In stock                | [Ubiquiti][3] |

**Key Details:**

- **Dual-WAN & Failover:** All models support dual-WAN (RJ45 + SFP+) with failover and load balancing[4][6].
- **5G WAN Connectivity:** None have built-in 5G; use an external 5G modem (e.g., via USB or Ethernet to WAN port). Ubiquiti recommends compatible LTE/5G modems for WAN backup[6].
- **10G SFP+ Uplink:** All models include at least one 10G SFP+ port for fibre backbone to your lab[1][2][3][4][6].
- **VLAN & Policy-Based Routing:** Full VLAN support and policy-based routing via UniFi OS and Network Controller[4][6].
- **QoS:** Automatic and customizable QoS for prioritizing traffic (voice/video, lab devices)[4].
- **Stock & Pricing (Black Friday 2025):**
    - **Ubiquiti Store UK:** UDM-Pro £300, UDM-Pro-Max £479, UDM-SE £429. All in stock[1][3].
    - **NetXL:** UDM-Pro-Max £518.99 (bulk discounts available), UDM-Pro £300. Both in stock[2].
    - **BroadbandBuyer:** UDM-Pro £300, in stock[4].
- **Purchase Links:**  
    - [Ubiquiti Store UK: UDM-Pro](https://uk.store.ui.com/uk/en/products/udm-pro)[1]  
    - [NetXL: UDM-Pro-Max](https://www.netxl.com/network-switches/ubiquiti-unifi-dream-machine-udm-pro-max/)[2]  
    - [BroadbandBuyer: UDM-Pro](https://www.broadbandbuyer.com/products/37823-ubiquiti-udm-pro/)[4]

**Notes on 5G Compatibility:**
- For 5G WAN, use a compatible external modem (e.g., Netgear Nighthawk M6, ZTE MC801A, or similar) connected via Ethernet to the WAN port. Ubiquiti does not currently offer a native 5G gateway or modem as of November 2025[6].
- UniFi OS supports WAN failover and policy-based routing with external modems.

**Recent/Upcoming Models:**
- No new Ubiquiti gateway models with built-in 5G or additional SFP+ ports have been released in 2024-2025 per available sources[3][8].
- UDM-Pro-Max is the newest and most capable for large home labs, with higher throughput and redundancy features[2][3].

**Summary:**  
For a UK residential dual-WAN setup with 5G + legacy broadband, VLANs, policy-based routing, and 10G SFP+ uplink, the **UDM-Pro-Max** is the most advanced option, followed by the UDM-Pro and UDM-SE. All require an external 5G modem for cellular WAN. All models are currently in stock at major UK retailers, with Black Friday pricing available.
