<H1>SFSXplorer: Scoring Function Space eXplorer</H1>
SFSXplorer is a Python package to explore the concept of Scoring Function Space (SFS). We apply the SFS concept to build a computational model targeted to a specific protein system (targeted-scoring function). SFSXplorer employs binding affinity data and protein-ligand structures (docked or crystallographic) to train machine learning models to predict binding affinity. We base this SFS exploration on a flexible polynomial scoring function. We have the versatility to vary the energy terms in the polynomial equation, which makes available unexplored regions of the SFS. 

<H2>Installing</H2>
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
<br> </br>
<H2>Additional Material Related to SFSXplorer</H2>
<a href = "https://doi.org/10.1007/978-1-0716-4949-7" title = "de Azevedo WF Jr, editor. Docking screens for drug discovery. 2nd ed. New York, NY: Springer; 2026.">
<img src="https://github.com/azevedolab/Docking/blob/2f26462b425b5050871ac6be258a46f7f4088584/docking_screens_2nd_ed_cover.png" width=200 align=left title="de Azevedo WF Jr, editor. Docking screens for drug discovery. 2nd ed. New York, NY: Springer; 2026."></a>
<p>
de Azevedo WF Jr, editor. Docking screens for drug discovery. 2nd ed. New York, NY: Springer; 2026. <a href = "https://doi.org/10.1007/978-1-0716-4949-7" title = "de Azevedo WF Jr, editor. Docking screens for drug discovery. 2nd ed. New York, NY: Springer; 2026.">DOI: 10.1007/978-1-0716-4949-7</a>
</p>
<a href="https://www.amazon.com/Docking-Screens-Discovery-Methods-Molecular/dp/1071649485/">
<img src="https://github.com/azevedolab/Docking/blob/main/amazon_logo_01.png" width=100 align=left title="de Azevedo WF Jr, editor. Docking screens for drug discovery. 2nd ed. New York, NY: Springer; 2026."></a>
<br> </br>
<br> </br>
<br> </br>
<br> </br>
<br> </br>
<br> </br>
<h2>Prof. Dr. Walter F. de Azevedo, Jr.</h2>
<img src="https://drive.usercontent.google.com/download?id=1ao9REI0b_bCbjDy2pu4k3Tbr35LCB5Qt&export=view&authuser=0" width=200 align=left title="Walter Filgueira de Azevedo, Jr. October 02, 2024. Alfenas-MG. Brazil."></a>
<p>
My scientific interests are interdisciplinary, with three main emphases: <a href = "https://doi.org/10.3390/molecules24030637" title = "Nussinov R, Tsai CJ, Shehu A, Jang H. Computational Structural Biology: Successes, Future Directions, and Challenges. Molecules. 2019 Feb 12;24(3):637. doi: 10.3390/molecules24030637">computational structural biology</a>, <a href = "https://www.ibm.com/topics/artificial-intelligence" title = "What is AI?">artificial intelligence</a>, and <a href = "http://www.scholarpedia.org/article/Complex_systems" title = "Complex systems">complex systems</a>. In my studies, I developed several free software programs to explore the concept of <a href = "https://www.eurekaselect.com/article/84362" title = "Heck GS, Pintro VO, Pereira RR, de Ávila MB, Levin NMB, de Azevedo WF. Supervised Machine Learning Methods Applied to Predict Ligand- Binding Affinity. Curr Med Chem. 2017;24(23):2459-2470.">Scoring Function Space</a>. </p>
<p>
As a result of my research, I published over 200 scientific works about protein structures, computer models of complex systems, and simulations of protein systems. These publications have generated over 12,000 citations on <a href = "https://scholar.google.com/citations?user=HWwJXJUAAAAJ&hl=pt-BR" title = "Link to Google Scholar">Google Scholar (h-index of 63)</a> and more than 10,000 citations and an <a href = "https://www.scopus.com/authid/detail.uri?authorId=7006435557" title = "de Azevedo Junior, Walter Filgueira. Scopus ID: 7006435557">h-index of 58 in Scopus</a>.   

Due to the impact of my work, I have been ranked among the most influential researchers in the world (Fields: Biophysics, Biochemistry & Molecular Biology, and Biomedical Research) according to a database created by <a href = "https://pubmed.ncbi.nlm.nih.gov/33064726/" title = "Ioannidis JPA, Boyack KW, Baas J. Updated science-wide author databases of standardized citation indicators. PLoS Biol. 2020 Oct 16;18(10):e3000918. doi: 10.1371/journal.pbio.3000918. PMID: 33064726; PMCID: PMC7567353.">Journal Plos Biology</a> (see news <a href = "https://www.pucrs.br/en/blog/research-database-includes-7-pucrs-professors-among-most-influential-in-the-world/" title = "Research database includes 7 PUCRS professors among most influential in the world">here</a>). The application of the same set of metrics recognized the influence of my work from 2021 to 2025 (<a href = "https://elsevier.digitalcommonsdata.com/datasets/btchxktzyw/3" title = "August 2021 data-update for Updated science-wide author databases of standardized citation indicators">Baas et al., 2021</a>; <a href = "https://elsevier.digitalcommonsdata.com/datasets/btchxktzyw/4" title = "September 2022 data-update for Updated science-wide author databases of standardized citation indicators">Ioannidis, 2022</a>, <a href = "https://elsevier.digitalcommonsdata.com/datasets/btchxktzyw/6" title = "October 2023 data-update for Updated science-wide author databases of standardized citation indicators">2023</a>, <a href = "https://elsevier.digitalcommonsdata.com/datasets/btchxktzyw/7" title = "August 2024 data-update for Updated science-wide author databases of standardized citation indicators">2024</a>, and <a href = "https://elsevier.digitalcommonsdata.com/datasets/btchxktzyw/8" title = "August 2025 data-update for Updated science-wide author databases of standardized citation indicators">2025</a>). Not bad for a poor guy who was a shoe seller at a store in São Paulo and had the opportunity to study at the University of São Paulo with a scholarship for food and housing. I was 23 when I initiated my undergraduate studies and was the first in my family to have access to higher education.
<br> </br>
<a href="https://www.scopus.com/authid/detail.uri?authorId=7006435557" title = "Link to Scopus">
<img src="https://drive.usercontent.google.com/download?id=1K_1skqZBcdmgJK41OJJcr4hbXepXHje_&export=view&authuser=0" width=800 alt="Link to Scopus"></a>  
<br><i>Document and Citation Trends (<a href="https://www.scopus.com/authid/detail.uri?authorId=7006435557" title = "Link to Scopus">Scopus ID: 7006435557</a>) (Data captured on January 30, 2026)</i></br>
<br> </br>
Regarding scientific impact (<a href = "https://www.sciencenews.org/article/rating-researchers" title = "Rating Researchers">Peterson, 2005</a>), Hirsch said that for a physicist, an h-index of 45 or higher could mean membership in the National Academy of Sciences of the USA. So far, there have been no invitations. No hard feelings because I am in good company. <a href = "https://theconversation.com/carl-sagans-scientific-legacy-extends-far-beyond-cosmos-240885" title = "Carl Sagan’s scientific legacy extends far beyond ‘Cosmos’">Carl Sagan</a> was never allowed into the National Academy of Sciences. According to an analysis of citations performed on Nov. 9, 2024 (<a href = "https://theconversation.com/carl-sagans-scientific-legacy-extends-far-beyond-cosmos-240885" title = "Carl Sagan’s scientific legacy extends far beyond ‘Cosmos’">The Conversation</a>), his work accumulates more than 1,000 citations per year on Google Scholar. Indeed, his current citation rate exceeds that of many members of the <a href = "https://www.nasonline.org/membership/" title = "National Academy of Sciences">National Academy of Sciences</a>. 

I will continue working in science with low-budget and interdisciplinary projects and combating <a href = "https://revistapesquisa.fapesp.br/en/the-seeds-of-mistrust/" title = "The seeds of mistrust: A new dictionary focuses on the varieties of denialism that confuse public opinion in Brazil and around the world. Ana Paula Orlandi, da Revista Pesquisa FAPESP">denialism</a> with science. The fight against <a href = "https://revistapesquisa.fapesp.br/en/the-seeds-of-mistrust/" title = "The seeds of mistrust: A new dictionary focuses on the varieties of denialism that confuse public opinion in Brazil and around the world. Ana Paula Orlandi, da Revista Pesquisa FAPESP">denialism</a> is a continuing work, and scientists should not forget their role in a complex society where social media has given the right to speak to legions of imbeciles.

“Social media gives the right to speak to legions of imbeciles who previously only spoke at the bar after a glass of wine, without damaging the community. They were immediately silenced, but now they have the same right to speak as a Nobel Prize winner. It’s the invasion of imbeciles.”

Umberto Eco. Source: <a href = "https://quoteinvestigator.com/2024/03/21/social-media/" title = "Quote Origin: Social Media Gives the Right To Speak To Legions of Imbeciles Who Previously Only Spoke in Bars After Drinking">Quote Investigator</a>
</p>
<br> </br>
"Let the light of science end the darkness of denialism." My quote (<a href = "https://doi.org/10.2174/092986732838211207154549" title = "DOI:10.2174/092986732838211207154549">DOI:10.2174/092986732838211207154549</a>). 
<br> </br>
