import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from config import COST_MAX, COST_MIN, LOCATION_THRESHOLD
from os.path import dirname, join, realpath


stats_dict = {
    'mean': 0,
    'median': 0,
    'sd': 0
}
insight_dict = {
    'price': stats_dict.copy(),
    'floor size': stats_dict.copy()
}
location_dict = {
    'raw-data': None,
    'price-mean': None,
    'price-median': None,
    'price-sd': None,
    'floor-size-mean': None,
    'floor-size-median': None,
    'floor-size-sd': None,
    'correlation': None,
    'y-intercept': None,
    'gradient': None,
    'residuals': None,
    'avg-residual': None
}
insights = {
    'general': insight_dict.copy(),
    'bachelors': insight_dict.copy(),
    '1bed': insight_dict.copy(),
    '2bed': insight_dict.copy(),
    '3bed': insight_dict.copy(),
    'locations': {}
}


def bedroom_insights(csv, room_size, insights, room_key):
    # Filter by room size
    if room_size != 0:
        filtered_data = csv[csv['bedrooms'] == room_size]
    else:
        filtered_data = csv
    
    # Filter out null values
    filtered_data = filtered_data[filtered_data['price'].notna()]
    
    # Filter out zeros
    filtered_data = filtered_data[filtered_data['price'] > 0]

    # Get stats
    room_price = filtered_data['price'].values
    mean = np.mean(room_price)
    median = np.median(room_price)
    sd = np.std(room_price)
    insights[room_key]['price']['mean'] = mean
    insights[room_key]['price']['median'] = median
    insights[room_key]['price']['sd'] = sd


def floor_size_insights(csv, room_size, insights, room_key):
    # Filter by room size
    if room_size != 0:
        filtered_data = csv[csv['bedrooms'] == room_size]
    else:
        filtered_data = csv
    
    # Filter out null values
    room_floor_size = filtered_data[filtered_data['floor size'].notna()]
    
    # Filter out zeros
    room_floor_size = room_floor_size[room_floor_size['floor size'] > 0]
    
    # Get stats
    room_floor_size = filtered_data['floor size'].values
    mean = np.mean(room_floor_size)
    median = np.median(room_floor_size)
    sd = np.std(room_floor_size)
    insights[room_key]['floor size']['mean'] = mean
    insights[room_key]['floor size']['median'] = median
    insights[room_key]['floor size']['sd'] = sd


#### LOCATIONAL INSIGHTS
def location_insights(csv, insights):
    location_count = {}

    for location in csv['location'].values:
        if location not in location_count:
            location_count[location] = 0
            
        location_count[location] += 1
        
    for location in location_count:
        location_data = csv[csv['location'] == location]
        
        # Filter out nans
        location_data = location_data[location_data['price'].notna()]
        location_data = location_data[location_data['floor size'].notna()]
        
        # Filter out zeros
        location_data = location_data[location_data['floor size'] > 0]
        location_data = location_data[location_data['price'] > 0]

        no_records = len(location_data)
        if no_records < LOCATION_THRESHOLD or no_records == 0:
            continue
        
        price = location_data['price'].values
        floor_size = location_data['floor size'].values
        
        # Get statistical values
        price_mean = np.mean(price)
        price_median = np.median(price)
        price_sd = np.std(price)
        floor_size_mean = np.mean(floor_size)
        floor_size_median = np.median(floor_size)
        floor_size_sd = np.std(floor_size)
        
        # Linear regression
        r = np.corrcoef(price, floor_size)[0, 1]
        if np.isnan(r):
            continue
        
        b = r*floor_size_sd/price_sd
        a = floor_size_mean - b*price_mean
        
        # Reserve a spot in the locations insights dictionary
        if location not in insights['locations']:
            insights['locations'][location] = location_dict.copy()
        
        insights['locations'][location]['raw-data'] = location_data
        insights['locations'][location]['price-mean'] = price_mean
        insights['locations'][location]['price-median'] = price_median
        insights['locations'][location]['price-sd'] = price_sd
        insights['locations'][location]['floor-size-mean'] = floor_size_mean
        insights['locations'][location]['floor-size-median'] = floor_size_median
        insights['locations'][location]['floor-size-sd'] = floor_size_sd
        insights['locations'][location]['correlation'] = r
        insights['locations'][location]['y-intercept'] = a
        insights['locations'][location]['gradient'] = b
        
        # Calculate residuals
        predicted_floor_sizes = []
        for p in price:
            predicted_floor_sizes.append(a + b*p)
        
        predicted_floor_sizes = np.array(predicted_floor_sizes)
        residuals = floor_size - predicted_floor_sizes
        insights['locations'][location]['residuals'] = residuals.tolist()
        insights['locations'][location]['avg-residual'] = np.mean(residuals)


def execute(filename):
    csv = pd.read_csv(filename, sep=';')
    upper_bound = csv['price'] <= COST_MAX
    lower_bound = csv['price'] >= COST_MIN
    csv = csv[np.logical_and(upper_bound, lower_bound)]
    
    room_sizes = [0, 0.5, 1, 2, 3]
    keys = ['general', 'bachelors', '1bed', '2bed', '3bed']

    for room_size, key in zip(room_sizes, keys):
        params = dict(
            csv=csv,
            room_size=room_size,
            insights=insights,
            room_key=key
        )
        bedroom_insights(**params)
        floor_size_insights(**params)

    location_insights(csv, insights)

    return insights


if __name__ == '__main__':
    filename = join(dirname(realpath(__file__)), 'data', 'property_24.csv')
    insights = execute(filename)
    
    print(insights)
