from dataclasses import dataclass, field
from sys import argv
from typing import Tuple

width = 8
height = 8


@dataclass
class Person:
    position: Tuple[int, int]
    state: str
    quarantined: bool
    since_getting_sick = 0
    n: int = field(init=False)

    def __post_init__(self):
        self.n = (self.position[0] << 2) ^ 7 * (self.position[1] << 3) ^ 5

    def bump(self):
        if self.state == 'S':
            self.since_getting_sick += 1
            if self.since_getting_sick == 14:
                self.state = 'R'
        self.gen_n()

    def gen_n(self):
        n = self.n

        n ^= n << 13
        n ^= n >> 17
        n ^= n << 5

        self.n = n % (1 << 30)


def get_new_cords(person: Person):
    x = person.position[0]
    y = person.position[1]

    if person.n % 4 == 0:
        x += 1
    if person.n % 4 == 1:
        x -= 1
    if person.n % 4 == 2:
        y += 1
    if person.n % 4 == 3:
        y -= 1

    return x % width, y % height


def print_world():
    for y in range(height):
        for x in range(width):
            dot = '.'
            for person in population:
                if person.position == (x, y):
                    dot = person.state
            print(dot, end='')
        print()


def next_iteration():
    for person in population:
        person.bump()
        if not person.quarantined:
            new_cords = get_new_cords(person)
            if not any(new_cords == p.position for p in population):
                person.position = new_cords
        if person.state == 'H' and any(
                p.state == 'S' and
                person.position[0] - 1 <= p.position[0] <= person.position[0] + 1 and
                person.position[1] - 1 <= p.position[1] <= person.position[1] + 1 for p in
                population):
            person.state = 'S'


generations = int(argv[1])
initial_state = argv[2].split(',')
population = []

for state in initial_state:
    population.append(Person((int(state[0]), int(state[1])), state[2], state[3] == '1'))

for i in range(generations):
    next_iteration()

print_world()
