import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.precision', 1)
pd.set_option('display.width', 100)


#all random occs first
def main(): 
    print(pd.__version__)
    column_names = ['atmtype', 'atmno', 'letter1', 'shortname', 'chain', 'num', 'x', 'y', 'z', 'occ', 'bfact', 'letter2']
    iline = pd.read_csv("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/randomocc2752.txt", 
                               names = column_names,
                               engine='python',
                               sep = '[ ]+')                               
    print(iline)
    
    occ = iline['occ']
    bfact = iline['bfact']
    
    plt.scatter(occ, bfact)
    plt.title("Pre occupancy refinement")
    plt.xlabel("Occupancy", fontsize=15)
    plt.ylabel("ADP", fontsize=15)
    plt.xlim([0.0, 1.0])
    plt.ylim([40, 200])
    plt.savefig("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/randomocc2752.png", format='png', bbox_inches='tight', dpi=300, alpha=0.5)
    plt.show()

main()

def main2(): 
    print(pd.__version__)
    column_names = ['atmtype', 'atmno', 'letter1', 'shortname', 'chain', 'num', 'x', 'y', 'z', 'occ', 'bfact', 'letter2']
    iline = pd.read_csv("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/randomocc2753.txt", 
                               names = column_names,
                               engine='python',
                               sep = '[ ]+')                               
    print(iline)
    
    occ = iline['occ']
    bfact = iline['bfact']
    
    plt.scatter(occ, bfact)
    plt.title("Pre occupancy refinement")
    plt.xlabel("Occupancy", fontsize=15)
    plt.ylabel("ADP", fontsize=15)
    plt.xlim([0.0, 1.0])
    plt.ylim([40, 200])
    plt.savefig("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/randomocc2753.png", format='png', bbox_inches='tight', dpi=300, alpha=0.5)
    plt.show()

main2()

def main3(): 
    print(pd.__version__)
    column_names = ['atmtype', 'atmno', 'letter1', 'shortname', 'chain', 'num', 'x', 'y', 'z', 'occ', 'bfact', 'letter2']
    iline = pd.read_csv("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/randomocc2754.txt", 
                               names = column_names,
                               engine='python',
                               sep = '[ ]+')                               
    print(iline)
    
    occ = iline['occ']
    bfact = iline['bfact']
    
    plt.scatter(occ, bfact)
    plt.title("Pre occupancy refinement")
    plt.xlabel("Occupancy", fontsize=15)
    plt.ylabel("ADP", fontsize=15)
    plt.xlim([0.0, 1.0])
    plt.ylim([40, 200])
    plt.savefig("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/randomocc2754.png", format='png', bbox_inches='tight', dpi=300, alpha=0.5)
    plt.show()

main3()

def main4(): 
    print(pd.__version__)
    column_names = ['atmtype', 'atmno', 'letter1', 'shortname', 'chain', 'num', 'x', 'y', 'z', 'occ', 'bfact', 'letter2']
    iline = pd.read_csv("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/randomocc2755.txt", 
                               names = column_names,
                               engine='python',
                               sep = '[ ]+')                               
    print(iline)
    
    occ = iline['occ']
    bfact = iline['bfact']
    
    plt.scatter(occ, bfact)
    plt.title("Pre occupancy refinement")
    plt.xlabel("Occupancy", fontsize=15)
    plt.ylabel("ADP", fontsize=15)
    plt.xlim([0.0, 1.0])
    plt.ylim([40, 200])
    plt.savefig("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/randomocc2755.png", format='png', bbox_inches='tight', dpi=300, alpha=0.5)
    plt.show()

main4()

def main5(): 
    print(pd.__version__)
    column_names = ['atmtype', 'atmno', 'letter1', 'shortname', 'chain', 'num', 'x', 'y', 'z', 'occ', 'bfact', 'letter2']
    iline = pd.read_csv("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/occrefine2752.txt", 
                               names = column_names,
                               engine='python',
                               sep = '[ ]+')                               
    print(iline)
    
    occ = iline['occ']
    bfact = iline['bfact']
    
    plt.scatter(occ, bfact)
    plt.title("Post occupancy refinement")
    plt.xlabel("Occupancy", fontsize=15)
    plt.ylabel("ADP", fontsize=15)
    plt.xlim([0.0, 1.0])
    plt.ylim([40, 200])
    plt.savefig("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/occrefine2752.png", format='png', bbox_inches='tight', dpi=300, alpha=0.5)
    plt.show()

main5()

def main6(): 
    print(pd.__version__)
    column_names = ['atmtype', 'atmno', 'letter1', 'shortname', 'chain', 'num', 'x', 'y', 'z', 'occ', 'bfact', 'letter2']
    iline = pd.read_csv("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/occrefine2753.txt", 
                               names = column_names,
                               engine='python',
                               sep = '[ ]+')                               
    print(iline)
    
    occ = iline['occ']
    bfact = iline['bfact']
    
    plt.scatter(occ, bfact)
    plt.title("Post occupancy refinement")
    plt.xlabel("Occupancy", fontsize=15)
    plt.ylabel("ADP", fontsize=15)
    plt.xlim([0.0, 1.0])
    plt.ylim([40, 200])
    plt.savefig("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/occrefine2753.png", format='png', bbox_inches='tight', dpi=300, alpha=0.5)
    plt.show()

main6()

def main7(): 
    print(pd.__version__)
    column_names = ['atmtype', 'atmno', 'letter1', 'shortname', 'chain', 'num', 'x', 'y', 'z', 'occ', 'bfact', 'letter2']
    iline = pd.read_csv("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/occrefine2754.txt", 
                               names = column_names,
                               engine='python',
                               sep = '[ ]+')                               
    print(iline)
    
    occ = iline['occ']
    bfact = iline['bfact']
    
    plt.scatter(occ, bfact)
    plt.title("Post occupancy refinement")
    plt.xlabel("Occupancy", fontsize=15)
    plt.ylabel("ADP", fontsize=15)
    plt.xlim([0.0, 1.0])
    plt.ylim([40, 200])
    plt.savefig("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/occrefine2754.png", format='png', bbox_inches='tight', dpi=300, alpha=0.5)
    plt.show()

main7()

def main8(): 
    print(pd.__version__)
    column_names = ['atmtype', 'atmno', 'letter1', 'shortname', 'chain', 'num', 'x', 'y', 'z', 'occ', 'bfact', 'letter2']
    iline = pd.read_csv("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/occrefine2755.txt", 
                               names = column_names,
                               engine='python',
                               sep = '[ ]+')                               
    print(iline)
    
    occ = iline['occ']
    bfact = iline['bfact']
    
    plt.scatter(occ, bfact)
    plt.title("Post occupancy refinement")
    plt.xlabel("Occupancy", fontsize=15)
    plt.ylabel("ADP", fontsize=15)
    plt.xlim([0.0, 1.0])
    plt.ylim([40, 200])
    plt.savefig("/dls/i23/data/2019/cm23006-3/processing/RUNNING/I19_2/results/refine9_20cyc_O1pcto99pc_Bpm30/occrefine2755.png", format='png', bbox_inches='tight', dpi=300, alpha=0.5)
    plt.show()
    
main8()

