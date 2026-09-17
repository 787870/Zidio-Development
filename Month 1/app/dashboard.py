import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Page Configuration
st.set_page_config(page_title="FORESIGHT Dashboard", page_icon="📊", layout="wide")

# Custom CSS Injection for Modern Cards, Glowing Badges, and Enterprise Styling
st.markdown("""
    <style>
    .metric-card {
        background: linear-gradient(135deg, #1e2530 0%, #161b22 100%);
        border: 1px solid #30363d;
        padding: 24px;
        border-radius: 14px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        border-color: #58a6ff;
    }
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #f0f6fc;
        margin-bottom: 0px;
        letter-spacing: -0.5px;
    }
    .team-badge {
        display: inline-block;
        background: linear-gradient(90deg, #1f6feb 0%, #388bfd 100%);
        color: white;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(56, 139, 253, 0.4);
    }
    .sub-title {
        color: #8b949e;
        font-size: 1.15rem;
        font-weight: 400;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section with Team Badge & Styled Typography
st.markdown('<div class="team-badge">🚀 Team #8 | Zidio Development</div>', unsafe_allow_html=True)
st.markdown('<p class="main-title">📊 Project FORESIGHT</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">AI-Powered Demand Forecasting & Real-Time Inventory Intelligence Dashboard</p>', unsafe_allow_html=True)
st.divider()

# 2. Load the Data with Caching
@st.cache_data
def load_inventory_data():
    df = pd.read_csv('Month 1/data/inventory_snapshots.csv')
    return df

inventory_df = load_inventory_data()

# 3. Apply Risk Logic
latest_date = inventory_df['Snapshot_Date'].max()
current_inventory = inventory_df[inventory_df['Snapshot_Date'] == latest_date].copy()
current_inventory['Stock_Health_Ratio'] = current_inventory['Current_Stock'] / current_inventory['Reorder_Point']

def assign_risk_clean(ratio):
    if ratio <= 1.0:
        return 'Stockout Risk'
    elif ratio >= 3.0:
        return 'Overstock'
    else:
        return 'Healthy'

current_inventory['Risk_Status'] = current_inventory['Stock_Health_Ratio'].apply(assign_risk_clean)

# Metric Calculations
stockout_count = len(current_inventory[current_inventory['Risk_Status'] == 'Stockout Risk'])
healthy_count = len(current_inventory[current_inventory['Risk_Status'] == 'Healthy'])
overstock_count = len(current_inventory[current_inventory['Risk_Status'] == 'Overstock'])

st.markdown(f"### 🔍 Current Inventory Health Status (As of `{latest_date}`)")

# 4. Modern Metric Cards Layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <h4 style="color: #ff7b72; margin:0; font-size: 1.05rem; font-weight: 600;">🚨 Critical Stockouts</h4>
            <h1 style="color: #ffffff; margin: 12px 0; font-size: 2.8rem; font-weight: 700;">{stockout_count}</h1>
            <p style="color: #ff7b72; margin:0; font-size:0.9rem; font-weight: 500;">⚠️ Immediate Action Required</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <h4 style="color: #3fb950; margin:0; font-size: 1.05rem; font-weight: 600;">✅ Healthy SKUs</h4>
            <h1 style="color: #ffffff; margin: 12px 0; font-size: 2.8rem; font-weight: 700;">{healthy_count}</h1>
            <p style="color: #3fb950; margin:0; font-size:0.9rem; font-weight: 500;">🟢 Optimal Stock Levels</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card">
            <h4 style="color: #58a6ff; margin:0; font-size: 1.05rem; font-weight: 600;">📦 Overstocked SKUs</h4>
            <h1 style="color: #ffffff; margin: 12px 0; font-size: 2.8rem; font-weight: 700;">{overstock_count}</h1>
            <p style="color: #58a6ff; margin:0; font-size:0.9rem; font-weight: 500;">💡 Capital Tied Up in Storage</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# 5. Seamless Dark-Mode Styled Chart Section
st.subheader("📈 Inventory Risk Category Distribution Matrix")

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 4.5))
fig.patch.set_facecolor('#0e1117')
ax.set_facecolor('#0e1117')

colors = {'Healthy': '#3fb950', 'Stockout Risk': '#ff7b72', 'Overstock': '#58a6ff'}

sns.countplot(
    data=current_inventory, 
    x='Risk_Status', 
    hue='Risk_Status', 
    order=['Stockout Risk', 'Healthy', 'Overstock'], 
    palette=colors,
    legend=False,
    ax=ax
)
ax.set_ylabel('Number of Products (SKUs)', color='#8b949e', fontsize=11, fontweight='500')
ax.set_xlabel('')
ax.tick_params(colors='#8b949e', labelsize=11, which='both')
for spine in ax.spines.values():
    spine.set_edgecolor('#30363d')

st.pyplot(fig)
