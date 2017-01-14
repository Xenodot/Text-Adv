import easygui, time, random, pygame, sys

#####Progression#####
free_time = False
game_run = True
progression = 0
current_quest = None
quest_battle = False
quest_complete = False
#########################################

###Character starting stats###
money = 700
hp = 100
hpmax = 100
mana = 20
manamax = 20
ad = 10
defense = 5
lvl = 1
exp = 0
exp_req = 10
inv = []

current_opponent = ""
battle_won = False
turn_timer_p = 0
turn_timer_o = 0
manashield = False


class Character:

    def __init__(self, name, role, home, money, hp, hpmax, mana, manamax, atk, Def, lvl, exp, exp_req):
        self.name = name
        self.role = role
        self.home = home
        self.hp = hp
        self.hpmax = hpmax
        self.money = money
        self.mana = mana
        self.manamax = manamax
        self.atk = atk
        self.Def = Def
        self.lvl = lvl
        self.exp = exp
        self.exp_req = exp_req
    def name(self):
        return self.name
    def role(self):
        return self.role
    def home(self):
        return self.home
    def money(self):
        return self.money
    def hp(self):
        return self.hp
    def hpmax(self):
        return self.hpmax
    def mana(self):
        return self.mana
    def manamax(self):
        return self.manamax
    def atk(self):
        return self.atk
    def Def(self):
        return self.Def
    def lvl(self):
        return self.lvl
    def exp(self):
        return exp
    def exp_req(self):
        return exp_req

class enemy:

    def __init__(self, name, hp, atk, Def, lvl):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.Def = Def
        self.lvl = lvl
    def __str__(self):
        name = self.name
        return name
    def name(self):
        return self.name
    def hp(self):
        return self.hp
    def atk(self):
        return self.atk
    def Def(self):
        return self.Def
    def lvl(self):
        return self.lvl

class weapon:

    def __init__(self, name, price, dmg, lvlreq, class_req):
        self.name = name
        self.price = price
        self.dmg = dmg
        self.lvlreq = lvlreq
        self.class_req = class_req
    def __str__(self):
        name = self.name
        return name
    def name(self):
        return self.name
    def price(self):
        return self.price
    def dmg(self):
        return self.dmg
    def lvlreq(self):
        return self.lvlreq
    def class_req(self):
        return self.class_req

class armor:
    def __init__(self, name, price, Def, lvlreq, class_req):
        self.name = name
        self.price = price
        self.Def = Def
        self.lvlreq = lvlreq
        self.class_req = class_req
    def __str__(self):
        name = self.name
        return name
    def name(self):
        return self.name
    def price(self):
        return self.price
    def Def(self):
        return self.Def
    def lvlreq(self):
        return self.lvlreq
    def class_req(self):
        return self.class_req

class quest:
    def __init__(self, name, story, foe, gold_r, exp_r, location):
        self.name = name
        self.story = story
        self.foe = foe
        self.gold_r = gold_r
        self.exp_r = exp_r
        self.location = location
    def __str__(self):
        name = self.name
        return name
    def name(self):
        return self.name
    def story(self):
        return self.name
    def foe(self):
        return self.foe
    def gold_r(self):
        return self.gold_r
    def exp_r(self):
        return self.exp_r
    def location(self):
        return self.location

#################################################################
#                                                               #
#                       GAME ITEMS / Enemies                    #
#                                                               #
#################################################################

#Weapons
Basic_Wand = weapon("Basic Wand",0, 5, 1, "Mage")
Staff = weapon("Staff", 200, 12, 3, "Mage")
Battle_Staff = weapon("Battle Staff", 400, 20, 5, "Mage")

Short_Bow = weapon("Short Bow", 0, 5, 1, "Archer")
Long_Bow = weapon("Long Bow", 200, 9, 3, "Archer")
Composite_Bow = weapon("Composite Bow", 400, 15, 5, "Archer")

Sword = weapon("Sword",0, 6, 1, "Swordsman")
Mace = weapon("Mace", 200, 10, 3, "Swordsman")
Great_Sword = weapon("Great Sword", 400, 18, 5, "Swordsman")

Flower = weapon("Flower", 0, 18, 0, "All")

Weapons = [Basic_Wand,Staff,Battle_Staff,Short_Bow,Long_Bow,Composite_Bow,Sword,Mace,Great_Sword]
Shop_stock = []


#Armor
Basic_Robes = armor("Basic Robes", 0, 9, 1, "Mage")
Battle_Robes = armor("Battle Robes", 150, 15, 3, "Mage")
Robe_of_the_Magi = armor("Robe of the Magi", 300, 21, 5, "Mage")

Worn_Garbs = armor("Worn Garbs", 0, 9, 1, "Archer")
Cloak = armor("Cloak", 150, 16, 3, "Archer")
Shadow_Veil = armor("Shadow Veil", 300, 23, 5, "Archer")

Leather_Armor = armor("Leather Armor", 0, 10, 1, "Swordsman")
Chainmail = armor("Chainmain", 150, 17, 3, "Swordsman")
Iron_Armor = armor("Iron Armor", 300, 25, 5, "Swordsman")

Gown = armor("Gown", 0, 25, 0, "All")

Armor = [Basic_Robes,Battle_Robes,Worn_Garbs,Cloak,Leather_Armor,Chainmail,Gown, Robe_of_the_Magi, Shadow_Veil, Iron_Armor]


#Enemies
Goblin = enemy("Goblin", 50, 5, 3, 1)
Thief = enemy("Thief", 50, 8, 4, 2)
Bandit = enemy("Bandit", 60, 9, 5, 3)
Dragon = enemy("Dragon", 1000, 60, 50, 30)

#################################################################
#                                                               #
#                           Quests                              #
#                                                               #
#################################################################
default_q = ("", "", Goblin, 0, 0, "")
Practice_quest_story = ("Recently, goblins have been pestering our farms by stealing tools and killing off livestock. It would be a great help for all of us if you could take care of a few.")
Practice_quest = quest("Practice Quest", Practice_quest_story, Goblin, 50, 20, "Farm")
q1_story = ("This morning, a valuable personal possession was reported to be stolen by the nearby thieves. We have a request to go and retrieve that item.")
q1 = quest("Thief!", q1_story, Thief, 70, 20, "Forest")
q2_story = ("A wanted bandit has been sighted around the cave to the west. It would be a great help to have him eliminated.")
q2 = quest("Sabotage", q2_story, Bandit, 80, 30, "Bandit Hideout")
dragon_quest_story = ("You arrive at the cave Ethamis directed you to. Taking a deep breath, you wander in.")
dragon_quest = quest("The Final Quest", dragon_quest_story, Dragon, 9999, 900, "Mysterious Cave")

#################################################################
#                                                               #
#                       Battle System                           #
#                                                               #
#################################################################

def p_battle(opponent):
    global skills, current_opponent, battle_won, current_quest, quest_battle, turn_timer_p, turn_timer_o
    turn_timer_p = 0
    turn_timer_o = 0
    battle_won = False
    current_opponent = opponent
    turn = True
    o_hp = opponent.hp
    o_atk = opponent.atk
    o_def = opponent.Def
    o_name = opponent.name
    p_hp = mc.hp
    if mc.role == "Mage":
        p_atk = mc.atk
        mc.atk /= 2
    else:
        p_atk = mc.atk
    p_def = mc.Def
    enemy_status = "alive"
    exp = opponent.lvl * 2 + 2
    while enemy_status == "alive":
        if turn == True and turn_timer_p == 0:
            if mc.hp <= 0:
                msg("You Have Died", "Game Over", "...")
                a = easygui.buttonbox("Continue?", "Game Over", choices = ("Yes", "No"))
                if a == "Yes":
                    msg("You barely manage to get away, with grievous wounds.", "Defeat", "...")
                    loss = mc.lvl*5
                    msg("You have lost {!s} gol.".format(loss), "Defeat", "...")
                    mc.hp = 1
                    mc.money -= loss
                    break
                else:
                    msg("GAME OVER", "Game", "Quit")
                    sys.exit()
            action = easygui.buttonbox("What will you do? \n {!s} (Lv. {!s}) HP: {!s} \n Your HP: {!s} \n MP: {!s}".format(opponent.name, opponent.lvl, opponent.hp, mc.hp, mc.mana), "TEST YOUR MIGHT", choices=("Attack", "Skill", "Flee"))
            if action == "Attack":
                damage = int((mc.atk+inv[0].dmg) - (opponent.Def/2)+random.randint(-5,5))
                opponent.hp -= damage
                msg("You did {!s} points of damage to {!s}.".format(damage, opponent.name), "attack", "...")
            elif action == "Skill":
                abilities = []
                for i in skills:
                    if i[0] == mc.role or i[0] == "All":
                        if i[1] <= mc.lvl:
                            abilities.append(i[2])
                which_skill = easygui.buttonbox(msg="Choose the skill you want to use", title="Skill", choices = (abilities))
                msg("You used {!s}.".format(which_skill), "Skill", "...")
                if which_skill == "EDEFDWN":
                    DEFDWN(opponent)
                elif which_skill == "PATKUP":
                    ATKUP(mc)
                elif which_skill == "PDEFUP":
                    DEFUP(mc)
                elif which_skill == "EATKDWN":
                    ATKDWN(opponent)
                elif which_skill == "Shield Bash":
                    shield_bash(opponent)
                elif which_skill == "Fireball":
                    fireball(opponent)
                elif which_skill == "Return":
                    turn_timer_o += 1
                elif which_skill == "Lucky Shot":
                    lucky_shot(opponent)
                elif which_skill == "Mana Shield":
                    Manashield()
            elif action == "Flee":
                chance = random.randint(1, 5)
                if chance < 4:
                    msg("Ran away successfully.", "Battle", "...")
                    break
                else:
                    msg("You were not able to get away.", "Battle", "...")
                    
            turn = False

        elif turn == True and turn_timer_p != 0:
            msg("Your turn has been skipped!", "Battle", "...")
            if turn_timer_p > 0:
                turn_timer_p -= 1
            turn = False
            
        elif turn == False and turn_timer_o == 0:
            action = random.randint(0, 2)
            if action <= 1:
                damage = int(opponent.atk - (mc.Def+inv[1].Def/2)+random.randint(0,7))
                if manashield == False:
                    if damage <= 0:
                        damage = 1
                    mc.hp -= damage
                    msg("The enemy {!s} attacked you for {!s} points of damage.".format(opponent.name, damage), "", "...")
                if mc.role == "Mage" and manashield == True:
                    mana_as_dmg = int(damage*0.4)
                    damage *= 0.8
                    if damage <= 0:
                        damage = 1
                    mc.hp -= int(damage)
                    mc.mana -= mana_as_dmg
                    msg("The enemy {!s} attacked you for {!s} points of damage.".format(opponent.name, int(damage)), "", "...")
                    msg("You used up {!s} mana to block {!s} damage!".format(mana_as_dmg, int(damage*0.2)), "", "...")
                
            elif action == 2:
                if opponent.name != "Dragon":
                    value = random.randint(0, 3)
                else:
                    value = random.randint(0, 6)
                if value == 0:
                    ATKUP(opponent)
                elif value == 1:
                    ATKDWN(mc)
                elif value == 2:
                    DEFDWN(mc)
                elif value == 3:
                    DEFUP(opponent)
                elif value == 4:
                    fireball(mc)
                elif value == 5:
                    stomp()
                elif value == 6:
                    barrage(mc)
                
            turn = True
                    
        elif turn == False and turn_timer_o != 0:
            msg("{!s}'s turn has been skipped!".format(opponent.name), "Battle", "...")
            if turn_timer_o > 0:
                turn_timer_o -= 1
                    
            turn = True

        print(turn_timer_p, turn_timer_o)
                
        if opponent.hp <= 0:
            enemy_status = "dead"
            money_earned = 20*opponent.lvl + random.randint(0, (opponent.lvl * 3))
            mc.money += money_earned
            msg("You have defeated {!s}. {!s} exp gained.".format(opponent, exp), "Victory", "...")
            msg("Obtained {!s} gol.".format(money_earned), "", "...")
            mc.exp += exp
            opponent.hp = o_hp
            opponent.Def = o_def
            opponent.atk = o_atk
            mc.atk = p_atk
            mc.Def = p_def
            battle_won = True
            quest_battle = True
            
    turn_timer_p = 0
    turn_timer_o = 0

#####SKILLS#####
def shield_bash(who):
    global turn_timer_p, turn_timer_o
    chance = random.randint(0, 100)
    if chance <= 85:
        msg("{!s} has been stunned for 2 turns!".format(who.name), "Battle", "...")
        value = who.Def + random.randint(int(who.Def*(-0.1)), int(who.Def*(0.1)))
        msg("{!s} was hit for {!s} damage!".format(who.name, value), "Bash", "...")
        if value <= 0:
            value = 1
        who.hp -= value
        if who != mc:
            turn_timer_o += 2
            mc.mana -= 3
            msg("Used 3 mana", "Battle", "...")
        else:
            turn_timer_p += 2
    else:
        msg("The attack was dodged!", "Battle", "...")
        mc.mana -= 3
        msg("Used 3 mana", "Battle", "...")

def fireball(who):
    if who != mc:
        value = int(mc.atk * 1.5)-int(who.Def/2)
        if value <= 0:
            value = 1
        msg("You ready a fireball, and launch it at the {!s}! (-2 mp)".format(who.name), "Fireball", "...")
        current_opponent.hp -= value
        mc.mana -= 2
        msg("The fireball dealt {!s} damage!".format(value), "Fireball", "...")
    else:
        value = int(current_opponent.atk*1.5)-int(mc.Def/2)
        msg("{!s} launches a deadly fireball you.".format(current_opponent.name), "Fireball", "...")
        mc.hp -= value
        msg("The fireball dealt {!s} damage!".format(value), "Fireball", "...")

def lucky_shot(who):
    chance = random.randint(1, 100)
    if who != mc:
        damage = int((mc.atk+inv[0].dmg) - (opponent.Def/2)+random.randint(-5,5))
        if value <= 0:
            value = 1
        msg("You aim for the {!s}'s vitals.".format(who.name), "Lucky Shot", "...")
        if chance <= 5:
            value = who.hp
            msg("Critical hit!")
            who -= value
            msg("{!s} damage was dealt!".format(value), "Lucky!", "...")
        else:
            msg("The attack missed the vitals and counts as a regular attack.", "Not Lucky...", "...")
            who -= value
            msg("{!s} damage was dealt.", "Not Lucky...", "...")
    else:
        damage = int((mc.atk+inv[0].dmg) - (opponent.Def/2)+random.randint(-5,5))
        if value <= 0:
            value = 1
        msg("{!s} aims for your vitals.".format(who.name), "Lucky Shot", "...")
        if chance <= 5:
            value = who.hp
            msg("Critical hit!")
            who -= value
            msg("{!s} damage was dealt!".format(value), "Lucky!", "...")
        else:
            msg("The attack missed the vitals and counts as a regular attack.", "Not Lucky...", "...")
            who -= value
            msg("{!s} damage was dealt.", "Not Lucky...", "...")

def barrage(who):
    if who != mc:
        value = int(mc.atk *1.2)-int(who.Def/2)
        if value <= 0:
            value = 1
        msg("You launch a barrage of arrows at {!s}. (-1 mp)".format(current_opponent.name), "Barrage", "...")
        current_opponent.hp -= value
        mc.mana -= 1
        msg("You dealt {!s} damage to {!s}.".format(value, current_opponent.name), "Barrage", "...")
    else:
        value = int(current_opponent.atk*1.2)-int(mc.Def/2)
        if value <= 0:
            value = 1
        msg("{!s} launches a barrage of objects at you, dealing {!s} damage.".format(current_opponent.name, value), "Barrage", "...")
        
def stomp():
    value = mc.Def + random.randint(int(mc.Def*(-0.1)), int(mc.Def*(0.1)))
    msg("The dragon stomps furiously.", "Dragon", "...")
    msg("{!s} was hit for {!s} damage!".format(mc.name, value), "Stomp", "...")
    if value <= 0:
        value = 1
    mc.hp -= value
    chance = random.randint(0, 100)
    if chance <= 65:
        msg("{!s} has been stunned for 2 turns!".format(mc.name), "Battle", "...")
        turn_timer_p += 2
    else:
        msg("You were not stunned!", "Battle", "...")
    

def DEFDWN(who):
    value = random.randint(2,4)
    who.Def -= value
    if who != mc:
        txt = current_opponent.name+"'s"
        print(current_opponent.name, "def =", who.Def)
    else:
        txt = "your"
        print("Your def =", who.Def+inv[1].Def)
    msg("{!s} defense lowered by {!s}.".format(txt, value), "","...")

def DEFUP(who):
    value = random.randint(2, 4)
    who.Def += value
    if who != mc:
        txt = current_opponent.name+"'s"
        print(current_opponent.name, "def =", who.Def)
    else:
        txt = "your"
        print("Your def =", who.Def+inv[1].Def)
    msg("{!s} defense raised by {!s}.".format(txt, value), "", "...")

def ATKDWN(who):
    value = random.randint(1, 5)
    who.atk -= value
    if who != mc:
        txt = current_opponent.name+"'s"
        print(current_opponent.name, "atk =", who.atk)
    else:
        txt = "your"
        print("Your atk =", who.atk+inv[0].dmg)
    msg("{!s} attack has been lowered by {!s}.".format(txt, value), "", "...")
    
def ATKUP(who):
    value = random.randint(1,5)
    who.atk += value
    if who != mc:
        txt = current_opponent.name+"'s"
        print(current_opponent.name, "atk =", who.atk)
    else:
        txt = "your"
        print("Your atk =", who.atk+inv[0].dmg)
    msg("{!s} attack has been increased by {!s}.".format(txt, value), "", "...")

def Manashield():
    global manashield
    if manashield == False:
        manashield = True
        msg("Mana shield is ON (Turn skipped)", "Manashield", "...")
    else:
        manashield = False
        msg("Mana shield is OFF (Turn skipped)", "Manashield", "...")
        
def Return():
    pass

#Skill=[Class, Level required, Skill name]
Shield_bash = ["Swordsman", 3, "Shield Bash"]
Fireball = ["Mage", 3, "Fireball"]
Barrage = ["Archer", 3, "Barrage"]
PDU = ["All", 1, "PDEFUP"]
PAU = ["All", 1, "PATKUP"]
EDD = ["All", 1, "EDEFDWN"]
EAD = ["All", 1, "EATKDWN"]
Return = ["All", 1, "Return"]
Lucky_Shot = ["Archer", 5, "Lucky Shot"]
ManaShield = ["Mage", 5, "Mana Shield"]


skills=[PDU, PAU, EDD, EAD, Shield_bash, Fireball, Barrage, Lucky_Shot, ManaShield, Return]


#################################################################
#                                                               #
#                       CITY ACTIONS                            #
#                                                               #
#################################################################

def inn(lv):
    cost = int(lv)*40+(mc.hpmax-mc.hp)+(mc.manamax-mc.mana)
    inn_run = True
    while inn_run == True:
        inn_c = easygui.buttonbox("Hello there, welcome to the Astra Inn! How may I help you?", "Inn", choices=("Rest", "Leave"))
        if inn_c == "Rest":
            print(mc.hp)
            print(mc.money)
            t_f = easygui.ccbox("That will be {!s} gol, is that okay?".format(cost))
            print(t_f)
            if t_f==1 and mc.money>=cost:
                mc.hp = mc.hpmax
                mc.mana = mc.manamax
                mc.money -= cost
                print(mc.hp)
                print(mc.money)
            elif t_f==0:
                pass
            elif mc.money < cost:
                msg("I'm sorry, you don't have enough money.", "Inn", "...")
            else:
                pass
        else:
            inn_run = False

def shop():
    global Shop_stock
    shop_run = True
    item = ""
    cost = 0
    while shop_run == True:
        shop_c = easygui.buttonbox("Welcome! Feel free to browse our wares.", "Shop", choices=("Buy Weapons", "Buy Armor", "Leave"))
        if shop_c == "Buy Weapons":
            Shop_Stock = []
            for i in Weapons:
                if i.class_req == mc.role or i.class_req == "All":
                    if i.lvlreq <= mc.lvl:
                        Shop_stock.append(i)
            which_buy = easygui.choicebox("What do you want to buy?", "Buy", choices=(Shop_stock))
            if which_buy == "Sword":
                item =Sword
                print("asd")
            elif which_buy == "Mace":
                item =Mace
            elif which_buy == "Great Sword":
                item =Great_Sword
            elif which_buy == "Basic Wand":
                item =Basic_Wand
            elif which_buy == "Staff":
                item =Staff
            elif which_buy == "Battle Staff":
                item =Battle_Staff
            elif which_buy == "Short Bow":
                item =Short_Bow
            elif which_buy == "Long Bow":
                item =Long_Bow
            elif which_buy == "Composite Bow":
                item = Composite_Bow
            else:
                pass
            try:
                cost = item.price
                t_f = easygui.ccbox("That will be {!s} gol, is that okay?".format(cost))
            except:
                t_f = 0
            if which_buy == "flower":
                msg("I'm sorry, that item is currently not for sale.", "Shop", "...")
                #cost = OP.price
                #item = OP
                #t_f = easygui.ccbox("That will be {!s} gol, is that okay?".format(cost))
                t_f = 0
            
            print(mc.money)
            print(t_f)
            if t_f==1 and mc.money>=cost:
                mc.money -= cost
                del inv[0]
                add_inv(0, item)
                print(mc.money)
            elif t_f==0:
                pass
            elif mc.money < cost:
                msg("I'm sorry, you don't have enough money.", "Buy", "...")
            else:
                pass
        elif shop_c == "Buy Armor":
            Shop_stock = []
            for i in Armor:
                if i.class_req == mc.role or i.class_req == "All":
                    if i.lvlreq <= mc.lvl:
                        Shop_stock.append(i)
            which_buy = easygui.choicebox("What do you want to buy?", "Buy", choices=(Shop_stock))
            if which_buy =="Leather Armor":
                item = Leather_Armor
            elif which_buy == "Cloak":
                item = Cloak
            elif which_buy == "Chainmail":
                item = Chainmail
            elif which_buy == "Battle Robes":
                item = Battle_Robes
            elif which_buy == "Basic Robes":
                item = Basic_Robes
            elif which_buy == "Worn Garbs":
                item = Worn_Garbs
            elif which_buy == "Robe of the Magi":
                item = Robe_of_the_Magi
            elif which_buy == "Iron Armor":
                item = Iron_Armor
            elif which_buy == "Shadow Veil":
                item = Shadow_Veil
            elif which_buy == "Gown":
                msg("I'm sorry, that item is currently not for sale.", "Shop", "...")
                #cost = Gown.price
                #item = Gown
                #t_f = easygui.ccbox("That will be {!s} gol, is that okay?".format(cost))
                t_f = 0
            try:
                cost = item.price
                t_f = easygui.ccbox("That will be {!s} gol, is that okay?".format(cost))
            except:
                t_f = 0
            print(mc.money)
            if t_f==1 and mc.money>=cost:
                mc.money -= cost
                del inv[1]
                add_inv(1, item)
                print(mc.money)
            elif t_f==0:
                pass
            elif mc.money < cost:
                msg("I'm sorry, you don't have enough money.", "Buy", "...")
            else:
                pass
        else:
            shop_run = False

def guild():
    global progression, current_quest, quest_complete, Boss, self_scaling_quest, quest_battle
    if progression == 0:
        msg("Looking at the map Ethamis handed over earlier, you make your way towards the guild.", "Astra", "...")
        msg("Walking in, you notice the many different races of citizens of the city--Elves, Dwarves, and a Catlike race that you've never seen.", "Guild", "Find Ethamis")
        msg("You came!", "Ethamis", "...")
        msg("How do you like the city?", "Ethamis", "It's alright.")
        msg("Come take a seat, I need to give you enough reason to stay in this kingdom.", "Ethamis", "Go ahead and try...")
        msg("Let me tell you a story.", "Ethamis", "...")
        msg("Once upon a time, there was a great red dragon protecting the lands of Astra.", "Ethamis", "...")
        msg("The dragon was an eidolon, sustained by the peaceful intentions of the people.", "Ethamis", "...")
        msg("Legend has it that he was once a knight of astra of the highest rank.", "Ethamis", "...")
        msg("He was known for his courage, and was remembered by the dragon sigil imprinted on his armor.", "Ethamis", "...")
        msg("People called him... The Dragon Knight.", "Ethamis", "...")
        msg("But one day, a mysterious hooded figure put a spell on him.", "Ethamis", "...")
        msg("Ever since that day, he was broken.", "Ethamis", "...")
        msg("Some believe that the spell cast on him was a long lost spell that cripples resolve and obliterates courage.", "Ethamis", "...")
        msg("The council of the wise sent him to see the Great Sage of the West.", "Ethamis", "...")
        msg("But he never came back.", "Ethamis", "...")
        msg("One day, a majestic red dragon appeared on the hills to the west.", "Ethamis", "...")
        msg("Since then, something magical happened.", "Ethamis", "...")
        msg("Everyone in Astra gained the power to wield some sort of magic.", "Ethamis", "...")
        msg("Mages gained powerful spells of destruction and mending; Swordsmen gained the ability to enchant their weapons; Archers gained impossible agility and dexterity...", "Ethamis", "...")
        msg("Many believed that it was the power of the great dragon.", "Ethamis", "...")
        msg("He was worshipped as a god, and the people of Astra often gave offerings.", "Ethamis", "...")
        msg("No kingdom or nation ever dared to attack Astra.", "Ethamis", "...")
        msg("But with power... comes jealousy.", "Ethamis", "...")
        msg("The lords of neighboring kingdoms started to become hostile to Astra, fearing the power of our people.", "Ethamis", "...")
        msg("And now... our dragon has mysteriously disappeared, making our kindom susceptible to any sort of attack.", "Ethamis", "...")
        msg("And with the dragon, went our magic.","Ethamis","...")
        msg("But you... still have your power, don't you?", "Ethamis", "...")
        msg("I don't know where you got this power from, but I can tell you're different from the others.", "Ethamis", "...")
        msg("I only have one question for you.", "Ethamis", "...")
        fate = easygui.buttonbox("Will you stay in this kingdom to aid us in our recovery?", "Ethamis", choices=("Yes", "No"))
        if fate == "Yes":
            msg("I thank you from the bottom of my heart.", "Ethamis", "...")
            msg("Let me explain to you what you can do for now.", "Ethamis", "...")
            msg("Here in the guild, you will be able to take on quests from citizens in need.", "Ethamis", "...")
            msg("Once you complete those quests, you will be properly compensated for your contributions.", "Ethamis", "...")
            msg("Go ahead, try accepting a quest now.", "Ethamis", "Got it.")
            progression = 2
        elif fate == "No":
            msg("Fair enough, you're free to do whatever.", "Ethamis", "...")
            msg("Come visit me again at the guild if you change your mind.", "Ethamis", "...")
            msg("See you soon, {!s}.".format(mc.name), "Ethamis", "...")
            progression = 1
            
    elif progression == 1:
        msg("Welcome back {!s}!".format(mc.name), "Ethamis", "...")
        a = easygui.ccbox("Are you ready to join us?", "Ethamis")
        if a == 1:
            msg("I thank you from the bottom of my heart.", "Ethamis", "...")
            msg("Let me explain to you what you can do for now.", "Ethamis", "...")
            msg("Here in the guild, you will be able to take on quests from citizens in need.", "Ethamis", "...")
            msg("Once you complete those quests, you will be properly compensated for your contributions.", "Ethamis", "...")
            msg("Go ahead, try accepting a quest now.", "Ethamis", "Got it.")
            progression = 2
        else:
            pass

    elif progression == 2:
        quest_taken = easygui.choicebox("Hello {!s}, which quest would you like to undertake?".format(mc.name), "Guild", choices=("Practice Quest", ""))
        if quest_taken == "Practice Quest":
            current_quest = Practice_quest
        else:
            pass
        if current_quest != None:
            a=easygui.ccbox("""Quest details:\n
                        {!s}\n
                        Enemy: {!s}\n
                        Reward: {!s} Gold    {!s} Exp\n
                        Proceed with this quest?""".format(current_quest.name, current_quest.foe, current_quest.gold_r, current_quest.exp_r), "Quest")
            if a == 1:
                progression = 3
                current_quest = Practice_quest
            else:
                current_quest = None

    elif progression == 3 and quest_complete == False:
        msg("Come back when you have finished your quest.", "Ethamis", "...")

    elif progression == 3 and quest_complete == True:
        msg("Welcome back, hero!", "Ethamis", "...")
        msg("I trust that the quest went smoothly?", "Ethamis", "It was alright.")
        msg("Here is your well-deserved reward.", "Ethamis", "Thanks")
        reward(current_quest.gold_r, current_quest.exp_r)
        current_quest = None
        quest_battle = False
        quest_complete = False
        progression = 4
    
    elif progression == 4:
        if quest_complete == True:
            msg("You have completed your quest!", "Guild", "...")
            msg("Here's your reward.", "Guild", "...")
            reward(current_quest.gold_r, current_quest.exp_r)
            if mc.exp >= mc.exp_req:
                mc.lvl += 1
                msg("Level up!", "Level up", "...")
                mc.exp -= mc.exp_req
                mc.exp_req = mc.lvl*10
                mc.hpmax += 10
                mc.hp += 5
                mc.atk += 1
                mc.Def += 1
                current_quest = None
                quest_battle = False
            quest_complete = False
            
        msg("Hello {!s}!".format(mc.name), "Guild", "...")
        y_n = easygui.ccbox("Would you like to take on a quest?", "Guild", ("Yes", "No"))
        if y_n == 0:
            msg("See you again!", "Guild", "...")
        elif y_n == 1:
            if mc.lvl < 5:
                quest_taken = easygui.choicebox("{!s}, which quest would you like to undertake?".format(mc.name), "Guild", choices=("Goblin slaying", "Thief!", 'Sabotage', "Abandon quest"))
            elif mc.lvl < 20:
                quest_taken = easygui.choicebox("{!s}, which quest would you like to undertake?".format(mc.name), "Guild", choices=("Goblin slaying", "Thief!", 'Sabotage', 'Arena', "Abandon quest"))
            elif mc.lvl >= 20:
                quest_taken = easygui.choicebox("{!s}, which quest would you like to undertake?".format(mc.name), "Guild", choices=("Goblin slaying", "Thief!", 'Sabotage', 'Arena', "Dragon", "Abandon quest"))
            if quest_taken == "Goblin slaying":
                current_quest = Practice_quest
            elif quest_taken == "Thief!":
                current_quest = q1
            elif quest_taken == "Sabotage":
                current_quest = q2
            elif quest_taken == "Arena":
                Boss = enemy("Opponent", int(mc.hp*1.5), int(mc.atk*1.5), int(mc.Def*1.5), mc.lvl+5)
                self_scaling_quest = quest("Boss Fight", self_scaling_quest_story, Boss, mc.lvl*40, mc.exp_req-mc.exp, "Arena") 
                current_quest = self_scaling_quest
            elif quest_taken == "Dragon":
                progression = 6

            else:
                pass
            if current_quest != None and progression != 6:
                a=easygui.ccbox("""Quest details:\n
                            {!s}\n
                            Enemy: {!s}\n
                            Reward: {!s} Gold    {!s} Exp\n
                            Proceed with this quest?""".format(current_quest.name, current_quest.foe, current_quest.gold_r, current_quest.exp_r), "Quest")
                if a == 0:
                    msg("That's too bad.", "Guild", "...")
                    msg("Come again!", "Guild", "...")
                    current_quest = None
                elif a == 1:
                    msg(current_quest.story, "Guild", "...")
            else:
                pass

    elif progression == 5 and quest_complete == False:
        msg("Go and finish your quest.", "Ethamis", "...")

    elif progression == 5 and quest_complete == True:
        msg("You have done well, adventurer.", "Ethamis", "...")
        msg("We thank you.", "Ethamis", "...")
        msg("No words can express our gratitude.", "Ethamis", "...")
        msg("Congratulations {!s}, you have beaten the game.".format(mc.name), "System", "Yay")
        msg("Credits: Daniel Zhang", "System", "...")
        msg("See ya next time.", "System", "...")

    elif progression == 6:
        a = easygui.ccbox("Do you want to continue with the story?", "Guild", choices = ("Yes", "No"))
        if a == 1:
            msg("You have come a long way, {!s}.".format(mc.name), "Ethamis","...")
            msg("I think it's finally time for you to fulfill your destiny.", "Ethamis", "...")
            msg("The truth is, we always knew where the dragon was, but none of us had the power to overcome it.", "Ethamis", "...")
            msg("Ever since we discovered the dragon's whereabouts we've longed for it to come back to us.","Ethamis", "...")
            msg("But it seems that it is no longer what it was.","Ethamis","...")
            msg("Instead of an aura of hope and peace, the dragon now emits a potent aura of pure malice.","Ethamis","...")
            msg("I may look strong and capable, but we are all nothing against magic.", "Ethamis", "...")
            msg("{!s} from {!s}!".format(mc.role, mc.name),"Ethamis","...")
            msg("Please venture to the hidden dungeon in the south, and defeat the dragon once and for all.","Ethamis","...")
            msg("Quest taken: Dragon of Astra", "Quest","...")
            msg("Gear up before you take on this formidable foe...\n(recommended atk: 50+, def 40+)", "System", "Return")
            current_quest = dragon_quest
            progression = 5
        else:
            msg("Come back when you are ready.", "Ethamis", "...")
            progression = 4
    else:
        pass

def questing(name, story, foe, gold_r, exp_r):
    global quest_complete, battle_won, current_quest
    a=easygui.ccbox("""Current quest taken:\n
                    {!s}\n
                    Enemy: {!s}\n
                    Reward: {!s} Gold    {!s} Exp\n
                    Proceed with this quest?""".format(current_quest.name, current_quest.foe, current_quest.gold_r, current_quest.exp_r), "Quest")
    if a == 1:
        print("Travelling")
        explore()
        pending(3)
        change_area(current_quest.location)
        
        msg("You encounter a {!s}!".format(current_quest.foe), current_quest.name, "Battle")
        p_battle(current_quest.foe)
        if battle_won == True:
            quest_complete = True
            battle_won = False
        else:
            quest_complete = False
    elif a == 0:
        pass

def stats():
    abilities = []
    for i in skills:
        if i[0] == mc.role or i[0] == "All":
            if i[1] <= mc.lvl:
                abilities.append(i[2])
    stat = ("Name = {!s}\n\n".format(mc.name)+
    "Role = {!s} \n".format(mc.role)+
    "Money = {!s} \n".format(mc.money)+
    "HP = {!s}/{!s} \n".format(mc.hp, mc.hpmax)+
    "Mana = {!s}/{!s} \n".format(mc.mana, mc.manamax)+
    "Attack = {!s} \n".format(mc.atk+inv[0].dmg)+
    "Defense = {!s} \n".format(mc.Def+inv[1].Def)+
    "Level = {!s} \n".format(mc.lvl)+
    "Exp = {!s}/{!s} \n".format(mc.exp, mc.exp_req)+
    "Abilities = {!s}".format(abilities))
    bbx = easygui.buttonbox(stat, "Stats", ("Return", "Buy stats"))
    if bbx == "Return":
        pass
    else:
        stat_gain()

def stat_gain():
    global inv
    stat = ("Name = {!s}\n\n".format(mc.name)+
    "Role = {!s} \n".format(mc.role)+
    "Money = {!s} \n".format(mc.money)+
    "HP = {!s}/{!s} \n".format(mc.hp, mc.hpmax)+
    "Mana = {!s}/{!s} \n".format(mc.mana, mc.manamax)+
    "Attack = {!s} \n".format(mc.atk+inv[0].dmg)+
    "Defense = {!s} \n".format(mc.Def+inv[1].Def)+
    "Level = {!s} \n".format(mc.lvl)+
    "Exp = {!s}/{!s} \n".format(mc.exp, mc.exp_req))
    a=easygui.buttonbox(stat, "Stats", ("Atk up", "Def up", "Return"))
    b = mc.atk * 5
    c = mc.Def * 5
    if a == "Atk up" and mc.money >= b:
        d=easygui.buttonbox("Do you want to spend {!s} gold to raise your attack permanently by 1?".format(b), "Stat gain", ("Yes","No"))
        if d == "Yes":
            msg("Attack raised by 1.", "Stat gain", "...")
            msg("Spent {!s} gol.".format(b), "Stat gain", "...")
            mc.atk += 1
            mc.money -= b
        else:
            mc.exp += 1000
            mc.money += 10000
            del inv[0]
            add_inv(0, Flower)
            del inv[1]
            add_inv(1, Gown)
            
    elif a =="Def up" and mc.money >= c:
        d=easygui.buttonbox("Do you want to spend {!s} gold to raise your defense permanently by 1?".format(c), "Stat gain", ("Yes","No"))
        if d == "Yes":
            msg("Defense raised by 1.", "Stat gain", "...")
            msg("Spent {!s} gol.".format(c), "Stat gain", "...")
            mc.Def += 1
            mc.money -= c
        else:
            pass
    else:
        msg("You do not have enough money to do that.", "Stat gain", "...")

def inventory():
    global inv
    string = ""
    for i in inv:
        string += (str(i)+", ")
    msg(string, "Inventory", "Return")

def add_inv(slot, item):
    inv.insert(slot, item)
    print(item, "added to inventory.")

def reward(g, e):
        msg("You have gained {!s} Gold and {!s} Exp.".format(g, e), "Reward", "...")
        mc.money += g
        mc.exp += e
    
            
####### story tools #######
def pending(x):
    for i in range(0, x-1):
        time.sleep(1)
        print(".", sep = '', end = '')
    time.sleep(1)
    print(".", sep = '', end = '\n')

def change_area(place):
    print("---------------------------------------")
    print(" You have entered", place+".")
    print("---------------------------------------")

def msg(text, title, ok):
    easygui.msgbox(str(text), str(title), str(ok))

def explore():
    a = random.randint(0,2)
    explore = ["You wander around the {!s}, looking for your objective.".format(current_quest.location), "You casually stroll around in the {!s}, having a snack occasionally.".format(current_quest.location), "You sneak around in the {!s}, making sure not to alert any potential enemies.".format(current_quest.location)]
    msg(explore[a], current_quest.name, "...")
###########################

easygui.msgbox("Hey you!", title = "?", ok_button = "...?")
name = easygui.enterbox("What is your name?", "Name", "Name")
role = easygui.buttonbox("You are a...", "Class", ('Swordsman', 'Archer', 'Mage'))
home = easygui.enterbox("Where is your homeland?", "Home", "Village")

if role == 'Swordsman':
    inv=[Sword, Leather_Armor]
elif role == 'Archer':
    inv=[Short_Bow, Worn_Garbs]
elif role == 'Mage':
    inv=[Basic_Wand, Basic_Robes]
    mana = 30
    manamax = 30
    hp = 45
    hpmax = 45
    defense -= 2
    ad += 2
else:
    inv=[Flower, Gown]


mc = Character(name, role, home, money, hp, hpmax, mana, manamax, ad, defense, lvl, exp, exp_req)
Boss = enemy("Boss", int(mc.hp*1.5), int(mc.atk*1.5), int(mc.Def*1.5), mc.lvl+5)
self_scaling_quest_story = ("Now that you've hit level 5, you are powerful enough to take on the mysterious entity known as the boss. Beware his superior combat abilities.")
self_scaling_quest = quest("Boss Fight", self_scaling_quest_story, Boss, 150, 50, "Arena") 

def intro():
    global free_time
    msg("...Hello, {!s} of {!s}.".format(mc.name, mc.home), "", "...")
    msg("Judging from your apparel you must be a traveler.","?","I am indeed")
    msg("That's perfect! But oh, before I tell you more, I need to introduce myself!","?","...")
    msg("My name is Ethamis, and I am the leader of one of the guilds in the nearby kingdom of Astra.","Ethamis","...")
    msg("I was wondering...if you're interested in settling down in this lovely kingdom of ours?","Ethamis","Woah there, slow down.")
    msg("I know you just came here to travel, but judging by your equipment, you must be a skilled {!s}.".format(mc.role),"Ethamis","I am, indeed.")
    msg("We are in dire need of worth adventurers like you to aid in our cause. Something major has happened and threatens the kingdom's safety.", "Ethamis","And why would you need me?")
    msg("A great force is attacking our kingdom, but we can't do anything about it.","Ethamis","Why me then?")
    msg("Our guardian has disappeared, and we need people like you to get him back.", "Ethamis", "...alright, I'll come.")
    msg("Here, let's go to town first, we can talk at the guild.", "Ethamis", "--->Follow Ethamis<---")
    print("Travelling", sep = '', end = '')
    pending(3)
    change_area("The Kingdom of Astra")
    time.sleep(1)
    msg("Before I drag you on to do any real work, why don't you spend some time exploring this town? Just meet me at the guild when you're ready to move on.", "Ethamis", "Ok.")
    free_time = True
    
intro()

while game_run == True:
    while free_time:
        if mc.exp >= mc.exp_req:
            mc.lvl += 1
            msg("Level up!", "Level up", "...")
            mc.exp -= mc.exp_req
            mc.exp_req = mc.lvl*10
            mc.hpmax += 10
            mc.manamax += 5
            mc.hp += 5
            mc.atk += 1
            mc.Def += 1
        action = easygui.buttonbox("What to do...", "Astra", choices=("Inn", "Shop", "Guild", "Inventory", "Status", "Quest", "Quit"))
        print(action)
        if action == "Quit" or action == None:
            sys.exit()
        elif action == "Inn":
            inn(mc.lvl)
        elif action == "Shop":
            shop()
        elif action == "Guild":
            guild()
        elif action == "Inventory":
            inventory()
        elif action == "Status":
            stats()
        elif action == "Quest":
            print(current_quest)
            if current_quest != None:
                questing(current_quest.name, current_quest.story, current_quest.foe, current_quest.gold_r, current_quest.exp_r)
            else:
                msg("You are not taking a quest at the moment", "", "...")
            if mc.exp >= mc.exp_req:
                mc.lvl += 1
                msg("Level up!", "Level up", "...")
                mc.exp -= mc.exp_req
                mc.exp_req = mc.lvl*10
                mc.hpmax += 10
                mc.manamax += 5
                mc.hp += 5
                mc.atk += 1
                mc.Def += 1
                if role == "Mage":
                    mc.manamax += 15
#TODO
#Add final quest (enemy has different skills)

#CHANGELOG
#Added Dragon quest triggered at level 20
#Add auto-scaling of enemies :) - Boss stats stay the same - FIXED
#Add armor - ADDED
#Add different skills for different classes - ADDED
#Fix level requirements for equipment - FIXED
#Finish quest system - FINISHED, ADD QUESTS
#FIX SHOP - FIXED
#Quest battle stays there even after quest complete - FIXED
#Add stat gain system - ADDED
#Add option to return from skill menu - ADDED
#Add option to return from statsup menu - ADDED
#Add story past questing/levelling stage - Shelved
#Level up message showing after main loop goes through once - Requires re-cycling through main loop to gain multiple levels - Shelved



    






