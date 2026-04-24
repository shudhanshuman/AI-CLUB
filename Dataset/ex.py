import pandas as pd

# =========================
# 1. Load dataset
# =========================
df = pd.read_csv("economic_full_1.csv")

# =========================
# 2. Define allowed indicators
# =========================
allowed_indicators = [
    "Access to electricity (% of population)",
    "Industry (including construction), value added (constant 2015 US$)",
    "Population, total",
    "Urban population (% of total population)",
    "GDP per capita (constant 2015 US$)",
    "GDP (constant 2015 US$)"
]

# =========================
# 3. Filter dataset
# =========================
filtered_df = df[df["Indicator Name"].isin(allowed_indicators)]

# =========================
# 4. Save result
# =========================
filtered_df.to_csv("filtered_indicators.csv", index=False)

print(f"✅ Rows before: {len(df)}")
print(f"✅ Rows after: {len(filtered_df)}")