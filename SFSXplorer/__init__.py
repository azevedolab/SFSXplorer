#!/usr/bin/env python3
#
################################################################################
# SFSXplorer                                                                   #
# Scoring Function Space eXplorer                                              #
################################################################################
#
# SFSXplorer reads input files generated by SAnDReS 2.0 (Xavier et al., 2016)
# (pdbqt and bind_#####.csv files) to create targeted scoring functions
# (Seifert, 2009). This program calculates energy terms loosely based on the
# AutoDock 4 Force Field (Morris et al., 1998; 2009) to explore the
# Scoring Function Space concept (Ross et al., 2013; Heck et al., 2017;
# Bitencourt-Ferreira & de Azevedo Jr., 2019; Veríssimo et al., 2022). We may
# vary the exponents of van der Waals and hydrogen-bond potentials and the
# parameters used to determine the electrostatic (Bitencourt-Ferreira & de
# Azevedo Jr., 2021) and desolvation potentials.
#
# References:
# Bitencourt-Ferreira G, de Azevedo WF Jr. Exploring the Scoring Function Space.
# Methods Mol Biol. 2019; 2053: 275–281.
#
# Bitencourt-Ferreira G, de Azevedo Junior WF. Electrostatic Potential Energy in
# Protein-Drug Complexes. Curr Med Chem. 2021; 28(24): 4954–4971.
#
# Heck GS, Pintro VO, Pereira RR, de Ávila MB, Levin NMB, de Azevedo WF.
# Supervised Machine Learning Methods Applied to Predict Ligand-Binding
# Affinity. Curr Med Chem. 2017; 24(23): 2459–2470.
#
# Morris GM, Goodsell D, Halliday R, Huey R, Hart W, Belew R, Olson A.
# Automated docking using a Lamarckian genetic algorithm and an empirical
# binding free energy function. J Comput Chem. 1998; 19: 1639–1662.
#
# Morris GM, Huey R, Lindstrom W, Sanner MF, Belew RK, Goodsell DS, Olson AJ.
# AutoDock4 and AutoDockTools4: Automated docking with
# selective receptor flexibility. J Comput Chem. 2009; 30(16): 2785–2791.
#
# Ross GA, Morris GM, Biggin PC. One Size Does Not Fit All: The Limits of
# Structure-Based Models in Drug Discovery. J Chem Theory Comput. 2013; 9(9):
# 4266–4274.
#
# Seifert MH. Targeted scoring functions for virtual screening. Drug Discov
# Today. 2009; 14(11-12): 562–569.
#
# Xavier MM, Heck GS, Avila MB, Levin NMB, Pintro VO, Carvalho NL, Azevedo WF.
# SAnDReS: a Computational Tool for Statistical Analysis of Docking Results and
# Development of Scoring Functions. Comb Chem High Throughput Screen. 2016;
# 9(10):801–812.
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
################################################################################
#
#  GNU General Public License
#  This file is part of SFSXplorer.
#
#    SFSXplorer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    SFSXplorer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with SFSXplorer. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
#
# Contact
# SFSXplorer and SAnDReS are in continuous development. Please, feel free to
# download the latest versions (https://github.com/azevedolab/) and use them in
# your machine-learning modeling. If you have any questions regarding SFSXplorer
# and SAnDReS, please e-mail me: at walter@azevedolab.net.
#
#
# Funding
# Funding Agency: Conselho Nacional de Desenvolvimento Científico e Tecnológico-
# National Counsel of Technological and Scientific Development (www.cnpq.br)
# Principal Investigator : Walter F. de Azevedo Jr., Ph.D
# Process Numbers: 472590/2012-0, 308883/2014-4, 309029/2018-0, and
# 306298/2022-8.
#
################################################################################
#
# Show message about SFSXplorer
print("""
SFSXplorer: A Python package for exploration of the Scoring Function Space.
Developed by Dr. Walter F. de Azevedo, Jr.
https://azevedolab.net/sfsxplorer.php
""")