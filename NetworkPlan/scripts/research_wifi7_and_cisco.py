#!/usr/bin/env python3
"""
Research Ubiquiti WiFi 7 systems and used Cisco hardware alternatives.
"""

import json
import os
from pathlib import Path
from typing import Dict

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

API_KEY = os.getenv("PERPLEXITY_API_KEY")
API_URL = "https://api.perplexity.ai/chat/completions"

RESEARCH_QUERIES = {
    "ubiquiti_wifi7": """Context: Designing a UK residential network for a 3-storey house with thick concrete walls (high RF attenuation). Need ceiling-mount APs with wired Ethernet backhaul. Planning for 3-4 APs total across ground, first, and second floors.

Task: Research Ubiquiti's new WiFi 7 access point systems available or announced for UK market (November 2025):
- WiFi 7 (802.11be) models with ceiling-mount form factor
- PoE requirements (802.3at/bt compatibility)
- Multi-link operation (MLO) and 6 GHz band support
- Transmit power and coverage specifications
- Controller requirements (UniFi Console, Dream Machine, Cloud Key)
- UK availability timeline and pricing

Focus: U7-Pro, U7-Enterprise, or any new WiFi 7 models announced in 2024-2025. Include comparison with WiFi 6E models (U6-Enterprise, U6-Pro) if WiFi 7 not yet available.

Deliverable: Comparison table with model names, WiFi generation (6E vs 7), band support (2.4/5/6 GHz), MLO capability, max throughput, PoE standard, expected UK pricing and availability dates. Include purchase links or pre-order information. Recommend best 3-4 AP configuration for concrete construction with wired backhaul.""",

    "cisco_used_hardware": """Context: Evaluating alternatives to Ubiquiti networking equipment for a UK residential home lab. Current requirements include:
- Dual-WAN router with load balancing, failover, 5G WAN support, 10G SFP+ uplink
- Core switch: 24-48 ports with PoE++ (802.3bt), 2+ 10G SFP+ uplinks
- Lab switch: 8-16 ports with 1G/2.5G/10G mix, 1+ 10G SFP+ uplink
- 3-4 ceiling-mount WiFi 6E/7 APs with PoE
- VLAN support, policy-based routing, QoS for home lab traffic
- Fibre backbone (10G) from first-floor rack to ground-floor lab

Task: Research used/refurbished Cisco enterprise networking equipment available on UK eBay and secondary market (November 2025) that could meet these requirements:

**Routers/Gateways:**
- Cisco ISR 4000 series or ASR 1000 series with dual-WAN capability
- Support for 10G SFP+ uplink and policy-based routing
- Compatible with USB/Ethernet 5G modems

**Switches:**
- Catalyst 3850/9300 series for core (PoE+/PoE++, 10G uplinks)
- Catalyst 2960-X/3650 series for lab access layer
- Meraki MS switches (if perpetual licensing available)

**Access Points:**
- Cisco Aironet 2800/3800/4800 series (WiFi 6/6E)
- Meraki MR46/MR56 (if perpetual licensing or used licenses available)
- Ceiling-mount models with PoE support

Focus: eBay UK listings, refurbished enterprise gear, total cost of ownership including licensing. Include compatibility with open-source controllers (OpenWRT, pfSense for routing; Cisco WLC or open alternatives for APs).

Deliverable: Component BOM with Cisco models, typical used UK pricing from eBay, licensing considerations, power consumption, rack space (U), and total estimated cost. Compare with equivalent Ubiquiti setup cost. Include purchase links to eBay searches and recommendations for best value configuration.""",
}


def query_perplexity(prompt: str, model: str = "sonar-pro") -> Dict:
    """Query Perplexity API with given prompt."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful research assistant specializing in UK technology procurement and enterprise networking equipment. Provide detailed, accurate information with current pricing and purchase links. Today's date is November 15, 2025."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2,
        "max_tokens": 4000,
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=120)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Response: {response.text}")
        raise
    return response.json()


def save_research(topic: str, result: Dict, output_dir: Path) -> None:
    """Save research results to markdown file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{topic}.md"

    content = result["choices"][0]["message"]["content"]

    # Extract citations if available
    citations = []
    if "citations" in result:
        citations = result["citations"]

    with output_file.open("w") as f:
        f.write(f"# {topic.replace('_', ' ').title()}\n\n")
        f.write(f"*Research conducted: {result.get('created', 'Unknown date')}*\n\n")
        f.write(content)
        f.write("\n\n")

        if citations:
            f.write("## Sources\n\n")
            for i, citation in enumerate(citations, 1):
                f.write(f"{i}. {citation}\n")

    print(f"✓ Saved {topic} research to {output_file}")


def main():
    """Execute research queries and save results."""
    wifi7_dir = ROOT / "research" / "wifi7"
    cisco_dir = ROOT / "cisco-alternative"

    print(f"Starting Perplexity research...\n")

    # WiFi 7 research
    print("Querying: Ubiquiti WiFi 7 systems...")
    try:
        wifi7_result = query_perplexity(RESEARCH_QUERIES["ubiquiti_wifi7"])
        save_research("ubiquiti_wifi7", wifi7_result, wifi7_dir)
        print()
    except Exception as e:
        print(f"✗ Failed to query WiFi 7: {e}\n")

    # Cisco hardware research
    print("Querying: Used Cisco hardware alternatives...")
    try:
        cisco_result = query_perplexity(RESEARCH_QUERIES["cisco_used_hardware"])
        save_research("cisco_used_hardware", cisco_result, cisco_dir)

        # Also save a summary comparison
        summary_file = cisco_dir / "README.md"
        with summary_file.open("w") as f:
            f.write("# Cisco Hardware Alternative Analysis\n\n")
            f.write("Analysis of used Cisco enterprise equipment as alternative to Ubiquiti for Fairfield network deployment.\n\n")
            f.write("## Research Files\n\n")
            f.write("- [Used Cisco Hardware Research](cisco_used_hardware.md)\n\n")
            f.write("## Requirements Comparison\n\n")
            f.write("| Component | Ubiquiti Approach | Cisco Alternative |\n")
            f.write("|-----------|------------------|-------------------|\n")
            f.write("| Gateway | UDM-Pro / UXG-Pro | ISR 4000 / ASR 1000 |\n")
            f.write("| Core Switch | USW-Pro/Enterprise | Catalyst 3850/9300 |\n")
            f.write("| Lab Switch | USW-Pro-Max | Catalyst 2960-X |\n")
            f.write("| Access Points | U6/U7 series | Aironet 2800/3800/4800 |\n")
            f.write("| Management | UniFi Controller | Cisco WLC / Meraki Cloud |\n\n")
            f.write("## Key Considerations\n\n")
            f.write("- **Licensing:** Cisco requires feature licenses (IP Base, IP Services) and potentially SmartNet\n")
            f.write("- **Power consumption:** Enterprise gear typically higher than prosumer\n")
            f.write("- **Rack space:** 1-2U per switch/router vs integrated Ubiquiti solutions\n")
            f.write("- **Complexity:** IOS CLI configuration vs UniFi GUI\n")
            f.write("- **Used market:** Strong availability on eBay UK for Catalyst/ISR hardware\n\n")

        print(f"✓ Created summary at {summary_file}")
        print()
    except Exception as e:
        print(f"✗ Failed to query Cisco hardware: {e}\n")

    print(f"✓ Research complete")
    print(f"  WiFi 7 results: {wifi7_dir}/")
    print(f"  Cisco alternative: {cisco_dir}/")


if __name__ == "__main__":
    main()
