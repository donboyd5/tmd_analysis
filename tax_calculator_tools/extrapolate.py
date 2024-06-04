"""
Extrapolation function based on Tax-Calculator.
"""

import numpy as np
import taxcalc as tc

def advance(recs, year, weights, gfdf):
    """
    Advance recs to a new year, given weights and growth factors.
    """
    recs = recs.copy()
    recs = extrapolate(recs, year, gfdf)
    column_name = f'WT{year}'
    recs['FLPDYR_base'] = recs.FLPDYR
    recs['s006_base'] = recs.s006
    recs['weight_tmd'] = weights[column_name] / 100.0
    recs.FLPDYR = year
    recs.s006 = recs.weight_tmd
    # recs = tc.Records(data=recs, start_year=year, gfactors=None, weights=None)
    return recs

def extrapolate(recs, year, gfdf):
    """
    Apply to variables the grow factor values for specified calendar year.
    """
    # pylint: disable=too-many-statements,no-member

    # DO NOT MODIFY IN PLACE
    recs = recs.copy()

    # put values in local dictionary
    gfv = {} # dict()
    for name in gfdf.columns:
        gfv[name] = gfdf.loc[gfdf['YEAR'] == year, name].values[0]
    # for name in GrowFactors.VALID_NAMES:
    #     gfv[name] = recs.gfactors.factor_value(name, year)

    # apply values to Records variables
    recs.PT_binc_w2_wages *= gfv['AWAGE']
    recs.e00200 *= gfv['AWAGE']
    recs.e00200p *= gfv['AWAGE']
    recs.e00200s *= gfv['AWAGE']
    recs.pencon_p *= gfv['AWAGE']
    recs.pencon_s *= gfv['AWAGE']
    recs.e00300 *= gfv['AINTS']
    recs.e00400 *= gfv['AINTS']
    recs.e00600 *= gfv['ADIVS']
    recs.e00650 *= gfv['ADIVS']
    recs.e00700 *= gfv['ATXPY']
    recs.e00800 *= gfv['ATXPY']
    # recs.e00900s[:] = np.where(recs.e00900s >= 0,
    #                             recs.e00900s * gfv['ASCHCI'],
    #                             recs.e00900s * gfv['ASCHCL'])
    # recs.e00900p[:] = np.where(recs.e00900p >= 0,
    #                             recs.e00900p * gfv['ASCHCI'],
    #                             recs.e00900p * gfv['ASCHCL'])
    # recs.e00900[:] = recs.e00900p + recs.e00900s
    # Conditional application using np.where
    recs['e00900s'] = np.where(
        recs['e00900s'] >= 0,
        recs['e00900s'] * gfv['ASCHCI'],
        recs['e00900s'] * gfv['ASCHCL']
    )
    recs['e00900p'] = np.where(
        recs['e00900p'] >= 0,
        recs['e00900p'] * gfv['ASCHCI'],
        recs['e00900p'] * gfv['ASCHCL']
    )
    recs['e00900'] = recs.e00900p + recs.e00900s
    recs.e01100 *= gfv['ACGNS']
    recs.e01200 *= gfv['ACGNS']
    recs.e01400 *= gfv['ATXPY']
    recs.e01500 *= gfv['ATXPY']
    recs.e01700 *= gfv['ATXPY']
    # recs.e02000[:] = np.where(recs.e02000 >= 0,
    #                             recs.e02000 * gfv['ASCHEI'],
    #                             recs.e02000 * gfv['ASCHEL'])
    recs['e02000'] = np.where(
    recs['e02000'] >= 0,
    recs['e02000'] * gfv['ASCHEI'],
    recs['e02000'] * gfv['ASCHEL']
    )
    recs.e02100 *= gfv['ASCHF']
    recs.e02100p *= gfv['ASCHF']
    recs.e02100s *= gfv['ASCHF']
    recs.e02300 *= gfv['AUCOMP']
    recs.e02400 *= gfv['ASOCSEC']
    recs.e03150 *= gfv['ATXPY']
    recs.e03210 *= gfv['ATXPY']
    recs.e03220 *= gfv['ATXPY']
    recs.e03230 *= gfv['ATXPY']
    recs.e03270 *= gfv['ACPIM']
    recs.e03240 *= gfv['ATXPY']
    recs.e03290 *= gfv['ACPIM']
    recs.e03300 *= gfv['ATXPY']
    recs.e03400 *= gfv['ATXPY']
    recs.e03500 *= gfv['ATXPY']
    recs.e07240 *= gfv['ATXPY']
    recs.e07260 *= gfv['ATXPY']
    recs.e07300 *= gfv['ABOOK']
    recs.e07400 *= gfv['ABOOK']
    recs.p08000 *= gfv['ATXPY']
    recs.e09700 *= gfv['ATXPY']
    recs.e09800 *= gfv['ATXPY']
    recs.e09900 *= gfv['ATXPY']
    recs.e11200 *= gfv['ATXPY']
    # ITEMIZED DEDUCTIONS
    recs.e17500 *= gfv['ACPIM']
    recs.e18400 *= gfv['ATXPY']
    recs.e18500 *= gfv['ATXPY']
    recs.e19200 *= gfv['AIPD']
    recs.e19800 *= gfv['ATXPY']
    recs.e20100 *= gfv['ATXPY']
    recs.e20400 *= gfv['ATXPY']
    recs.g20500 *= gfv['ATXPY']
    # CAPITAL GAINS
    recs.p22250 *= gfv['ACGNS']
    recs.p23250 *= gfv['ACGNS']
    recs.e24515 *= gfv['ACGNS']
    recs.e24518 *= gfv['ACGNS']
    # SCHEDULE E
    recs.e26270 *= gfv['ASCHEI']
    recs.e27200 *= gfv['ASCHEI']
    recs.k1bx14p *= gfv['ASCHEI']
    recs.k1bx14s *= gfv['ASCHEI']
    # MISCELLANOUS SCHEDULES
    recs.e07600 *= gfv['ATXPY']
    recs.e32800 *= gfv['ATXPY']
    recs.e58990 *= gfv['ATXPY']
    recs.e62900 *= gfv['ATXPY']
    recs.e87530 *= gfv['ATXPY']
    recs.e87521 *= gfv['ATXPY']
    recs.cmbtp *= gfv['ATXPY']
    # BENEFITS
    recs.other_ben *= gfv['ABENOTHER']
    recs.mcare_ben *= gfv['ABENMCARE']
    recs.mcaid_ben *= gfv['ABENMCAID']
    recs.ssi_ben *= gfv['ABENSSI']
    recs.snap_ben *= gfv['ABENSNAP']
    recs.wic_ben *= gfv['ABENWIC']
    recs.housing_ben *= gfv['ABENHOUSING']
    recs.tanf_ben *= gfv['ABENTANF']
    recs.vet_ben *= gfv['ABENVET']
    # remove local dictionary
    del gfv
    return recs
