import ROOT as r
import sys

def python_example(samples=10000):
    # Histogram filled with a normal distribution
    #r.gStyle.SetOptStat(0)  # turn off default stats box in histograms
    
    tr = r.TRandom3()
    hist1 = r.TH2F("hist1","random gauss;x;y",100,50,150,100,50,150)
    fpeak = r.TF2("fpeak","exp(-0.5*(x-[0])*(x-[0])/[2]/[2] - 0.5*(y-[1])*(y-[1])/[3]/[3])",50,150,50,150)
    fpeak.SetParameters(100,100,6,6)
    hist1.FillRandom("fpeak",samples)
    tc1 = r.TCanvas("c1","Canvas1")
    hist1.Draw("COLZ")
    tc1.Update()

    # A multi panel plot
    tc2 = r.TCanvas("c2","Canvas2")
    tc2.Divide(2,2)  # divide in to 2x2 panels
    tc2.cd(1)
    hist1.Draw("COLZ")

    # add a random uniform offset to the histogram
    hist2 = hist1.Clone("hist2")
    hist2.SetTitle("Gauss+offset;x;y")
    for i in range(samples//3):
        hist2.Fill(tr.Uniform(50,150), tr.Uniform(50,150))
    tc2.cd(2)
    hist2.Draw("COLZ")

    # apply an offset to give us a 1/x^2 baseline
    hist3 = hist1.Clone("hist3")
    hist3.SetTitle("Gauss+offset2;x;y")
    base2 = r.TF1("base2","1/x/x",1,10)
    for i in range(samples*30):
        x = base2.GetRandom()*10+40;
        y = base2.GetRandom()*10+40
        hist3.Fill(x,y)
    tc2.cd(3).SetLogy()
    hist3.Draw("COLZ")

    # a double gaussian
    hist4 = hist1.Clone("hist4")
    hist4.SetTitle("Double Gaussian;x;y")
    fpeak.SetParameters(1,1,20,20)
    hist4.FillRandom("fpeak",samples//2)
    tc2.cd(4)
    hist4.Draw("COLZ")

    tc2.Update()
    input("hit 'return' to continue")

    # save our plot outputs
    tc2.SaveAs("canvas2d_py.png")
    
if __name__ == '__main__':
    samples=10000
    if len(sys.argv)>1: samples=int(sys.argv[1])
    python_example(samples)
