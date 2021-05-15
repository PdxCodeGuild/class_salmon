'''

Turn-based Action Point COMBAT system
v2

Roadmap >>

* Add an "Aimed Attack[A]"
    > Head[H], Torso[T], etc.
    > Increased difficulty, but higher damage and/or special effect (reduce enemy AP)

* Add "Disarm[D]"
    > Useable only on armed enemies
    > Unequips their primary weapon

* Refine Block[B] mechanism
    > Add diminishing returns on subsequent blocks

* Add "Throw[T]"
* Add "Shoot[S]"

* For each weapon type, add other unique combat modifiers
    > increased/decrease AP point cost
    > Temporary conditions - Stun, Disorient, Blind, etc.

'''

import random
import time


class Entity:
    def __init__(self, name=f'Enemy', target=None):
        self.name = name
        self.health = 30
        self.health_cap = 30
        self.action_points = 2
        self.ap_cap = 5
        self.damage = 4
        self.accuracy = 60
        self.heal_cap = 8
        self.target = target
        self.combo_points = 0
        self.cp_cap = 3
        self.quick_name = 'JAB'
        self.strong_name = 'PUNCH'
        self.vicious_name = 'SLAM'
        self.block_status = False
        self.block_amount = 2

    def ap_combo_check(self, req_ap=0, req_combo=0):
        if req_ap > self.action_points:
            print("\tYou don't have enough action points for that ability!")
            return False
        if req_combo > self.combo_points:
            print(f"\tThat ability requires {req_combo} combo points to execute!")
            return False
        else:
            return True

    def quick_attack(self):
        ap_cost = 1
        combo_cost = 0
        if self.ap_combo_check(ap_cost, combo_cost) == True:
            print(f"The {self.name} attempts to {self.quick_name} {self.target.name}!")
            time.sleep(.5)
            quick_modifier = 10
            dmg = int(self.damage / 3)
            x = random.randint(1, 100)
            self.action_points -= ap_cost
            if x < self.accuracy + quick_modifier:
                if self.target.block_status == False:
                    print(f"\tThe {self.quick_name} damages {self.target.name} for {dmg}!")
                    self.target.health -= dmg
                else:
                    print(f"\t{self.target.name} BLOCKS the {self.quick_name}, reducing the damage by {self.target.block_amount}.")
                    modified_dmg = dmg - self.target.block_amount
                    if modified_dmg < 0:
                        modified_dmg = 0
                    if modified_dmg > 0:
                        print(f"\tThe {self.quick_name} damages {self.target.name} for {modified_dmg}!")
                        self.target.health -= modified_dmg
                self.action_points += 2
                if self.action_points > self.ap_cap:
                    self.action_points = self.ap_cap
                self.combo_points += 1
                if self.combo_points > self.cp_cap:
                    self.combo_points = self.cp_cap
            else:
                print(f"\t{self.target.name} evades the {self.quick_name}!")
                self.combo_points = 0
        else:
            return

    def strong_attack(self):
        ap_cost = 3
        combo_cost = 1
        if self.ap_combo_check(ap_cost, combo_cost) == True:
            print(f"The {self.name} attempts to {self.strong_name} {self.target.name}!")
            time.sleep(.5)
            strong_modifier = -10
            dmg = int(self.damage / 2)
            x = random.randint(1, 100)
            self.action_points -= ap_cost
            if x < self.accuracy + strong_modifier:
                print(f"\tThe {self.strong_name} damages {self.target.name} for {dmg}!")
                self.target.health -= dmg
                self.action_points += 4
                if self.action_points > self.ap_cap:
                    self.action_points = self.ap_cap
                self.combo_points += 1
                if self.combo_points > self.cp_cap:
                    self.combo_points = self.cp_cap
            else:
                print(f"\t{self.target.name} evades the {self.strong_name}!")
                self.combo_points = 0
        else:
            return

    def vicious_attack(self):
        ap_cost = 5
        combo_cost = 2
        if self.ap_combo_check(ap_cost, combo_cost) == True:
            print(f"The {self.name} attempts to {self.vicious_name} {self.target.name}!")
            time.sleep(.5)
            vicious_modifier = -20
            dmg = self.damage
            x = random.randint(1, 100)
            self.action_points -= ap_cost
            if x < self.accuracy + vicious_modifier:
                print(f"\tThe {self.vicious_name} damages {self.target.name} for {dmg}!")
                self.target.health -= dmg
                # self.combo_points += 1
                # if self.combo_points > self.cp_cap:
                #     self.combo_points = self.cp_cap
            else:
                print(f"\t{self.target.name} evades the {self.vicious_name}!")
                self.combo_points = 0
                self.action_points = 0
        else:
            return

    def heal(self):
        ap_cost = 2
        if self.ap_combo_check(ap_cost) == True:
            random_heal = random.randint(int(self.heal_cap / 2), self.heal_cap)
            self.health += random_heal
            print(f"The {self.name} heals itself for {random_heal}!")
            if self.health > self.health_cap:
                self.health = self.health_cap
            self.action_points -= ap_cost
        else:
            return

    def block(self):
        ap_cost = 1
        if self.ap_combo_check(ap_cost) == True:
            print(f"{self.name} prepares to BLOCK!")
            print(f"\tBlocking will reduce incoming damage by {self.block_amount}.")
            self.block_status = True
            self.action_points -= ap_cost
            time.sleep(1)

    def equip_weapon(self, type):
        weapon_types = {'spear': {'dmg': 9, 'quick': 'STAB', 'strong': 'SLASH', 'vicious': 'SKEWER'},
                        'club': {'dmg': 9, 'quick': 'BLUDGEON', 'strong': 'SMASH', 'vicious': 'DEMOLISH'}}
        self.quick_name = weapon_types[type]['quick']
        self.strong_name = weapon_types[type]['strong']
        self.vicious_name = weapon_types[type]['vicious']
        self.damage = weapon_types[type]['dmg']

    def reset_combat_turn(self):
        self.combo_points = 0
        self.action_points = 2
        self.target.block_status = False
        print()


class BasicEnemy(Entity):
    def __init__(self, name, target=None):
        Entity.__init__(self, name, target)

    def combat_turn(self):
        print(f"The {self.name} ATTACKS! >>")
        print()
        while self.action_points > 0 and self.target.health > 0:
            if self.action_points >= 5 and self.health >= 12 and self.combo_points >= 2:
                self.vicious_attack()
            elif self.action_points >= 2 and self.health < 12:
                self.heal()
            elif self.action_points >= 3 and self.combo_points >= 1:
                self.strong_attack()
            elif self.action_points > 1:
                self.quick_attack()
            elif self.action_points == 1:
                self.block()
            else:
                pass
        self.reset_combat_turn()


class PlayerCharacter(Entity):
    def __init__(self, name, target=None):
        Entity.__init__(self, name, target)

    def combat_interface(self):
        print()
        print(f'HEALTH {self.health} | ENEMY {self.target.health}')
        print('AP', '*' * self.action_points, '| CP', '+' * self.combo_points, end=' | ')

    def player_combat_turn(self):
        while self.action_points > 0 and self.target.health > 0:
            player_one.combat_interface()
            print('ACTIONS >> Quick Atk[Q]', end='')
            if self.combo_points >= 1:
                print(' | Strong Atk[S]', end='')
            if self.combo_points >= 2:
                print(' | Vicious Atk[V]', end='')
            if self.action_points >= 2:
                print(' | Heal[H]', end='')
            if self.action_points >= 1:
                print(' | Block[B] ', end='')
            action = input('>> ')
            if action == 'q':
                self.quick_attack()
            elif action == 's':
                self.strong_attack()
            elif action == 'v':
                self.vicious_attack()
            elif action == 'h':
                self.heal()
            elif action == 'b':
                self.block()
        self.reset_combat_turn()


player_one = PlayerCharacter('Reluctant Adventurer')

enemy001 = BasicEnemy('Drone')

player_one.equip_weapon('spear')
enemy001.equip_weapon('club')


def combat_round(hero, enemy):
    hero.target = enemy
    enemy.target = hero
    while player_one.health > 0 and enemy001.health > 0:
        if hero.health > 0:
            player_one.player_combat_turn()
        if enemy.health > 0:
            enemy.combat_turn()
        if hero.health <= 0:
            print(f"{hero} has been slain by {enemy}!")
        if enemy.health <= 0:
            print(f"{enemy} has been slain by {hero}!")
        print()


combat_round(player_one, enemy001)
