module load phenix

#phenix.refine I18.pdb I18.mtz main.number_of_macro_cycles=25 refinement.input.xray_data.high_resolution=2.06 refinement.refine.strategy=individual_sites+individual_adp+occupancies refinement.group_occupancy.number_of_macro_cycles=100

#phenix.refine I18.pdb I18.mtz refine.eff

#phenix.refine I18.pdb I18.mtz main.number_of_macro_cycles=10 refinement.input.xray_data.high_resolution=2.06 refinement.refine.strategy=individual_adp+occupancies adp.individual.isotropic=all
phenix.refine FutA.pdb FutA.mtz main.number_of_macro_cycles=50 refinement.input.xray_data.high_resolution=1.50 refinement.refine.strategy=individual_adp+occupancies+individual_sites

