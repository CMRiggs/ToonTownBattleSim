class Battle:
    def __init__(self, toons, cogs):
        """Toons and Cogs are both arrays of up to 4 toons/cogs objects.
        Index 0 represents the far right position"""
        self.toons = toons
        self.cogs = cogs