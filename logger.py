class Logger:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        with open(self.file_name, 'w') as file:
            file.write("=== Simulation Metadata ===\n")
            file.write(f"Population Size: {pop_size}\n")
            file.write(f"Vaccination Percentage: {vacc_percentage}\n")
            file.write(f"Virus: {virus_name}\n")
            file.write(f"Mortality Rate: {mortality_rate}\n")
            file.write(f"Basic Reproduction Number: {repro_rate}\n\n")

    def log_interactions(self, infected_id, random_person_id, did_infect):
        with open(self.file_name, 'a') as file:
            status = "infected" if did_infect else "did not infect"
            file.write(f"Infected Person {infected_id} interacted with Person {random_person_id} and {status}.\n")

    def log_step_summary(self, step, interactions, new_infections):
        with open(self.file_name, 'a') as file:
            file.write(f"Step {step}:\n")
            file.write(f"  Total Interactions: {interactions}\n")
            file.write(f"  New Infections: {new_infections}\n\n")

    def log_final_summary(self, pop_size, living, dead, vaccinated, steps):
        with open(self.file_name, 'a') as file:
            file.write("=== Final Summary ===\n")
            file.write(f"Total Population: {pop_size}\n")
            file.write(f"Living: {living}\n")
            file.write(f"Dead: {dead}\n")
            file.write(f"Vaccinated: {vaccinated}\n")
            file.write(f"Total Steps: {steps}\n")
