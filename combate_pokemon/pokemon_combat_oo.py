
class BasePokemon:
    vida_base = 100
    ataque = 10
    nombre = "Pokemon"
    attacks = []

    def __init__(self):
        self.vida = self.vida_base

    def atacar(self, enemigo, attack_name=None):
        if not attack_name:
            enemigo.recibir_dano(self.ataque)
        else:
            for attack in self.attacks:
                if attack.name == attack.name:
                    enemigo.recibir_dano(attack.ataque)

    def recibir_dano(self, damage):
        self.vida -= damage

    def mostrar_vida(self):
        print("Vida de {}: {}".format(self.nombre, self.vida))

class BasePokemonAttack:
    name = ""
    damage = 0



class ChispazoAttack(BasePokemonAttack):
    name = "Chispazo"
    damage = 10


class BolaVoltioAttack(BasePokemonAttack):
    name = "Bola voltio"
    damage = 9


class Charmander(BasePokemon):
    vida_base = 100
    ataque = 10
    nombre = "Charmander"



class Pikachu(BasePokemon):
    vida_base = 120
    ataque = 12
    nombre = "Pikachu"
    attacks = [ChispazoAttack, BolaVoltioAttack]

class Bulbasaur(BasePokemon):
    vida_base = 90
    ataque = 7
    nombre = "Bulbasaur"


class Squirtle (BasePokemon):
    vida_base = 100
    ataque = 3
    nombre = "Squirtle"
