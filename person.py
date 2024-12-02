import random
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated, infection = None):
        # A person has an id, is_vaccinated and possibly an infection
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated # Bool
        self.infection = infection # Virus object
        self.is_alive = True # Bool

    def did_survive_infection(self) -> bool:
        if self.infection:
            survival_chance = 1 - self.infection.mortality_rate
            if random.random() > survival_chance:
                # Person has died
                self.is_alive = False
            else:
                # The person survived
                self.is_alive = True
            self.infection = None
        return self.is_alive

if __name__ == "__main__":
    random.seed(42)
    # This section is incomplete finish it and use it to test your Person class
    # TODO Define a vaccinated person and check their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    # TODO Test unvaccinated_person's attributes here...
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    # Test an infected person. An infected person has an infection/virus
    virus = Virus("Dysentery", 0.7, 0.2)
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection == virus
    # Test survival of infected people
    people = []
    for i in range(1, 100):
        # Create infected people
        people.append(Person(i + 4, False, virus))

    did_survive = 0
    did_not_survive = 0

    for person in people:
        survived = person.did_survive_infection()
        if survived:
            did_survive += 1
        else:
            did_not_survive += 1

    print(f"Survived: {did_survive}")
    print(f"Did not survive: {did_not_survive}")

    # Results should roughly match mortality rate
    assert abs(did_not_survive / len(people) - virus.mortality_rate) < 0.1, \
        "Mortality rate does not match expected value."

    # Test infection spread
    uninfected_people = [Person(i + 104, False) for i in range(100)]
    newly_infected = 0
    for person in uninfected_people:
        if random.random() < virus.repro_rate:
            person.infection = virus
            newly_infected += 1

    print(f"Newly infected: {newly_infected}")
    print(f"Not infected: {len(uninfected_people) - newly_infected}")

    # Results should roughly match reproduction rate
    assert abs(newly_infected / len(uninfected_people) - virus.repro_rate) < 0.1, \
        "Results do not match expected values."