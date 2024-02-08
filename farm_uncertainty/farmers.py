# -*- coding: utf-8 -*-
# Copyright (c) 2023 LEEP - University of Exeter (UK)
# Mattia C. Mancini (m.c.mancini@exeter.ac.uk),
# Amy Binner (a.r.binner@exeter.ac.uk)
# February 2024
"""
Class Farmer to generate instances of farmers which constitute the
main agents of the agent-based model simulating farmer uptake of
agri-environmental schemes on their land based on uncertain future
conditions (prices and climate)
"""


# pylint: disable = R0903
class Farmer:
    """
    Farmer
    ------------------------

    Required input parameters for initialisation:
    :param famer_id: unique identifier of a farmer. Needed to keep track
           of farmer behaviour

    Methods defined here:

    __str__(self, /)
        Return str(self)

    """

    def __init__(self, farmer_id):
        self.farmer_id = farmer_id

    def __str__(self):
        pass


# pylint: enable = R0903
