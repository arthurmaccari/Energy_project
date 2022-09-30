
from Parsers import parse_yml_file


# TURPE related functions

def get_turpe_CS_c_coefficients(contract, params):
    return params["turpe"][contract.tariffOption]["c"]

def compute_TURPE(household):
    """
    Computes the TURPE paid by the household on a yearly basis.

    :type household:        Household
    :content household:     The considered household.
    """

    params_FR = parse_yml_file("_1_Params/Params_FR.yml")

    # The CG part
    cg = params_FR["turpe"]["CG"][household.contract.type]

    # The CC part
    cc = params_FR["turpe"]["CC"]
    
    # The CS part
    b = params_FR["turpe"]["CS"][household.contract.tariffOption]["b"]
    cs = b*household.contract.powConSub
    c = get_turpe_CS_c_coefficients(household.contract, params_FR)
    length = len(c)
    for i in range(length):
        cs += c[i]*household.powCon[i]

    return cg+cc+cs

# CISPE related functions
