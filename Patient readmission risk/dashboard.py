import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 



df=pd.read_csv("C:\\Users\\sanja\\OneDrive\\Desktop\\DINKY_Tops\\Projects\\Patient readmission risk analysis\\dataset\\diabetic_data.csv")

# print(df.head())
# print(df.shape)
# print(df.describe())
# print(df.info())


#check missing values 
# print(df.isnull().sum()) 

#drop missing values 
df.drop(columns=['max_glu_serum', 'A1Cresult'], inplace=True)
# print(df.isnull().sum()) 

#finding ?
# print((df=="?").sum())

#replace ? with NAN
df.replace("?", pd.NA, inplace=True)
# print((df=="?").sum())
# print(df.isnull().sum()) 

#dropping null values 
df.drop(columns=['weight', 'payer_code', 'medical_specialty',
                 'encounter_id', 'patient_nbr'], inplace=True)
# print(df.isnull().sum()) 

#replacing null values 
df.columns = df.columns.str.strip()
df['race'] = df['race'].fillna(df['race'].mode()[0])
df['diag_1'] = df['diag_1'].fillna('Unknown')
df['diag_2'] = df['diag_2'].fillna('Unknown')
df['diag_3'] = df['diag_3'].fillna('Unknown')
# print(df.isnull().sum()) 


#target column 
# print(df['readmitted'].value_counts())
# print(df['readmitted'].value_counts(normalize=True) * 100)





# ==============================
# 📌 FEATURE ENGINEERING
# ==============================

# Target variable (30-day readmission)
df['readmitted_30'] = df['readmitted'].apply(lambda x: 1 if x == '<30' else 0)

# Total visits
df['total_visits'] = (
    df['number_outpatient'] +
    df['number_emergency'] +
    df['number_inpatient']
)


total_patients = len(df)
avg_stay = df['time_in_hospital'].mean()
avg_visits = df['total_visits'].mean()
readmit_rate = df['readmitted_30'].mean() * 100

# ==============================
# DASHBOARD 1: PATIENT OVERVIEW
# ==============================

import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# KPI CALCULATIONS
# ------------------------------

total_patients = len(df)
avg_stay = df['time_in_hospital'].mean()
avg_visits = df['total_visits'].mean()
readmit_rate = df['readmitted_30'].mean() * 100

# Readmission by age
age_readmit = (
    df.groupby('age')['readmitted_30']
    .mean()
    .reset_index()
)

age_readmit['readmitted_30'] *= 100

# ------------------------------
# DASHBOARD LAYOUT
# ------------------------------

fig = plt.figure(figsize=(18, 10))

gs = fig.add_gridspec(
    3,
    4,
    height_ratios=[1, 4, 4]
)

# fig.suptitle(
#     "Patient Demographics & Utilization Dashboard",
#     fontsize=18,
#     fontweight='bold'
# )

# # ------------------------------
# # KPI CARDS
# # ------------------------------

# ax_kpi1 = fig.add_subplot(gs[0, 0])
# ax_kpi2 = fig.add_subplot(gs[0, 1])
# ax_kpi3 = fig.add_subplot(gs[0, 2])
# ax_kpi4 = fig.add_subplot(gs[0, 3])

# for ax in [ax_kpi1, ax_kpi2, ax_kpi3, ax_kpi4]:
#     ax.axis('off')

# ax_kpi1.text(
#     0.5, 0.5,
#     f"{total_patients:,}\nTotal Patients",
#     ha='center',
#     va='center',
#     fontsize=14,
#     fontweight='bold'
# )

# ax_kpi2.text(
#     0.5, 0.5,
#     f"{avg_stay:.1f}\nAvg Stay (Days)",
#     ha='center',
#     va='center',
#     fontsize=14,
#     fontweight='bold'
# )

# ax_kpi3.text(
#     0.5, 0.5,
#     f"{avg_visits:.1f}\nAvg Visits",
#     ha='center',
#     va='center',
#     fontsize=14,
#     fontweight='bold'
# )

# ax_kpi4.text(
#     0.5, 0.5,
#     f"{readmit_rate:.1f}%\nReadmission Rate",
#     ha='center',
#     va='center',
#     fontsize=14,
#     fontweight='bold'
# )

# # ------------------------------
# # CHART 1: AGE DISTRIBUTION
# # ------------------------------

# ax1 = fig.add_subplot(gs[1, 0:2])

# sns.countplot(
#     x='age',
#     data=df,
#     order=sorted(df['age'].unique()),
#     palette='viridis',
#     ax=ax1
# )

# ax1.set_title("Patient Distribution by Age Group")
# ax1.tick_params(axis='x', rotation=45, labelsize=8)

# # ------------------------------
# # CHART 2: HOSPITAL STAY
# # ------------------------------

# ax2 = fig.add_subplot(gs[1, 2:4])

# sns.histplot(
#     df['time_in_hospital'],
#     bins=15,
#     kde=True,
#     ax=ax2
# )

# ax2.axvline(
#     df['time_in_hospital'].mean(),
#     color='red',
#     linestyle='--',
#     label='Mean'
# )

# ax2.legend()
# ax2.set_title("Time in Hospital Distribution")

# # ------------------------------
# # CHART 3: TOTAL VISITS
# # ------------------------------

# ax3 = fig.add_subplot(gs[2, 0:2])

# sns.histplot(
#     df['total_visits'],
#     bins=20,
#     kde=True,
#     ax=ax3
# )

# ax3.set_xlim(0, 20)
# ax3.set_title("Total Visits Distribution")

# # ------------------------------
# # CHART 4: READMISSION BY AGE
# # ------------------------------

# ax4 = fig.add_subplot(gs[2, 2:4])

# sns.barplot(
#     x='age',
#     y='readmitted_30',
#     data=age_readmit,
#     palette='Set2',
#     ax=ax4
# )

# ax4.set_title("Readmission Rate by Age Group")
# ax4.set_ylabel("Readmission (%)")
# ax4.tick_params(axis='x', rotation=45, labelsize=8)

# # ------------------------------
# # FINAL SPACING
# # ------------------------------

# plt.subplots_adjust(
#     top=0.90,
#     hspace=0.60,
#     wspace=0.35
# )

# plt.show()

# # ------------------------------------2-------------------------------------
# ==============================
# DASHBOARD 2: READMISSION RISK
# ==============================



# ------------------------------
# KPI CALCULATIONS
# ------------------------------

def risk_level(row):
    if row['total_visits'] > 3 and row['time_in_hospital'] > 7:
        return 'High'
    elif row['total_visits'] > 1:
        return 'Medium'
    else:
        return 'Low'

df['risk_level'] = df.apply(risk_level, axis=1)

risk_pct = df['risk_level'].value_counts(normalize=True) * 100

high_risk_pct = risk_pct.get('High', 0)
medium_risk_pct = risk_pct.get('Medium', 0)
low_risk_pct = risk_pct.get('Low', 0)

avg_meds = df['num_medications'].mean()

# ------------------------------
# DASHBOARD LAYOUT
# ------------------------------

fig = plt.figure(figsize=(18, 10))

gs = fig.add_gridspec(
    3,
    4,
    height_ratios=[1, 4, 4]
)

fig.suptitle(
    "Readmission Risk & Clinical Factors Dashboard",
    fontsize=18,
    fontweight='bold'
)

# ------------------------------
# KPI CARDS
# ------------------------------

ax_kpi1 = fig.add_subplot(gs[0, 0])
ax_kpi2 = fig.add_subplot(gs[0, 1])
ax_kpi3 = fig.add_subplot(gs[0, 2])
ax_kpi4 = fig.add_subplot(gs[0, 3])

for ax in [ax_kpi1, ax_kpi2, ax_kpi3, ax_kpi4]:
    ax.axis('off')

ax_kpi1.text(
    0.5, 0.5,
    f"{high_risk_pct:.1f}%\nHigh Risk",
    ha='center',
    va='center',
    fontsize=14,
    fontweight='bold'
)

ax_kpi2.text(
    0.5, 0.5,
    f"{medium_risk_pct:.1f}%\nMedium Risk",
    ha='center',
    va='center',
    fontsize=14,
    fontweight='bold'
)

ax_kpi3.text(
    0.5, 0.5,
    f"{low_risk_pct:.1f}%\nLow Risk",
    ha='center',
    va='center',
    fontsize=14,
    fontweight='bold'
)

ax_kpi4.text(
    0.5, 0.5,
    f"{avg_meds:.1f}\nAvg Medications",
    ha='center',
    va='center',
    fontsize=14,
    fontweight='bold'
)

# ------------------------------
# CHART 1
# HOSPITAL STAY VS READMISSION
# ------------------------------

ax1 = fig.add_subplot(gs[1, 0:2])

sns.boxplot(
    x='readmitted_30',
    y='time_in_hospital',
    data=df,
    palette='Set3',
    ax=ax1
)

ax1.set_title("Hospital Stay vs Readmission")
ax1.set_xlabel("Readmitted (0=No, 1=Yes)")
ax1.set_ylabel("Days in Hospital")

# ------------------------------
# CHART 2
# TOTAL VISITS VS READMISSION
# ------------------------------

ax2 = fig.add_subplot(gs[1, 2:4])

sns.boxplot(
    x='readmitted_30',
    y='total_visits',
    data=df,
    palette='coolwarm',
    ax=ax2
)

ax2.set_ylim(0, 20)
ax2.set_title("Total Visits vs Readmission")
ax2.set_xlabel("Readmitted (0=No, 1=Yes)")
ax2.set_ylabel("Total Visits")

# ------------------------------
# CHART 3
# MEDICATIONS VS READMISSION
# ------------------------------

ax3 = fig.add_subplot(gs[2, 0:2])

sns.boxplot(
    x='readmitted_30',
    y='num_medications',
    data=df,
    palette='pastel',
    ax=ax3
)

ax3.set_title("Medications vs Readmission")
ax3.set_xlabel("Readmitted (0=No, 1=Yes)")
ax3.set_ylabel("Number of Medications")

# ------------------------------
# CHART 4
# RISK LEVEL VS READMISSION
# ------------------------------

ax4 = fig.add_subplot(gs[2, 2:4])

sns.countplot(
    x='risk_level',
    hue='readmitted_30',
    data=df,
    palette='Set1',
    ax=ax4
)

ax4.set_title("Risk Level vs Readmission")
ax4.set_xlabel("Risk Level")
ax4.set_ylabel("Patient Count")
ax4.legend(title="Readmitted")

# ------------------------------
# SPACING
# ------------------------------

plt.subplots_adjust(
    top=0.90,
    hspace=0.60,
    wspace=0.35
)

plt.show()