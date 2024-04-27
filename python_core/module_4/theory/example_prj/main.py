from data import load_data, clean_data
from processing import calculate_statistics

def main():
    filename = "temperatures.txt"
    raw_data = load_data(filename)
    temperatures = clean_data(raw_data)
    stats = calculate_statistics(temperatures)

    if stats:
        print(f"Minimum Temperatures: {stats['min']}°C")
        print(f"Maximum Temperatures: {stats['max']}°C")
        print(f"Average Temperatures: {stats['average']:.2f}°C")
        print(f"Median Temperatures: {stats['median']:.2f}°C")
    else:
        print("No temperature data available")

if __name__ == "__main__":
    main()
