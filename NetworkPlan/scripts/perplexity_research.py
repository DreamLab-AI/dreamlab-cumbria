#!/usr/bin/env python3
"""
Perplexity API research utility for Fairfield network equipment BOM.
Queries Perplexity API with optimized prompts and saves results.
"""

import json
import os
from pathlib import Path
from typing import Dict, List

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

API_KEY = os.getenv("PERPLEXITY_API_KEY")
API_URL = "https://api.perplexity.ai/chat/completions"

RESEARCH_PROMPTS = {
    "ubiquiti_gateways": """Context: I'm designing a UK residential network with dual-WAN (5G + legacy broadband) and need policy-based routing with QoS for a home lab environment.

Task: Research current Ubiquiti gateway/router options available in the UK market (November 2025) that support:
- Dual-WAN with load balancing and failover
- 5G WAN connectivity (either built-in or via compatible external modem)
- 10G SFP+ uplink capability for fibre backbone to lab
- VLAN support and policy-based routing
- Current stock availability at major UK retailers

Focus: UniFi Dream Machine Pro, UXG-Pro, or newer models released in 2024-2025. Include 5G compatibility options (USB dongles, Ethernet-connected modems).

Deliverable: Comparison table with model names, SKUs, key specs (WAN ports, SFP+ support, throughput), current UK pricing from at least 3 retailers (including any Black Friday 2025 discounts), and stock availability. Include purchase links.""",

    "ubiquiti_switches": """Context: Building a structured cabling system for a 3-storey UK home with a ground-floor lab requiring 10G connectivity via fibre backbone. Core rack is on first floor, needs to distribute to 3-4 APs plus lab switch.

Task: Research Ubiquiti switches available in the UK (November 2025) suitable for:
- Core switch: 24-48 ports with at least 2× 10G SFP+ uplinks, full PoE++ (802.3bt) for Wi-Fi 6E APs
- Lab switch: 8-16 ports with at least 1× 10G SFP+ uplink, mixture of 1G/2.5G/10G copper ports

Focus: UniFi Switch Pro/Enterprise models, USW-Pro-Max, USW-Enterprise-24-PoE, or newer 2024-2025 releases. Include total PoE budget specifications.

Deliverable: Table with model, port count, SFP+ ports, PoE budget, backplane capacity, current UK pricing from major retailers, Black Friday 2025 deals, and purchase links.""",

    "ubiquiti_aps": """Context: Deploying wired-backhaul APs across 3 floors of a UK house with thick concrete walls (high RF attenuation). Need 3-4 ceiling-mount APs with excellent 5 GHz/6 GHz performance and PoE.

Task: Research current Ubiquiti Wi-Fi 6 and Wi-Fi 6E access points available in UK market (November 2025):
- Ceiling-mount models suitable for residential deployment
- PoE requirements (802.3at/bt compatibility)
- 5 GHz and 6 GHz band support
- Transmit power and coverage specs

Focus: U6+, U6-Pro, U6-Enterprise, U7-Pro, or newer models. Prioritise 6 GHz support for future-proofing.

Deliverable: Comparison table with model, Wi-Fi generation, band support (2.4/5/6 GHz), max throughput, PoE standard, coverage estimate, current UK pricing at major retailers including Black Friday 2025 offers, and purchase links. Recommend best 3-AP configuration for concrete construction.""",

    "5g_modems": """Context: Need to connect a Ubiquiti gateway to UK 5G mobile networks (EE, Vodafone, Three, O2) using an external high-gain directional antenna mounted on west-facing wall. Indoor modem connects to router via Ethernet.

Task: Research 5G CPE/modem options compatible with Ubiquiti networking equipment in UK market (November 2025):
- Ethernet WAN output (RJ45) to connect to UniFi gateway
- External antenna support (TS9, SMA, or N-type connectors)
- UK 5G band support (n1, n3, n7, n20, n28, n38, n78)
- Directional/high-gain antennas suitable for outdoor mounting

Focus: Industrial/prosumer 5G modems from brands like Teltonika, Peplink, Mikrotik, or similar. Include antenna options with 10+ dBi gain.

Deliverable: Table with modem models, supported bands, antenna connectors, Ethernet specs, outdoor antenna options, current UK pricing and availability including Black Friday deals, and purchase links for both modems and antennas.""",

    "server_racks": """Context: Need to rack-mount in a 2.33m × 2.09m room: Supermicro dual-PSU 4U workstation (4×GPU chassis, full-depth), 12-18U of networking equipment (UniFi gateway, 24-48 port PoE switch, patch panels, UPS). Standard rack depth required for Supermicro chassis.

Task: Research mini/wall-mount server racks available on UK eBay and major retailers (November 2025):
- 18U-24U height minimum
- 600mm+ depth to accommodate full-depth Supermicro chassis
- Wall-mount or floor-standing options suitable for small room
- Load capacity 100kg+
- Cable management and ventilation features

Focus: Budget-friendly options including used/refurbished racks on eBay UK. Include brands like StarTech, APC, Raising Electronics, or generic 19" racks.

Deliverable: Table with rack type (wall/floor), height (U), depth, load capacity, current pricing (new and used eBay listings), and purchase links. Highlight best value options under £500.""",

    "fibre_components": """Context: Installing OM4 or singlemode fibre backbone between first-floor rack room and ground-floor lab in UK residential property. Need 10G SFP+ connectivity with LC connectors.

Task: Research fibre optic components available from UK suppliers (November 2025):
- Fibre patch panels (LC, 12-24 port) for rack mounting
- Pre-terminated OM4/OS2 fibre cables (LC-LC, 20-30m lengths)
- 10GBASE-SR or 10GBASE-LR SFP+ transceivers (Ubiquiti-compatible)
- Fibre cable management and routing accessories

Focus: UK suppliers like FS.com UK, Broadband Buyer, CPC Farnell. Include Ubiquiti U Fiber modules if available.

Deliverable: Component list with part numbers, specs, UK pricing including Black Friday deals, and purchase links. Recommend complete fibre solution for single 10G link.""",
}


def query_perplexity(prompt: str, model: str = "llama-3.1-sonar-huge-128k-online") -> Dict:
    """
    Query Perplexity API with given prompt.

    Args:
        prompt: Research prompt text
        model: Perplexity model to use (default: sonar-huge for comprehensive research)

    Returns:
        API response dict with content and citations
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful research assistant specializing in UK technology procurement. Provide detailed, accurate information with current pricing and purchase links. Today's date is November 14, 2025."
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
    response.raise_for_status()
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
    """Execute all research queries and save results."""
    output_dir = ROOT / "research"

    print(f"Starting Perplexity research for {len(RESEARCH_PROMPTS)} topics...\n")

    results = {}

    for topic, prompt in RESEARCH_PROMPTS.items():
        print(f"Querying: {topic}...")
        try:
            result = query_perplexity(prompt)
            results[topic] = result
            save_research(topic, result, output_dir)
            print()
        except Exception as e:
            print(f"✗ Failed to query {topic}: {e}\n")
            results[topic] = {"error": str(e)}

    # Save combined results as JSON
    json_output = output_dir / "research_results.json"
    with json_output.open("w") as f:
        json.dump(results, f, indent=2)

    print(f"\n✓ All research saved to {output_dir}/")
    print(f"✓ Combined JSON results: {json_output}")


if __name__ == "__main__":
    main()
