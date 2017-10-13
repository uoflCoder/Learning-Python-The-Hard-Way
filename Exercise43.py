#Exercise 43

#The scence is an object
class Scene(object):

    #Scene has a enter function
    def enter(self):
        pass

#Game engine object is an object
class Engine(object):

    #Game engine has an __init__ function
    #that has a scene_map associated with it
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

#Death is a scene
class Death(Scene):

    def enter(self):
        pass

#LaserWeaponArmory is a scene
class LaserWeaponArmory(Scene):

    def enter(self):
        pass

#TheBridge is a scene
class TheBridge(Scene):

    def enter(self):
        pass

#EscapePod is a scene
class EscapePod(Scene):

    def enter(self):
        pass

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
        pass

#a_map is a Map instance with the start_scene
#value 'central_corridor'
a_map = Map('central_corridor')

#a_game has is a Engine instance
#with an Map instance called a_map
a_game = Engine(a_map)

#call the play function in the Engine instance
a_game.play()
