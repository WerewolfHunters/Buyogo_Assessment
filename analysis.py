# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load cleaned dataset
# df = pd.read_csv("data/cleaned_hotel_bookings.csv")

# # Convert date
# df['date'] = pd.to_datetime(df['arrival_date_year'].astype(str) + '-' +
#                             df['arrival_date_month'] + '-' +
#                             df['arrival_date_day_of_month'].astype(str))

# def revenue_trends():
#     """Plots revenue trends over time."""
#     monthly_revenue = df.groupby(df['date'].dt.to_period("M"))['adr'].sum()
#     monthly_revenue.plot(kind='line', title='Revenue Trends Over Time')
#     plt.show()

# def cancellation_rate():
#     """Calculates and prints the cancellation rate."""
#     rate = df['is_canceled'].mean() * 100
#     print(f"Cancellation Rate: {rate:.2f}%")

# def top_booking_countries():
#     """Plots the top 10 booking countries."""
#     top_countries = df['country'].value_counts().head(10)
#     sns.barplot(x=top_countries.index, y=top_countries.values)
#     plt.title("Top 10 Booking Countries")
#     plt.xticks(rotation=45)
#     plt.show()

# def lead_time_distribution():
#     """Plots the booking lead time distribution."""
#     sns.histplot(df['lead_time'], bins=50, kde=True)
#     plt.title("Booking Lead Time Distribution")
#     plt.show()

# # Example usage
# if __name__ == "__main__":
#     revenue_trends()
#     cancellation_rate()
#     top_booking_countries()
#     lead_time_distribution()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/cleaned_hotel_bookings.csv")

# Convert date
df['date'] = pd.to_datetime(df['arrival_date_year'].astype(str) + '-' +
                            df['arrival_date_month'] + '-' +
                            df['arrival_date_day_of_month'].astype(str))

def revenue_trends():
    """Returns a revenue trends plot instead of showing it."""
    monthly_revenue = df.groupby(df['date'].dt.to_period("M"))['adr'].sum()
    fig, ax = plt.subplots()
    monthly_revenue.plot(kind='line', title='Revenue Trends Over Time', ax=ax)
    return fig  # Return figure object

def cancellation_rate():
    """Calculates and returns the cancellation rate."""
    rate = df['is_canceled'].mean() * 100
    return f"Cancellation Rate: {rate:.2f}%"

def top_booking_countries():
    """Returns a figure for the top 10 booking countries plot."""
    top_countries = df['country'].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=top_countries.index, y=top_countries.values, ax=ax)
    ax.set_title("Top 10 Booking Countries")
    ax.set_xticklabels(top_countries.index, rotation=45)
    return fig

def lead_time_distribution():
    """Returns a figure for the booking lead time distribution plot."""
    fig, ax = plt.subplots()
    sns.histplot(df['lead_time'], bins=50, kde=True, ax=ax)
    ax.set_title("Booking Lead Time Distribution")
    return fig

# Example usage
if __name__ == "__main__":
    revenue_trends()
    cancellation_rate()
    top_booking_countries()
    lead_time_distribution()