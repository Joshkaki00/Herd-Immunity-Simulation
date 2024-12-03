import random
from virus import Virus


class Person:
    def __init__(self, _id, is_vaccinated, infection=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True

    def did_survive_infection(self):
        if self.infection is not None:
            if random.random() < self.infection.mortality_rate:
                self.is_alive = False
            else:
                self.is_alive = True
                self.is_vaccinated = True
            self.infection = None
        return self.is_alive


if __name__ == "__main__":
    random.seed(42)

    # Test vaccinated person
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    # Test infected person
    virus = Virus("Dysentery", 0.7, 0.2)
    infected_person = Person(3, False, virus)
    assert infected_person.did_survive_infection() in [True, False]

    # Population stats
    people = [Person(i, False, virus) for i in range(100)]
    deaths = sum(1 for p in people if not p.did_survive_infection())
    print(f"Deaths: {deaths}, Survival rate: {100 - deaths}%")