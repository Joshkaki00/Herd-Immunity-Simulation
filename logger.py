class Logger:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        with open(self.file_name, "w") as f:
            f.write(f"Population Size: {pop_size}\n")
            f.write(f"Vaccination Percentage: {vacc_percentage}\n")
            f.write(f"Virus Name: {virus_name}\n")
            f.write(f"Mortality Rate: {mortality_rate}\n")
            f.write(f"Reproduction Rate: {repro_rate}\n")
            f.write("=== Start of Simulation ===\n\n")

    def log_step_summary(self, step, new_infections, interactions, living, dead, vaccinated):
        with open(self.file_name, "a") as f:
            f.write(f"Step {step}:\n")
            f.write(f"  New Infections: {new_infections}\n")
            f.write(f"  Total Interactions: {interactions}\n")
            f.write(f"  Total Living: {living}\n")
            f.write(f"  Total Dead: {dead}\n")
            f.write(f"  Total Vaccinated: {vaccinated}\n\n")

    def log_final_summary(self, pop_size, living, dead, vaccinated, steps):
        with open(self.file_name, "a") as f:
            f.write("=== Final Summary ===\n")
            f.write(f"Total Population: {pop_size}\n")
            f.write(f"Living: {living}\n")
            f.write(f"Dead: {dead}\n")
            f.write(f"Vaccinated: {vaccinated}\n")
            f.write(f"Total Steps: {steps}\n")
