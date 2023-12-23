import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

#menyiapkandata
hour_data = pd.read_csv("all_data.csv")
hour_data.head()

#menyiapkan daily rent
def create_daily_rent_df(df):
    daily_rent_df = df.groupby(by='dateday').agg({
        'count':'sum'
    }).reset_index()
    return daily_rent_df

#daily casual_rent_df
def create_daily_casual_rent_df(df):
    daily_casual_rent_df = df.groupby(by='dateday').agg({
        'casual':'sum'
    }).reset_index()
    return daily_casual_rent_df

#daily_registered_rent_df
def create_daily_registered_rent_df(df):
    daily_registered_rent_df = df.groupby(by='dateday').agg({
        'registered':'sum'
    }).reset_index()
    daily_registered_rent_df['dateday'] = pd.to_datetime(hour_data['dateday'])
    
    return daily_registered_rent_df

#createmonthly
def create_monthly_rent_df(df):
    monthly_rent_df = df.groupby(by='month').agg ({
        'count' : 'sum'
    })
    order_months = [
        'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
    ]
    monthly_rent_df = monthly_rent_df.reindex(order_months, fill_value=0)
    return monthly_rent_df

#createweekday
def create_weekday_rent_df(df):
    weekday_rent_df = df.groupby(by='weekday').agg({
        'count':'sum'
    })
    return weekday_rent_df

#Createworkingday
def create_workingday_rent_df(df):
    workingday_rent_df = df.groupby(by='workingday').agg({
        'count':'sum'
    })
    return workingday_rent_df

#CreateHoliday
def create_holiday_rent_df(df):
    holiday_rent_df = df.groupby(by='holiday').agg({
        'count':'sum'
    })
    return holiday_rent_df


     #membuat sidebar kalender
min_date = pd.to_datetime(hour_data["dateday"]).min()
max_date = pd.to_datetime(hour_data["dateday"]).max()
 

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
   
    main_df = hour_data[(hour_data["dateday"] >= str(start_date)) & 
                (hour_data["dateday"] <= str(end_date))]

#menyiapkan dataframee
daily_rent_df = create_daily_rent_df(main_df)
daily_casual_rent_df = create_daily_casual_rent_df(main_df)
daily_registered_rent_df = create_daily_registered_rent_df(main_df)
monthly_rent_df = create_monthly_rent_df(main_df)
weekday_rent_df = create_weekday_rent_df(main_df)
workingday_rent_df = create_workingday_rent_df(main_df)
holiday_rent_df = create_holiday_rent_df(main_df)

#membuat judul di dashboard
st.header('Bike rental Dashboard')

#membuat jumlah penyewaan harian
st.subheader('Daily Rentals')
col1, col2, col3 = st.columns(3)

with col1:
    daily_rent_casual = daily_casual_rent_df['casual'].sum()
    st.metric('Casual User', value=daily_rent_casual)

with col2:
    daily_rent_registered = daily_registered_rent_df['registered'].sum()
    st.metric('Registered User', value=daily_rent_registered)

with col3:
    daily_rent_total = daily_rent_df['count'].sum()
    st.metric('Total Pengguna', value=daily_rent_total)

#Penyewaan Workingday,Weekday dan holiday
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15,10))

colors1=["tab:blue", "tab:orange"]
colors2=["tab:blue", "tab:orange"]
colors3=["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown", "tab:pink"]

# Berdasarkan workingday
sns.barplot(
    x='workingday',
    y='count',
    data=workingday_rent_df,
    palette=colors1,
    ax=axes[0])

for index, row in enumerate(workingday_rent_df['count']):
    axes[0].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

axes[0].set_title('Number of Rents based on Working Day')
axes[0].set_ylabel(None)
axes[0].tick_params(axis='x', labelsize=15)
axes[0].tick_params(axis='y', labelsize=10)

# Berdasarkan holiday
sns.barplot(
  x='holiday',
  y='count',
  data=holiday_rent_df,
  palette=colors2,
  ax=axes[1])

for index, row in enumerate(holiday_rent_df['count']):
    axes[1].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

axes[1].set_title('Number of Rents based on Holiday')
axes[1].set_ylabel(None)
axes[1].tick_params(axis='x', labelsize=15)
axes[1].tick_params(axis='y', labelsize=10)

# Berdasarkan weekday
sns.barplot(
  x='weekday',
  y='count',
  data=weekday_rent_df,
  palette=colors3,
  ax=axes[2])

for index, row in enumerate(weekday_rent_df['count']):
    axes[2].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

axes[2].set_title('Number of Rents based on Weekday')
axes[2].set_ylabel(None)
axes[2].tick_params(axis='x', labelsize=15)
axes[2].tick_params(axis='y', labelsize=10)

plt.tight_layout()
st.pyplot(fig)

#jumlah penyewaan berdasasrkan bulan
st.subheader('Monthly Rentals')
fig, ax = plt.subplots(figsize=(24, 8))
ax.plot(
    monthly_rent_df.index,
    monthly_rent_df['count'],
    marker='o', 
    linewidth=2,
    color='tab:blue'
)

for index, row in enumerate(monthly_rent_df['count']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.tick_params(axis='x', labelsize=25, rotation=45)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)