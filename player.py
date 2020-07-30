import random

class Player:
    """
    Basic player elements including geospace and moveability.
    """

    def __init__(self):
        super().__init__()
        # Player variables.
        self.geospace = [0, 0] # X, Y --- A 2D plane of position. Min: -50, Max: 50 for both planes.

        # Keep track if certain movements are possible (based on geospace).
        self.forward = True
        self.backward = True
        self.leftward = True
        self.rightward = True

        # If the player traveled at all.
        self.moved = False

    def assess_geospace(self, direction, paces):
        """
        Assess geospatial location of the player, assess if movements are valid, and move the player accordingly.
        """

        # Forward movement.
        if paces > 0 and direction == 1:
            if not self.forward:
                print("You cannot move forward, for there is a steep mountain there.")
                self.moved = False
                return self.moved
            else:
                print(f'You move {paces} steps ahead.')
                self.backward = True
                self.moved = True
        # Backward movement.
        elif paces < 0 and direction == 1:
            if not self.backward:
                print("You cannot move backward, for there is a river there.")
                self.moved = False
                return self.moved
            else:
                print(f'You move {paces/-1} steps back.')
                self.forward = True
                self.moved = True
        # Leftward movement.
        elif paces < 0 and direction == 0:
            if not self.leftward:
                print("You cannot move leftward, for there is a ravine there.")
                self.moved = False
                return self.moved
            else:
                print(f'You move {paces/-1} steps to the left.')
                self.rightward = True
                self.moved = True
        # Rightward movement.
        elif paces > 0 and direction == 0:
            if not self.rightward:
                print("You cannot move rightward, for you lack the required DLC (it's only $5 bucks).")
                self.moved = False
                return self.moved
            else:
                print(f'You move {paces} steps to the right.')
                self.leftward = True
                self.moved = True

        # Add the pace (movement) to the player's geolocation.
        self.geospace[direction] += paces

        # Assess if the player has reached the boundaries.        
        # Y Direction (Forward).
        if self.geospace[1] >= 50:
            self.geospace[1] = 50
            print("You reach a steep mountain and can no longer move towards this direction.")
            self.forward = False

        # Y Direction (Backward).
        if self.geospace[1] <= -50:
            self.geospace[1] = -50
            print("There is a large river here ahead, and you cannot swim.")
            self.backward = False
        
        # X Direction (Leftward).
        if self.geospace[0] <= -50:
            self.geospace[0] = -50
            print("You walk up to a ravine and can no longer move towards this direction.")
            self.rightward = False
        
        # X Direction (Rightward).
        if self.geospace[0] >= 50:
            self.geospace[0] = 50
            print("There is a cave ahead, but you lack the necessary DLC to access it.")
            self.leftward = False

        return self.moved