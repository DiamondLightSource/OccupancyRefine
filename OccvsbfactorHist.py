import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.precision', 1)
pd.set_option('display.width', 100)



def main(): 
    print(pd.__version__)
    column_names = ['atmtype', 'atmno', 'letter1', 'shortname', 'chain', 'num', 'x', 'y', 'z', 'occ', 'bfact', 'letter2']
    iline = pd.read_csv("/dls/i23/data/2019/cm23006-3/processing/RUNNING/FutA/results/run1_occandbfactonly/randomocc.txt", 
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
    plt.ylim([1, 100])
#    plt.show()
    plt.savefig("/dls/i23/data/2019/cm23006-3/processing/RUNNING/FutA/results/run1_occandbfactonly/randomocc.png", format='png', bbox_inches='tight', dpi=300, alpha=0.5)
    plt.show()

main()


def main2(): 
    print(pd.__version__)
    column_names = ['atmtype', 'atmno', 'letter1', 'shortname', 'chain', 'num', 'x', 'y', 'z', 'occ', 'bfact', 'letter2']
    iline = pd.read_csv("/dls/i23/data/2019/cm23006-3/processing/RUNNING/FutA/results/run1_occandbfactonly/occrefine.txt", 
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
    #plt.xlim([0.0, 1.0])
    #plt.ylim([1, 100])
#    plt.show()
    plt.savefig("/dls/i23/data/2019/cm23006-3/processing/RUNNING/FutA/results/run1_occandbfactonly/occrefine.png", format='png', bbox_inches='tight', dpi=300, alpha=0.5)
    plt.show()

main2()
