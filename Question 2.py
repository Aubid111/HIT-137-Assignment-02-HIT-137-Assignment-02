import pandas as pd

# run command "pip install openpyxl" in the terminal to install the openpyxl library. Without installing this first, the code will not work. 

def calculate_average_temperatures(file_path, output_file):
    # Define Australian seasons
    seasons = {
        "Summer": ["December", "January", "February"],
        "Autumn": ["March", "April", "May"],
        "Winter": ["June", "July", "August"],
        "Spring": ["September", "October", "November"],
    }

    # Part A) Create a dictionary to store the cumulative sums and counts for each season
    season_data = {season: {"sum": 0, "count": 0} for season in seasons}

    # Read the Excel file from the GitHub repository. Please note that we have combined all the years into a single spreadsheet. 
    xls = pd.ExcelFile(file_path)

    # Loop through each sheet (year)
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)

        # Process each season
        for season, months in seasons.items():
            for month in months:
                if month in df.columns:
                    season_data[season]["sum"] += df[month].sum()
                    season_data[season]["count"] += df[month].count()

    # Calculate the average temperatures for each season
    average_temperatures = {
        season: season_data[season]["sum"] / season_data[season]["count"]
        if season_data[season]["count"] > 0 else None
        for season in seasons
    }

    # Write the results to the output file
    with open(output_file, "w") as f:
        for season, avg_temp in average_temperatures.items():
            f.write(f"{season}: {avg_temp:.2f}\n" if avg_temp is not None else f"{season}: No Data\n")

def find_largest_temperature_range(file_path, output_file):
    # Read the Excel file from the GitHub repository
    xls = pd.ExcelFile(file_path)

    # Dictionary to store temperature ranges by station
    station_ranges = {}

    # Loop through each sheet (year)
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)

        # Calculate the range for each station in the sheet
        for _, row in df.iterrows():
            station_name = row["STATION_NAME"]
            temperatures = row.iloc[4:16]  # Assuming temperature columns are from E to P
            if temperatures.notnull().any():
                temp_range = temperatures.max() - temperatures.min()
                if station_name in station_ranges:
                    station_ranges[station_name] = max(station_ranges[station_name], temp_range)
                else:
                    station_ranges[station_name] = temp_range

    # Find the station(s) with the largest temperature range
    max_range = max(station_ranges.values())
    largest_range_stations = [station for station, temp_range in station_ranges.items() if temp_range == max_range]

    # Write the results to the output file
    with open(output_file, "w") as f:
        f.write(f"Largest Temperature Range: {max_range:.2f}\n")
        f.write("Stations with Largest Range:\n")
        for station in largest_range_stations:
            f.write(f"{station}\n")

def find_warmest_and_coolest_stations(file_path, output_file):
    # Read the Excel file from the GitHub repository
    xls = pd.ExcelFile(file_path)

    # Dictionary to store average temperatures by station
    station_avg_temps = {}

    # Loop through each sheet (year)
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)

        # Calculate the average temperature for each station in the sheet
        for _, row in df.iterrows():
            station_name = row["STATION_NAME"]
            temperatures = row.iloc[4:16]  # Assuming temperature columns are from E to P
            if temperatures.notnull().any():
                avg_temp = temperatures.mean()
                if station_name in station_avg_temps:
                    station_avg_temps[station_name].append(avg_temp)
                else:
                    station_avg_temps[station_name] = [avg_temp]

    # Calculate overall average temperature for each station
    station_avg_temps = {
        station: sum(temps) / len(temps) for station, temps in station_avg_temps.items()
    }

    # Find the warmest and coolest stations
    max_avg_temp = max(station_avg_temps.values())
    min_avg_temp = min(station_avg_temps.values())
    warmest_stations = [station for station, avg_temp in station_avg_temps.items() if avg_temp == max_avg_temp]
    coolest_stations = [station for station, avg_temp in station_avg_temps.items() if avg_temp == min_avg_temp]

    # Write the results to the output file
    with open(output_file, "w") as f:
        f.write(f"Warmest Station(s) (Avg Temp: {max_avg_temp:.2f}):\n")
        for station in warmest_stations:
            f.write(f"{station}\n")
        f.write(f"\nCoolest Station(s) (Avg Temp: {min_avg_temp:.2f}):\n")
        for station in coolest_stations:
            f.write(f"{station}\n")

if __name__ == "__main__":
    file_path = "TEMPERATURE DATA.xlsx"  # Replace this with the actual file path after cloning the repository

    # Calculate average temperatures
    avg_output_file = "average_temp.txt"
    calculate_average_temperatures(file_path, avg_output_file)
    print(f"Average seasonal temperatures have been saved to {avg_output_file}.")

    # Find the station with the largest temperature range
    range_output_file = "largest_temp_range_station.txt"
    find_largest_temperature_range(file_path, range_output_file)
    print(f"Stations with the largest temperature range have been saved to {range_output_file}.")

    # Find the warmest and coolest stations
    warmest_coolest_output_file = "warmest_and_coolest_station.txt"
    find_warmest_and_coolest_stations(file_path, warmest_coolest_output_file)
    print(f"Warmest and coolest stations have been saved to {warmest_coolest_output_file}.")

