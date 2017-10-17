#Exercise 45
from textwrap import dedent
class Scene(object):

    def __init__(self):

        print("This scene is under construction")
        print("Come back another time")

class UpsideDown(Scene):

    def __init__(self):
        pass

    def enter(self):
        print(dedent("""You awake in a dark eerie forest with slime all over your chest
                        it's difficult to breath and you are gasping for air. All of a sudden
                        you see it. The demagorgon. What do you do?"""))

        response = input(">")

        if response == "run":
            print("""You escape by the skin of your kneck the monster shrieks in anger it follows you as
                     you enter an old abandoned house to hide""")

            return 'CreepyHouse'

        elif response == "fight":
            print("""You just became the demagorgon's dinner mate.""")

            return 'Death'

        else:
            return 'Death'


class CreepyHouse(Scene):

    def __init__(self):
        pass

    def enter(self):
        print(dedent("""You enter the door and find a pistol and a lighter what do you do?"""))

        response = input(">")

        if response == "burn":
            print("""You burn to death but take the demagorgon with you""")

            return 'Death'

        elif response == "shoot":
            print("""You hurt the demagorgon and escape.""")

            return 'End'

        else:
            return 'Death'


class End(Scene):

    def __init__(self):
        pass

    def enter(self):
        print(dedent("""You won"""))


        exit(0)

class Death(Scene):

    def __init__(self):
        pass

    def enter(self):
        print("Bruh you dead")
        exit(0)

class Engine(object):

    scenes = {'UpsideDown':UpsideDown(),
              'CreepyHouse':CreepyHouse(),
              'End':End(),
              'Death':Death()}

    def __init__(self, opening_scene):

        self.open_scene(opening_scene)

    def open_scene(self, scene_name):

        self.current_scene = self.scenes.get(scene_name)

        while self.current_scene != 'End' or self.current_scene != 'Death':

            self.next_scene = self.current_scene.enter()
            self.current_scene = self.scenes.get(self.next_scene)
            input(">....")

        self.current_scene.enter()

game = Engine('UpsideDown')
