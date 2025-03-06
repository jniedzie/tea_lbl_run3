# Example on how to run:
# ./skimmer --config bw_run3_example_skimmer_config.py --input_path /eos/cms/store/cmst3/group/lightbylight/tea_samples/lbl/initial/ntuple_0.root --output_trees_path ../test.root

extraEventCollections = {
  "Electrons": {
    "inputCollections": ["electron"],
    "pt": (2., 9999999.),
    "eta": (-2.5, 2.5),
  },
}

nEvents = -1
printEveryNevents = 10000

weightsBranchName = "genWeight"
eventsTreeNames = ("Events",)

triggerSelection = [
    "HLT_HIUPC_DoubleEG2_NotMBHF2AND_v8",
]

eventCuts = {
    "nElectrons": (2, 2),
}

branchesToKeep = ["*"]
branchesToRemove = []
specialBranchSizes = {}
