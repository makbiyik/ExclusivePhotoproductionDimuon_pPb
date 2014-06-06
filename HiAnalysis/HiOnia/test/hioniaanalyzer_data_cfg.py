import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("HIOnia")

# setup 'analysis'  options
options = VarParsing.VarParsing ('analysis')

# setup any defaults you want
options.outputFile = (
"file:/afs/cern.ch/work/m/makbiyik/public/UPC_event_Hiskim/d0725/CMSSW_5_3_8_HI_patch2/src/StarlightReco/Data_honiaanalyzer.root")


#options.secondaryOutputFile =("file:/afs/cern.ch/work/m/makbiyik/public/UPC_event_Hiskim/d0725/CMSSW_5_3_8_HI_patch2/src/d0812/out_hiskim_d0812/hionia_starlight_pPb_gg_to_mumu_minv80_120.root",)


options.inputFiles =(



"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_100_1_jA0.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_101_1_UDN.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_102_1_eGM.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_103_1_OYL.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_104_1_Yvk.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_105_1_khJ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_106_1_HEW.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_107_1_qzT.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_108_1_kNI.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_109_1_xv5.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_10_1_wr8.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_110_1_fyJ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_111_1_3ZR.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_112_1_wo8.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_113_1_YiU.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_114_1_fsb.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_115_1_mlp.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_116_1_neQ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_117_1_hEC.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_118_1_aro.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_119_1_IZJ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_11_1_614.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_120_1_2rO.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_121_1_Wgk.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_122_1_Kqg.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_123_1_lpi.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_124_1_8DY.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_125_1_NBe.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_126_1_3Jz.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_127_1_DaH.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_128_1_u8e.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_129_1_BEb.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_12_1_tCW.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_130_1_LsQ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_131_1_o6f.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_132_1_gSz.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_133_1_TVu.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_134_1_lbY.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_135_1_wNj.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_136_1_xiQ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_137_1_2rZ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_138_1_rwV.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_139_1_viH.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_13_1_B16.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_140_1_rXG.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_141_1_jym.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_142_1_KI1.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_143_1_TJO.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_144_1_NaC.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_145_1_RKw.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_146_1_zgu.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_147_1_uIL.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_148_1_OBJ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_149_1_Kbh.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_14_1_smW.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_150_1_wD3.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_151_1_ry4.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_152_1_lwI.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_153_1_OZA.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_154_1_ZVf.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_155_1_VsN.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_156_1_1en.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_157_1_w3h.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_158_2_ZHZ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_159_1_793.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_15_1_9MV.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_160_1_n8p.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_161_1_nXN.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_162_1_CEJ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_163_1_bLV.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_164_1_LIJ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_165_1_5iw.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_166_1_k81.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_167_1_mOX.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_168_1_qZP.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_169_1_RRT.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_16_1_aph.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_170_1_bYz.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_171_1_jgX.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_172_1_c6Y.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_173_1_ETE.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_174_1_3IZ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_175_1_qXg.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_176_1_DVR.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_177_1_tGI.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_178_1_NU2.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_179_1_6cw.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_17_1_nhT.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_180_1_MpK.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_181_1_i5l.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_182_1_Y75.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_183_1_ooI.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_184_1_JGW.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_185_1_OQp.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_186_1_cL2.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_187_1_IGz.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_188_1_B1z.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_189_1_00F.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_18_1_KNy.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_190_1_1pb.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_191_1_JOq.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_192_1_TPx.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_193_2_Qzm.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_194_1_AtE.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_195_1_22z.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_196_1_cKE.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_197_1_E6x.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_198_2_Iko.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_199_3_HeG.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_19_1_pnC.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_1_1_yzV.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_200_1_6k3.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_201_1_XRd.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_202_1_g5Y.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_203_1_WJl.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_204_1_mij.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_205_1_fAP.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_206_1_Dvr.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_207_1_zcm.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_208_1_Wzx.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_209_1_m4m.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_20_1_TRy.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_210_1_RhI.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_211_1_DYh.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_212_1_yIk.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_213_1_lGL.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_214_1_1EK.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_215_1_F7t.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_216_1_tJG.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_217_1_T1m.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_218_1_o93.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_219_1_J9U.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_21_1_JbL.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_220_1_dBj.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_221_1_yTy.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_222_1_F7L.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_223_1_IBI.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_224_1_J05.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_225_1_3xM.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_226_1_NkF.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_227_1_EsU.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_228_2_KHT.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_229_4_g5m.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_22_1_QUf.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_230_1_vrw.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_231_1_qb2.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_232_1_Dc8.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_233_1_7p9.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_234_1_wL2.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_235_1_tVw.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_236_1_Pz0.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_237_1_v6K.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_238_1_2y1.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_239_1_dVz.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_23_1_PQP.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_240_1_fyk.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_241_1_XgE.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_242_1_OSf.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_243_1_YuP.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_244_1_WYb.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_245_1_uJE.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_246_1_gis.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_247_2_kkC.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_248_1_JG9.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_249_1_VAF.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_24_1_oIT.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_250_1_JMv.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_251_1_cuz.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_252_1_Ak9.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_253_3_mbW.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_254_1_wEg.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_255_1_nUK.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_256_1_ik1.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_257_1_sNS.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_258_1_Xes.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_259_1_f8X.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_25_1_e6b.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_260_1_fQY.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_261_1_PzM.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_262_1_mER.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_263_1_DE6.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_264_1_tQz.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_265_1_zZW.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_266_1_ntS.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_267_1_7JC.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_268_2_ipK.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_269_2_uuL.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_26_1_8TZ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_270_1_v72.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_271_1_bbz.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_272_1_XNu.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_273_1_Cgp.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_274_1_M0D.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_275_1_N3G.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_276_1_wNa.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_277_1_YNv.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_278_1_2Jx.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_279_1_jLa.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_27_1_mTi.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_280_1_In3.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_281_1_q9p.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_282_2_P2S.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_283_2_zot.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_284_1_oPl.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_285_3_J62.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_286_1_p3X.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_287_1_9bt.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_288_1_Mkr.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_289_1_Mmp.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_28_1_tgA.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_290_1_0w1.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_291_1_MnY.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_292_1_w9u.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_293_1_TZC.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_294_2_AfB.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_295_1_bfj.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_296_1_4N9.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_297_1_k8o.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_298_1_1YF.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_299_1_EIh.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_29_2_asa.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_2_1_ASG.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_300_1_pXs.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_301_1_eY3.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_302_1_yQq.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_303_1_Eq7.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_304_2_M6a.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_305_1_ZuO.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_306_1_aUC.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_307_1_2tX.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_308_2_c1s.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_309_1_ZlP.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_30_1_eRu.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_31_1_WN2.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_32_1_qQU.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_33_1_Ctq.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_34_1_pKR.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_35_1_P8f.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_36_1_6K9.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_37_1_WKe.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_38_1_pSd.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_39_1_Xvm.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_3_1_B1S.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_40_1_QE0.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_41_1_pDy.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_42_1_GxG.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_43_1_zwr.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_44_2_XKA.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_45_1_iQn.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_46_1_y00.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_47_1_48e.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_48_1_41O.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_49_1_fNp.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_4_1_T4k.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_50_1_GxX.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_51_1_10T.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_52_1_p09.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_53_1_IjB.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_54_1_p9c.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_55_1_UN2.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_56_1_ehj.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_57_1_65b.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_58_1_Qnt.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_59_1_J2U.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_5_1_piy.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_60_1_Lqc.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_61_1_bVU.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_62_1_jOp.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_63_1_a9O.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_64_1_kcg.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_65_1_dWU.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_66_1_3zd.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_67_1_eR8.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_68_1_QAk.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_69_1_Uiz.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_6_1_AEl.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_70_1_xtQ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_71_1_EmQ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_72_1_plo.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_73_1_T7d.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_74_1_LBB.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_75_1_DYX.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_76_1_slr.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_77_1_74C.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_78_1_LyG.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_79_1_9UQ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_7_1_oV8.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_80_1_PYx.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_81_1_7z9.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_82_1_3tM.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_83_1_ZY1.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_84_1_tFT.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_85_1_1Tc.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_86_1_Z0z.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_87_1_Oyg.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_88_1_7bm.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_89_1_4tu.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_8_1_RFf.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_90_1_SPx.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_91_1_lYd.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_92_1_3SC.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_93_1_Uxx.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_94_1_trE.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_95_1_CnS.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_96_1_RSV.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_97_1_zFn.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_98_1_7BI.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_99_1_dRZ.root",
"file:root://eoscms//eos/cms/store/group/phys_diffraction/FSQ-13-009/pAUPC/posrapidity/onia2MuMuPAT_9_1_9B6.root")


#options.inputFiles = 'file:/afs/cern.ch/work/d/ddutta/private/CMSSW_5_3_8_HI/src/HiSkim/HiOnia2MuMu/test/onia2MuMuPAT_paminbias.root'




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
                                isMC = cms.untracked.bool(False),
                                isPromptMC = cms.untracked.bool(False),

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

