#!/usr/bin/env python3
#
################################################################################
# SFSXplorer                                                                   #
# Scoring Function Space eXplorer                                              #
################################################################################
#
# Class to calculate intermolecular van der Waals potential based on 
# atomic coordinates in the PDBQT format. It calculates the potential energy 
# based on Assisted Model Building with Energy Refinement (AMBER) force field 
# (Cornell et al., 1995) using the energy terms derived from the AutoDock4 
# (Morris et al., 1998; 2009). The traditional 12/6 potential energy is 
# modified to adapt to the data used to train the scoring function. We vary the
# exponents (m and n parameters) to scan the Scoring Function Space 
# (Ross et al., 2013; Heck et al., 2017; Bitencourt-Ferreira & de Azevedo Jr., 
# 2019; Veríssimo et al., 2022) to find the van der Waals potential adequate 
# to a targeted protein system.
#
# References:
# Bitencourt-Ferreira G, de Azevedo WF Jr. Exploring the Scoring Function Space. 
# Methods Mol Biol. 2019; 2053: 275-281.
#
# Cornell WD, Cieplak P, Bayly CI, Gould IR, Merz KM Jr, Ferguson DM, Spellmeyer
#  DC, Fox T, Caldwell JW, Kollman PA (1995). A Second Generation Force Field 
# for the Simulation of Proteins, Nucleic Acids, and Organic Molecules. 
# J Am Chem Soc. 1995; 117 (19): 5179–5197.
#
# Heck GS, Pintro VO, Pereira RR, de Ávila MB, Levin NMB, de Azevedo WF. 
# Supervised Machine Learning Methods Applied to Predict Ligand-Binding 
# Affinity. Curr Med Chem. 2017;24(23):2459–2470.
#
# Morris GM, Goodsell D, Halliday R, Huey R, Hart W, Belew R, Olson A. 
# Automated docking using a Lamarckian genetic algorithm and an empirical 
# binding free energy function. J Comput Chem. 1998; 19:1639–1662.
#
# Morris GM, Huey R, Lindstrom W, Sanner MF, Belew RK, Goodsell DS, Olson AJ. 
# AutoDock4 and AutoDockTools4: Automated docking with 
# selective receptor flexibility. J Comput Chem. 2009; 30(16): 2785–2791.
#
# Ross GA, Morris GM, Biggin PC. One Size Does Not Fit All: The Limits of 
# Structure-Based Models in Drug Discovery. J Chem Theory Comput. 2013; 9(9): 
# 4266–4274.  
#
# Veríssimo GC, Serafim MSM, Kronenberger T, Ferreira RS, Honorio KM, 
# Maltarollo VG. Designing drugs when there is low data availability: 
# one-shot learning and other approaches to face the issues of a 
# long-term concern. Expert Opin Drug Discov. 2022; 17(9): 929–947. 
# 
################################################################################
# Dr. Walter F. de Azevedo, Jr.                                                #
# https://azevedolab.net/                                                      #
# January 12, 2023                                                             #
################################################################################
#
# Import section
import numpy as np

# Define PairwisePot() class
class PairwisePot(object):
    """Class to calculate pairwise potential energy for van der Waals 
        interactions based on the assisted Model Building with Energy Refinement
        (AMBER) force field (Cornell et al., 1995)"""
        
    # Define potential() method (it is better to follow n=12,m=6) 
    def potential(self,reqm_i,epsilon_i,reqm_j,epsilon_j,r,n,m):
        """Method to calculate pairwise potential energy based on the
            assisted Model Building with Energy Refinement (AMBER) force 
            field (Cornell et al., 1995).
            
            Inputs
            reqm_i      : Sum of vdW radii of two like atoms (in Angstrom)
            epsilon_i   : Well depth (in Kcal/mol)
            reqm_j      : Sum of vdW radii of two like atoms (in Angstrom)
            epsilon_j   : Well depth (in Kcal/mol)
            r           : Intermolecular distance
            m           : Attraction expoent (6)
            n           : Repulsion expoent (12)
            
            Outputs
            cn, cm      : cn and cm are constants whose values depend on the 
                          depth of the energy well and the equilibrium 
                          separation of the two atoms’ nuclei.
            v           : van der Waals potential energy
            """
                
        # To obtain the Rij value for non H-bonding atoms
        reqm = 0.5*(reqm_i+reqm_j)
        
        #  To obtain the epsilon value for non H-bonding atoms
        epsilon = np.sqrt(epsilon_i*epsilon_j)
        
        # Calculate cm and cn parameters if n != m
        if n != m:
            cm = (n/(n-m))*epsilon*reqm**m 
            cn = (m/(n-m))*epsilon*reqm**n
        else:
            return None,None,None
                
        # Calculate v(r)        
        v = cn/r**n - cm/r**m
        
        # Return results
        return cn,cm,v