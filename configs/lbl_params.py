# event cuts
eventCuts = {
    # "max_ZDCenergyPerSide": 10000.0,  # <4n
    "max_ZDCenergyPerSide": 7000.0,  # <3n
    # "max_ZDCenergyPerSide": 4000.0,  # <2n
    # "max_ZDCenergyPerSide": 1600.0,  # <1n

    "min_diphotonMass": 5.0,  # only used in LbL analysis
    "max_diphotonPt": 1.0,  # only used in LbL analysis

    "min_dielectronMass": 5.0,  # only used in QED analysis
    "max_dielectronPt": 1.0,  # only used in QED analysis

    "max_Nelectrons": 0,  # 0 for LbL analysis, 2 for QED analysis
    "max_Ntracks": 0,
    "max_Nmuons": 0,
    "max_Ntowers": 0,
}

# good object definitions
photonCuts = {
    "min_et": 2.0,
    "max_absEta": 2.2,
    "max_swissCross": 0.95,
    "max_SCEtaWidth_barrel": 0.0106,
    "max_SCEtaWidth_endcap": 0.0272,
    "max_hOverE_barrel": 0.04596,
    "max_hOverE_endcap": 0.0590,
    "max_sigmaIEtaIEta_barrel": 0.02,
    "max_sigmaIEtaIEta_endcap": 0.06,
    "max_seedTime": 3.0,
}

electronCuts = {
    "min_pt": 2.0,
    "max_absEtaSC": 2.2,

    "max_nMissingHits": 1,
    "max_hOverE": 0.005,
    "max_deltaEtaAtVertex": 0.1,

    # we don't apply electron isolation:
    "max_PFChIso_barrel": 999999,
    "max_PFPhoIso_barrel": 999999,
    "max_PFNeuIso_barrel": 999999,
    "max_PFChIso_endcap": 999999,
    "max_PFPhoIso_endcap": 999999,
    "max_PFNeuIso_endcap": 999999,
}

trackCuts = {
    "min_pt": 0.3,
    "max_absEta": 2.4,
    "min_nValidHits": 4,

    # we don't apply these track selections:
    "max_normalizedChi2": 999999,
    "max_dxy": 999999,
    "max_dz": 999999,
    "max_dxyOverError": 999999,
    "max_dzOverError": 999999,
}

muonCuts = {
    "min_pt": 2.5,
    "max_absEta": 2.4,
}


# calorimeter cuts
caloNoiseThresholds = {
    "HFp": 6.0,
    "HFm": 6.0,
    
    # "HFp": 9.1, # + 0.8 - 1.3
    # "HFm": 8.8, # + 0.7 - 1.0
    
    "HB": 2.8,
    "HE": 1.0,
    "EB": 0.7,
    "EE": 3.0,
}

caloNoiseVariables = {
    "HFm": "energy",
    "HFp": "energy",
    "HB": "hadE",
    "HE": "hadE",
    "EB": "emE",
    "EE": "emE",
}


# detector parameters
deadEtas = {
    "HFp": (29, 30), # 2.853 -- 3.139
    "HFm": (-29, -30),
    
    # "HFp": (29,), # 2.853 -- 3.000
    # "HFm": (-29,),

    "HE": (-16, 16), #  1.305 -- 1.392
}

caloEtaEdges = {
    "maxEB": 1.479,
    "minEE": 1.479,
    "maxEE": 3.0,

    "maxHB": 1.305,
    "minHE": 1.305,
    "maxHE": 3.0,

    "minHF": 2.9,
    "maxHF": 5.2,
}

detectorParams = {
    "crack_start": 1.4442,
    "crack_end": 1.566,

    "crackHadron_start": 1.305,
    "crackHadron_end": 1.41,

    "hem_etaStart": -3.0,
    "hem_etaEnd": -1.39,
    "hem_phiStart": -1.6,
    "hem_phiEnd": -0.9,

    "caloTower_etaMax": 2.4,
}


# matching between calorimeters and photons/electrons
caloMatching = {
    "maxDeltaEta_EB": 0.15,
    "maxDeltaPhi_EB": 0.15,
    "maxDeltaEta_EE": 0.15,
    "maxDeltaPhi_EE": 0.15,
}


# matching between photons and electrons
electronPhotonMatching = {
    "maxDeltaEta": 0.5,  # ???
    "maxDeltaPhi": 0.5,  # ???
}

# matching between tracks and electrons
electronTrackMatching = {
    "maxDeltaEta": 0.15,
    "maxDeltaPhi": 0.7,
}


#  scaling parameters

luminosity = 1647.180726  # μb^-1, with ZDC
# luminosity = 1647.2  # μb^-1, without ZDC
luminosity_err = luminosity * 0.015  # 1.5% uncertainty

reference_alp_cross_section = 10e-3  # μb

# QED needs to be scaled up, depending on the ZDC cut
# qed_scaling = 1.0  # 4n OR
# qed_scaling = 2.2  # 1n AND
# qed_scaling = 2.3  # 2n AND
# qed_scaling = 2.7  # 3n AND
# qed_scaling = 2.5  # 4n AND
# qed_scaling = 1.0  # Xn0n, no scaling
qed_scaling = 0.5  # adding SC + SL
# qed_scaling = 2.047  # no CEP


# LbL may be scaled up due to NLO corrections
lbl_scaling = 1.05  # inclusive
# lbl_scaling = 1.05 * 0.74  # 0n0n
# lbl_scaling = 1.05 * (0.74 + 0.046 + 0.006)  # 0n0n + 0n1n + 1n0n + 1n1n

crossSections = {
    "lbl": 2.59 * lbl_scaling,  # μb
    
    "qed": 8827.220 * qed_scaling,  # μb
    "qed_starlight": 7920.0 * qed_scaling,  # μb
    "qed_MG_ee_a": 13.45 * qed_scaling,  # μb
    "qed_MG_ee_aa": 0.1945 * qed_scaling,  # μb
    
    "cep": 5.8e-3,  # we scale it to data

    "alps_5": reference_alp_cross_section,
    "alps_6": reference_alp_cross_section,
    "alps_9": reference_alp_cross_section,
    "alps_11": reference_alp_cross_section,
    "alps_14": reference_alp_cross_section,
    "alps_16": reference_alp_cross_section,
    "alps_22": reference_alp_cross_section,
    "alps_30": reference_alp_cross_section,
    "alps_50": reference_alp_cross_section,
    "alps_90": reference_alp_cross_section,
    
    # nb -> μb, g = 0.2 TeV-1
    # "alps_14": 70.21369385210362 * 1e-3, 
    # "alps_30": 21.396925059153958 * 1e-3,
    
    # nb -> μb, g = 0.25 TeV-1
    # "alps_14": 109.82586410834259 * 1e-3, 
    # "alps_30": 33.46834007669329 * 1e-3,
    
    # nb -> μb, g = 0.3 TeV-1
    # "alps_14": 158.28699751455125 * 1e-3, 
    # "alps_30": 48.23638862799777 * 1e-3,
}


# photon ET > 2.0 GeV, diphoton pt < 1 GeV
scale_factors = {
    "photonReco": 0.9758,
    "photonID": 0.946,
    "electronRecoID": 0.943,
    "l1eg": 1.0089,
    "l1hf": 0.8716,
    "che": 0.9252,
    
    "nee": 0.8487,  # old SF
    # "nee": 0.953,  # new SF (higher HF thresholds)
}

scale_factor_errors = {
    "photonReco": 0.0314,
    "photonID": 0.049,
    "electronRecoID": 0.0085,
    "l1eg": 0.002,
    "l1hf": 0.054,
    "che": 0.0087,
    "nee": 0.0085,
}


def get_scale_factor(photon=True):
    value = 1
    error = 0

    to_skip = "electron" if photon else "photon"
    squared = "photon" if photon else "electron"

    for variable in scale_factors:
        if to_skip in variable:
            continue

        error += (scale_factor_errors[variable] / scale_factors[variable])**2
        value *= scale_factors[variable]

        if squared in variable:
            error += (scale_factor_errors[variable] /
                      scale_factors[variable])**2
            value *= scale_factors[variable]

    sf_error = value * error**(1/2)

    return value, sf_error


nGenEvents = {
    "lbl": 466000,
    
    "cep": 668000,  # we scale it to data

    "qed_MG_ee_a": 10228329,
    "qed_MG_ee_aa": 6457150,
    "qed": 59260000,
    "qed_starlight": 66750000,

    "alps_5": 754000,
    "alps_6": 729000,
    "alps_9": 722000,
    "alps_11": 692000,
    "alps_14": 712000,
    "alps_16": 682000,
    "alps_22": 694000,
    "alps_30": 719000,
    "alps_50": 511000,
    "alps_90": 449000,
}


#  significance & limits parameters
cep_scaling_min_acoplanarity = 0.015
n_acoplanarity_bins = 40
n_mass_bins = 200

do_qed_sampling = True
qed_sampling_n_events = 400
qed_sampling_transition_point = 0.026
qed_sampling_fit_max_aco = 0.2

do_lbl_sampling = False

uncertainty_on_zero = 1.84  # 95% CL
# uncertainty_on_zero = 1.14  # 68% CL

total_uncertainty_qed = 1.068
total_uncertainty_lbl_run2 = 1.23
non_stat_uncertainty_lbl_run2 = 1.18
stat_uncertainty_lbl_run2 = 1.15

total_uncertainty_lbl_run1 = 1.24
alp_mc_uncertainty = 1.03

total_diphoton_efficiency = 0.1352
total_diphoton_efficiency_err = 0.0030
