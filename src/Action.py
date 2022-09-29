class Action:
    def __init__(self, performer, receiver, action):
        # The person performing the action (toon or cog)
        self.performer = performer

        # The person receiving the action (toon or cog)
        self.receiver = receiver

        # The action (gag if toon, attack if cog)
        self.action = action