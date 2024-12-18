from datetime import datetime

class Logger:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(self.file_name, 'w') as file:
            file.write("")  # Clear existing content

    def write_metadata(self, pop_size, initial_infected, virus_name, mortality_rate, repro_rate):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.file_name, 'a') as file:
            file.write(f"Simulation Date: {date}\n")
            file.write(f"Initial Population Size: {pop_size}\n")
            file.write(f"Initial Infected People: {initial_infected}\n")
            file.write(f"Virus Name: {virus_name}\n")
            file.write(f"Virus Mortality Rate: {mortality_rate * 100:.2f}%\n")
            file.write(f"Virus Reproduction Rate: {repro_rate * 100:.2f}%\n")
            file.write("=== Start of Simulation ===\n\n")

    def log_step_summary(self, step, new_infections, deaths, living, dead, vaccinated):
        with open(self.file_name, "a") as f:
            f.write(f"Step {step}:\n")
            f.write(f"  New Infections: {new_infections}\n")
            f.write(f"  Deaths This Step: {deaths}\n")
            f.write(f"  Total Living: {living}\n")
            f.write(f"  Total Dead: {dead}\n")
            f.write(f"  Total Vaccinated: {vaccinated}\n\n")

    def log_final_summary(self, pop_size, living, dead, vaccinated, total_interactions, vaccination_interactions, death_interactions, reason):
        with open(self.file_name, "a") as f:
            f.write("=== Final Summary ===\n")
            f.write(f"Total Population: {pop_size}\n")
            f.write(f"Living: {living}\n")
            f.write(f"Dead: {dead}\n")
            f.write(f"Vaccinated: {vaccinated}\n")
            f.write(f"Total Interactions: {total_interactions}\n")
            f.write(f"Interactions Resulting in Vaccination: {vaccination_interactions}\n")
            f.write(f"Interactions Resulting in Death: {death_interactions}\n")
            f.write(f"Simulation Ended Because: {reason}\n")
