class pirate:
    total = 0
    MAX_HEALTH = 5
    DEFAULT_HEALTH = 3

    def __init__(self, name=None, health=None):
        self.name = self.check_name(name)
        self.health = self.check_health(health)
        pirate.total += 1

    def check_name(self, name):
        if name == None:
            return f'P{pirate.total}'
        else:
            return name

    def check_health(self, health):
        if health == None or health <= 0 or health > pirate.MAX_HEALTH:
            return pirate.DEFAULT_HEALTH
        else:
            return health

    def __str__(self):
        return f'[{self.name}, {self.health}]'