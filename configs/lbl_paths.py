qed_superchic = "qed"
qed_mg1gamma = "qed_MG_ee_a"
qed_mg2gamma = "qed_MG_ee_aa"
qed_starlight = "qed_starlight"

# qed_name = qed_superchic
qed_names = [qed_superchic, qed_starlight]

facility = "lxplus"
# facility = "NAF"

processes = (
    # "collisionData",
    "lbl",
    # "cep",
    # qed_superchic,
    # qed_starlight,
    # qed_mg1gamma,
    # qed_mg2gamma,
    # "qed_sc_noPhotos",

    # "alps_5",
    # "alps_6",
    # "alps_9",
    # "alps_11",
    # "alps_14",
    # "alps_16",
    # "alps_22",
    # "alps_30",
    # "alps_50",
    # "alps_90",

    # "emptyBeams",
    # "collisionDataZeroBias",
)

# this is the final final skim:
skim = "skimmed_lblSelections_final_photonMatchingdeltaPhi0p15"

# skim = "initial"
# skim = "afterTrigger"
# skim = "skimmed_qedSelections"

acoplanarity_histogram_name = "diphoton_acoplanarity{}"
# mass_histogram_name = "diphoton_mass{}"
mass_histogram_name = "diphotonSR_mass{}"

if facility == "NAF":
    base_path = "/data/dust/user/jniedzie/light_by_light/ntuples"
elif facility == "lxplus":
    base_path = "/eos/cms/store/cmst3/group/lightbylight/tea_samples"

merged_histograms_path = base_path + "/{}/merged_{}_histograms.root"
