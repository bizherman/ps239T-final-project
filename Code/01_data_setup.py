# In order to collect the relevant articles, I used LexisNexis Academic (http://www.lexisnexis.com/hottopics/lnacademic) to search for all instances of Planned Parenthood in The New York Times, from when it first appeared in 1969 to the present.

# I batch downloaded files, 500 at a time, and then culled them into a single .txt file, “PP_NYT.txt”.

# I then used 02_split_ln.py to take the long .txt file of articles and organize it into a .csv file, where each observation (row) was a single article. To do that I ran the following code:

# First cd into the correct working directory (be sure to put in your own working directory)
cd /Users/elizabeth/Documents/Berkeley/PS239T/ps239T-final-project
python Code/02_split_ln.py Data/PP_NYT.txt

# This should produce a .csv file that will have the data, which can be used for the subsequent analyses.