# Challenge Problem #1 - Destination Prediction

# Setup

You consult with a major US auto manufacturer. As part of new car purchase (and purchase and
agreement of terms of the telemetry package) car start locations will be sent to the manufacturer
every time the car starts.

# Data

| Timestamp           | Latitude | Longitude | car_id |
| ------------------- | -------- | --------- | ------ |
| 2023-01-01 00:00:00 | 37.7749  | -122.4194 | 1      |
| 2023-01-01 02:34:01 | 37.3749  | -120.4l34 | 1      |
| 2023-01-01 01:32:02 | 38.4749  | -124.0834 | 2      |
| ...                 | ...      | ...       | ...    |

- Geocodes for every start of the car but NOT paths along which the car traveled
- Tens-of-thousands of unique `car_id`
- Hundreds of starts per car

# Problem

Can you predict the destination of the car sometime during the week for a given user to the
manufacture can provide enhancements to the user (Early mention of traffic, coupon for gas, etc.)

# Possible Solutions

1. Historical Frequency
   - Discretize a city or country into a grid
   - Truncate the geocodes to a given precision
   - Bin the data into geocode bin and timestamp for a given car
   - Get a crude probability of being at a given location based on the historical frequency. How
     often has the car been at `Location` historically.

$$ P(Location, Car) = \frac{N(Location, Car)}{N(Location)} $$

- Pick a threshold over which you could make a prediction.

## Example

If a driver has consistently played soccer at a certain location every Saturday at 10:00 AM, for the
last 10 years, you can be very confident that they will be at that location again next Saturday at
10:00 AM. If however, a driver plays a game at the same field infrequenly and sometimes has errands
they have ran and the historical frequency says the car has only been at that park 10% of the time,
do not make a prediction.
