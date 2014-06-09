# for the list of used tags please see:
# https://twiki.cern.ch/twiki/bin/view/CMS/Onia2MuMuSamples

import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

# set up process
process = cms.Process("Onia2MuMuPAT")

# setup 'analysis'  options
options = VarParsing.VarParsing ('analysis')

# setup any defaults you want
options.inputFiles = (

"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/starlight//HLT_50_100_new_out/slight_config_HIpPb2013_pbP_to_mumu_minv_50_100_0.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/starlight//HLT_50_100_new_out/slight_config_HIpPb2013_pbP_to_mumu_minv_50_100_1.root")


#options.outputFile = ('file:/afs/cern.ch/work/m/makbiyik/public/UPC_event_Hiskim/d0725/CMSSW_5_3_8_HI_patch2/src/UPC_V01/d0428/pPb2013_pbP_to_mumu_minv_50_100_hskim.root')
options.outputFile = ('Test.root')

#options.maxEvents = -1 # -1 means all events
#options.maxEvents =260000
# get and parse the command line arguments
options.parseArguments()

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'STARTHI53_V17::All'

# Common offline event selection
process.load("HeavyIonsAnalysis.Configuration.collisionEventSelection_cff")

# pile up rejection
process.load('Appeltel.RpPbAnalysis.PAPileUpVertexFilter_cff')

# Centrality for pPb
process.load('RecoHI.HiCentralityAlgos.HiCentrality_cfi')

# HLT dimuon trigger
import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltOniaHI = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltOniaHI.HLTPaths = ["HLT_PAUpcSingleMuOpenPixel_TrackVeto_v1",
                              "HLT_PADoubleMu4_Acoplanarity03_v1",
                              "HLT_PAUpcSingleMuOpenTkMu_Onia_v1"
                              ]
process.hltOniaHI.throw = False
process.hltOniaHI.andOr = True
process.hltOniaHI.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")


from HiSkim.HiOnia2MuMu.onia2MuMuPAT_cff import *
onia2MuMuPAT(process, GlobalTag=process.GlobalTag.globaltag, MC=True, HLT="HLT", Filter=True)

# onia2MuMuPAT.outputCommands=cms.untracked.vstring('keep *','keep *_towerMaker_*_*')

#process.onia2MuMuPatTrkTrk.addMuonlessPrimaryVertex = False
#process.onia2MuMuPatTrkTrk.resolvePileUpAmbiguity = False

process.patMuonSequence = cms.Sequence(
#    process.hltOniaHI *
#    process.PAcollisionEventSelection *
    process.pileupVertexFilterCutGplus * 
    process.pACentrality_step *
    process.genMuons *
    process.patMuonsWithTriggerSequence
    )

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
process.source.fileNames = cms.untracked.vstring(
    options.inputFiles
    )

# filter on lumisections
#from HiSkim.HiOnia2MuMu.goodLumiSectionListHI_cfi import *
#process.source.lumisToProcess = goodLumisToProcess

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )
process.outOnia2MuMu.fileName = cms.untracked.string( options.outputFile )
process.outOnia2MuMu.outputCommands.extend(cms.untracked.vstring('keep *_towerMaker_*_*','keep *_castorreco_*_*','keep ZDC*_hcalDigis_*_*'))
# process.outOnia2MuMu.outputCommands.extend(cms.untracked.vstring(''))
# process.outOnia2MuMu.outputCommands.extend(cms.untracked.vstring(''))

process.e = cms.EndPath(process.outOnia2MuMu)

process.schedule = cms.Schedule(process.Onia2MuMuPAT,
                                process.e)


