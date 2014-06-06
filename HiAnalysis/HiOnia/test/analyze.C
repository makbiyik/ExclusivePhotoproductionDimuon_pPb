#define MyClass_cxx
#include "MyClass.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <iostream>


void analyze(){
   MyClass t;
   t.Loop();
}

void MyClass::Loop()
{

   Long64_t nentries = fChain->GetEntriesFast();
   nentries = 471188;

   Long64_t nbytes = 0, nb = 0;   
   
   TH1::SetDefaultSumw2();
    
   TFile* outf;
    outf = new TFile("hsignal.root","recreate");
  
   TH1D * hsignal = new TH1D("hsignal","Track Eta",100,-3,3);
   TH1D * hbkg = new TH1D("hbkg","Track Eta",100,-3,3);
   TNtuple * t= new TNtuple("nt","HLT_L1","pt:m:y:l1:l2:nHLT_L2Mu0:extra1cm:extra5mm");

   TCanvas *c1=new TCanvas("c1","demo of Trees",10,10,800,800);
   c1->Divide(1,1);
   for (Long64_t jentry=0; jentry<nentries;jentry++) {

      nb = fChain->GetEntry(jentry);   nbytes += nb;

      if(nPrimVertexCand != 1){
	 //	 cout<<"Too many vertex"<<endl;
	 continue;
      }

      double E[2] = {0,0};
      double mumass =0.1057;
      
      E[0] = sqrt (MuonCand_p[0]*MuonCand_p[0]+mumass*mumass);       
      E[1] = sqrt (MuonCand_p[1]*MuonCand_p[1]+mumass*mumass); 
      
      TLorentzVector v1 (MuonCand_px[0],MuonCand_py[0],MuonCand_pz[0],E[0]);    
      TLorentzVector v2 (MuonCand_px[1],MuonCand_py[1],MuonCand_pz[1],E[1]);          
      TLorentzVector vsum = v1+v2;
      
      t->Fill(vsum.Pt(),vsum.M(),vsum.Rapidity(),HLT_L1DoubleMu0,HLT_L2DoubleMu0,nHLTL2DiMu0MuonCand,MuMu_extratracks1cm,MuMu_extratracks5mm);
      
      if(2.8<MuMu_mass && MuMu_mass<3.3){
	 hsignal->Fill(vsum.Rapidity());
      }
      
      if(2.55<MuMu_mass && MuMu_mass<2.8 || 3.3<MuMu_mass && MuMu_mass<3.55){
	 hbkg->Fill(vsum.Rapidity());
      }
      
      cout<<"Number of rapidity: "<<vsum.Rapidity()<<endl;
      
      cout<<"Number of vsummass: "<<vsum.M()<<endl;
      cout<<"Number of MuMu_mass: "<<MuMu_mass<<endl;
      cout<<"Number of MuonCand: "<<nMuonCand<<endl;
      cout<<"---------------"<<endl;
            
   }
   
   outf->cd(); 
   c1->cd(1);
   c1->Update();
   outf->Write();
   
//hsignal->Draw();
 
}
