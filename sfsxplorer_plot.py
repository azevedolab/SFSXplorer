#!/usr/bin/env python3
#
################################################################################
# SFSXplorer                                                                   #
# Scoring Function Space eXplorer                                              #
################################################################################
#
################################################################################
# Dr. Walter F. de Azevedo, Jr.                                                #
# https://azevedolab.net/                                                      #
# January 12, 2023                                                             #
################################################################################
#
# To plot Lennard-Jones potentials
# python3 sfsxplorer_plot.py misc/inputs/plot_parameters_LJ.in plots/lj.pdf 1000 > plot_LJ.log &
#
# To plot hydrogen-bond potentials
# python3 sfsxplorer_plot.py misc/inputs/plot_parameters_HB.in plots/hb.pdf 1000 > plot_HB.log &
#
# To plot electrostatic potentials (setup 01)
# python3 sfsxplorer_plot.py misc/inputs/plot_parameters_ELE1.in plots/ele1.pdf 1000 > plot_ELE1.log &
#
# To plot electrostatic potentials (setup 02)
# python3 sfsxplorer_plot.py misc/inputs/plot_parameters_ELE2.in plots/ele2.pdf 1000 > plot_ELE2.log &
#
# To plot electrostatic potentials (setup 03)
# python3 sfsxplorer_plot.py misc/inputs/plot_parameters_ELE3.in plots/ele3.pdf 1000 > plot_ELE3.log &
#
# To plot desolvatation potentials
# python3 sfsxplorer_plot.py misc/inputs/plot_parameters_DESOL.in plots/desol.pdf 1000 > plot_DESOL.log &
#
# To plot all potentials (setup 01)
# python3 sfsxplorer_plot.py misc/inputs/plot_parameters_ALL1.in plots/all1.pdf 1000 > plot_ALL1.log &
#
# To plot all potentials (setup 02)
# python3 sfsxplorer_plot.py misc/inputs/plot_parameters_ALL2.in plots/all2.pdf 1000 > plot_ALL2.log &
#
# To plot all potentials (setup 03)
# python3 sfsxplorer_plot.py misc/inputs/plot_parameters_ALL3.in plots/all3.pdf 1000 > plot_ALL3.log &
#
# To plot dieletric permittivity functions
# python3 sfsxplorer_plot.py misc/inputs/plot_parameters_EPSILON.in plots/epsilon.pdf 1000 > plot_EPSILON.log &
#
# Import section
import sys
from SFSXplorer import plot_potentials as pp

# Define main()
def main():

    # Get input files from terminal
    plot_in = sys.argv[1]       # Input file with plotting parameters
    plot_out = sys.argv[2]      # Output plot file (eg., lj.pdf, lj.png)
    dpi_in = int(sys.argv[3])   # DPI for plotting

    # Instantiate an object of the Plot_V class
    potentials = pp.Plot_V(plot_in,plot_out,dpi_in)

    # Call read_plot_parameters()
    potentials.read_plot_parameters()

    # Call gen_plot()
    potentials.gen_plot()

main()