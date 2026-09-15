import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Page Configuration
st.set_page_config(page_title="FORESIGHT Dashboard", page_icon="📊", layout="wide")
st.title("📊 Project FORESIGHT: Demand & Inventory Intelligence")
st.markdown("### Executive Summary Dashboard - Zidio Development")
st.divider()

# 2. Load the Data (Using caching so the web app runs super fast)
@st.cache_data
def load_inventory_data():
    # Looks back one folder to find the data directory
    df = pd.read_csv('../data/inventory_snapshots.csv')
    return df

inventory_df = load_inventory_data()

# 3. Apply Your Phase 6 Risk Logic
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

# 4. Build the Top Metric Cards
st.subheader(f"Current Inventory Health (As of {latest_date})")

stockout_count = len(current_inventory[current_inventory['Risk_Status'] == 'Stockout Risk'])
healthy_count = len(current_inventory[current_inventory['Risk_Status'] == 'Healthy'])
overstock_count = len(current_inventory[current_inventory['Risk_Status'] == 'Overstock'])

col1, col2, col3 = st.columns(3)
col1.metric(label="🚨 Critical Stockouts", value=stockout_count, delta="- Immediate Action Required", delta_color="inverse")
col2.metric(label="✅ Healthy SKUs", value=healthy_count)
col3.metric(label="📦 Overstocked SKUs", value=overstock_count, delta="Capital Tied Up", delta_color="off")

st.divider()

# 5. Render Your Perfected Chart
st.subheader("Risk Category Distribution")
fig, ax = plt.subplots(figsize=(10, 4))
colors = {'Healthy': '#2ecc71', 'Stockout Risk': '#e74c3c', 'Overstock': '#3498db'}

sns.countplot(
    data=current_inventory, 
    x='Risk_Status', 
    hue='Risk_Status', 
    order=['Stockout Risk', 'Healthy', 'Overstock'], 
    palette=colors,
    legend=False,
    ax=ax # Tells seaborn to draw inside the Streamlit figure
)
plt.ylabel('Number of Products')
plt.xlabel('')

# Display the plot in the web app
st.pyplot(fig)