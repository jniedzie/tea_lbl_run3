from lbl_params import *

nEvents = -1
printEveryNevents = 1000

base_path = "/nfs/dust/cms/user/jniedzie/light_by_light/"

# for LbL analysis:
applyTrigger = False

applyTwoTracksTwoPhotons = False
applyTwoPhotons = True
applySinglePhoton = False
applyThreePhotons = False
applyTwoElectrons = False
applyZeroPhotonElectron = False

applyChargedExclusivity = True
applyNeutralExclusivity = True
applyDiphotonPt = True
applyZDC = True

applyEtDelta = False


# for QED analysis:
# applyTrigger = False
# applyTwoTracksTwoPhotons = False
# applyTwoPhotons = False
# applyTwoElectrons = True
# applyDiphotonPt = False
# applyChargedExclusivity = False
# applyNeutralExclusivity = True
# applyZDC = True
# applyEtDelta = False

sample = "collisionData"
# sample = "lbl"
# sample = "cep"
# sample = "qed"
# sample = "qed_MG_ee_aa"

# skim = "skimmed_lblSelections"
# skim = "skimmed_qedSelections"
# skim = "initial"

inputFilePath = f"{base_path}/ntuples/{sample}/initial/ntuple_0.root"
treeOutputFilePath = "../skimmed_test.root"

# weightsBranchName = "genWeight"
eventsTreeNames = ["Events",]

# define simple event-level selections
eventSelections = {}

specialBranchSizes = {}
branchesToKeep = ["*"]
branchesToRemove = []
