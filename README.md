# SFSXplorer - Scoring Function Space eXplorer
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

The program SFSXplorer allows us to explore the scoring function space. All necessary files to run SFSXplorer are in the zipped folder.
The input file sfs.in is shown below,

chklig_in,chklig.in

dataset_dir,/Users/labioquest/Desktop/AutoDock3_Dataset/Dataset/

scores_out,scores_out.csv

sandres_out,sandres_out.csv

binding_type,ki


The first line brings the name of the chklig file, that brings the list of thd PDB files present in the dataset. The second line shows
the directory where the PDB files are.
The follwing two lines indicate the output files and the last line the type of binding affinity.
The chklig.in is as follows,

/# Type of binding information: ki

CHKLIG,1DWB,BEN,H,  1, 2.92

CHKLIG,1ETR,MIT,H,  1, 7.40

...


The first column is a keyword to indicate that this line brings ligand data. The second column shows the PDB access code, followed by
the ligand id, ligand chain, ligand number, and the binding affinity. The firt line shows the type of binding affinity.

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

-Russo S, de Azevedo WF. Advances in the Understanding of the Cannabinoid Receptor 1 - Focusing on the Inverse Agonists Interactions. Curr Med Chem. 2018. doi: 10.2174/0929867325666180417165247 

-Shoichet BK. Virtual screening of chemical libraries. Nature. 2004; 432(7019):862–865.

-Smith JM. Natural selection and the concept of a protein space. Nature. 1970; 225(5232): 563–564.

-Stockwell BR. Exploring biology with small organic molecules. Nature. 2004; 432(7019):846–854.

-Xavier MM, Heck GS, de Avila MB, Levin NM, Pintro VO, Carvalho NL, Azevedo WF Jr. SAnDReS a Computational Tool for Statistical Analysis of Docking Results and Development of Scoring Functions. Comb. Chem. High Throughput Screen. 2016; 19(10): 801–12.


