Name: Biz Herman
Date: 9 December 2015

Welcome to this final project for PS239T! 

## Short Description

This project provides code to carry out both sentiment analysis and topic modeling for a large number of articles on a single subject, in this case Planned Parenthood. The beauty of this code, however, is that it can be applied to any body of documents, in order to examine how the sentiment shifts over time, and to identify trends in the topics covered.

## Dependencies

This code depends on the following software:

1. R, version 3.1
2. Python, version 2.7, Anaconda distribution.

There are a number of packages that need to be installed in the R code, including:

1. qdap
2. data.table
3. scales
4. plyr
5. ggplot2
6. mallet
7. wordcloud

## Files

List all other files contained in the repo, along with a brief description of each one, like so:

#### Data

1. PP_NYT.csv: Contains data from LexisNexis, batch downloaded and split using 02_split_ln.py. Includes information on all articles containing the term "Planned Parenthood," from 1982 to 2015.
2. PP_NYT.txt: Contains the text for all the articles containing the term "Planned Parenthood," from 1982 to 2015, batch downloaded from LexisNexis.
3. stoplist.csv: Common words used that are eliminated from the documents when modeling topics in 04_TopicModeling.Rmd.

#### Code

1. 01_data_setup.py: Explains article collection process from LexisNexis, and provides code for splitting articles into .csv file.
2. 02_split_ln.py: Neal Caren's python code that does the actual splitting of the LexisNexis articles, is referenced in the code written in the first file.
3. 03_polarity.Rmd: Conducts sentiment analysis and visualizations of the articles, both of a truncated range from 2010 to the present, as well as for the entire collection of articles.
4. 04_TopicModeling.Rmd: Conducts topic modeling and visualization of topics of articles, both of a truncated range from 2010 to the present, as well as for the entire collection of articles.

#### Results

1. Graphic_PPDendogram.png: Dendogram produced in 04_TopicModeling.Rmd, summarizing relationship of various topics generated.
2. Graphic_PPSince1982.png: 
3. Graphic_PPSince2000.png: Tracking sentiment analysis from 2000 to the present.
4. Graphic_PPSince2009.png: Tracking sentiment analysis from 2009 to the present.
5. Graphic_PPWCAllArticles.png: Wordcloud of the most common words used in all articles on Planned Parenthood.
6. Graphic_PPWCAllTopics.png: Wordcloud of the most common words used in each topic generated in 04_TopicModeling.Rmd on articles on Planned Parenthood.
7. PS239T_Presentation.html: Presentation given to PS239T summarizing results.
8. topic-docs.csv: Transposing and normalizing the document topics for the smaller subset of articles, from 2010 to 2015.
9. topic-docs2.csv: Transposing and normalizing the document topics for the entire set of artciles, from 1982 to 2015.
10. topic-labels.csv: The topic labels for the smaller subset of articles, from 2010 to 2015.
11. topic-labels2.csv: The topic labels for the entire set of articles, from 1982 to 2015.


## More Information

Code developed using code from Rochelle Terman's PS239T course, taught at UC Berkeley in Fall 2015, and from Neal Caren.

To get in touch, please write elizabethdherman@gmail.com or visit www.bizherman.com!
