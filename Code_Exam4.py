#!/usr/bin/env python
# coding: utf-8

# In[61]:


#!/usr/bin/env python3
# import packages
import argparse
import pandas as pd

# calculate possible kmers in sequence to be analyzed
def count_kmers(length_k, string_to_input):
    """
    Calculate the number of possible kmers in a given string
    
    Parameters: 
    string_to_input -- sequence string to be analyzed 
    length_k -- length of kmers in given string
    
    return: number of possible kmers
    """  
    string = len(string_to_input) # counts the length of given string 
    a = 4**length_k # kmer calculation 1
    b = string - length_k + 1 # kmer calculation 2
    if a > b: # to return the option with lower value
        return b
    else: 
        return a
    
#calculate the actual observed kmers in given string
def obsvd_kmers(length_k, string_to_input):
    """
    Calculate the actual observed kmers in a given string
    
    Parameters:
    string_to_input = sequence string to be analyzed 
    length_k =  length of kmers in given string
    
    Return: number of observed kmers
    """
    kmer_list = [] # create empty data frame to store kmers in
    second_list = [] # create empty data frame  
    count = 0 # create empty counter 
    string = len(string_to_input) # calculate length of string
    for i in range(1, string+1):  # "i" is an integer within the range of 1 to the number of kmers in the string
        kmer_value = string_to_input[(i-1):(i-1+k)] # pull out kmer for k value of interest
        if len(kmer_value) == k: # only include kmer_value for the length of kmers we are interested in
            kmer_list.append(kmer_value) # put kmers into a new df
    for item in kmer_list:
        if item not in second_list: # add new unique kmers to new df
            count += 1 # increase count by +1 if there is another unique value not in "kmer_list"
            second_list.append(item)
    return(count) # output of the observerd kmer count

#create data frame with all possible and observed k values
def write_df(string_to_input):
    '''
    create a data frame with all k values, including possible and observed k-mers
    
    Parameters:
    string_to_input = sequence string to be analyzed 
    
    Returns: 
    dataframe: a dataframe that lists all possible and observed kmers as well as row for calculated totals
    '''
    
    dataframe = [] # create empty data frame 
    string = len(ex) # caluclate length of string 
    for i in range(1, string+1): # all possible lengths of k depending on string
        k = i # k equal to the range of 1 to the length of the string
        dataframe.append([obsvd_kmers(length_k, string_to_input), count_kmers(length_k, string_to_input)]) # calculate totals for possible, observed kmers and then combine totals together add them to the df 
    df = pd.DataFrame(dataframe, index = range(1,string+1), columns = ['observed_kmers', 'possible_kmers']) # pandas dataframe- fill 
    df.loc['total']= df.sum() # sum row
    return(df)

#calculate the linguistic complexity for string
def linguistic_complex(dataframe):
  """
  Calculate linguistic complexity
  
  Parameters:
  df -- the data frame from write_df
  
  Return:
  LC = calculate linguistic complexity of given string
  """
  LC = df.loc['Total', 'Observed_kmers']/df.loc['Total', 'Possible_kmers'] #calculate linguistic complexity by dividing these by each other
  return(LC)

# combine all of the functions above into one file
def main(args): 
  """
  ouput new data frame with calculated linguistic complexity 
  
  Parameters:
  CSV file: file with list of sequence strings 
  
  Returns: 
  Dataframe, CSV file: Creates a csv file 
  Linguistic complexity (automated message): Prints a message on command line with string and linguistic complexity of the string
  """
  last = [] # create empty dataframe
  for i in args.data:
    string = i # each line generates string
    df = write_df(x) 
    out = linguistic_complexity(df) # calculate linguistic complexity according to df
    df.to_csv(i+'sequence.csv') # create data frame as a csv file
    print("The linguistic complexity of", x, "is", out) # linguistic complexity automatically displayed to command line 
    
if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument('dataframe', type=argparse.FileType('r'))
    args = parser.parse_args()
    main(args)   


# In[ ]:




