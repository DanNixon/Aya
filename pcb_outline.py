#!/usr/bin/env python3

import numpy as np
import solid as sp

import cad, layout, utils


def place_right_hand_side():
    board_outline = layout.generate_board_outline() + layout.split_offset
    return cad.case_outline(board_outline)


def place_left_hand_side():
    board_outline = utils.mirror_in_x(
        layout.generate_board_outline()
    ) - layout.split_offset
    return cad.case_outline(board_outline)


u = sp.union()(place_right_hand_side(), place_left_hand_side())
print(sp.scad_render(u))
