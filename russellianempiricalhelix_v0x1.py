"""
Unified Phase-Interference Model: 4D Atlas & Zx Boundary Engine
---------------------------------------------------------------
Version: Synergy & Fracture Matrix (H-Wave + C-Wave Superposition)

SUMMARY OF USAGE CASE ALIGNMENT TYPES & ALTERNATIVES:
This template acts as a test system analysis boundary logic. It evaluates the 
Phase Differential (Delta-Phi) between overlapping geometric anchors.

1. THERMODYNAMIC BASELINE VARIANT
   - Usage Case: Fluid dynamics, base-state energy, polarity (e.g., H2O).
   - Alignment: Anchored to Hydrogen (Z=1, Phase 0).
   - Alternative [In Comments]: Pure Quantum DFT calculations; restricts data 
     strictly to empirical orbital mechanics without topological interpolation.

2. BIOLOGICAL LATTICE VARIANT
   - Usage Case: Organic chemistry, metastable structures, 4D CAD lattices.
   - Alignment: Anchored to Carbon (Z=6 offset).
   - Alternative [In Comments]: Speculative Organic Lattice; forces all elements 
     into tetrahedral symmetry, ignoring fluid thermodynamic limits.

3. UNIFIED SYNERGY VARIANT (THE COMBINED RATIO)
   - Usage Case: Verifying biological compatibility (C-H-O interactions).
   - Alignment: Superposition of Variant 1 and 2.
   - Boundary Condition: Met by Delta-Phi < Synergy Threshold. Renders 
     "Synergy Bridges" where waves constructively resonate.
   - Alternative [In Comments]: Multi-parameter molecular docking simulations.

4. NEGATOR STRESS TEST (FRACTURE ANALYSIS)
   - Usage Case: Identifying toxicity, radioactivity, and structural shear.
   - Alignment: Targets extreme Delta-Phi dissonance (e.g., Arsenic Z=33).
   - Boundary Condition: Met by Delta-Phi > Fracture Threshold. Triggers Zx mitigation.
   - Alternative [In Comments]: Destructive resonance screening; analyzing lattice breakdown.

Dependencies: pip install numpy plotly
"""

import numpy as np
import plotly.graph_objects as go
import math
import os

# --- EMPIRICAL DATA SETUP ---
SYMBOLS = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og", "Uue", "Ubn"
]

NAMES = [
    "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
    "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium",
    "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
    "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
    "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin",
    "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
    "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
    "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury",
    "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium",
    "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
    "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium",
    "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson", "Ununennium", "Unbinilium"
]

# --- BOUNDARY LOGIC & SYSTEM PARAMETERS ---
O_LEN = 18.0       
ALPHA = 0.025      
GAMMA = 0.015      

# Offsets for Phase Calculation
CARBON_OFFSET = (2 * math.pi * 6) / O_LEN
H_OFFSET = 0.0

# Pattern Recognition Thresholds
T1 = 0.35                      # Metastable Empirical Friction
T2 = 0.55                      # Critical Empirical Instability
SYNERGY_THRESHOLD = 0.15       # Delta-Phi maximum for Constructive Synergy Bridge
FRACTURE_THRESHOLD = 0.60      # Delta-Phi minimum for Destructive Phase Negator (e.g., Arsenic)

def calculate_spl(Z, theta, offset):
    """Calculates SPL S(Z) score for a specific geometric anchor offset."""
    theta_shifted = theta - offset
    kappa = abs(math.cos(theta_shifted)) * math.exp(GAMMA * Z) * 0.05
    H = abs(math.sin(theta_shifted + math.pi/4))
    
    I_val = 0.0
    if Z in [43, 61, 83, 84, 86, 112, 115, 118]:
        I_val = 1.0 
    elif Z > 100:
        I_val = 0.5 + 0.5 * abs(math.sin(Z))
        
    return (0.3 * kappa) + (0.2 * H) + (0.5 * I_val)

def generate_unified_data():
    nodes = []
    synergy_bridges_x, synergy_bridges_y, synergy_bridges_z = [], [], []
    zx_fracture_nodes = []
    frac_lines_x, frac_lines_y, frac_lines_z = [], [], []
    
    for Z in range(1, 121):
        sym = SYMBOLS[Z-1]
        name = NAMES[Z-1]
        
        # Base Topological Math
        theta_base = (2 * math.pi * Z) / O_LEN
        r = math.exp(ALPHA * Z)
        
        # H-Wave Coordinates (Thermodynamic Baseline)
        theta_H = theta_base - H_OFFSET
        x_H = r * math.cos(theta_H)
        y_H = r * math.sin(theta_H)
        S_H = calculate_spl(Z, theta_base, H_OFFSET)
        
        # C-Wave Coordinates (Biological Baseline)
        theta_C = theta_base - CARBON_OFFSET
        x_C = r * math.cos(theta_C)
        y_C = r * math.sin(theta_C)
        S_C = calculate_spl(Z, theta_base, CARBON_OFFSET)
        
        # THE NEW VARIABLE: Phase Differential Pattern Recognition
        delta_phi = abs(S_H - S_C)
        
        # Classify Node Logic based on Boundaries
        status_H = "Stable" if S_H < T1 else ("Metastable" if S_H < T2 else "Critical")
        status_C = "Stable" if S_C < T1 else ("Metastable" if S_C < T2 else "Critical")
        
        nodes.append({
            "Z": Z, "Symbol": sym, "Name": name, 
            "x_H": x_H, "y_H": y_H, "z": Z, "S_H": S_H, "Status_H": status_H,
            "x_C": x_C, "y_C": y_C, "S_C": S_C, "Status_C": status_C,
            "DeltaPhi": delta_phi
        })
        
        # PATTERN RECOGNITION 1: Constructive Synergy Bridges (Organic Resonance)
        if delta_phi < SYNERGY_THRESHOLD and (S_H < T2 and S_C < T2):
            synergy_bridges_x.extend([x_H, x_C, None])
            synergy_bridges_y.extend([y_H, y_C, None])
            synergy_bridges_z.extend([Z, Z, None])
            
        # PATTERN RECOGNITION 2: Destructive Negators & Critical Fracture (Zx Generation)
        # Specifically targeting extreme dissonance like Arsenic (Z=33)
        if delta_phi > FRACTURE_THRESHOLD or S_H >= T2 or S_C >= T2:
            # Generate mitigation node based on combined friction
            Zx_val = Z + (1.0 - abs(math.sin(theta_base))) * 0.5 
            
            # Eject into a "safe" topological orbit
            theta_x = theta_base + (math.pi / 2) 
            r_x = r * 1.15 
            x_x = r_x * math.cos(theta_x)
            y_x = r_x * math.sin(theta_x)
            
            zx_fracture_nodes.append({
                "Zx": round(Zx_val, 2), "Base_Z": Z, "Symbol": f"Zx({sym})", 
                "Name": f"Mitigation/Fracture Node", "Reason": "Destructive Negator" if delta_phi > FRACTURE_THRESHOLD else "Empirical Instability",
                "x": x_x, "y": y_x, "z": Z, 
                "Color": "#ff00ff" if delta_phi > FRACTURE_THRESHOLD else "#00ffff" # Magenta for Phase Negator, Cyan for standard instability
            })
            
            # Tether the diamond back to its originating thermodynamic coordinate
            frac_lines_x.extend([x_H, x_x, None])
            frac_lines_y.extend([y_H, y_x, None])
            frac_lines_z.extend([Z, Z, None])
            
    return nodes, synergy_bridges_x, synergy_bridges_y, synergy_bridges_z, zx_fracture_nodes, frac_lines_x, frac_lines_y, frac_lines_z

def render_unified_ui(nodes, syn_x, syn_y, syn_z, zx_nodes, frac_x, frac_y, frac_z):
    fig = go.Figure()

    # TRACE 0: H-Wave Backbone
    fig.add_trace(go.Scatter3d(
        x=[n["x_H"] for n in nodes], y=[n["y_H"] for n in nodes], z=[n["z"] for n in nodes],
        mode='lines', line=dict(color='rgba(100, 150, 255, 0.4)', width=3),
        name='H-Wave Path (Thermodynamic)', hoverinfo='skip'
    ))

    # TRACE 1: C-Wave Backbone
    fig.add_trace(go.Scatter3d(
        x=[n["x_C"] for n in nodes], y=[n["y_C"] for n in nodes], z=[n["z"] for n in nodes],
        mode='lines', line=dict(color='rgba(100, 255, 100, 0.4)', width=3),
        name='C-Wave Path (Biological)', hoverinfo='skip'
    ))

    # TRACE 2: H-Wave Nodes
    fig.add_trace(go.Scatter3d(
        x=[n["x_H"] for n in nodes], y=[n["y_H"] for n in nodes], z=[n["z"] for n in nodes],
        mode='markers+text',
        marker=dict(size=5, color=["#4488ff" if n["S_H"] < T1 else "#ffff00" if n["S_H"] < T2 else "#ff0000" for n in nodes], opacity=0.9),
        text=[n["Symbol"] for n in nodes], textposition="top center", textfont=dict(color='white', size=8),
        hovertemplate="<b>%{customdata[3]} (H-Anchor)</b><br>Z = %{customdata[0]}<br>SPL: %{customdata[1]:.3f}<br>Status: %{customdata[2]}<extra></extra>",
        customdata=[[n["Z"], n["S_H"], n["Status_H"], n["Name"]] for n in nodes], name='Thermodynamic Nodes'
    ))

    # TRACE 3: C-Wave Nodes
    fig.add_trace(go.Scatter3d(
        x=[n["x_C"] for n in nodes], y=[n["y_C"] for n in nodes], z=[n["z"] for n in nodes],
        mode='markers+text',
        marker=dict(size=5, color=["#44ff44" if n["S_C"] < T1 else "#ffff00" if n["S_C"] < T2 else "#ff0000" for n in nodes], opacity=0.9),
        text=[n["Symbol"] for n in nodes], textposition="bottom center", textfont=dict(color='white', size=8),
        hovertemplate="<b>%{customdata[3]} (C-Anchor)</b><br>Z = %{customdata[0]}<br>SPL: %{customdata[1]:.3f}<br>Status: %{customdata[2]}<extra></extra>",
        customdata=[[n["Z"], n["S_C"], n["Status_C"], n["Name"]] for n in nodes], name='Biological Nodes'
    ))

    # TRACE 4: Synergy Bridges (The Unified Interference Pattern)
    fig.add_trace(go.Scatter3d(
        x=syn_x, y=syn_y, z=syn_z,
        mode='lines', line=dict(color='rgba(255, 255, 255, 0.8)', width=2),
        name='Synergy Bridges (Delta-Phi Resonance)', hoverinfo='skip'
    ))

    # TRACE 5: Fracture / Zx Mitigation Nodes (Destructive Pattern Recognition)
    fig.add_trace(go.Scatter3d(
        x=[n["x"] for n in zx_nodes], y=[n["y"] for n in zx_nodes], z=[n["z"] for n in zx_nodes],
        mode='markers', marker=dict(size=7, color=[n["Color"] for n in zx_nodes], symbol='diamond', line=dict(width=1, color='white')),
        hovertemplate="<b>%{customdata[3]}</b><br>Base Anchor: Z=%{customdata[0]} (%{customdata[1]})<br>Zx = %{customdata[2]}<br>Cause: %{customdata[4]}<extra></extra>",
        customdata=[[n["Base_Z"], n["Symbol"], n["Zx"], n["Name"], n["Reason"]] for n in zx_nodes], name='Fracture/Mitigation Nodes'
    ))

    # TRACE 6: Fracture Tethers (Visualizing the relation to the base anchor)
    fig.add_trace(go.Scatter3d(
        x=frac_x, y=frac_y, z=frac_z,
        mode='lines', line=dict(color='rgba(255, 100, 255, 0.4)', width=1.5, dash='dot'),
        name='Fracture Tethers', hoverinfo='skip'
    ))

    # --- BOUNDARY LOGIC PRACTICAL USAGE TOGGLES ---
    # Trace Index: 0:H-Path, 1:C-Path, 2:H-Nodes, 3:C-Nodes, 4:Bridges, 5:Fractures, 6:Tethers
    updatemenus = [
        dict(
            type="buttons", direction="down", x=1.0, y=1.0, xanchor="right", yanchor="top", showactive=True,
            buttons=list([
                dict(label="[1] Unified Synergy (All Data)", method="update", 
                     args=[{"visible": [True, True, True, True, True, True, True]}]),
                dict(label="[2] Thermodynamic (H-Wave)", method="update", 
                     args=[{"visible": [True, False, True, False, False, False, False]}]),
                dict(label="[3] Biological (C-Wave)", method="update", 
                     args=[{"visible": [False, True, False, True, False, False, False]}]),
                dict(label="[4] Fracture Test (Arsenic/Negators)", method="update", 
                     args=[{"visible": [True, True, False, False, False, True, True]}]),
            ]),
            font=dict(color="#000000"), bgcolor="#f0f0f0", bordercolor="#444444"
        )
    ]

    fig.update_layout(
        title="Unified Phase-Interference Model: Usage Case Boundary Logic",
        template="plotly_dark", updatemenus=updatemenus,
        scene=dict(
            xaxis=dict(showbackground=False, showgrid=False, zeroline=False, showticklabels=False, title=''),
            yaxis=dict(showbackground=False, showgrid=False, zeroline=False, showticklabels=False, title=''),
            zaxis=dict(showbackground=False, gridcolor='rgba(255,255,255,0.1)', title='Atomic Mass / Octave Evolution'),
            camera=dict(up=dict(x=0, y=0, z=1), center=dict(x=0, y=0, z=0), eye=dict(x=-1.5, y=-1.5, z=1.5))
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )

    filename = "Unified_Phase_Interference_Model.html"
    fig.write_html(filename)
    print(f"Unified Boundary System complete. Output saved to: {os.path.abspath(filename)}")

if __name__ == "__main__":
    nodes, syn_x, syn_y, syn_z, zx_nodes, frac_x, frac_y, frac_z = generate_unified_data()
    render_unified_ui(nodes, syn_x, syn_y, syn_z, zx_nodes, frac_x, frac_y, frac_z)