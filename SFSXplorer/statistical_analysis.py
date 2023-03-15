#!/usr/bin/env python3
#
################################################################################
# SFSXplorer                                                                   #
# Scoring Function Space eXplorer                                              #
################################################################################
#
# Program to carry out statistical analysis of the predictive performance of 
# energy terms loosely based on AutoDock4 Force Field (Morris et al., 1998; 
# 2009). It uses metrics indicated by Walsh et al. 2021. It also calculates 
# correlation coefficients (Zar, 1972).
#
# References:
#
# Morris GM, Goodsell D, Halliday R, Huey R, Hart W, Belew R, Olson A. 
# Automated docking using a Lamarckian genetic algorithm and an 
# empirical binding free energy function. J Comput Chem. 1998; 19:1639–1662.
#
# Morris GM, Huey R, Lindstrom W, Sanner MF, Belew RK, Goodsell DS, Olson AJ. 
# AutoDock4 and AutoDockTools4: Automated docking with 
# selective receptor flexibility. J Comput Chem. 2009; 30(16): 2785–2791.
#
# Walsh I, Fishman D, Garcia-Gasulla D, Titma T, Pollastri G; 
# ELIXIR Machine Learning Focus Group; Harrow J, Psomopoulos FE, Tosatto SCE. 
# DOME: recommendations for supervised machine learning validation in biology. 
# Nat Methods. 2021; 18(10): 1122–1127.
#
# Zar JH. Significance Testing of the Spearman Rank Correlation Coefficient. J 
# Am Stat Assoc. 1972; 67(339): 578–580.
#
#
################################################################################
# Dr. Walter F. de Azevedo, Jr.                                                #
# https://azevedolab.net/                                                      #
# January 12, 2023                                                             #
################################################################################
#
# Define Stats class

class Stats(object):
    """Class to carry out statistical analysis of energy terms"""

    # Define constructor method
    def __init__(self,sfs_in):
        """Constructor method"""

        # Set up attribute
        self.sfs_in = sfs_in        # Input file with parameters
              
        # Show message
        print("\n\nPerforming statistical analysis...")

    # Define read_stats_in()
    def read_stats_in(self):
        """Method to read parameters necessary to carry out statistical 
        analysis"""
        
        # Import libraries
        import csv
        import sys
                            
        # Try open stats.in file
        try:
            fo_stats = open(self.sfs_in,"r")
            csv_stats = csv.reader(fo_stats)
        except IOError:
            sys.exit("\nIOError! I can't find ",self.sfs_input," file!")
        
        # Looping through stats.in
        for line in csv_stats:
            if line[0] == "#":
                continue
            elif line[0].strip() == "scores_out":
                self.scores_out = str(line[1])
                self.stats_analysis = self.scores_out.replace(".csv",
                                                    "_stats_analysis.csv")
            elif line[0].strip() == "exp_string":
                self.exp_string = str(line[1])
            elif line[0].strip() == "n_features_in":
                self.n_features_in = int(line[1].strip())
            elif line[0].strip() == "features_in":
                # Set up an empty list
                features_list = []
                
                # Looping through the features
                for i in range(1,self.n_features_in+1):
                    features_list.append(line[i])
        
        # Close file
        fo_stats.close()

        # Open CSV file
        import csv
        fo_data = open(self.scores_out,"r")
        csv_data = csv.reader(fo_data)
        
        # Read first line
        for line in csv_data:
            self.header = line
            break
        
        # Set up an empty lists
        self.columns = []
        self.terms = []
        
        # looping through self.header
        for i,term in enumerate(self.header):
            if term in features_list:
                self.columns.append(i)
                self.terms.append(term)
        
        # Close file
        fo_data.close()
            
    # Define read_data() method
    def read_data(self):
        """Method to read CSV file and return arrays"""

        # Import library
        import numpy as np
        
        # Open CSV file
        pie_in = np.genfromtxt(self.scores_out, skip_header = 1, delimiter=",")
        
        # Get rid of the pie's first slice
        # pie1 = np.transpose(pie_in[:,1:]) # you transpose it and slice it row 
        # and column
        pie1 = pie_in[:,1:]   # Without transposing it

        # Get the number of rows and columns
        self.n_rows, self.n_cols = pie1.shape

        # Set up a zeros array
        self.pie2go = np.zeros((self.n_rows, self.n_cols))

        # Slicing the pie1
        for c in range(self.n_cols):
            for r in range(self.n_rows):
                self.pie2go[r,c] = pie1[r,c]
    
    # Define write_metrics() method
    def write_metrics(self):
        """Method to generate a csv file with the metrics"""
        
        # Open file to store statistical analysis
        fo_metrics = open(self.stats_analysis,"w")
        
        # Write header
        header_string = "Feature,r,p-value,r2,rho,p-value,MSE,RMSE,RSS,MAE,R2"
        fo_metrics.write(header_string+"\n")
        
        # Looping through self.columns()
        for i in range(len(self.columns)):
            r2 = self.r_array[i]**2 # Calculate r2 (Pearson squared)
            line_o = self.terms[i]+","
            line_o += str(self.r_array[i])+","+str(self.p_v_r_array[i])+","
            line_o += str(r2)+","
            line_o += str(self.rho_array[i])+","+str(self.p_v_rho_array[i])+","
            line_o += str(self.mse_array[i])+","+str(self.rmse_array[i])+","
            line_o += str(self.rss_array[i])+","+str(self.mae_array[i])+","
            line_o += str(self.r2_array[i])
            fo_metrics.write(line_o+"\n")
            print(line_o)
        
        # Close file
        fo_metrics.close()
        
    # Define get_experimental_index() method
    def get_experimental_index(self):
        """Method to get index of experimental column from a CSV file"""

        # Import library
        import csv

        # Open CSV file
        fo1 = open(self.scores_out,"r")
        csv1 = csv.reader(fo1)
        
        # Read first line
        for line in csv1:
            self.headers = line
            break
        
        # Find index of exp_string
        self.index_experimental = self.headers.index(self.exp_string)
        
        # Show message
        print("\nString "+self.exp_string+" in column: ",
                self.index_experimental)
        
        # Close file
        fo1.close()

    # Define show_it() method
    def show_it(self):
        """Method to show array"""
        
        # Slicing the pie1
        for c in range(self.n_cols):
            for r in range(self.n_rows):
                print(self.pie2go[r,c])
            print("Column ",c)
    
    # Define show_column() method
    def show_column(self,col_in):
        """Method to show array"""
    
        # Update column number
        col_in -= 1
        
        # Slicing the pie1
        for r in range(self.n_rows):
            print(self.pie2go[r,col_in])

    # Define get_array() method
    def get_array(self,col_in):
        """Method to get array"""
        
        # Import section
        import numpy as np
        
        # Update column number
        col_in -= 1
        
        # Set up an np.array
        data_array = np.zeros(self.n_rows)
            
        # Assign column to array
        i = 0
        for r in range(self.n_rows):
            data_array[i] = self.pie2go[r,col_in]
            i += 1
        
        # Return array
        return data_array
            
    # Define calc_ESS() method
    def calc_ESS(self,x,y_pred):
        """Calculate Explained Sum of Squares (ESS).
        Not used here."""

        # Import library
        import numpy as np

        # Get number of data points
        n = len(x)

        # Set up array with zeros
        aux = np.zeros(n,dtype=float)

        # Calculate mean of x
        mean_y_in = np.mean(x)

        # Looping through data points y_pred
        for i in range(n):
            aux[i] = (y_pred[i] - mean_y_in)**2

        # Calculates Explained Sum of Squares (ESS)
        self.ess = np.sum(aux)

    # Define calc_RSS() method
    def calc_RSS(self,x,y_pred):
        """Calculate Residual Sum of Squares (RSS)"""

        # Import library
        import numpy as np

        # Get number of data points
        n = len(x)

        # Set up array with zeros
        aux = np.zeros(n,dtype=float)

        # Calculate aux
        for i in range(n):
            aux[i] = (x[i] - y_pred[i])**2

        # Calculates Residual Sum of Squares (RSS)
        rss = np.sum(aux)
        
        # Return rss
        return rss

    # Define bundle()
    def bundle(self):
        """Method to calculate metrics"""
        
        # Import section
        import numpy as np
        from sklearn.metrics import r2_score
        from scipy import stats
        from sklearn.metrics import mean_absolute_error
        from sklearn.metrics import mean_squared_error
        
        # Set up np.arrays
        self.rho_array = np.zeros(self.n_features_in)
        self.p_v_rho_array = np.zeros(self.n_features_in)
        self.r_array = np.zeros(self.n_features_in)
        self.p_v_r_array = np.zeros(self.n_features_in)
        self.r2_array = np.zeros(self.n_features_in)
        self.mae_array = np.zeros(self.n_features_in)
        self.mse_array = np.zeros(self.n_features_in)
        self.rmse_array = np.zeros(self.n_features_in)
        self.rss_array = np.zeros(self.n_features_in)
        self.std_dev_array = np.zeros(self.n_features_in)
        
        # Invoke get_experimental_index() method
        self.get_experimental_index()
        
        # Get experimental array
        y_exp = self.get_array(self.index_experimental)
        
        # Looping through self.columns()
        for i in range(len(self.columns)):
            #print(self.columns[i],self.terms[i])
        
            # Invoke get_array() method
            y_pred = self.get_array(self.columns[i])

            ####################################################################
            # Metrics
            # Try to calculate Spearman rank correlation coefficient 
            # and p-values
            try:
                self.rho_array[i],self.p_v_rho_array[i] = \
                                                stats.spearmanr(y_exp,y_pred)
            except:
                self.rho_array[i],self.p_v_rho_array[i] = None,None
                
                
            # Try to calculate Pearson correlation coefficient and p-value
            try:
                self.r_array[i],self.p_v_r_array[i] = \
                                                stats.pearsonr(y_exp,y_pred)
            except:
                self.r_array[i],self.p_v_r_array[i] = None,None
                

            # Calculate MAE, MSE and RMSE
            self.mae_array[i] = mean_absolute_error(y_exp,y_pred)
            self.mse_array[i] = mean_squared_error(y_exp,y_pred)
            self.rmse_array[i] = mean_squared_error(y_exp,y_pred,squared=False)
            
            # Invoke calc_RSS method
            self.rss_array[i] = self.calc_RSS(y_exp,y_pred)
            
            # Calculate R2
            self.r2_array[i] = r2_score(y_exp,y_pred)
            
            # Calculate standard deviation
            self.std_dev_array[i] = np.std(y_pred,ddof=1)  # Standard deviation
            # https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.std.html

            # Show metrics
            print("\n\nFor ",self.terms[i])
            print("rho: ",self.rho_array[i])
            print("r: ",self.r_array[i])
            print("MAE: ",self.mae_array[i])
            print("MSE: ",self.mse_array[i])
            print("RMSE: ",self.rmse_array[i])
            print("RSS: ",self.rss_array[i])
            print("R2: ",self.r2_array[i])
            print("SD: ",self.std_dev_array[i])
        
            ####################################################################
        
        # Show maximum values for metrics
        print("\n\n\nMaximum rho: ",np.max(self.rho_array))
        print("Maximum r: ",np.max(self.r_array))
        print("Minimum MAE: ",np.min(self.mae_array))
        print("Minimum MSE: ",np.min(self.mse_array))
        print("Minimum RMSE: ",np.min(self.rmse_array))
        print("Minimum RSS: ",np.min(self.rss_array))
        print("Maximum R2: ",np.max(self.r2_array))
        
        # Invoke write_metrics() method
        self.write_metrics()
        
        # Show message
        msg_o = "\n\n\n\n\nStatistical analysis written in "
        msg_o += self.stats_analysis
        msg_o += "\n\nMetrics partially based on: "
        msg_o += "Walsh I, Fishman D, Garcia-Gasulla D, Titma T, Pollastri G; "
        msg_o += "ELIXIR Machine Learning Focus Group; Harrow J, Psomopoulos "
        msg_o += "FE, Tosatto SCE. DOME: recommendations for supervised "
        msg_o += "machine learning validation in biology. Nat Methods. 2021 "
        msg_o += "Oct;18(10):1122-1127. \n"
        print(msg_o)
            