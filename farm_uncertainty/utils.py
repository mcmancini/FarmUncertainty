# -*- coding: utf-8 -*-
# Copyright (c) 2023 LEEP - University of Exeter (UK)
# Mattia C. Mancini (m.c.mancini@exeter.ac.uk),
# Amy Binner (a.r.binner@exeter.ac.uk)
# February 2024

"""
Utility functions for the agent-based model to investigate
farmer uptake of agri-environmental schemes under uncertainty
(climate and prices) based on different payment mechanisms.
=============================================================

Functions defined here
----------------------

generate_farmers(num_farmers)
    generates "num_farmers" instances of the class Farmer
"""

import uuid
from farm_uncertainty.farmers import Farmer


def generate_farmers(num_farmers):
    """
    generates "num_farmers" instances of the class Farmer

    input parameters:
    :param num_farmers: integer specifying how many farmers
        to generate

    returns a list of instances of the class Farmer
    """
    farmers = []
    for _ in range(num_farmers):
        farmer_id = uuid.uuid4()
        farmers.append(Farmer(farmer_id=farmer_id))
    return farmers
