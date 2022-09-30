
import _4_Utils.France.Taxes as taxes_fr


class Household():
    """
    A class to create a household.
    """

    def __init__(self, nbOc, rev, elecEqmt, contract):
        """
        :type nbOc:         int
        :content nbOc:      The number of people in the household.

        :type rev:          int
        :content rev:       The yearly revenue of the household.

        :type elecEqmt:     dict
        :content elecEqmt:  A dictionary of dummies to account for the electric equipments
                            in the household.
        
        :type contract:     Contract
        :content contract:  The electricity contract the household susbscribed to.
        """

        self.nbOc = nbOc
        self.rev = rev
        self.elecEqmt = elecEqmt
        self.contract = contract

        self.powCon = [0,0,0,0] # HPH, HCH, HPB, HCB


class Household_FR(Household):
    """
    A class to create a French household.
    """

    def __init__(self, nbOc, rev, elecEqmt, contract):
        """
        See Household class for a description of the variables.
        """
        super().__init__(nbOc, rev, elecEqmt, contract)
    
    def compute_TURPE(self):
        """
        Computes the TURPE paid by the household on a yearly basis.
        """
        
        self.turpe = taxes_fr.compute_TURPE(self)

