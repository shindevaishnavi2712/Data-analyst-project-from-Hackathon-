from pathlib import Path
import pandas as pd
import streamlit as st

ROOT=Path(__file__).resolve().parent
DATA=ROOT/"data"
st.set_page_config(page_title="VoltRelay Energy Analytics",layout="wide")
st.title("VoltRelay Energy | Hackathon Submission Dashboard")
st.caption("Prepared by Vaishnavi Shinde")

def load(name):
    p=DATA/f"{name}.csv"
    return pd.read_csv(p) if p.exists() else None

st.warning("The supplied package does not include swap_events.csv. Revenue, completed swaps, attempt failure rate, queue abandonment, retention and contribution margin are not calculated.")
s=load("stations"); t=load("support_tickets"); b=load("batteries"); h=load("station_hourly_status"); r=load("riders")
if s is not None:
    st.subheader("Network footprint")
    c1,c2=st.columns(2)
    c1.metric("Stations",f"{s.station_id.nunique():,}")
    c2.metric("Cities",f"{s.city.nunique():,}")
    st.bar_chart(s.groupby("city").station_id.nunique())
if t is not None:
    st.subheader("Customer support")
    c1,c2,c3=st.columns(3)
    c1.metric("Tickets",f"{len(t):,}")
    c2.metric("Unresolved",f"{(t.resolution_status=='unresolved').sum():,}")
    c3.metric("CSAT missing",f"{t.csat_score.isna().mean():.1%}")
    st.bar_chart(t.category.value_counts())
if b is not None:
    st.subheader("Battery supplier snapshot")
    bs=b.assign(retired=b.retired_date.notna()).groupby("supplier").agg(
        battery_count=("battery_id","count"),
        avg_current_soh=("current_soh_pct","mean"),
        retired_share=("retired","mean"))
    st.dataframe(bs,use_container_width=True)
if h is not None:
    st.subheader("Telemetry quality")
    st.bar_chart(h.telemetry_status.value_counts())
if r is not None:
    st.subheader("Rider profiles")
    st.metric("Rider profiles",f"{r.rider_id.nunique():,}")
    st.caption("Home-city aliases must be standardized before city-level comparisons.")
