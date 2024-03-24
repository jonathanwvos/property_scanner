from config import PREFERRED_AREAS, SD_ABOVE, SD_BELOW
from os.path import dirname, join, realpath


def filter_by_price(raw_data, price_mean, price_sd):
    filtered_locations = []
    
    # for location_data in raw_data:
    for _, location_data in raw_data.iterrows():
        price = location_data['price']
        
        if price <= price_mean + SD_ABOVE*price_sd and price >= price_mean - SD_BELOW*price_sd:
            filtered_locations.append(location_data)
            
    return filtered_locations


def allocate_location(rec, locations):
    for location in locations:
        no_beds = location['bedrooms']

        if no_beds in [1, 2, 3]:        
            rec[f'{int(no_beds)}bed'].append(location)


def create_recommendations_files(rec):
    for bed in rec:
        filename = join(dirname(realpath(__file__)), 'data', f'{bed}_recommendations.txt')
        
        with open(filename, 'w') as f:
            for loc in rec[bed]:
                f.write(f"{loc.url}\n")
        
def execute(insights):
    recommendations = {
        '1bed': [],
        '2bed': [],
        '3bed': []
    }
    
    for location in PREFERRED_AREAS:
        if location not in insights['locations']:
            continue
        
        location_data = insights['locations'][location]
        raw_data = location_data['raw-data']
        
        if len(raw_data) == 0:
            continue
        
        price_mean = insights['locations'][location]['price-mean']
        price_sd = insights['locations'][location]['price-sd']
        
        filtered_by_price = filter_by_price(raw_data, price_mean, price_sd)
        
        allocate_location(recommendations, filtered_by_price)
    
    create_recommendations_files(recommendations)
