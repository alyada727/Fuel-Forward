import streamlit as st

##################### Home Page #####################
st.set_page_config(page_title="Fuel Forward", layout="wide")

st.markdown("""
<style>

/* Main page background */
.stApp {
    background-color: #EAF6FF;
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #D9EEFA;
}

/* General text */
html, body, [class*="css"] {
    color: #1F2D3D;
    font-family: 'Arial', sans-serif;
}

/* Top navigation buttons */
div.stButton > button {
    background-color: #A7D8F5;
    color: #12344D;
    border: none;
    border-radius: 12px;
    padding: 12px 20px;
    font-weight: bold;
    font-size: 16px;
    transition: 0.3s;
}

/* Hover effect for buttons */
div.stButton > button:hover {
    background-color: #7FC8F8;
    color: #0B2239;
    border: none;
}

/* Select boxes */
div[data-baseweb="select"] > div {
    background-color: white;
    border-radius: 10px;
}

/* Headers */
h1, h2, h3 {
    color: #1B4965;
}

/* FEI box styling */
.fei-box {
    background-color: #f5f7fa;
    border: 1px solid #d9dee5;
    border-radius: 15px;
    padding: 22px;
    margin-top: 20px;
}

.score-box {
    background-color: #ffffff;
    border: 1px solid #d9dee5;
    border-radius: 12px;
    padding: 16px;
    margin-top: 16px;
}
</style>
""", unsafe_allow_html=True)

##################### Naming #####################
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "chemical" not in st.session_state:
    st.session_state.chemical = "Hydrogen"

if "concentration" not in st.session_state:
    st.session_state.concentration = "50%"

if "temperature" not in st.session_state:
    st.session_state.temperature = "Medium"

if "pressure" not in st.session_state:
    st.session_state.pressure = "75%"

##################### Navigating Pages #####################
def go_to(page_name):
    st.session_state.page = page_name


##################### Header #####################
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Home", use_container_width=True):
        go_to("Home")
        st.rerun()

with col2:
    if st.button("Simulator", use_container_width=True):
        go_to("Simulator")
        st.rerun()

with col3:
    if st.button("Chemical Info", use_container_width=True):
        go_to("Chemical Info")
        st.rerun()

with col4:
    if st.button("Hybrid/EV", use_container_width=True):
        go_to("Hybrid/EV")
        st.rerun()

with col5:
    if st.button("Alternate Options", use_container_width=True):
        go_to("Alternate Options")
        st.rerun()

st.markdown("---")


##################### Chemical Info #####################
chemical_options = [
    "Biodiesel",
    "Hydrogen",
    "Lithium Sulfur Battery",
    "Lithium Ion Battery",
    "Ethanol",
    "Biobutanol",
]

concentration_options = ["25%", "50%", "75%"]
temperature_options = ["Low", "Medium", "High"]
pressure_options = ["25%", "50%", "75%", "100%"]

chemical_info = {
    "Hydrogen": {
        "description": "Hydrogen can power vehicles through fuel cells or modified combustion engines. In fuel-cell systems, hydrogen reacts with oxygen to produce electricity and water.",
        "best_use": "Best for low tailpipe-emission transportation when clean hydrogen production and fueling infrastructure are available.",
        "advantages": [
            "Produces water as the main direct byproduct in fuel-cell vehicles",
            "Very high energy density by mass",
            "Fast refueling compared with most battery systems",
            "Can be produced from renewable-powered electrolysis"
        ],
        "challenges": [
            "Storage is difficult because hydrogen needs high-pressure tanks or cryogenic handling",
            "Most hydrogen today is not produced renewably",
            "Fuel cells and hydrogen production are still expensive",
            "Fueling infrastructure is limited"
        ],
        "environment_notes": [
            "Very low point-of-use emissions",
            "Lifecycle impact depends heavily on production method",
            "Steam methane reforming has high carbon emissions",
            "Renewable electrolysis can make hydrogen much cleaner"
        ],
        "fun_fact": "A hydrogen vehicle can refuel in about 3 to 5 minutes and a fuel-cell version releases only water vapor at the tailpipe.",
        "fei_score": "66/100"
    },

    "Biodiesel": {
        "description": "Biodiesel is an alternative fuel made from vegetable oils, animal fats, or recycled used cooking oil. It is mainly used in diesel engines, often in blends such as B20.",
        "best_use": "Best as a lower-carbon diesel substitute when waste oil or recycled feedstocks are available.",
        "advantages": [
            "Can reduce overall carbon pollution compared with regular diesel",
            "Made from waste oil instead of relying only on fossil fuels",
            "Can often use existing diesel engines and fuel stations",
            "Less flammable than gasoline"
        ],
        "challenges": [
            "Has slightly less energy than regular diesel",
            "Can thicken in cold weather",
            "Cannot be used in regular gasoline cars",
            "Limited feedstock means it cannot replace all diesel demand"
        ],
        "environment_notes": [
            "Strong sustainability benefit when made from recycled cooking oil",
            "Still creates emissions during use",
            "Cold-weather performance can reduce practicality",
            "Even small biodiesel blends can improve lubrication in diesel systems"
        ],
        "fun_fact": "Adding a small amount of biodiesel can help reduce friction and wear in diesel engines.",
        "fei_score": "78/100"
    },

    "Lithium Sulfur Battery": {
        "description": "Lithium-sulfur batteries use lithium metal as the anode and sulfur as the cathode. They are a promising next-generation battery because of their very high theoretical energy density.",
        "best_use": "Best for future EV designs that need lighter battery packs and longer driving range.",
        "advantages": [
            "Very high theoretical energy density",
            "Sulfur is abundant, lightweight, and low-cost",
            "Could potentially outperform lithium-ion batteries in range",
            "Uses existing EV charging infrastructure"
        ],
        "challenges": [
            "Polysulfide shuttle effect causes capacity fade",
            "Lithium metal instability can create dendrite risk",
            "Cycle life is still limited in many prototypes",
            "Technology is not yet as mature as lithium-ion"
        ],
        "environment_notes": [
            "Low direct operating emissions",
            "Sulfur can come from industrial byproducts",
            "Lithium mining still has environmental impact",
            "Manufacturing impact may be lower than Li-ion in the long term"
        ],
        "fun_fact": "Lithium-sulfur batteries could potentially double EV range at the same weight if the stability issues are solved.",
        "fei_score": "77/100"
    },

    "Lithium Ion Battery": {
        "description": "Lithium-ion batteries are the dominant battery technology in modern electric vehicles. They are well-understood, rechargeable, and supported by a large global supply chain.",
        "best_use": "Best for current real-world EVs because the technology is mature and widely available.",
        "advantages": [
            "High powertrain efficiency in electric vehicles",
            "Good cycle life compared with emerging battery chemistries",
            "Large manufacturing base and growing charging networks",
            "Very low operating cost per mile"
        ],
        "challenges": [
            "Mining lithium, nickel, and cobalt has environmental costs",
            "Battery packs are heavy",
            "Manufacturing is energy-intensive",
            "Thermal runaway remains a safety concern"
        ],
        "environment_notes": [
            "Zero tailpipe emissions during use",
            "Lifecycle emissions improve when charged with renewable electricity",
            "Materials are finite but recyclable",
            "Environmental impact is higher during production than during driving"
        ],
        "fun_fact": "Home charging is one of the biggest practical advantages of lithium-ion EVs.",
        "fei_score": "71/100"
    },

    "Ethanol": {
        "description": "Ethanol is a liquid biofuel made from fermented biomass such as corn, sugarcane, or cellulosic feedstocks. It is commonly blended with gasoline in fuels like E10, E15, and E85.",
        "best_use": "Best as a renewable blending fuel in flex-fuel systems where existing fuel infrastructure is important.",
        "advantages": [
            "Renewable in principle because it is biomass-based",
            "Works in many existing fuel systems with blends",
            "High octane rating can support higher compression ratios",
            "Burns cleaner than gasoline in some respects"
        ],
        "challenges": [
            "Lower energy density than gasoline",
            "Still emits CO2 at the tailpipe",
            "Large-scale production can require major land, water, and fertilizer use",
            "Pure ethanol can be hard on some older engine materials"
        ],
        "environment_notes": [
            "Environmental impact depends heavily on feedstock and farming practices",
            "Cellulosic ethanol is cleaner than corn ethanol",
            "Lower energy density means more fuel may be needed per mile",
            "Can reduce carbon emissions compared with gasoline in the right system"
        ],
        "fun_fact": "Ethanol is a high-octane fuel, so it can help performance-oriented engines run efficiently.",
        "fei_score": "59/100"
    },

    "Biobutanol": {
        "description": "Biobutanol is a biomass-based liquid fuel that behaves much more like gasoline than ethanol does. It is often considered a strong drop-in fuel candidate.",
        "best_use": "Best as a practical gasoline-like renewable fuel that fits existing vehicle and fuel infrastructure.",
        "advantages": [
            "Closer to gasoline than ethanol in behavior and energy content",
            "About 90 percent of gasoline's energy content",
            "Can often work without major engine modifications",
            "Non-corrosive and does not mix with water, so it fits existing pipelines better"
        ],
        "challenges": [
            "Production is more difficult and expensive than ethanol",
            "Large-scale production capacity is still limited",
            "Still requires energy-intensive fermentation processes",
            "Not yet common in the fuel market"
        ],
        "environment_notes": [
            "Can be nearly carbon-neutral when sourced sustainably",
            "Lower vapor pressure means less evaporation and smog formation than some fuels",
            "Strong infrastructure compatibility improves practicality",
            "Production energy demand still affects total sustainability"
        ],
        "fun_fact": "Biobutanol is often called a strong 'drop-in' fuel because it behaves so much like gasoline.",
        "fei_score": "85/100"
    },
}


##################### Fuel Index #####################
base_scores = {
    "Hydrogen": {
        "energy_density": 15,
        "system_efficiency": 14,
        "carbon_emissions": 19,
        "renewability": 8,
        "waste_byproducts": 5,
        "infrastructure": 6,
        "storage_transport": 3,
        "weight_penalty": 8,
        "stability_risk": 6,
    },
    "Biodiesel": {
        "energy_density": 11,
        "system_efficiency": 10,
        "carbon_emissions": 10,
        "renewability": 8,
        "waste_byproducts": 3,
        "infrastructure": 9,
        "storage_transport": 4,
        "weight_penalty": 7,
        "stability_risk": 8,
    },
    "Lithium Sulfur Battery": {
        "energy_density": 13,
        "system_efficiency": 13,
        "carbon_emissions": 17,
        "renewability": 6,
        "waste_byproducts": 4,
        "infrastructure": 6,
        "storage_transport": 4,
        "weight_penalty": 7,
        "stability_risk": 6,
    },
    "Lithium Ion Battery": {
        "energy_density": 12,
        "system_efficiency": 14,
        "carbon_emissions": 16,
        "renewability": 5,
        "waste_byproducts": 4,
        "infrastructure": 7,
        "storage_transport": 4,
        "weight_penalty": 6,
        "stability_risk": 7,
    },
    "Ethanol": {
        "energy_density": 10,
        "system_efficiency": 10,
        "carbon_emissions": 11,
        "renewability": 8,
        "waste_byproducts": 3,
        "infrastructure": 8,
        "storage_transport": 4,
        "weight_penalty": 8,
        "stability_risk": 8,
    },
    "Biobutanol": {
        "energy_density": 11,
        "system_efficiency": 11,
        "carbon_emissions": 12,
        "renewability": 8,
        "waste_byproducts": 3,
        "infrastructure": 7,
        "storage_transport": 4,
        "weight_penalty": 8,
        "stability_risk": 8,
    },
}


def clamp(value, low, high):
    return max(low, min(high, value))


def apply_modifiers(scores, chemical, concentration, temperature, pressure):
    s = scores.copy()

    # Concentration effects
    if concentration == "25%":
        s["energy_density"] -= 2
        s["system_efficiency"] -= 1
        s["carbon_emissions"] += 1 if chemical in ["Ethanol", "Biodiesel", "Biobutanol"] else 0
    elif concentration == "50%":
        pass
    elif concentration == "75%":
        s["energy_density"] += 1
        if chemical in ["Ethanol", "Biodiesel", "Biobutanol"]:
            s["carbon_emissions"] -= 1
            s["waste_byproducts"] -= 1
        if chemical == "Hydrogen":
            s["stability_risk"] -= 1

    # Temperature effects
    if temperature == "Low":
        if chemical in ["Biodiesel", "Ethanol", "Biobutanol"]:
            s["system_efficiency"] -= 2
            s["waste_byproducts"] -= 1
        if chemical in ["Lithium Sulfur Battery", "Lithium Ion Battery"]:
            s["system_efficiency"] -= 1
            s["stability_risk"] -= 1
        if chemical == "Hydrogen":
            s["stability_risk"] += 1

    elif temperature == "Medium":
        s["system_efficiency"] += 1

    elif temperature == "High":
        if chemical == "Hydrogen":
            s["system_efficiency"] -= 1
            s["stability_risk"] -= 2
        elif chemical in ["Lithium Sulfur Battery", "Lithium Ion Battery"]:
            s["stability_risk"] -= 2
            s["system_efficiency"] -= 1
        else:
            s["carbon_emissions"] -= 1
            s["stability_risk"] -= 1

    # Pressure effects
    if pressure == "25%":
        s["energy_density"] -= 2
        s["system_efficiency"] -= 1
        if chemical == "Hydrogen":
            s["storage_transport"] += 1

    elif pressure == "50%":
        pass

    elif pressure == "75%":
        s["energy_density"] += 1
        if chemical == "Hydrogen":
            s["stability_risk"] -= 1
        if chemical in ["Ethanol", "Biodiesel", "Biobutanol"]:
            s["carbon_emissions"] -= 1

    elif pressure == "100%":
        s["energy_density"] += 1
        s["stability_risk"] -= 2
        if chemical == "Hydrogen":
            s["storage_transport"] -= 1
        if chemical in ["Ethanol", "Biodiesel", "Biobutanol"]:
            s["carbon_emissions"] -= 1
            s["waste_byproducts"] -= 1

    limits = {
        "energy_density": (0, 15),
        "system_efficiency": (0, 15),
        "carbon_emissions": (0, 20),
        "renewability": (0, 10),
        "waste_byproducts": (0, 5),
        "infrastructure": (0, 10),
        "storage_transport": (0, 5),
        "weight_penalty": (0, 10),
        "stability_risk": (0, 10),
    }

    for key, (low, high) in limits.items():
        s[key] = clamp(s[key], low, high)

    return s


def build_report(chemical, concentration, temperature, pressure, total_score):
    chemical_reports = {
        "Hydrogen": "Hydrogen remains one of the cleanest options because its direct use mainly produces water, but storage demands and high-pressure handling affect practicality.",
        "Biodiesel": "Biodiesel benefits from being renewable and compatible with liquid-fuel systems, but it still creates combustion-related environmental impacts.",
        "Lithium Sulfur Battery": "Lithium-sulfur batteries have low direct emissions during use and strong energy promise, though stability and development challenges still matter.",
        "Lithium Ion Battery": "Lithium-ion batteries perform efficiently in use with low direct emissions, but lifecycle impacts from mining and manufacturing remain important.",
        "Ethanol": "Ethanol is a renewable liquid fuel with decent infrastructure compatibility, but its combustion still contributes to emissions and byproducts.",
        "Biobutanol": "Biobutanol offers renewable fuel potential and useful energy content, though it still behaves like a combustion fuel in environmental terms.",
    }

    concentration_reports = {
        "25%": "The lower concentration reduces energy delivery and can make the system less effective overall.",
        "50%": "The medium concentration gives a balanced setup between output and control.",
        "75%": "The higher concentration improves energy delivery, but in some systems it can increase handling or emissions concerns.",
    }

    temperature_reports = {
        "Low": "Low temperature conditions can reduce efficiency for liquid fuels and batteries, while improving stability for some storage systems.",
        "Medium": "Medium temperature provides the most balanced operating conditions for most fuel systems.",
        "High": "High temperature can increase energy losses, stress the system, and create greater stability concerns.",
    }

    pressure_reports = {
        "25%": "Lower pressure reduces system stress but can also reduce useful output.",
        "50%": "Moderate pressure gives a stable operating point without strong extremes.",
        "75%": "Higher pressure improves output in some systems but begins to increase risk and storage demands.",
        "100%": "Maximum pressure may improve performance, but it usually adds safety and containment concerns.",
    }

    if total_score >= 85:
        final_line = "Overall, this combination is an excellent environmental choice with strong fuel-system performance."
    elif total_score >= 70:
        final_line = "Overall, this combination is a good option with moderate tradeoffs between performance and environmental impact."
    elif total_score >= 55:
        final_line = "Overall, this combination is usable, but its environmental and system tradeoffs are more noticeable."
    else:
        final_line = "Overall, this combination is less favorable because its environmental and operational drawbacks outweigh its benefits."

    return " ".join([
        chemical_reports[chemical],
        concentration_reports[concentration],
        temperature_reports[temperature],
        pressure_reports[pressure],
        final_line,
    ])


def get_environmental_score(scores):
    return sum(scores.values())


def get_car_position(total_score):
    # Simple movement scaling for visual effect
    return clamp(int((total_score / 100) * 650), 120, 650)


##################### Home Page #####################
if st.session_state.page == "Home":
    st.markdown(
        """
        <h1 style='text-align: center;'>Fuel Forward</h1>
        <h3 style='text-align: center; font-weight: normal; color: #555;'>
            Explore how different chemical systems affect car performance and environmental impact
        </h3>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown("## About This Project")
    st.write(
        "This project explores how different fuels and energy systems can affect the performance of a small chemical car. "
        "Instead of only comparing speed or power, the simulator also looks at environmental impact, practicality, and overall fuel quality."
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style="
                padding: 20px;
                border-radius: 15px;
                background-color: #f5f7fa;
                border: 1px solid #d9dee5;
                height: 100%;
            ">
                <h3 style="margin-top: 0;">What the Simulator Does</h3>
                <ul style="line-height: 1.8;">
                    <li>Lets users test different <b>chemical systems</b></li>
                    <li>Changes results based on <b>concentration, temperature, and pressure</b></li>
                    <li>Generates an <b>environmental report</b> for each setup</li>
                    <li>Scores each option using a custom <b>Fuel Excellence Index (FEI)</b></li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style="
                padding: 20px;
                border-radius: 15px;
                background-color: #f5f7fa;
                border: 1px solid #d9dee5;
                height: 100%;
            ">
                <h3 style="margin-top: 0;">Why It Matters</h3>
                <ul style="line-height: 1.8;">
                    <li>Some fuels are cleaner but harder to store</li>
                    <li>Some are practical but less sustainable</li>
                    <li>Engineers have to balance <b>performance, safety, and environmental impact</b></li>
                    <li>This project connects chemistry to real-world transportation design</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")



##################### Simulator Page #####################
elif st.session_state.page == "Simulator":
    st.subheader(" Simulator")

    st.sidebar.header("Simulation Controls")

    st.session_state.chemical = st.sidebar.selectbox(
        "Choose a chemical system:",
        chemical_options,
        index=chemical_options.index(st.session_state.chemical),
    )

    st.session_state.concentration = st.sidebar.selectbox(
        "Choose concentration:",
        concentration_options,
        index=concentration_options.index(st.session_state.concentration),
    )

    st.session_state.temperature = st.sidebar.selectbox(
        "Choose temperature:",
        temperature_options,
        index=temperature_options.index(st.session_state.temperature),
    )

    st.session_state.pressure = st.sidebar.selectbox(
        "Choose pressure:",
        pressure_options,
        index=pressure_options.index(st.session_state.pressure),
    )

    chemical = st.session_state.chemical
    concentration = st.session_state.concentration
    temperature = st.session_state.temperature
    pressure = st.session_state.pressure

    scores = apply_modifiers(
        base_scores[chemical],
        chemical,
        concentration,
        temperature,
        pressure,
    )

    total_score = get_environmental_score(scores)
    report = build_report(chemical, concentration, temperature, pressure, total_score)
    car_position = get_car_position(total_score)

    st.markdown(
        f"""
        <style>
        .road-container {{
            display: flex;
            justify-content: center;
            margin-top: 20px;
            margin-bottom: 30px;
        }}

        .road {{
            position: relative;
            width: 850px;
            height: 180px;
            background: linear-gradient(to top, #555 60%, #87CEEB 60%);
            border-radius: 15px;
            overflow: hidden;
            border: 3px solid #333;
        }}

        .lane-line {{
            position: absolute;
            top: 110px;
            width: 100%;
            height: 6px;
            background: repeating-linear-gradient(
                to right,
                white 0px,
                white 40px,
                transparent 40px,
                transparent 80px
            );
        }}

        .car {{
            position: absolute;
            top: 55px;
            left: {car_position}px;
            font-size: 70px;
        }}
        </style>

        <div class="road-container">
            <div class="road">
                <div class="lane-line"></div>
                <div class="car">🚗</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write(f"**Selected Combination:** {chemical}, {concentration} concentration, {temperature} temperature, {pressure} pressure")

    st.markdown("##### 1. Energy Performance (30 Points)")
    st.write(f"- **Energy Density:** {scores['energy_density']} / 15")
    st.write(f"- **System Efficiency:** {scores['system_efficiency']} / 15")

    st.markdown("##### 2. Environmental Impact (35 Points)")
    st.write(f"- **Carbon / Emissions:** {scores['carbon_emissions']} / 20")
    st.write(f"- **Renewability:** {scores['renewability']} / 10")
    st.write(f"- **Waste / Byproducts:** {scores['waste_byproducts']} / 5")

    st.markdown("##### 3. Practical Use & Infrastructure (15 Points)")
    st.write(f"- **Infrastructure Compatibility:** {scores['infrastructure']} / 10")
    st.write(f"- **Storage & Transport Difficulty:** {scores['storage_transport']} / 5")

    st.markdown("##### 4. Vehicle Dynamics & Safety (20 Points)")
    st.write(f"- **Weight Penalty:** {scores['weight_penalty']} / 10")
    st.write(f"- **Stability / Risk:** {scores['stability_risk']} / 10")

    st.markdown(
        f"""
        <div class="score-box">
            <h3 style="margin-bottom: 8px;">Environmental Report</h3>
            <p style="margin-bottom: 0px;">{report}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="score-box">
            <h3 style="margin-bottom: 8px;">Final Environmental Score</h3>
            <p style="font-size: 24px; font-weight: bold; margin-bottom: 0px;">{total_score} / 100</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)


##################### Chemical Info Page #####################
elif st.session_state.page == "Chemical Info":
    chemical = st.session_state.chemical
    info = chemical_info[chemical]

    st.subheader(f"{chemical} Information")

    st.markdown(
        f"""
        <div style="
            padding: 22px;
            border-radius: 15px;
            background-color: #f5f7fa;
            border: 1px solid #d9dee5;
            margin-bottom: 18px;
        ">
            <h3 style="margin-top: 0;">Overview</h3>
            <p><strong>Description:</strong> {info['description']}</p>
            <p><strong>Best Use:</strong> {info['best_use']}</p>
            <p><strong>FEI Reference Score:</strong> {info['fei_score']}</p>
            <p><strong>Fun Fact:</strong> {info['fun_fact']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Advantages")
        for item in info["advantages"]:
            st.write(f"- {item}")

        st.markdown("### Environmental Notes")
        for item in info["environment_notes"]:
            st.write(f"- {item}")

    with col2:
        st.markdown("### Challenges")
        for item in info["challenges"]:
            st.write(f"- {item}")


##################### Hybrid/EV Page #####################
elif st.session_state.page == "Hybrid/EV":
    st.subheader("Hybrid & EV Information")

    hybrid_ev_table = {
        "Feature": ["Power Source", "Fuel", "Emissions", "Refueling"],
        "Hybrid (HEV)": [
            "Gasoline Engine + Electric Motor",
            "Gasoline",
            "Reduced tailpipe emissions",
            "3-5 minutes at a gas station",
        ],
        "Electric Vehicle (EV)": [
            "Battery + Electric Motor(s)",
            "Electricity (Plug-in)",
            "Zero tailpipe emissions",
            "30 mins (Fast) to 8+ hours (Home)",
        ],
    }

    st.table(hybrid_ev_table)

    st.markdown("#### How EVs and Hybrids are Better")
    st.markdown("""
- **Efficiency:** EVs convert over **77%** of electrical energy from the grid into power at the wheels, while conventional gas vehicles usually convert only **12%–30%**.
- **Maintenance:** EVs have far fewer moving parts, so they avoid things like oil changes, spark plugs, timing belts, and oxygen sensors.
- **Performance:** Electric motors provide **instant torque**, which means smoother acceleration and quicker response in city driving.
- **Energy Recovery:** Both EVs and hybrids can use **regenerative braking**, which captures energy normally lost as heat and sends it back into the battery.
    """)

    st.markdown("#### Why Purchase an EV/Hybrid Over a Gas Car?")
    st.markdown("""
- **Long-Term Savings:** While the upfront price is often higher, the fuel/electricity cost per mile is usually much lower.
- **Convenience:** EV owners with home charging can essentially “refuel” overnight without going to a gas station.
- **Environmental Impact:** Even including battery manufacturing, EVs usually have a lower lifetime carbon footprint, especially as the grid shifts toward wind and solar.
- **Quiet Comfort:** Without a traditional combustion engine, EVs are much quieter and can reduce driver fatigue.
    """)

    st.markdown("#### Top 2026 Models to Consider")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("##### All-Electric (EV)")
        st.markdown("""
- **Hyundai Ioniq 5 / 6** — Known for ultra-fast charging (10% to 80% in ~18 mins)
- **Tesla Model 3 / Y** — Industry benchmark for charging and software
- **Chevrolet Equinox EV** — One of the more affordable long-range SUVs
- **Ford Mustang Mach-E** — Sporty, tech-heavy crossover
        """)

    with col2:
        st.markdown("##### Hybrid (HEV) / Plug-in Hybrid (PHEV)")
        st.markdown("""
- **Toyota Prius / Prius Prime** — Gold standard for efficiency
- **Honda Civic Hybrid** — Strong balance of fun and fuel savings
- **Toyota RAV4 Hybrid** — Best-selling hybrid SUV
- **Hyundai Tucson Plug-in Hybrid** — About 33 miles of all-electric driving before gas kicks in
        """)


##################### Alternate Options Page #####################
elif st.session_state.page == "Alternate Options":
    st.subheader("Why Aren't Alternative Fuels Standard Yet?")

    st.markdown("Fuels like ethanol, biobutanol, biodiesel, and hydrogen all work in real systems, " \
    "but each one has a major drawback that makes it hard to replace gasoline on a large scale. " \
    "Most of the challenge is not whether the fuel works — it is whether it can be produced, transported, and used by millions of people affordably and safely.")

    st.markdown("#### Fuel Challenges and Advantages")
    st.markdown("")

    alt1, alt2 = st.columns(2)

    with alt1:
        st.markdown("##### Ethanol")
        st.markdown("""
- Commonly blended into gasoline (such as E10)
- Renewable and already used in many fuel systems
- **Main issue:** Pure ethanol can damage some engine materials, and producing enough biomass would require a lot of farmland
- **Interesting note:** Ethanol is a high-octane fuel, so it can help performance engines run efficiently while lowering emissions compared with gasoline
        """)

        st.markdown("##### Biodiesel")
        st.markdown("""
- Made from vegetable oils, animal fats, or recycled cooking grease
- Can often work in diesel engines with little modification
- **Main issue:** There is not enough waste oil or soybean oil available to replace all diesel use
- **Interesting note:** Biodiesel improves lubrication, so even small blends can help reduce engine wear
        """)

    with alt2:
        st.markdown("##### Biobutanol")
        st.markdown("""
- Similar to ethanol, but behaves much more like gasoline
- Can often be used in modern gas vehicles without major changes
- **Main issue:** It is much harder and more expensive to produce at large scale
- **Interesting note:** It is considered a strong “drop-in fuel” because it works well with current fuel pipelines and storage systems
        """)

        st.markdown("##### Hydrogen")
        st.markdown("""
- Can be used in fuel cells or burned in specially designed engines
- Produces water as the main byproduct in fuel-cell vehicles
- **Main issue:** Storage and fueling infrastructure are major barriers because hydrogen requires high-pressure systems
- **Interesting note:** Hydrogen vehicles can refuel in about 3-5 minutes, which is much faster than charging most EVs
        """)

    st.markdown("---")
    st.markdown("#### High-Efficiency Gas-Only Options")

    st.write(
        "If someone is not ready for a hybrid or EV yet, some gasoline-only cars are still designed to use fuel very efficiently."
    )
    st.markdown("##### Top Compact & Subcompact Cars")

    st.markdown("""
    - **Mitsubishi Mirage — 39 MPG**  
      Extremely lightweight and uses a very small 3-cylinder engine, which helps maximize fuel economy.

    - **Nissan Versa — 35 MPG**  
    One of the more affordable gas cars on the market and uses an efficient CVT transmission.

    - **Honda Civic (Non-Hybrid) — 36 MPG**  
     Uses a 1.5L turbo engine that gives a strong balance between power and highway efficiency.
    """)

    st.markdown("##### Top Sedans & Hatchbacks")

    st.markdown("""
    - **Volkswagen Jetta — 34 MPG**  
    Designed for efficient highway driving with engine tuning focused on fuel savings.

    - **Toyota Corolla (Gas) — 35 MPG**  
    Uses Toyota's Dynamic Force engine to extract more energy from each drop of fuel.

    - **Hyundai Elantra (Gas) — 34 MPG**  
    Has a streamlined body design that reduces drag and improves mileage.
    """)