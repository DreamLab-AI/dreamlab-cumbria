# ubiquiti switches

*Research conducted: 2025-11-14 13:27 UTC*

# Ubiquiti UniFi Switches for UK Home Lab Infrastructure

Based on current UK availability as of November 2025, I need to clarify that the search results provide limited pricing and availability data for the specific models you're requesting. However, I can provide guidance on the suitable Ubiquiti switch options for your structured cabling system.

## Core Switch Requirements Analysis

For your ground-floor lab with 10G fibre backbone and distributed Wi-Fi 6E access points, you'll need a switch with **PoE++ (802.3bt) capability** to support newer Wi-Fi 7 models like the U7-Pro and E7, which require PoE++ power delivery[1]. The older Switch Enterprise 24/48 PoE (Gen1) models feature 2.5 GbE PoE+ output but are **not compatible with PoE++ requirements** of current-generation access points[5][6].

## Available Models for Your Use Case

**Professional Max & XG Series** (Recommended for 10G backbone)

The Professional Max and XG models represent Ubiquiti's current high-performance switching tier, featuring 2.5 Gbps RJ45 interfaces, 10 Gbps RJ45 ports, and PoE+++ capability[1]. These models include Etherlighting™ RGB port identification based on activity or VLAN assignment, which is valuable for managing complex home lab deployments.

**Enterprise Campus Series** (Latest 2024-2025 Release)

The Enterprise Campus 24 PoE and Enterprise Campus 48 PoE represent the newest enterprise-grade options available in the UK market[2]. These are Layer 3 switches with PoE+++ output and support for 10 GbE RJ45 plus 25G SFP28 connections for high-availability designs.

| Model | Port Count | 10G/25G Uplinks | PoE Budget | Layer | UK Price |
|-------|-----------|-----------------|-----------|-------|----------|
| Enterprise Campus 24 PoE (ECS-24-PoE) | 24× 1G + 10G RJ45 | 25G SFP28 | 1050W PoE+++ | Layer 3 | £1,989.00 |
| Enterprise Campus 48 PoE (ECS-48-PoE) | 48× 1G + 10G RJ45 | 25G SFP28 | 2150W PoE+++ | Layer 3 | £2,785.00 |
| Enterprise Campus 48S PoE (ECS-48S-PoE) | 48× 1G + 10G RJ45 | 25G SFP28 | 2150W PoE+++ | Layer 3 | £3,180.00 |
| Enterprise Campus 24S PoE (ECS-24S-PoE) | 24× 1G + 10G RJ45 | 25G SFP28 | 1050W PoE+++ | Layer 3 | £2,385.00 |

## Recommended Configuration for Your Setup

**Core Rack (First Floor):** The **Enterprise Campus 24 PoE** (£1,989.00) provides sufficient capacity for 3-4 Wi-Fi 6E/7 access points with its 1050W PoE+++ budget, while the 25G SFP28 ports accommodate your fibre backbone. The stacking-capable "S" variant (ECS-24S-PoE, £2,385.00) offers future expansion capability if you plan to add additional switches.

**Lab Switch (Ground Floor):** For the lab requiring mixed copper connectivity, the Professional Max or XG series would be appropriate, though specific UK pricing and availability for these models was not available in current search results. These models support the 1× 10G SFP+ uplink requirement plus 2.5G/10G copper ports you specified.

## Important Compatibility Notes

The older **Switch Enterprise 24 PoE (Gen1)** and **Switch Enterprise 48 PoE (Gen1)** models listed at £1,989.00 and higher are **not compatible with PoE++ requirements** of Wi-Fi 7 access points[5][6]. Ensure you specify the newer Enterprise Campus series when purchasing.

## Purchasing Information

The Enterprise Campus models are available directly from the **Ubiquiti UK Store** (uk.store.ui.com). Black Friday 2025 deals were not detailed in current search results, so I recommend checking the Ubiquiti UK Store directly for November promotional pricing. Major UK technology retailers including Laptop Outlet also stock Ubiquiti professional switching equipment.

For the most current pricing, availability, and Black Friday promotions, contact the Ubiquiti UK Store directly or check with authorized UK resellers, as pricing and promotional information changes frequently and was not fully captured in the available search results.
