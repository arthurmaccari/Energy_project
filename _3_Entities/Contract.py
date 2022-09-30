
#powCon: "BT<=36kVa", "BT>36kVa", "HTA"

class Contract():
    """
    A class to create an energy contract.
    """

    def __init__(self, powConSub, type, tariffOption):
        """
        :type powConSub:    string
        :content powConSub: The power connection subscription.
        """
        
        self.powConSub = powConSub
        self.type = type
        self.tariffOption = tariffOption