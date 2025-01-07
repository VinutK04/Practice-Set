emp_data = [
    {"Name": "Ravi", "Salary": "30000", "Location": "Mumbai"},
    {"Name": "Santhosh", "Salary": "20000", "Location": "Bangalore"},
    {"Name": "Anu", "Salary": "40000", "Location": "Mumbai"},
    {"Name": "Raju", "Salary": "35000", "Location": "Bangalore"},
    {"Name": "Sita", "Salary": "25000", "Location": "Delhi"}
]

# 1. Count employees in each location
location_counts = {}
for employee in emp_data:
    location = employee["Location"]
    location_counts[location] = location_counts.get(location, 0) + 1

print("Number of employees in each location:")
for location, count in location_counts.items():
    print(f"{location}: {count}")
    
# 2. Calculate min, max, and avg salary for each location
location_stats = {}
for employee in emp_data:
    location = employee["Location"]
    salary = int(employee["Salary"]) 

    if location not in location_stats:
        location_stats[location] = {
            "min": salary,
            "max": salary,
            "sum": salary,
            "count": 1
        }
    else:
        location_stats[location]["min"] = min(location_stats[location]["min"], salary)
        location_stats[location]["max"] = max(location_stats[location]["max"], salary)
        location_stats[location]["sum"] += salary
        location_stats[location]["count"] += 1

print("\nSalary statistics for each location:")
for location, stats in location_stats.items():
    avg_salary = stats["sum"] / stats["count"]
    print(f"{location}: Min: {stats['min']}, Max: {stats['max']}, Avg: {avg_salary}")
