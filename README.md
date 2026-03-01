# Azure Demand Forecasting & Capacity Optimization System  
## Milestone 1 — Data Collection & Preparation

This project focuses on building a demand forecasting and capacity optimization pipeline for Azure compute and storage workloads.  
Milestone-1 covers dataset creation, external variable integration, data cleaning, validation, and preparation for modeling.

---

# 🎯 Milestone Objective

Compile and prepare historical-style cloud usage data along with external driver variables, and transform it into a clean, consistent, model-ready dataset for forecasting.

---

# 📊 Dataset Overview

A realistic synthetic dataset was generated because real Azure operational demand data is not publicly available.

Dataset size:
- **Rows:** 100–150 (configurable generator)
- **Columns:** 15
- **Granularity:** Hourly timestamps
- **Regions:** US East, India South, Europe West
- **Services:** Compute, Storage

---

# 🧾 Dataset Fields

## Core Usage Metrics
- timestamp
- region
- service_type
- usage_units
- cost_usd
- availability_pct

## Calendar Features
- is_holiday
- is_weekend

## External Variables
- market_index
- economic_index
- cloud_price_index
- temperature_c

## Operational Context
- network_latency_ms
- request_count
- scaling_events

---

# ⚙️ Milestone-1 Tasks Completed

✅ Created realistic multi-region demand dataset  
✅ Added external market & economic variables  
✅ Standardized timestamp and categorical formats  
✅ Normalized region/service labels  
✅ Handled missing values using interpolation and derived fills  
✅ Removed duplicates using composite keys  
✅ Performed range validation checks  
✅ Generated cleaned dataset  
✅ Produced validation reports and plots  

---

# 🧹 Data Cleaning Methods

- Timestamp → converted to datetime
- Region → lowercase + standardized format
- Usage → interpolated within region groups
- Cost → recomputed from usage where missing
- Availability → forward-filled by region
- Invalid ranges → filtered
- Duplicates → removed using (timestamp, region, service_type)

