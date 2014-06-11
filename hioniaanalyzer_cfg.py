import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("HIOnia")

# setup 'analysis'  options
options = VarParsing.VarParsing ('analysis')

# setup any defaults you want
options.outputFile ='file:/afs/cern.ch/work/m/makbiyik/public/UPC_event_Hiskim/d0725/CMSSW_5_3_8_HI_patch2/src/UPC_V01/d0526/Hionia_Data_Melike_pPb.root_v6.root' # Pbp run: Pb going in -Z direction
options.secondaryOutputFile = "Jpsi_DataSet.root",
options.inputFiles =(
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_100_1_KZl.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_101_1_ItD.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_102_1_3gk.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_103_1_di5.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_104_1_VoP.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_105_1_Xt0.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_106_1_g3z.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_107_1_uu6.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_108_1_6Cc.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_109_1_7Bg.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_10_1_oUt.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_110_1_yxe.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_111_1_PWw.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_112_1_JXY.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_113_1_wcR.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_114_1_vTQ.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_115_1_dbA.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_116_1_J56.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_117_1_v42.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_118_1_5Z9.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_119_1_KJU.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_11_1_T6N.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_120_1_0Zf.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_121_1_fnO.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_122_1_gy8.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_123_1_urn.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_124_1_hC1.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_125_1_UqO.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_126_1_V49.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_127_1_Fnb.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_128_1_DXr.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_129_1_iEP.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_12_1_Ige.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_130_1_5fQ.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_131_1_x9V.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_132_1_CZp.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_133_1_egv.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_134_1_A9w.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_135_1_fll.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_13_1_es9.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_14_1_Ttd.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_15_1_Gay.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_16_1_Bdm.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_17_1_XYd.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_18_1_hmP.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_19_1_KLj.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_1_1_3mb.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_20_1_ks3.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_21_1_E8J.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_22_1_aiu.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_23_1_Llx.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_24_1_uXX.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_25_1_QOL.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_26_1_4s0.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_27_1_xga.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_28_1_rx5.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_29_1_PfO.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_2_1_nqZ.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_30_1_1Ib.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_31_1_ABo.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_32_1_kL1.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_33_1_QXi.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_34_1_7vH.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_35_1_Nxc.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_36_1_Ql7.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_37_1_Fic.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_38_1_R94.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_39_1_EDE.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_3_1_KK8.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_40_1_s0b.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_41_1_0Bp.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_42_1_DJD.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_43_1_jih.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_44_1_9eL.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_45_1_APt.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_46_1_WnD.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_47_1_Dhr.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_48_1_6oi.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_49_1_EDF.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_4_1_PAd.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_50_1_ku9.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_51_1_fDL.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_52_1_wM5.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_53_1_oUH.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_54_1_NnW.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_55_1_dwZ.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_56_1_Wwx.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_57_3_0qw.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_58_2_KMj.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_59_2_lpx.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_5_1_Gty.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_60_2_bF1.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_61_3_Toa.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_62_1_tEg.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_63_3_PQ2.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_64_2_4IT.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_65_1_41A.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_66_2_Hct.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_67_1_EiN.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_68_2_EZb.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_69_2_MFs.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_6_1_8pt.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_70_1_TfQ.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_71_1_TEi.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_72_1_XXa.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_73_1_5u7.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_74_1_jrN.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_75_1_oPX.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_76_1_onL.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_77_1_80e.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_78_1_qpq.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_79_1_tfq.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_7_1_WJa.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_80_1_KgD.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_81_1_zQR.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_82_1_nXN.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_83_1_ap7.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_84_1_Yrp.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_85_1_RkA.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_86_1_coP.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_87_1_ZFo.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_88_1_Gku.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_89_1_4YA.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_8_1_2GD.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_90_1_FmW.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_91_1_jts.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_92_1_j02.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_93_1_o2V.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_94_1_9qj.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_95_1_IRP.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_96_1_JHY.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_97_1_6G1.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_98_1_9qr.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_99_1_ick.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/makbiyik/hiskim_v1/Data_HiSkim_v5_9_1_RlF.root")

options.maxEvents = -1 # -1 means all events

# get and parse the command line arguments
options.parseArguments()

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = -100

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


# ONLY FOR MONTE-CARLO :
#process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck') # ONLY FOR MONTE-CARLO :



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
				CaloTowerLabel = cms.InputTag("towerMaker"),
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
                                #changed 2->0 and 0 is muon(+)muon(-)
                                #-- Gen Details
                                oniaPDG = cms.int32(443),
                                isHI = cms.untracked.bool(False),
                                isPA = cms.untracked.bool(True),
                                isMC = cms.untracked.bool(False),#MC->Data change true or false
                                isPromptMC = cms.untracked.bool(False),#MC->Data change true or false

                                #-- Histogram configuration
                                combineCategories = cms.bool(False),
                                fillRooDataSet = cms.bool(False),
                                fillTree = cms.bool(True),
                                fillHistos = cms.bool(False),
                                minimumFlag = cms.bool(False),#I changed true to false.
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
                                                                    
                                                                   "hltMuOpenTkMu1TkMuMassFilteredUpcOnia"),




                                # 211313 - 211631 : 12.55 nb-1 (Pbp run: Pb going in -Z direction) 
                                # 210498-211256: 18.40 nb-1 (pPb run: Pb going in +Z direction)
                                lowlimitRun = cms.uint32(210498),
                                upplimitRun = cms.uint32(211256))                                               
#process.p = cms.Path(process.hltDblMuOpen*process.hionia)
process.p = cms.Path(process.hionia)
