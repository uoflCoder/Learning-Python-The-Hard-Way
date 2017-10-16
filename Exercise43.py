#Exercise 43

#The scence is an object
class Scene(object):

    #Scene has a enter function
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)
#Game engine object is an object
class Engine(object):

    #Game engine has an __init__ function
    #that has a scene_map associated with it
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #Got an error don't know why


#Death is a scene
class Death(Scene):

    quips = ["You died.",
            "I wouldn't be happy if I were you.",
            "Come on I thought you were better than this!",
            "You lost hard.",
            "You're worse at this than your Dad's jokes."]

    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):


    def enter(self):
        print("""The Gothons of Planet Percal #25 have invaded your
                        ship and destoryed your entire crew. You are the last
                        surviving  member and your last mission is to get the
                        neutron destruct bomb from the Weapons Armory, put it
                        in the bridge, and blow the ship up after getting
                        into an escape pod. You're running down the central
                        corridor to the Weapons Armory when an Gothon jumps
                        out, red scaly skin, dark grimy teeth, and an evil
                        clown costume flowing around his hate filled body.
                        He's blocking the door to the Armory and about to pull
                        a weapon to blast you""")

        print("What do you Do?")

        action = input(">")

        if action == "shoot!":

            print("""Quick on the draw you yank out your blaster and fire
                     it at the Gothon. His clown costume is flowing moving around his body, which
                     throws off your aim. Your laser hits his costume but misses him entirely. This
                     completely ruins his brand new costume his mother bought him, which makes him
                     fly into an insane range and blast you repeatedly in the face until you are
                     dead. Then he eats you.""")
            return 'death'

        elif action == "dodge!":
            print("""Like a world class boxer you dodge, weave, slip and slide
                     right as the Gothon's blaster cranks a laser past your head.
                     In the middle of your artfull dodge your foot slips and you
                     bang your head on the metal wall and pass out. You wake up
                     shortly after only to die as the Gothom stomps on your head
                     and eats you""")
            return 'death'

        elif action == 'tell a joke':

            print("""Lucky for you they made you learn
                     Gothon insults in the academy. You
                     tell the one Gothon joke you know:
                     'sdlkj wikje shw, gueb, owow, bomom.'
                     The Gothon stops, tries not to laugh,
                     then bursts out laughing and can't move.
                     While he's laughing you run up and shoot
                     him square in the head putting him down,
                     then jump through the Weapon Armory door.""")
            return 'laser_weapon_armory'

        else:

            print("DOES NOT COMPUTE!")
            return 'central_corridor'

#LaserWeaponArmory is a scene
class LaserWeaponArmory(Scene):

    def enter(self):
        print("""You do a dive roll into the Weapon Armory,
                 crouch and scan the room for more Gothons
                 that might be hiding. It's dead quiet, too quiet.
                 You stand up and run to the far side of the room
                 and find the neutron in its container. There's a
                 keypad lock on the box and you need the code to
                 get the bomb out. If you get the code wrong 10 times
                 then the lock closes forever and you can't get the bomb.
                 The code is 3 digits""")

        code = str(randint(1,9)) + str(randint(1,9)) + str(randint(1,9))
        guess = input("[keypad]>")
        guesses = 0
        while guess != code and guesses < 9:
            print("BZZZEDDD!!!!")
            guesses += 1
            guess = input("[keypad]>")

        if guess == code:
            print("""The container clicks open and the seal breaks,
                     letting gas out. You grab the neutron bomb and run
                     as fast as you can to the bridge where you must place
                     it in the right spot""")

            return 'the_bridge'




#TheBridge is a scene
class TheBridge(Scene):

    def enter(self):
        print("""You burst onto the Bridge with the neutron
                 destruct bomb under your arm and surprise 5 Gothons
                 who are trying to take control of the ship. Each
                 one of them has an even uglier clown costume than
                 the last. They haven't pulled their weapons out yet,
                 as they see the active bomb under your arm and don't
                 want to set it off.""")

        print("What do you do?")
        action = input(">")

        if action == "throw the bomb":
            print("""In a panic you throw the bomb at the group of
                     Gothons and make a leap for the door. Right as
                     you drop it a Gothon shoots you right in the back
                     killing you. As you die you see another Gothon
                     desperately trying to disarm the bomb. You die knowing
                     they will probably blow up when it goes off.""")

        elif action == "slowly place the bomb":
            print("""You point your blaster at the bomb under your arm
                     and the Gothons put their hands up and start to sweat.
                     You inch backward to the door, open it, and then
                     carefully place the bomb on the floor, pointing
                     your blaster at it. You then jump back through the door,
                     punch the close button and blast the lock so the Gothon's
                     can't get out. Now that the bomb is placed you run to the
                     escape pod to get off this ship.""")

            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


#EscapePod is a scene
class EscapePod(Scene):

    def enter(self):
        print("""You rush through the ship desparately trying to
                 make it to the escape pod before the whole ship
                 exploedes. It seems like hardly any Gothons are
                 on the ship, so your run is clear of interference.
                 You get to the chamber with the escape pods, and
                 now need to pick one to take. Some of them could
                 be damaged but you don't have time to look.
                 There's 5 pods which one do you take""")

        good_pod = randint(1,5)
        guess = input("[pod#]")

        if guess != str(good_pod):
            print("""You jump into pod {guess} and hit the eject button.
                     The pod escapes out into the void of space, then
                     implodes as the hull ruptures, crushing your body into
                     jam jelly""")
            return 'death'

        else:
            print("""You jump into pod {guess} and hit the eject button.
                     The pod easily slides out into space heading planet below.
                     As it flies to the planet, you look back and see your ship
                     implode then explode like a bright star, taking out the Gothon
                     ship at the same time. You won!""")
            return 'finished'


#Map is an object
class Map(object):

    #Map has an init function that has a start scene
    def __init__(self, start_scene):
        pass

    #Map has a next scene
    def next_scene(self, scene_name):
        pass

    #Map has an opening scene
    def opening_scene(self):

        CenCor = CentralCorridor()
        CenCor.enter()

#a_map is a Map instance with the start_scene
#value 'central_corridor'
a_map = Map('central_corridor')

#a_game has is a Engine instance
#with an Map instance called a_map
a_game = Engine(a_map)

#call the play function in the Engine instance
a_game.play()
