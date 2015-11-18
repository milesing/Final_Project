#importing my libraries
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#This line makes my Log2 fold calculation work. 
pd.options.mode.chained_assignment = None



def main(data):
	'''Driver function for data analysis'''
	#my main function
	munge(data)
	plot(smaller_data)
	#Inverse band pass because it removes the middle and keeps the edges
	inverse_band_pass()
	
	

def munge(data):
	'''trims data and adds log2 fold values'''
	data = pd.read_excel('journal.pone.0112102.s005.XLSX')
	#this removes the many zeroes from the data. 
	small_data = data[(data.T != 0).all()]
	#this allows smaller_data to be used outside of the munge function.
	global smaller_data
	smaller_data = small_data[['gene','value_1','value_2']]
	#here is my log2 fold calculation
	smaller_data['Log2_Fold'] = np.log2(smaller_data.value_2) - np.log2(smaller_data.value_1) 
	return (smaller_data)
	
    
    
def plot(smaller_data):
	'''Makes a simple plot of log2 fold values'''
	#This is my plot function, it's pretty simple as its main function is simply to show the shape of the data
	plt.plot(smaller_data.Log2_Fold,linestyle='',marker='x')
	plt.ylabel('Log2 Fold')
	plt.savefig('test_fig')
	
def inverse_band_pass():
	'''Grabs the extremities of the data.'''
	#In this function I grab the upper and lower extremities of the data and write them to csv files. 
	high_pass_data = smaller_data[smaller_data['Log2_Fold'] >= 9]
	low_pass_data  = smaller_data[smaller_data['Log2_Fold'] <= -6]
	
	high_pass_data.to_csv('Genes with high log2 fold score.')
	low_pass_data.to_csv('Genes with low log2 fold score.')
	
	
	
main(sys.argv[1])
	
