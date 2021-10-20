class Player:

    LEVEL = 0

    def __init__(self, username, password):
        self._CREDENTIALS = {
            'username': username,
            'password': password
        }
    
    def __str__(self):
        return f'Username: {self._CREDENTIALS["username"]} Level: {self.LEVEL}'

    @property
    def username(self):
        return self._CREDENTIALS["username"]
              
class Planet:

    def __init__(self, name=None, resources=[]):
        self._name = name
        self._resources = resources

    def __add_resources(self, *resources):
        for resource in resources:
            self._resources.append(resource)

    def __remove_resources(self, *resources):
        for resource in resources:
            self._resources.remove(resource)

class Universe:

    def __init__(self, planets=[]):
        self._planets = planets

    def __add_planet(self, planet):
        self._planets.append(planet)
    
    def __remove_planet(self, planet):
        self._planets.remove(planet)
