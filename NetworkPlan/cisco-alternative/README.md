# Cisco Hardware Alternative Analysis

Analysis of used Cisco enterprise equipment as alternative to Ubiquiti for Fairfield network deployment.

## Research Files

- [Used Cisco Hardware Research](cisco_used_hardware.md)

## Requirements Comparison

| Component | Ubiquiti Approach | Cisco Alternative |
|-----------|------------------|-------------------|
| Gateway | UDM-Pro / UXG-Pro | ISR 4000 / ASR 1000 |
| Core Switch | USW-Pro/Enterprise | Catalyst 3850/9300 |
| Lab Switch | USW-Pro-Max | Catalyst 2960-X |
| Access Points | U6/U7 series | Aironet 2800/3800/4800 |
| Management | UniFi Controller | Cisco WLC / Meraki Cloud |

## Key Considerations

- **Licensing:** Cisco requires feature licenses (IP Base, IP Services) and potentially SmartNet
- **Power consumption:** Enterprise gear typically higher than prosumer
- **Rack space:** 1-2U per switch/router vs integrated Ubiquiti solutions
- **Complexity:** IOS CLI configuration vs UniFi GUI
- **Used market:** Strong availability on eBay UK for Catalyst/ISR hardware

