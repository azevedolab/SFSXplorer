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
<img src="https://drive.usercontent.google.com/download?id=1qWkaR3YMBMcfofbC9uYrq-gSfsR1BTjx&export=view&authuser=0" width=200 align=left title="de Azevedo WF Jr, editor. Docking screens for drug discovery. 2nd ed. New York, NY: Springer; 2026.">
</a>
<p>
de Azevedo WF Jr, editor. Docking screens for drug discovery. 2nd ed. New York, NY: Springer; 2026. <a href = "https://doi.org/10.1007/978-1-0716-4949-7" title = "de Azevedo WF Jr, editor. Docking screens for drug discovery. 2nd ed. New York, NY: Springer; 2026.">DOI: 10.1007/978-1-0716-4949-7</a>
</p>
<a href="https://www.amazon.com/Docking-Screens-Discovery-Methods-Molecular-ebook/dp/B0FVTT27Z9">
<img src="https://drive.usercontent.google.com/download?id=1ktGUzRY-SOoRjdvc6xKzzBNXzB6ibJfc&export=view&authuser=0" width=100 align=left title="de Azevedo WF Jr, editor. Docking screens for drug discovery. 2nd ed. New York, NY: Springer; 2026.">
</a>
<br> </br>
<br> </br>
<br> </br>
<br> </br>
<br> </br>
<br> </br>
<h2><a href = "https://github.com/azevedolab/About-Me" title = "About Prof. Walter Filgueira de Azevedo, Jr."> About Me </a> </h2> 
<a href="https://scholar.google.com/citations?user=HWwJXJUAAAAJ" title = "Link to Google Scholar">
<img src="https://drive.usercontent.google.com/download?id=1rL_DWbMj6timTlYlhn9Hwm1acq8AU4QV&export=view&authuser=0" height=24 alt="Link to Google Scholar"></a>  
<a href="https://www.scopus.com/authid/detail.uri?authorId=7006435557" title = "Link to Scopus">
<img src="https://drive.usercontent.google.com/download?id=1URGO8UDkZV_4wX_4c0_gUvhEjfnUyqCQ&export=view&authuser=0" height=24 alt="Link to Scopus"></a>
<a href="https://heyzine.com/flip-book/8d3ce2eb08.html" title = "Link to Curriculum Vitae (Flipbook)">
<img src="https://drive.usercontent.google.com/download?id=17kToUZlwbJ4PgorpUY7EGQA1lFnR_2Gh&export=view&authuser=0" height=24 alt="Link to Curriculum Vitae (Flipbook)"></a>

<br> </br>
