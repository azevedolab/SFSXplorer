#!/usr/bin/env python3
#
################################################################################
# SFSXplorer                                                                   #
# Scoring Function Space eXplorer                                              #
################################################################################
#
# Class to calculate intermolecular electrostatic potential based on 
# protein-ligand atomic coordinates in the PDBQT format. It uses 
# pair-wise energetic terms of the AutoDock4 Force Field 
# (Morris et al., 1998; 2009). Here we explore the Scoring Function Concept 
# (Ross et al., 2013; Heck et al., 2017; Bitencourt-Ferreira & de Azevedo Jr., 
# 2019; Veríssimo et al., 2022) to generate models to predict binding affinity
# for protein systems.
#
#
# References:
# Bitencourt-Ferreira G, de Azevedo WF Jr. Exploring the Scoring Function Space.
# Methods Mol Biol. 2019; 2053: 275–281.
#
# Heck GS, Pintro VO, Pereira RR, de Ávila MB, Levin NMB, de Azevedo WF.
# Supervised Machine Learning Methods Applied to Predict
# Ligand-Binding Affinity. Curr Med Chem. 2017; 24(23): 2459–2470.
#
# Morris GM, Goodsell D, Halliday R, Huey R, Hart W, Belew R, Olson A.
# Automated docking using a Lamarckian genetic algorithm and an
# empirical binding free energy function. J Comput Chem. 1998; 19:1639–1662.
#
# Morris GM, Huey R, Lindstrom W, Sanner MF, Belew RK, Goodsell DS, Olson AJ.
# AutoDock4 and AutoDockTools4: Automated docking with 
# selective receptor flexibility. J Comput Chem. 2009 Dec; 30(16): 2785–2591.
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

# Define PairwiseElecPot() class
class PairwiseElecPot(object):
    """Class to calculate pairwise electric potential energy based on the 
    Autodock4 force field"""
        
    # Define dist() method
    def dist(self,x1,y1,z1,x2,y2,z2):
        """Method to calculate Euclidian distance"""
                
        # Calculate Euclidian distance
        d = np.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

        # Return distance
        return d
        
    # Define epsilon0() method
    def epsilon0(self,r,l,k,A,e0):
        """Method to calcule sigmoidal distance-dependent dielectric function"""

        # Set up constants
        # taken from http://autodock.scripps.edu/faqs-help/manual/autodock-3-user-s-guide/AutoDock3.0.5_UserGuide.pdf
        # A = -8.5525
        # l = 0.003627
        # k = 7.7839
        # e0 = 78.4       # Dielectric constant of bulk water at 25˚C
        B = e0 - A

        # A sigmoidal distance-dependent dielectric function is used to model 
        # solvent screening,based on the work of Mehler and Solmajer.
        # Mehler, E.L. and Solmajer, T. (1991) “Electrostatic effects in 
        # proteins: comparison of
        # dielectric and charge models” Protein Engineering, 4, 903-910.
        e0_r = A + B/(1+k*np.exp(-l*B*r))

        # Return result
        return e0_r

    # Define epsilon0_tanh() method
    def epsilon0_tanh(self,r,l,k,A,e0):
        """Method to calcule distance-dependent dielectric function using 
        tanh"""

        # Set up constants
        # taken from http://autodock.scripps.edu/faqs-help/manual/autodock-3-user-s-guide/AutoDock3.0.5_UserGuide.pdf
        # A = -8.5525
        # l = 0.003627
        # k = 7.7839
        # e0 = 78.4       # Dielectric constant of bulk water at 25˚C
        B = e0 - A

        # A sigmoidal distance-dependent dielectric function is used to model 
        # solvent screening,based on the work of Mehler and Solmajer.
        # Mehler, E.L. and Solmajer, T. (1991) “Electrostatic effects in 
        # proteins: comparison of
        # dielectric and charge models” Protein Engineering, 4, 903-910.
        # e0_r = A + B/(1+k*np.exp(-l*B*r))
        # e0_r = A + B*(1/2+(k/2)*np.tanh(l*B*r/2))
        # e0_r = A + B*(1/2+(1/2)*np.tanh(l*B*r/2)) OK!
        # e0_r = A + B*(1/2+(1/2)*np.tanh(l*B*r/2))
        e0_r = A + B*(np.exp(l*B*r)-k*np.exp(-l*B*r))/(np.exp(l*B*r)+k*np.exp(-l*B*r))

        # Return result
        return e0_r
    
    # Define potential() method
    def potential(self,ligand,receptor,l,k,a,e0,log_w,tanh_w):
        """Method to calculate pairwise electric potential energy based on the
         AutoDock equation"""
        
        # Assign zero to v_r
        v_r = 0
        
        # Looping through ligand atoms
        for line_i in ligand:
            
            # Looping through receptor atoms
            for line_j in receptor:
                
                # Get atom type
                atom_i = line_i[77:79]
                atom_j = line_j[77:79]
                
                # Get atomic coordinate for i atom
                x_i = float(line_i[30:38])
                y_i = float(line_i[38:46])
                z_i = float(line_i[46:54])
                q_i = float(line_i[66:75])
                
                # Get atomic coordinate for j atom
                x_j = float(line_j[30:38])
                y_j = float(line_j[38:46])
                z_j = float(line_j[46:54])
                q_j = float(line_j[66:75])
                
                # Invoking dist() method
                r = self.dist(x_i,y_i,z_i,x_j,y_j,z_j)
                ep = log_w*self.epsilon0(r,l,k,a,e0) + tanh_w*self.epsilon0_tanh(r,l,k,a,e0)
                v = q_i*q_j/(r*ep) 
                
                # Calculate potential for all atoms
                v_r += v
                
        # Return result
        return v_r