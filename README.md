# SFSXplorer - Scoring Function Space eXplorer
# Installation
You need to have Python 3 installed on your computer to run SFSXplorer. In addition, you also need NumPy (1.14.5*), Matplotlib, scikit-learn (0.19.1*), and SciPy (1.1.0*).
*You can use higher versions as well.

Windows

Step 1. Download SFSXplorer 

Step 2. Unzip the zipped file SFSXplorer.zip

Step 3. Copy SFSXplorer directory to c:\ 

Step 4. Open a command prompt window and type: cd c:\SFSXplorer 

Step 5. Then type: python run_sfsxplorer.py 



Linux

Step 1. Download SFSXplorer

Step 2. Unzip the zipped file SFSXplorer.zip

Step 3. Copy SFSXplorer directory to the directory of your choice

Step 4. Open a terminal and type cd /your personal directory/SFSXplorer

Step 5. Then type: python run_sfsxplorer.py

That´s it, good exploration of the scoring function space. 

The program SFSXplorer allows us to explore the scoring function space. All necessary files to run SFSXplorer are in the zipped folder.
The input file sfs.in is shown below,

#Set up general parameters for SFSXplorer

chklig_in,Inputs/chklig.in

dataset_dir,F:\Projects\SFSXplorer2020e\Dataset\

scores_out,Outputs/scores_out.csv

sandres_out,Outputs/sandres_out.csv

binding_type,ki

#For electrostatic potential (set up parameters for arrays)

l_i,0.001787        # Initial value of lambda used in dieletric permittivity calculation (0.001787) (float)

l_f,0.003627        # Final value of lambda used in dieletric permittivity calculation (0.003627) (float)

n_l,5               # Number of elements of lambda used in dieletric permittivity calculation (5) (integer)

k_i,3.4781          # Initial value of k used in dieletric permittivity calculation (3.4781) (float)

k_f,7.7839          # Final value of k used in dieletric permittivity calculation (7.7839) (float)

n_k,5               # Number of elements of k used in dieletric permittivity calculation (5) (integer)

a_i,-20.929         # Initial value of A used in dieletric permittivity calculation (-20.929) (float)

a_f,-8.5525         # Final value of A used in dieletric permittivity calculation (-8.5525) (float)

n_a,5               # Number of elements of A used in dieletric permittivity calculation (5) (integer)

e0_i,70.0           # Initial value of epsilon0(e0) (70.0) (dielectric constant of bulk water at 25˚C e0 = 78.4) (float)

e0_f,78.4           # Final value of epsilon0(e0) (78.4) (dielectric constant of bulk water at 25˚C e0 = 78.4) (float)

n_e0,5              # Number of elements of epsilon0(e0) (5) (dielectric constant of bulk water at 25˚C e0 = 78.4) (float)

#For Solvatation potential (set up parameters for arrays)

m_sol_i,1           # Initial value of expoent m (1) (integer)

m_sol_f,4           # Final value of expoent m (4) (integer)

n_m_sol,4           # Number of elements of expoent m (4) (integer)

n_sol_i,1           # Initial value of expoent n (1) (integer)

n_sol_f,4           # Final value of expoent n (4) (integer)

n_n_sol,4           # Number of elements of expoent nnnnn (4) (integer)

sigma_sol_i,2.5     # Initial value of sigma used in desolvatation potential (2.5 Angtrom)

sigma_sol_f,5.5     # Final value of sigma used in desolvatation potential (5.5 Angstrom)

n_sigma_sol,4       # Number of elements of sigma used in desolvatation potential (5)


The first line brings the name of the chklig file, that has the list of the PDB files present in the dataset. The second line shows
the directory where the PDB files are.
The next two lines indicate the output files and the last line the type of binding affinity. The following lines bring specific information about each
energy term calculated by SFSXplorer.

The chklig.in is as follows,

#Type of binding information: ki

CHKLIG,1DWB,BEN,H,  1, 2.92

CHKLIG,1ETR,MIT,H,  1, 7.40
...

The first column is a keyword to indicate that this line brings ligand data. The second column shows the PDB access code, followed by
the ligand id, ligand chain, ligand number, and the binding affinity. The first line shows the type of binding affinity.


# Overview


<img src=https://azevedolab.net/resources/going_through_scoring_function_space_2018_11_30a.gif>

In our research, we see protein-ligand interaction as a result of the relation between the protein space (Smith, 1970) and the chemical space (Bohacek et al., 1996; Kirkpatrick & Ellis, 2004), and we propose to represent these sets as a unique complex system, where the application of computational methodologies may contribute to generate models to predict protein-ligand binding affinities. Such approaches have the potential to create novel semi-empirical force fields to predict binding affinity with superior predictive power when compared with standard methodologies. 

We propose to use the abstraction of a mathematical space composed of infinite computational models to predict ligand-binding affinity. We named this space as the scoring function space (Heck et al., 2017). By the use of supervised machine learning techniques is possible to explore this scoring function space and build a computational model targeted to a specific biological system. For instance, we created targeted-scoring functions for coagulation factor Xa (Xavier et al., 2016), cyclin-dependent kinases (de Ávila et al., 2017; Levin et al., 2018), HIV-1 protease (Pintro & de Azevedo, 2017), estrogen receptor (Amaral et al., 2018), cannabinoid receptor 1 (Russo & de Azevedo, 2018), and 3-dehydroquinate dehydratase (de Ávila & de Azevedo, 2018). We have also developed a scoring function to predict Gibbs free energy of binding for protein-ligand complexes (Bitencourt-Ferreira & de Azevedo, 2018). We developed the programs SAnDReS, SFSXplorer, and Taba to generate computational models to predict ligand-binding affinity. SAnDReS, SFSXplorer, and Taba are integrated computational tools to explore the scoring function space.        

Firstly, let´s consider the protein space composed of protein structures. This protein space can be represented by the protein structure space, as depicted by Hou et al. 2005 and shown below (Fig. 1). In this figure, elements of the protein structure space are represented by spheres. The sphere color represents the superfamilies of protein structures. Analysis of the protein structure space indicated that proteins with similar structures clustered together in this space. Also, the authors pointed out that the distribution of structural classes of this space followed closely that of the protein fold space.

<img src="https://azevedolab.net/resources/PNAS_2018_12_02a.jpg" height="300">
<I>Fig. 1. Protein structure space (Hou et al. 2005).</I>
<P>&nbsp;</P>

We take this finite protein space as a starting point to the application of the concept of scoring function space. The sequence of
figures below captures the main concepts necessary to understand the scoring function space. If we pick an element of the protein space,
for instance, the cyclin-dependent kinase family, we may identify all ligands that bind to this protein.

<img src="https://azevedolab.net/resources/sfs_azevedolab_2018_09_26_view1.gif" height="150">
<I>Fig. 2. Protein space (Heck et al. 2017).</I>
<P>&nbsp;</P>

Now, let’s consider the chemical space (Fig. 3), which is formed by small molecules that may bind or not to an element of the protein space (Bohacek et al., 1996; Dobson, 2004; Kirkpatrick & Ellis, 2004; Lipinski & Hopkins, 2004; Shoichet, 2004; Stockwell, 2004).


<img src="https://azevedolab.net/resources/sfs_azevedolab_2018_09_26_view2.gif" height="150">
<I>Fig. 3. Chemical space.</I>
<P>&nbsp;</P>

If we take into account a subspace of the chemical space composed of structures that bind to cyclin-dependent kinase family, it is easy to imagine an association involving the cyclin-dependent kinase and this subspace of the chemical space. We represent this relationship as an arrow from the protein space to the chemical space, as indicated below (Fig. 4). 

<img src="https://azevedolab.net/resources/sfs_azevedolab_2018_09_26_view3.gif" height="150">
<I>Fig. 4. Relationship between the protein and chemical spaces.</I>
<P>&nbsp;</P>

Finally, we consider a mathematical space composed of infinite scoring functions, each element of this space is a mathematical function that uses the atomic coordinates of protein-ligand complexes to predict the binding affinity. We indicate this relationship as an arrow from the scoring function space to the arrow indicating the relation between CDK and the chemical space, as shown below (Fig. 5).

<img src="https://azevedolab.net/resources/azevedolab_sfs_2018_09_21.png" height="300">
<I>Fig. 5. A view of the scoring function space as a way to develop a computational model to predict ligand-binding affinity. Structures of proteins available with the following PDB access codes: 2OW4, 2OVU, 2IDZ, 2GSJ, 2G85, 2A4l, 1ZTB, 1Z99, 1WE2, 1M73, 1FLH, and 1FHJ.</I>
<P>&nbsp;</P>

Moving forward, we propose that there exist at least one scoring function capable of predicting the ligand binding affinity of the elements of the chemical space for a component of the protein space. 
So, the basic idea is quite simple; we intend to identify an element of the scoring function space that predicts the binding affinity of a component of the protein space for all elements of the subspace of the chemical space composed of ligands for the element of the protein space.


<B>References</B>
<P>&nbsp;</P>

-Amaral MEA, Nery LR, Leite CE, de Azevedo Junior WF, Campos MM. Pre-clinical effects of metformin and aspirin on the cell lines of different breast cancer subtypes. Invest New Drugs. 2018; 36(5):782–796. 

-Bitencourt-Ferreira G, de Azevedo Jr. WF. Development of a machine-learning model to predict Gibbs free energy of binding for protein-ligand complexes. Biophys Chem. 2018; 240: 63–69.  

-Bohacek RS, McMartin C, Guida WC. The art and practice of structure-based drug design: a molecular modeling perspective. Med Res Rev. 1996; 16(1):3–50.

-de Ávila MB, Xavier MM, Pintro VO, de Azevedo WF. Supervised machine learning techniques to predict binding affinity. A study for cyclin-dependent kinase 2.  Biochem Biophys Res Commun. 2017; 494: 305–310.

-de Ávila MB, de Azevedo WF Jr. Development of machine learning models to predict inhibition of 3-dehydroquinate dehydratase. Chem Biol Drug Des. 2018;92:1468–1474.

-Dobson CM. Chemical space and biology. Nature. 2004; 432(7019):824–828. 

-Heck GS, Pintro VO, Pereira RR, de Ávila MB, Levin NMB, de Azevedo WF. Supervised Machine Learning Methods Applied to Predict Ligand-Binding Affinity. Curr Med Chem. 2017; 24(23): 2459–2470. 

-Hou J, Jun SR, Zhang C, Kim SH. Global mapping of the protein structure space and application in structure-based inference of protein function. Proc Natl Acad Sci U S A. 2005; 102(10):3651-6.

-Levin NMB, Pintro VO, Bitencourt-Ferreira G, Mattos BB, Silvério AC, de Azevedo Jr. WF. Development of CDK-targeted scoring functions for prediction of binding affinity. Biophys Chem. 2018; 235: 1–8. 

-Lipinski C, Hopkins A. Navigating chemical space for biology and medicine. Nature. 2004;432(7019):855–861. 

-Kirkpatrick P, Ellis C. Chemical Space. Nature 2004; 432:823  

-Pintro VO, Azevedo WF. Optimized Virtual Screening Workflow. Towards Target-Based Polynomial Scoring Functions for HIV-1 Protease. Comb Chem High Throughput Screen. 2017; 20(9): 820–827.   

-Russo S, De Azevedo WF. Advances in the Understanding of the Cannabinoid Receptor 1 - Focusing on the Inverse Agonists Interactions. Curr Med Chem. 2019; 26(10): 1908–1919. 

-Shoichet BK. Virtual screening of chemical libraries. Nature. 2004; 432(7019):862–865.

-Smith JM. Natural selection and the concept of a protein space. Nature. 1970; 225(5232): 563–564.

-Stockwell BR. Exploring biology with small organic molecules. Nature. 2004; 432(7019):846–854.

-Xavier MM, Heck GS, de Avila MB, Levin NM, Pintro VO, Carvalho NL, Azevedo WF Jr. SAnDReS a Computational Tool for Statistical Analysis of Docking Results and Development of Scoring Functions. Comb. Chem. High Throughput Screen. 2016; 19(10): 801–12.
