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
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_0.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_1.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_10.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_100.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_101.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_102.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_104.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_105.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_106.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_107.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_108.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_109.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_11.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_110.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_112.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_113.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_115.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_116.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_117.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_118.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_119.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_120.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_121.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_122.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_123.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_124.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_125.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_126.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_127.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_128.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_129.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_13.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_130.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_131.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_132.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_133.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_134.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_135.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_136.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_137.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_139.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_14.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_140.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_141.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_142.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_143.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_144.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_145.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_146.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_147.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_148.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_149.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_15.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_150.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_151.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_152.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_153.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_154.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_155.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_156.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_158.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_159.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_16.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_160.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_161.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_162.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_163.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_164.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_165.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_166.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_167.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_169.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_17.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_170.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_171.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_172.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_173.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_174.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_175.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_176.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_178.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_179.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_18.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_181.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_182.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_183.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_184.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_185.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_186.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_188.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_189.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_19.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_190.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_191.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_192.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_193.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_195.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_196.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_197.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_198.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_199.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_2.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_20.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_21.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_22.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_23.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_24.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_25.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_26.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_27.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_28.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_29.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_30.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_31.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_32.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_34.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_35.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_36.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_37.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_38.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_4.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_40.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_41.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_42.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_43.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_44.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_45.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_46.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_47.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_48.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_49.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_5.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_50.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_51.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_52.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_53.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_54.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_55.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_56.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_57.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_58.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_59.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_6.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_60.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_61.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_62.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_63.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_64.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_65.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_67.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_69.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_7.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_70.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_71.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_73.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_74.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_76.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_77.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_78.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_79.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_8.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_80.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_82.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_83.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_84.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_85.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_86.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_87.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_88.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_89.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_9.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_90.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_91.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_92.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_93.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_94.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_95.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_96.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_97.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_98.root",
"file:root://eoscms//eos/cms/store/group/phys_heavyions/cbaus/pPb_5020_EposLHC_5_3_8_HI_patch2_showerlibrary/RECO/job_N500_99.root")


options.outputFile = ('file:/afs/cern.ch/work/m/makbiyik/public/UPC_event_Hiskim/d0725/CMSSW_5_3_8_HI_patch2/src/StarlightReco/EPOS_LHC.root')

options.maxEvents = -1 # -1 means all events
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

process.e = cms.EndPath(process.outOnia2MuMu)

process.schedule = cms.Schedule(process.Onia2MuMuPAT,
                                process.e)


