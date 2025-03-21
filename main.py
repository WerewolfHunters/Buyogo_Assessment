import pandas as pd

# Load dataset
df = pd.read_csv("data/hotel_bookings.csv")

# Fill missing values
df['children'].fillna(0, inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['agent'].fillna(0, inplace=True)
df['company'].fillna(0, inplace=True)

# Convert reservation_status_date to datetime
df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])

# Save cleaned dataset
df.to_csv("data/cleaned_hotel_bookings.csv", index=False)
print("✅ Cleaned dataset saved as 'cleaned_hotel_bookings.csv'.")
