import re
from datetime import datetime
import os


def analyze_simulation_log(logfile_path):
    if not os.path.exists(logfile_path):
        raise FileNotFoundError(f"The log file '{logfile_path}' does not exist.")

    with open(logfile_path, 'r') as file:
        lines = file.readlines()

    # Extract inputs using regex, with error handling for missing patterns
    try:
        population_size = int(re.search(r"Initial Population Size: (\d+)", "".join(lines)).group(1))
        percent_vaccinated = float(re.search(r"Vaccination Percentage: (\d+.\d+)%", "".join(lines)).group(1))
        virus_name = re.search(r"Virus Name: (.+)", "".join(lines)).group(1)
        mortality_rate = float(re.search(r"Virus Mortality Rate: (\d+.\d+)%", "".join(lines)).group(1))
        repro_rate = float(re.search(r"Virus Reproduction Rate: (\d+.\d+)%", "".join(lines)).group(1))
        total_dead = int(re.search(r"Total Dead: (\d+)", "".join(lines)).group(1))
        total_vaccinated = int(re.search(r"Vaccinated: (\d+)", "".join(lines)).group(1))
        interactions_vaccination = int(re.search(r"Interactions Resulting in Vaccination: (\d+)", "".join(lines)).group(1))
    except AttributeError as e:
        raise ValueError("Log file is missing required information or is improperly formatted.") from e

    # Calculate percentages
    percentage_infected = ((population_size - total_vaccinated - total_dead) / population_size) * 100
    percentage_dead = (total_dead / population_size) * 100

    # Prepare results
    results = {
        "Population Size": population_size,
        "Percent Vaccinated": percent_vaccinated,
        "Virus Name": virus_name,
        "Mortality Rate": mortality_rate,
        "Reproductive Rate": repro_rate,
        "Percentage Infected": percentage_infected,
        "Percentage Dead": percentage_dead,
        "Interactions Resulting in Vaccination": interactions_vaccination
    }
    return results


def save_answers_to_file(results, output_file):
    with open(output_file, 'w') as file:
        file.write("Simulation Analysis Results\n")
        file.write("===========================\n")
        file.write(f"Date of Analysis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        file.write(f"Population Size: {results['Population Size']}\n")
        file.write(f"Percent Vaccinated: {results['Percent Vaccinated']}%\n")
        file.write(f"Virus Name: {results['Virus Name']}\n")
        file.write(f"Mortality Rate: {results['Mortality Rate']}%\n")
        file.write(f"Reproductive Rate: {results['Reproductive Rate']}%\n\n")
        file.write(f"Percentage Infected: {results['Percentage Infected']:.2f}%\n")
        file.write(f"Percentage Dead: {results['Percentage Dead']:.2f}%\n")
        file.write(f"Interactions Resulting in Vaccination: {results['Interactions Resulting in Vaccination']}\n")


if __name__ == "__main__":
    try:
        # Define the log file and output file
        logfile = 'simulation_log.txt'
        output_file = 'answers.txt'

        # Perform analysis and save results
        results = analyze_simulation_log(logfile)
        save_answers_to_file(results, output_file)

        print("Analysis complete. Results saved to 'answers.txt'.")
    except Exception as e:
        print(f"An error occurred: {e}")
