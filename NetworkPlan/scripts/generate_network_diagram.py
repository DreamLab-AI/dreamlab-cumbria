#!/usr/bin/env python3
"""
Generate comprehensive network diagram for Fairfield House infrastructure.
Shows physical layout, equipment placement, and connectivity.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch, Circle
from matplotlib.lines import Line2D
import networkx as nx
from pathlib import Path

# Output configuration
ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "diagrams"
OUTPUT_DIR.mkdir(exist_ok=True)

# Color scheme
COLORS = {
    'wan': '#FF6B6B',
    'core': '#4ECDC4',
    'fibre': '#FFD93D',
    'copper': '#95E1D3',
    'ap': '#A8E6CF',
    'lab': '#C7CEEA',
    'background': '#F8F9FA',
    'border': '#2C3E50',
    'text': '#2C3E50',
}

def create_physical_layout_diagram():
    """Create diagram showing 3-floor physical layout with equipment placement."""
    fig, axes = plt.subplots(3, 1, figsize=(16, 20))
    fig.patch.set_facecolor(COLORS['background'])

    floors = [
        ("Ground Floor", 0),
        ("First Floor", 1),
        ("Second Floor", 2)
    ]

    for idx, (floor_name, ax_idx) in enumerate(floors):
        ax = axes[ax_idx]
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.set_aspect('equal')
        ax.set_facecolor('#FFFFFF')
        ax.set_title(f'{floor_name} - Equipment & Cable Layout',
                     fontsize=16, fontweight='bold', pad=20)
        ax.axis('off')

        # Draw compass (West = Top)
        compass_x, compass_y = 9.2, 7.2
        ax.text(compass_x, compass_y + 0.3, 'W', ha='center', fontsize=10, fontweight='bold')
        ax.arrow(compass_x, compass_y, 0, 0.2, head_width=0.1, head_length=0.05, fc='black')

        if idx == 0:  # Ground floor
            # Lab (north-west = top-left)
            lab = FancyBboxPatch((0.5, 5), 3.5, 2.5, boxstyle="round,pad=0.1",
                                edgecolor=COLORS['border'], facecolor=COLORS['lab'],
                                linewidth=3, alpha=0.7)
            ax.add_patch(lab)
            ax.text(2.25, 7.2, 'LAB', fontsize=14, fontweight='bold', ha='center')
            ax.text(2.25, 6.7, '7.99m × 6.75m', fontsize=10, ha='center')

            # AP-G1 (Lab ceiling)
            ap_g1 = Circle((2.25, 6.2), 0.2, facecolor=COLORS['ap'],
                          edgecolor='black', linewidth=2)
            ax.add_patch(ap_g1)
            ax.text(2.25, 5.7, 'AP-G1\n(U6-Enterprise)', fontsize=9, ha='center',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

            # Fibre termination point
            fibre_term = Rectangle((3.5, 5.5), 0.3, 0.3, facecolor=COLORS['fibre'],
                                   edgecolor='black', linewidth=2)
            ax.add_patch(fibre_term)
            ax.text(3.65, 5.15, 'Fibre\nPatch', fontsize=8, ha='center')

            # Cat6 ring around lab
            cat6_ring = Rectangle((0.6, 5.1), 3.3, 2.3, fill=False,
                                 edgecolor=COLORS['copper'], linewidth=3, linestyle='--')
            ax.add_patch(cat6_ring)
            ax.text(0.7, 5.0, 'Cat6 Ring\n(8-12 outlets)', fontsize=8)

            # Kitchen/Living (south-west = bottom-left)
            kitchen = FancyBboxPatch((0.5, 1.5), 3, 2.5, boxstyle="round,pad=0.1",
                                    edgecolor=COLORS['border'], facecolor='#FFE5CC',
                                    linewidth=2, alpha=0.6)
            ax.add_patch(kitchen)
            ax.text(2, 3.5, 'Kitchen/Living', fontsize=12, ha='center')

            # Optional AP-G2 (central hallway)
            ap_g2 = Circle((5.5, 4), 0.2, facecolor=COLORS['ap'],
                          edgecolor='black', linewidth=2, linestyle='--')
            ax.add_patch(ap_g2)
            ax.text(5.5, 3.5, 'AP-G2\n(Optional)', fontsize=9, ha='center',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

            # Stair core (central)
            stair = Rectangle((5, 2.5), 1.5, 2, facecolor='#D5D8DC',
                            edgecolor='black', linewidth=2)
            ax.add_patch(stair)
            ax.text(5.75, 3.5, 'Stair\nCore', fontsize=10, ha='center', fontweight='bold')

            # WAN entry point
            wan_entry = Rectangle((7, 6.5), 0.4, 0.4, facecolor=COLORS['wan'],
                                 edgecolor='black', linewidth=2)
            ax.add_patch(wan_entry)
            ax.text(7.2, 6.1, 'WAN\nEntry', fontsize=8, ha='center')

            # Primary riser (bathroom stack)
            riser = Rectangle((7.5, 2), 0.8, 4, facecolor='#AED6F1',
                            edgecolor='black', linewidth=2, linestyle=':')
            ax.add_patch(riser)
            ax.text(7.9, 4, 'Primary\nRiser', fontsize=9, ha='center',
                   rotation=90, va='center')

            # Legend
            ax.text(0.5, 0.7, '← Thick walls = Concrete/Breezeblock (high RF attenuation)',
                   fontsize=9, style='italic')

        elif idx == 1:  # First floor
            # RACK ROOM (east/central-right)
            rack_room = FancyBboxPatch((7, 3), 2.3, 2.1, boxstyle="round,pad=0.1",
                                      edgecolor=COLORS['border'], facecolor=COLORS['core'],
                                      linewidth=4, alpha=0.8)
            ax.add_patch(rack_room)
            ax.text(8.15, 4.8, 'RACK ROOM', fontsize=14, fontweight='bold', ha='center')
            ax.text(8.15, 4.5, '2.33m × 2.09m', fontsize=10, ha='center')

            # Equipment in rack
            equipment = [
                ('18U Rack', 4.2),
                ('UDM-Pro-Max', 3.95),
                ('ECS-24-PoE', 3.7),
                ('Supermicro 4U', 3.45),
                ('UPS 1500VA', 3.2),
            ]
            for eq, y_pos in equipment:
                ax.text(7.3, y_pos, f'• {eq}', fontsize=8, va='center')

            # Bathroom (adjacent to rack room)
            bathroom = Rectangle((6, 3), 0.8, 2.1, facecolor='#E8DAEF',
                                edgecolor='black', linewidth=2)
            ax.add_patch(bathroom)
            ax.text(6.4, 4.05, 'Bath', fontsize=9, ha='center', rotation=90, va='center')

            # Bedrooms
            bedroom1 = FancyBboxPatch((0.5, 4.5), 2.5, 2.5, boxstyle="round,pad=0.1",
                                     edgecolor=COLORS['border'], facecolor='#FAD7A0',
                                     linewidth=2, alpha=0.6)
            ax.add_patch(bedroom1)
            ax.text(1.75, 6.5, 'Bedroom 1', fontsize=11, ha='center')
            ax.text(1.75, 5.2, '2× RJ45', fontsize=9, ha='center')

            bedroom2 = FancyBboxPatch((3.5, 4.5), 2, 2.5, boxstyle="round,pad=0.1",
                                     edgecolor=COLORS['border'], facecolor='#FAD7A0',
                                     linewidth=2, alpha=0.6)
            ax.add_patch(bedroom2)
            ax.text(4.5, 6.5, 'Bedroom 2', fontsize=11, ha='center')

            # Landing/hallway
            landing = Rectangle((3, 2.5), 3, 1.5, facecolor='#ECF0F1',
                               edgecolor='black', linewidth=1, linestyle='--')
            ax.add_patch(landing)
            ax.text(4.5, 3.25, 'Landing', fontsize=10, ha='center')

            # AP-F1 (landing ceiling)
            ap_f1 = Circle((4.5, 3.25), 0.25, facecolor=COLORS['ap'],
                          edgecolor='black', linewidth=2)
            ax.add_patch(ap_f1)
            ax.text(4.5, 2.7, 'AP-F1\n(U6-Enterprise)', fontsize=9, ha='center',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

            # Stair core
            stair = Rectangle((5, 1), 1.5, 2, facecolor='#D5D8DC',
                            edgecolor='black', linewidth=2)
            ax.add_patch(stair)
            ax.text(5.75, 2, 'Stair', fontsize=10, ha='center')

            # Primary riser
            riser = Rectangle((6, 1), 0.8, 6, facecolor='#AED6F1',
                            edgecolor='black', linewidth=2, linestyle=':')
            ax.add_patch(riser)

            # Fibre backbone annotation
            ax.annotate('', xy=(7.5, 1.5), xytext=(7.5, 0.5),
                       arrowprops=dict(arrowstyle='<->', color=COLORS['fibre'], lw=3))
            ax.text(7.8, 1, '10G Fibre\nto Lab', fontsize=9, ha='left',
                   bbox=dict(boxstyle='round', facecolor=COLORS['fibre'], alpha=0.7))

        else:  # Second floor
            # Living room (central)
            living = FancyBboxPatch((2, 4), 3.5, 3, boxstyle="round,pad=0.1",
                                   edgecolor=COLORS['border'], facecolor='#D6EAF8',
                                   linewidth=2, alpha=0.6)
            ax.add_patch(living)
            ax.text(3.75, 6.5, 'Living Room', fontsize=12, ha='center')

            # AP-S1 (living room ceiling)
            ap_s1 = Circle((3.75, 5.5), 0.25, facecolor=COLORS['ap'],
                          edgecolor='black', linewidth=2)
            ax.add_patch(ap_s1)
            ax.text(3.75, 4.9, 'AP-S1\n(U6-Enterprise)', fontsize=9, ha='center',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

            # Bedroom
            bedroom3 = FancyBboxPatch((6, 4.5), 2.5, 2.5, boxstyle="round,pad=0.1",
                                     edgecolor=COLORS['border'], facecolor='#FAD7A0',
                                     linewidth=2, alpha=0.6)
            ax.add_patch(bedroom3)
            ax.text(7.25, 6.5, 'Bedroom 3', fontsize=11, ha='center')
            ax.text(7.25, 5.2, '2× RJ45', fontsize=9, ha='center')

            # Bathroom
            bathroom2 = Rectangle((6, 2), 1.5, 1.8, facecolor='#E8DAEF',
                                 edgecolor='black', linewidth=2)
            ax.add_patch(bathroom2)
            ax.text(6.75, 2.9, 'Bath', fontsize=9, ha='center')

            # Balcony (west = top)
            balcony = Rectangle((1, 7), 4, 0.8, facecolor='#ABEBC6',
                               edgecolor='black', linewidth=2, linestyle='--')
            ax.add_patch(balcony)
            ax.text(3, 7.4, 'Balcony', fontsize=10, ha='center')

            # 5G antenna on west elevation
            antenna = Circle((3, 7.6), 0.15, facecolor=COLORS['wan'],
                           edgecolor='black', linewidth=2)
            ax.add_patch(antenna)
            ax.text(3, 7.9, '5G Ant', fontsize=8, ha='center', fontweight='bold')

            # Primary riser
            riser = Rectangle((6, 1), 0.8, 6, facecolor='#AED6F1',
                            edgecolor='black', linewidth=2, linestyle=':')
            ax.add_patch(riser)
            ax.text(6.4, 4, 'Riser', fontsize=9, ha='center', rotation=90, va='center')

    plt.tight_layout()
    output_file = OUTPUT_DIR / "physical_layout.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor=COLORS['background'])
    print(f"✓ Saved physical layout diagram: {output_file}")
    plt.close()


def create_logical_network_diagram():
    """Create logical network topology diagram with equipment and connections."""
    fig, ax = plt.subplots(figsize=(18, 12))
    fig.patch.set_facecolor(COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    ax.axis('off')

    # Title
    fig.suptitle('Fairfield House Network Infrastructure - Logical Topology',
                 fontsize=18, fontweight='bold', y=0.98)

    # WAN Layer (top)
    wan_y = 10

    # Legacy broadband
    legacy_box = FancyBboxPatch((1, wan_y), 2, 0.8, boxstyle="round,pad=0.05",
                               edgecolor='black', facecolor=COLORS['wan'],
                               linewidth=2)
    ax.add_patch(legacy_box)
    ax.text(2, wan_y + 0.4, 'Legacy Broadband', fontsize=11, ha='center', fontweight='bold')
    ax.text(2, wan_y + 0.1, '~10 Mbps', fontsize=9, ha='center')

    # 5G WAN
    fiveg_antenna = FancyBboxPatch((4.5, wan_y), 1.5, 0.8, boxstyle="round,pad=0.05",
                                  edgecolor='black', facecolor=COLORS['wan'],
                                  linewidth=2)
    ax.add_patch(fiveg_antenna)
    ax.text(5.25, wan_y + 0.6, '5G Antenna', fontsize=10, ha='center', fontweight='bold')
    ax.text(5.25, wan_y + 0.35, '(West Elevation)', fontsize=8, ha='center', style='italic')
    ax.text(5.25, wan_y + 0.1, 'Directional 10+dBi', fontsize=8, ha='center')

    # 5G Modem
    fiveg_modem = FancyBboxPatch((6.5, wan_y), 2.5, 0.8, boxstyle="round,pad=0.05",
                                edgecolor='black', facecolor=COLORS['wan'],
                                linewidth=2)
    ax.add_patch(fiveg_modem)
    ax.text(7.75, wan_y + 0.6, '5G CPE/Modem', fontsize=10, ha='center', fontweight='bold')
    ax.text(7.75, wan_y + 0.35, 'Teltonika RUTX50', fontsize=9, ha='center')
    ax.text(7.75, wan_y + 0.1, 'Ethernet WAN Output', fontsize=8, ha='center')

    # Connection from antenna to modem
    ax.plot([6, 6.5], [wan_y + 0.4, wan_y + 0.4], 'r-', linewidth=2)

    # Gateway Layer
    gateway_y = 8

    # UDM-Pro-Max
    gateway = FancyBboxPatch((3, gateway_y), 3.5, 1.2, boxstyle="round,pad=0.05",
                            edgecolor='black', facecolor=COLORS['core'],
                            linewidth=3)
    ax.add_patch(gateway)
    ax.text(4.75, gateway_y + 0.9, 'UniFi Dream Machine Pro Max', fontsize=12,
            ha='center', fontweight='bold')
    ax.text(4.75, gateway_y + 0.6, '(UDM-Pro-Max)', fontsize=10, ha='center')
    ax.text(4.75, gateway_y + 0.35, '2× WAN, 2× 10G SFP+, 5 Gbps IPS', fontsize=9, ha='center')
    ax.text(4.75, gateway_y + 0.1, 'Dual-WAN, QoS, VLANs, Policy Routing', fontsize=8,
            ha='center', style='italic')

    # WAN connections to gateway
    ax.annotate('', xy=(4, gateway_y + 1.2), xytext=(2.5, wan_y),
               arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(3, gateway_y + 1.5, 'WAN1', fontsize=8, ha='center',
            bbox=dict(boxstyle='round', facecolor='white'))

    ax.annotate('', xy=(5.5, gateway_y + 1.2), xytext=(7.75, wan_y),
               arrowprops=dict(arrowstyle='->', color='red', lw=3))
    ax.text(6.5, gateway_y + 1.5, 'WAN2 (5G Primary)', fontsize=8, ha='center',
            bbox=dict(boxstyle='round', facecolor='white'))

    # Core Switch Layer
    switch_y = 6

    # Core switch
    core_switch = FancyBboxPatch((2.5, switch_y), 4.5, 1.2, boxstyle="round,pad=0.05",
                                edgecolor='black', facecolor=COLORS['core'],
                                linewidth=3)
    ax.add_patch(core_switch)
    ax.text(4.75, switch_y + 0.9, 'UniFi Enterprise Campus 24 PoE', fontsize=12,
            ha='center', fontweight='bold')
    ax.text(4.75, switch_y + 0.6, '(ECS-24-PoE)', fontsize=10, ha='center')
    ax.text(4.75, switch_y + 0.35, '24× 1GbE + 10G RJ45, 25G SFP28, 1050W PoE+++',
            fontsize=9, ha='center')
    ax.text(4.75, switch_y + 0.1, 'Layer 3, VLAN routing, QoS', fontsize=8,
            ha='center', style='italic')

    # Gateway to switch connection
    ax.plot([4.75, 4.75], [gateway_y, switch_y + 1.2], color=COLORS['fibre'],
            linewidth=4, linestyle='-')
    ax.text(5, switch_y + 1.4, '10G SFP+', fontsize=9, ha='left',
            bbox=dict(boxstyle='round', facecolor=COLORS['fibre'], alpha=0.7))

    # Distribution Layer
    dist_y = 3.5

    # Lab switch
    lab_switch = FancyBboxPatch((0.5, dist_y), 2.5, 0.9, boxstyle="round,pad=0.05",
                               edgecolor='black', facecolor=COLORS['lab'],
                               linewidth=2)
    ax.add_patch(lab_switch)
    ax.text(1.75, dist_y + 0.65, 'Lab Switch', fontsize=10, ha='center', fontweight='bold')
    ax.text(1.75, dist_y + 0.4, 'Pro Max/XG Series', fontsize=9, ha='center')
    ax.text(1.75, dist_y + 0.15, '10G SFP+ + Multi-Gig', fontsize=8, ha='center')

    # Fibre link to lab
    ax.plot([3, 3], [switch_y, dist_y + 0.9], color=COLORS['fibre'],
            linewidth=4, linestyle='-')
    ax.text(3.3, dist_y + 1.5, '10G Fibre\nOM4 30m', fontsize=9, ha='left',
            bbox=dict(boxstyle='round', facecolor=COLORS['fibre'], alpha=0.7))

    # APs
    ap_positions = [
        (3.5, dist_y, 'AP-G1\n(Lab)'),
        (5.5, dist_y, 'AP-F1\n(1st Floor)'),
        (7.5, dist_y, 'AP-S1\n(2nd Floor)'),
        (9.5, dist_y, 'AP-G2\n(Optional)'),
    ]

    for i, (x, y, label) in enumerate(ap_positions):
        linestyle = '--' if 'Optional' in label else '-'
        alpha = 0.5 if 'Optional' in label else 1.0

        ap = Circle((x, y + 0.45), 0.35, facecolor=COLORS['ap'],
                   edgecolor='black', linewidth=2, alpha=alpha, linestyle=linestyle)
        ax.add_patch(ap)
        ax.text(x, y + 0.45, 'WiFi 6E', fontsize=8, ha='center', fontweight='bold')
        ax.text(x, y + 0.05, label, fontsize=8, ha='center')
        ax.text(x, y - 0.2, 'U6-Enterprise', fontsize=7, ha='center', style='italic')

        # PoE connection from core switch
        ax.plot([4.75, x], [switch_y, y + 0.8], color=COLORS['copper'],
               linewidth=2, linestyle=linestyle)

        # First connection gets labeled
        if i == 0:
            ax.text(4, switch_y - 0.3, 'PoE+ Cat6', fontsize=8, ha='center',
                   bbox=dict(boxstyle='round', facecolor=COLORS['copper'], alpha=0.7))

    # End Devices Layer
    device_y = 1.5

    # Lab devices
    lab_device = FancyBboxPatch((0.2, device_y), 2, 0.7, boxstyle="round,pad=0.05",
                               edgecolor='black', facecolor=COLORS['lab'],
                               linewidth=2)
    ax.add_patch(lab_device)
    ax.text(1.2, device_y + 0.5, 'Lab Workstations', fontsize=10, ha='center', fontweight='bold')
    ax.text(1.2, device_y + 0.25, 'Supermicro 4U Server', fontsize=8, ha='center')
    ax.text(1.2, device_y + 0.05, '8-12× RJ45 Outlets (Cat6 Ring)', fontsize=7, ha='center')

    ax.plot([1.75, 1.2], [dist_y, device_y + 0.7], color=COLORS['copper'],
           linewidth=2)

    # Client devices
    client_device = FancyBboxPatch((5, device_y), 3, 0.7, boxstyle="round,pad=0.05",
                                  edgecolor='black', facecolor='#E8F8F5',
                                  linewidth=2)
    ax.add_patch(client_device)
    ax.text(6.5, device_y + 0.5, 'Client Devices', fontsize=10, ha='center', fontweight='bold')
    ax.text(6.5, device_y + 0.25, 'Bedrooms: 2× RJ45 per room', fontsize=8, ha='center')
    ax.text(6.5, device_y + 0.05, 'WiFi: Laptops, phones, IoT devices', fontsize=7, ha='center')

    # VLAN annotation box
    vlan_box = FancyBboxPatch((11, 7), 3.5, 2.5, boxstyle="round,pad=0.1",
                             edgecolor='black', facecolor='white',
                             linewidth=2, linestyle='--')
    ax.add_patch(vlan_box)
    ax.text(12.75, 9.2, 'VLAN Configuration', fontsize=11, ha='center', fontweight='bold')

    vlans = [
        ('VLAN 10', 'LAB', '#C7CEEA'),
        ('VLAN 20', 'HOME', '#D5F4E6'),
        ('VLAN 30', 'IOT', '#FFE5CC'),
        ('VLAN 40', 'GUEST', '#FADBD8'),
        ('VLAN 99', 'Management', '#D5D8DC'),
    ]

    for i, (vlan_id, vlan_name, color) in enumerate(vlans):
        y_offset = 8.7 - (i * 0.35)
        vlan_label = Rectangle((11.3, y_offset - 0.15), 0.4, 0.25,
                               facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(vlan_label)
        ax.text(11.9, y_offset, f'{vlan_id}: {vlan_name}', fontsize=9, va='center')

    # BOM Summary box
    bom_box = FancyBboxPatch((11, 3.5), 3.5, 3, boxstyle="round,pad=0.1",
                            edgecolor='black', facecolor='white',
                            linewidth=2, linestyle='--')
    ax.add_patch(bom_box)
    ax.text(12.75, 6.2, 'Core BOM Summary', fontsize=11, ha='center', fontweight='bold')

    bom_items = [
        ('UDM-Pro-Max', '£479'),
        ('ECS-24-PoE Switch', '£1,989'),
        ('3× U6-Enterprise AP', '£710'),
        ('5G Modem + Antenna', '£650'),
        ('18U Rack + UPS', '£700'),
        ('Fibre + Cabling', '£690'),
        ('', ''),
        ('TOTAL', '£5,891'),
    ]

    for i, (item, price) in enumerate(bom_items):
        y_offset = 5.8 - (i * 0.3)
        if item:
            fontweight = 'bold' if item == 'TOTAL' else 'normal'
            ax.text(11.3, y_offset, item, fontsize=9, va='center', fontweight=fontweight)
            ax.text(14.2, y_offset, price, fontsize=9, va='center', ha='right', fontweight=fontweight)
            if item == 'TOTAL':
                ax.plot([11.3, 14.2], [y_offset + 0.1, y_offset + 0.1], 'k-', linewidth=1)

    # Legend
    legend_elements = [
        Line2D([0], [0], color=COLORS['wan'], lw=3, label='WAN Connection'),
        Line2D([0], [0], color=COLORS['fibre'], lw=3, label='10G Fibre'),
        Line2D([0], [0], color=COLORS['copper'], lw=2, label='Cat6/PoE'),
        Line2D([0], [0], color='gray', lw=2, linestyle='--', label='Optional'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=10, framealpha=0.9)

    # Set axis limits
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 11)

    output_file = OUTPUT_DIR / "logical_topology.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor=COLORS['background'])
    print(f"✓ Saved logical topology diagram: {output_file}")
    plt.close()


def create_infrastructure_summary():
    """Create infrastructure summary diagram with key specs and pricing."""
    fig, ax = plt.subplots(figsize=(16, 10))
    fig.patch.set_facecolor(COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    ax.axis('off')

    fig.suptitle('Fairfield House Network Infrastructure - Equipment Summary',
                 fontsize=16, fontweight='bold', y=0.97)

    # Column headers
    headers = ['Category', 'Equipment', 'Specifications', 'Qty', 'Unit Price', 'Total']
    col_widths = [1.5, 3, 4.5, 0.6, 1.2, 1.2]
    col_x = [0.5, 2.2, 5.5, 10.2, 11, 12.4]

    header_y = 9
    for i, (header, x) in enumerate(zip(headers, col_x)):
        ax.text(x, header_y, header, fontsize=11, fontweight='bold', ha='left')

    ax.plot([0.5, 13.8], [header_y - 0.15, header_y - 0.15], 'k-', linewidth=2)

    # Equipment data
    equipment_data = [
        ('Core Network', 'UDM-Pro-Max', '1× 2.5GbE WAN, 1× 10G SFP+ WAN, 2× 10G SFP+ LAN, 5 Gbps IPS', 1, '£479.00', '£479.00'),
        ('Core Network', 'ECS-24-PoE Switch', '24× 1GbE + 10G RJ45, 25G SFP28, 1050W PoE+++, Layer 3', 1, '£1,989.00', '£1,989.00'),
        ('Core Network', 'Lab Switch (Pro Max)', '8-16 port, 10G SFP+ uplink, multi-gig ports', 1, '£500.00', '£500.00'),
        ('', '', '', '', '', ''),
        ('Access Points', 'U6-Enterprise', 'WiFi 6E tri-band, 10.2 Gbps, 802.3at PoE+, 2.5GbE', 3, '£236.62', '£709.86'),
        ('', '', '', '', '', ''),
        ('WAN', '5G Modem (RUTX50)', 'Ethernet WAN, ext antenna, UK bands, dual SIM', 1, '£500.00', '£500.00'),
        ('WAN', '5G Antenna', 'Directional panel, 10+ dBi, outdoor rated', 1, '£150.00', '£150.00'),
        ('', '', '', '', '', ''),
        ('Rack & Power', '18U Server Rack', '800-1000mm depth, floor-standing, used/refurb', 1, '£400.00', '£400.00'),
        ('Rack & Power', 'UPS 1500VA', 'Rack-mount 2U-3U, 10-15 min runtime', 1, '£300.00', '£300.00'),
        ('', '', '', '', '', ''),
        ('Fibre Backbone', 'OM4 Fibre Kit', '30m LC-LC 8-fibre, patch panel, 2× SFP+ modules', 1, '£145.00', '£145.00'),
        ('', '', '', '', '', ''),
        ('Structured Cabling', 'Cat6 Cable Package', '2× 305m boxes U/UTP LSZH', 1, '£179.98', '£179.98'),
        ('Structured Cabling', 'Patch Panel 48-port', '1U rack-mount Cat6', 1, '£54.99', '£54.99'),
        ('Structured Cabling', 'Keystone Jacks', 'Cat6 toolless, 40 units', 1, '£99.60', '£99.60'),
        ('Structured Cabling', 'Faceplates & Boxes', 'Various sizes, 60 units total', 1, '£84.40', '£84.40'),
        ('Structured Cabling', 'Cable Trunking', 'Mini trunking 25mm & 40mm, 60m total', 1, '£102.70', '£102.70'),
        ('', '', '', '', '', ''),
        ('Tools & Misc', 'Installation Tools', 'Cable tester, punchdown, stripper', 1, '£21.96', '£21.96'),
        ('Tools & Misc', 'Patch Cables', 'Copper + fibre assortment', 1, '£100.00', '£100.00'),
        ('Tools & Misc', 'Cable Management', 'Velcro ties, labels, fixings', 1, '£75.00', '£75.00'),
    ]

    current_y = header_y - 0.5
    category_colors = {
        'Core Network': '#4ECDC4',
        'Access Points': '#A8E6CF',
        'WAN': '#FF6B6B',
        'Rack & Power': '#95E1D3',
        'Fibre Backbone': '#FFD93D',
        'Structured Cabling': '#C7CEEA',
        'Tools & Misc': '#D5D8DC',
    }

    for row in equipment_data:
        if row[0]:  # Non-empty row
            category, equipment, specs, qty, unit_price, total = row

            # Background color for category
            if category:
                bg_rect = Rectangle((0.4, current_y - 0.15), 13.5, 0.35,
                                   facecolor=category_colors.get(category, 'white'),
                                   alpha=0.3, edgecolor='none')
                ax.add_patch(bg_rect)

            # Text
            ax.text(col_x[0], current_y, category, fontsize=9, ha='left', fontweight='bold' if category else 'normal')
            ax.text(col_x[1], current_y, equipment, fontsize=9, ha='left')
            ax.text(col_x[2], current_y, specs, fontsize=8, ha='left')
            ax.text(col_x[3], current_y, str(qty), fontsize=9, ha='center')
            ax.text(col_x[4], current_y, unit_price, fontsize=9, ha='left')
            ax.text(col_x[5], current_y, total, fontsize=9, ha='left', fontweight='bold')

        current_y -= 0.35

    # Totals section
    current_y -= 0.2
    ax.plot([0.5, 13.8], [current_y + 0.15, current_y + 0.15], 'k-', linewidth=2)

    totals = [
        ('Equipment Subtotal', '£5,691.49'),
        ('Estimated contingency (5%)', '£284.57'),
        ('', ''),
        ('TOTAL PROJECT COST', '£5,976.06'),
    ]

    for label, value in totals:
        fontweight = 'bold' if 'TOTAL' in label else 'normal'
        fontsize = 11 if 'TOTAL' in label else 10

        if label:
            ax.text(col_x[4], current_y, label, fontsize=fontsize, ha='left', fontweight=fontweight)
            ax.text(col_x[5], current_y, value, fontsize=fontsize, ha='left', fontweight=fontweight)

            if 'TOTAL' in label:
                bg_rect = Rectangle((10.9, current_y - 0.15), 2.95, 0.35,
                                   facecolor='#FFD93D', alpha=0.5, edgecolor='black', linewidth=1)
                ax.add_patch(bg_rect)

        current_y -= 0.35

    # Notes section
    notes_y = 0.8
    ax.text(0.5, notes_y, 'Notes:', fontsize=10, fontweight='bold')
    notes = [
        '• All prices include VAT and reflect Black Friday 2025 discounts where available',
        '• Lab switch pricing estimated; contact Ubiquiti UK for current Professional Max/XG series pricing',
        '• 5G modem and antenna pricing estimated; contact UK suppliers (LinITX) for current availability',
        '• Rack pricing based on used/refurbished units from eBay UK; new racks £400-600',
        '• Installation labor NOT included (Phase 1: Product selection only)',
    ]

    current_note_y = notes_y - 0.3
    for note in notes:
        ax.text(0.7, current_note_y, note, fontsize=8, style='italic')
        current_note_y -= 0.25

    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)

    output_file = OUTPUT_DIR / "equipment_summary.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor=COLORS['background'])
    print(f"✓ Saved equipment summary diagram: {output_file}")
    plt.close()


def main():
    """Generate all network diagrams."""
    print("Generating Fairfield House network infrastructure diagrams...\n")

    create_physical_layout_diagram()
    print()

    create_logical_network_diagram()
    print()

    create_infrastructure_summary()
    print()

    print(f"\n✓ All diagrams saved to {OUTPUT_DIR}/")
    print("\nGenerated diagrams:")
    print("  1. physical_layout.png - 3-floor equipment placement and cabling routes")
    print("  2. logical_topology.png - Network topology with VLANs and connections")
    print("  3. equipment_summary.png - Complete BOM with specifications and pricing")


if __name__ == "__main__":
    main()
