
#include "analysis_upc_Dimuon.C"
#include "analysisUPC_Comparison.C"

void Efficiency_data_mc(const char* algo = "STARLIGHT",const char* label = "PLOT"){
 
  const char* hist_acceptanceratio= "hR";
  const char*hist_data_merge="hMuMu_data_pPb_Pbp_m";
  const char* hist_gen ="h_gen_sum";

  TH1::SetDefaultSumw2();
  using namespace std;
 
  
  TFile*outf;
  TFile*inf_acceptanceratio = new TFile("compare_data_mc.root");
  TFile*inf_data_merge = new TFile("analysis_upc_sum.root");//infa Reco
  TFile*inf_gen = new TFile("compare_data_mc.root");//Gen
  TH1D*h_ratio = (TH1D*)inf_acceptanceratio->Get(hist_acceptanceratio);
  TH1D*h_data_merge= (TH1D*)inf_data_merge->Get(hist_data_merge);
  TH1D*h_gen = (TH1D*)inf_gen->Get(hist_gen);
  
   cout << h_ratio->GetBinWidth(1)  << " " << h_data_merge->GetBinWidth(1) << endl;
   cout << h_ratio->GetBinWidth(1)  << " " << h_gen->GetBinWidth(1) << endl;




  /*  TH1D* h_ratio_sum = new TH1D("hR_sum", "hR_sum", h_ratio->GetNbinsX()*2, h_ratio->GetXaxis()->GetXmin(), 
  	                                            h_ratio_25_50->GetXaxis()->GetXmax());
						    
						    cout << h_ratio->GetBinWidth(1)  << " " << h_ratio_25_50->GetBinWidth(1) << endl;
						    cout << h_ratio->GetXaxis()->GetXmin() << " " << h_ratio->GetXaxis()->GetXmax() << endl;
						    cout << h_ratio_25_50->GetXaxis()->GetXmin() << " " << h_ratio_25_50->GetXaxis()->GetXmax() << endl;
						    // h_ratio_25_50->GetXaxis()->GetXmax()
						    */


 
  outf= new TFile("Efficiency_data_mc.root","recreate");
  outf->cd();
  
  h_ratio->SetLineColor(kRed+1);
  h_ratio->SetMarkerColor(kRed+1);
  h_data_merge->SetLineColor(1);
  h_data_merge->SetMarkerColor(1);
  h_gen->SetLineColor(kBlue+1);
  h_gen->SetMarkerColor(kBlue+1);

  /*
  for (int iBin=0; iBin<h_ratio->GetNbinsX(); ++iBin) {
  h_ratio_sum->SetBinContent(iBin+1, h_ratio->GetBinContent(iBin+1));
  h_ratio_sum->SetBinContent(iBin+1+h_ratio->GetNbinsX(), h_ratio_25_50->GetBinContent(iBin+1));
  }*/
  //  h_ratio_sum->Add(h_ratio);
  //  h_ratio_sum->Add(h_ratio_25_50);
  
  h_ratio->GetXaxis()->SetRangeUser(10,50);
  TCanvas * ctest = new TCanvas("test");
  ctest->Divide(3);
  ctest->cd(1);
  h_data_merge->Draw();
  ctest->cd(2);
  h_ratio->Draw();
  //h_ratio_25_50->Draw();

  ctest->cd(3);
  h_gen->Draw();

  TH1D*hR= (TH1D*)h_data_merge->Clone("hR"); hR->Sumw2();
  
  TH1::SetDefaultSumw2();
  using namespace std;
  const double accept = 0.222715 ;
  const double lumi = 34.6;
 hR->Scale(lumi);
 hR->Divide(h_ratio); 
 hR->Divide(h_gen);

  //h_gen->Scale(1./h_gen->GetBinWidth(1));
  //hR->Scale(1./accept);
  //hR->Scale(1./hR->GetBinWidth(1));
  //hR->SetXTitle("Rapidity #mu_{+} #mu_{-} (GeV/c)");
 
 hR->SetXTitle("Mass(GeV/c^{2} #mu_{+}#mu_{-}");
 hR->GetXaxis()->SetRangeUser(10,50);

  //hR->SetLineColor(kRed+1);
  //hR->SetLineWidth(2);
 hR->SetMarkerStyle(20);
 hR->SetMarkerSize(1.0);
  //hR->GetXaxis()->SetTitle(" Mass  #mu_{+} #mu_{-} (GeV/c^{2})");
 hR->GetYaxis()->SetTitle("Lumi integrated");
 hR->GetXaxis()->SetRangeUser(10,50);
 //hR->Rebin(5);

 hR->Rebin(5);
 hR->Scale(1./5);
 
 TLegend *leg2=new TLegend(0.12,0.76,0.35,0.87);
  leg2->AddEntry(h_data_merge,"pPb #sqrt{S_{NN}}=5.02 TeV","");
  leg2->AddEntry(h_data_merge,"CMS own work","");
  leg2->SetFillColor(0);
  //leg2->SetLineWidth(2);
  leg2->SetBorderSize(0);
  leg2->SetFillStyle(0);
  leg2->SetTextFont(23);
  leg2->SetTextSize(14);
  TLegend *t3=new TLegend(0.60,0.67,0.99,0.87);
  //t3->AddEntry(h1c,label,"mass");
  
  t3->AddEntry(h_data_merge,"Data","l");
  t3->AddEntry(h_ratio,"L/1/nb","l");
  t3->AddEntry(h_gen,"Gen","l");
  t3->AddEntry(h_data_merge,algo,"");
  t3->SetFillColor(0);
  //t3->SetLineWidth(2);
  t3->SetBorderSize(0);
  t3->SetFillStyle(0);
  t3->SetTextFont(23);
  t3->SetTextSize(14);
  TLegend *t1=new TLegend(0.60,0.67,0.89,0.87);
  //t1->AddEntry(hR,"");
  
  //t1->AddEntry(hR,"MC","");
  t1->AddEntry(hR,algo,"");
  t1->SetFillColor(0);
  t1->SetBorderSize(0);
  t1->SetFillStyle(0);
  t1->SetTextFont(23);
  t1->SetTextSize(14);
  gStyle->SetOptStat(0);

  TCanvas* c2 = new TCanvas("c2","The Ntuple can",400,400); c2->cd();

  TF1* fitFunc = new TF1("fitFunc", "[0]", 0, 1000);
  fitFunc->SetLineWidth(3);
  fitFunc->SetLineColor(kRed);
 hR->Fit(fitFunc);
   
  
 hR->Draw();
  t1->Draw(); 
  leg2->Draw(); 
  outf->Write();
 
  //c2->Print(Form("/afs/cern.ch/work/m/makbiyik/public/UPC_event_Hiskim/d0725/CMSSW_5_3_8_HI_patch2/src/UPC_V01/d0317/Figure_d0404/figure_ratio_%s.gif",algo,h_data_merge));

}
