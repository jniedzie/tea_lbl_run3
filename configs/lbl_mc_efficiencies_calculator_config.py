from lbl_params import *

nEvents = -1
printEveryNevents = 1000

base_path = "/nfs/dust/cms/user/jniedzie/light_by_light/"


# sample = "collisionData"
# sample = "lbl_noTrigger"
# sample = "lbl"
# sample = "cep"
sample = "qed"
# sample = "qed_noTrigger"

skim = "initial"

inputFilePath = f"{base_path}/ntuples/{sample}/merged_initial.root"
# treeOutputFilePath = inputFilePath.replace("initial", skim)

# weightsBranchName = "genWeight"
eventsTreeNames = ["Events",]

# define simple event-level selections
eventSelections = {}

specialBranchSizes = {}
branchesToKeep = ["*"]
branchesToRemove = []
