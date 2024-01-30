# SFSXplorer - Scoring Function Space eXplorer
SFSXplorer is a Python package to explore the concept of Scoring Function Space (SFS). We apply the SFS concept to build a computational model targeted to a specific protein system (targeted-scoring function). SFSXplorer employs binding affinity data and protein-ligand structures (docked or crystallographic) to train machine learning models to predict binding affinity. We base this SFS exploration on a flexible polynomial scoring function. We have the versatility to vary the energy terms in the polynomial equation, which makes available unexplored regions of the SFS. 
# Installing
We describe installation and tutorials running on Linux. For more information see <a href="https://azevedolab.net/resources/sfsxplorer_2023.pdf" title ="SFSXplorer User Guide">SFSXplorer User Guide</a>
You should type all commands shown here in a Linux terminal. The easiest way to open
a Linux terminal is to use the Ctrl+Alt+T key combination.

<B>Step 1</B>. Download Anaconda Installer for Linux <a href="https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh" title="Anaconda Installer for Linux">here</a>.

Go to the directory where you have the installer file and type the following commands:
<pre><I>    chmod u+x Anaconda3-2021.11-Linux-x86_64.sh
    ./Anaconda3-2021.11-Linux-x86_64.sh</I></pre>
<P>Follow the instructions of the installer. You may use a newer installer, but be sure to have the right installer in the above command lines.
</P>
<B>Step 2.</B> To run SFSXplorer properly, you need <a href="https://scikit-learn.org/stable/" title="Scikit-Learn. Machine Learning in Python">Scikit-Learn</a> 1.4.0. To be sure you have
version 1.4.0, open a terminal, and type the following commands:
<pre><I>    python3 -m pip uninstall scikit-learn
    python3 -m pip install scikit-learn==1.4.0</I></pre>
    
<P><B>Step 3</B>. Download SFSXplorer <a href="https://github.com/azevedolab/SFSXplorer/raw/master/sfs.zip" title="Zipped folder with SFSXplorer">here</a>. Copy the sfs zipped directory (<a href="https://github.com/azevedolab/SFSXplorer/raw/master/sfs.zip" title="Zipped folder with SFSXplorer">sfs.zip</a>) to wherever you want it and unzip the zipped directory.
Type the following command:</P>
<pre><I>    unzip sfs.zip</I></pre>
<P>Now you have SFSXplorer ready to run. Please access SFSXplorer User Guide <a href="https://azevedolab.net/resources/sfsxplorer_2023.pdf" title ="SFSXplorer User Guide">here</a> for tutorials and details about input files and commands to run it.
