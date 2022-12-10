class candidate():
    def __init__(self, name):
        """
        Create a candidate.
        :param name: Name of the candidate.
        """
        self.name = name
        self.votes = 0

    def addvote(self):
        """
        Increases the votes of a candidate by 1.
        """
        self.votes += 1

    def votecount(self) -> int:
        """
        Get the amount of votes allocated to a given candidate.
        :return: The votes allocated to the candidate.
        """
        return self.votes

    def getname(self) -> str:
        """
        Get the name of a given candidate.
        :return: The name of the candidate.
        """
        return self.name

    def resetvotes(self):
        """
        Resets the votes allocated to a given candidate back to zero.
        """
        self.votes = 0

