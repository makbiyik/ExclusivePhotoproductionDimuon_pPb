import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("HIOnia")

# setup 'analysis'  options
options = VarParsing.VarParsing ('analysis')

# setup any defaults you want
options.outputFile = (
"file:/afs/cern.ch/work/m/makbiyik/public/UPC_event_Hiskim/d0725/CMSSW_5_3_8_HI_patch2/src/StarlightReco/pbP_to_mumu_minv_10_25_honiaanalyzer.root")
options.secondaryOutputFile = "Jpsi_DataSet.root"



options.inputFiles =(
"file:/afs/cern.ch/work/m/makbiyik/public/UPC_event_Hiskim/d0725/CMSSW_5_3_8_HI_patch2/src/StarlightReco/pbP_to_mumu_minv_10_25_hskim.root")


options.maxEvents = -1 # -1 means all events

# get and parse the command line arguments
options.parseArguments()

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = 'GR_E_V33::All' # express reco
process.GlobalTag.globaltag = 'GR_P_V43D::All' # prompt reco

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import *
overrideCentrality(process)

process.HeavyIonGlobalParameters = cms.PSet(
    centralityVariable = cms.string("HFtowersPlusTrunc"),
    nonDefaultGlauberModel = cms.string(""),
    centralitySrc = cms.InputTag("pACentrality"),
    pPbRunFlip = cms.untracked.uint32(211313)
    )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

process.options = cms.untracked.PSet(
                  wantSummary = cms.untracked.bool(True),
                  SkipEvent = cms.untracked.vstring('ProductNotFound')
                  )
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        options.inputFiles
    )
)

process.hltDblMuOpen = cms.EDFilter("HLTHighLevel",
                 TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                 HLTPaths = cms.vstring("HLT_PAL1DoubleMuOpen_v*"),
                 eventSetupPathsKey = cms.string(''),
                 andOr = cms.bool(True),
                 throw = cms.bool(False)
)

process.hltDblMu0 = cms.EDFilter("HLTHighLevel",
                 TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                 HLTPaths = cms.vstring("HLT_PAL1DoubleMu0_HighQ_v*"),
                 eventSetupPathsKey = cms.string(''),
                 andOr = cms.bool(True),
                 throw = cms.bool(False)
)

process.hltDblMu3 = cms.EDFilter("HLTHighLevel",
                 TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                 HLTPaths = cms.vstring("HLT_PAL2DoubleMu3_v*"),
                 eventSetupPathsKey = cms.string(''),
                 andOr = cms.bool(True),
                 throw = cms.bool(False)
)

process.hltMu3 = cms.EDFilter("HLTHighLevel",
                 TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                 HLTPaths = cms.vstring("HLT_PAMu3_v*"),
                 eventSetupPathsKey = cms.string(''),
                 andOr = cms.bool(True),
                 throw = cms.bool(False)
)

process.hltMu7 = cms.EDFilter("HLTHighLevel",
                 TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                 HLTPaths = cms.vstring("HLT_PAMu7_v*"),
                 eventSetupPathsKey = cms.string(''),
                 andOr = cms.bool(True),
                 throw = cms.bool(False)
)

process.hltMu12 = cms.EDFilter("HLTHighLevel",
                 TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                 HLTPaths = cms.vstring("HLT_PAMu12_v*"),
                 eventSetupPathsKey = cms.string(''),
                 andOr = cms.bool(True),
                 throw = cms.bool(False)
)

process.hltMult100DblMu3 = cms.EDFilter("HLTHighLevel",
                 TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                 HLTPaths = cms.vstring("HLT_PAPixelTrackMultiplicity100_L2DoubleMu3_v*"),
                 eventSetupPathsKey = cms.string(''),
                 andOr = cms.bool(True),
                 throw = cms.bool(False)
)

process.hionia = cms.EDAnalyzer('HiOniaAnalyzer',
                                srcMuon = cms.InputTag("patMuonsWithTrigger"),
                                srcMuonNoTrig = cms.InputTag("patMuonsWithoutTrigger"),
                                src = cms.InputTag("onia2MuMuPatTrkTrk"),
                                srcTracks = cms.InputTag("generalTracks"),
                                genParticles = cms.InputTag("genParticles"),
                                primaryVertexTag = cms.InputTag("offlinePrimaryVertices"),
                                triggerResultsLabel = cms.InputTag("TriggerResults","","HLT"),
                                srcCentrality = cms.InputTag("pACentrality"),
                                
                                #-- Reco Details
                                useBeamSpot = cms.bool(False),
                                useRapidity = cms.bool(True),
                                
                                #--
                                maxAbsZ = cms.double(24.0),
                                
                                pTBinRanges = cms.vdouble(0.0, 6.0, 8.0, 9.0, 10.0, 12.0, 15.0, 40.0),
                                etaBinRanges = cms.vdouble(0.0, 2.5),
                                centralityRanges = cms.vdouble(20,40,100),

                                onlyTheBest = cms.bool(False),		
                                applyCuts = cms.bool(True),
                                storeEfficiency = cms.bool(False),
                      
                                removeSignalEvents = cms.untracked.bool(False),
                                removeTrueMuons = cms.untracked.bool(False),
                                storeSameSign = cms.untracked.bool(True),
                                
                                #-- Gen Details
                                oniaPDG = cms.int32(443),
                                isHI = cms.untracked.bool(False),
                                isPA = cms.untracked.bool(True),
                                isMC = cms.untracked.bool(True),
                                isPromptMC = cms.untracked.bool(True),

                                #-- Histogram configuration
                                combineCategories = cms.bool(False),
                                fillRooDataSet = cms.bool(False),
                                fillTree = cms.bool(True),
                                fillHistos = cms.bool(False),
                                minimumFlag = cms.bool(True),
                                fillSingleMuons = cms.bool(True),
                                histFileName = cms.string(options.outputFile),		
                                dataSetName = cms.string(options.secondaryOutputFile),
                                
                                #--
                                # NumberOfTriggers = cms.uint32(8),
                                dblTriggerPathNames = cms.vstring("HLT_PADoubleMu4_Acoplanarity03_v1"),

                                dblTriggerFilterNames = cms.vstring("hltDoubleMu4ExclL3PreFiltered"),
                                
                                sglTriggerPathNames = cms.vstring("HLT_PAUpcSingleMuOpenPixel_TrackVeto_v1",
                                                                  
							          "HLT_PAUpcSingleMuOpenTkMu_Onia_v1"),
                                                             
                                sglTriggerFilterNames = cms.vstring("~hltPACountPAPixFilter10",
                                                                    
                                                                   "hltMuOpenTkMu1TkMuMassFilteredUpcOnia")


                                
                                  )                                               
#process.p = cms.Path(process.hltDblMuOpen*process.hionia)
process.p = cms.Path(process.hionia)
