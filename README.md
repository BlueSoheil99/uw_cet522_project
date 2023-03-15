# uw_cet522_project

## A Fundamental Diagram (FD) and Macroscopic Fundamental Diagram (MFD) illustration app for Seattle highways

Soheil Keshavarz (BlueSoheil99), Shakiba Naderian (Shakiba97), Mohammad Mehdi Oshanreh (mohammadm3gtr)

The Fundamental diagram illustrates the relationship between traffic flow variables for small segments of a road network. On the other hand, Macroscopic fundamental diagrams (MFD) are an aggregation of these variables at different times and days, independent of demand and time, and provide a powerful tool for understanding traffic flow patterns in specific aggregated parts of the network. In this study, we explored the possibility of observing a low-scatter relationship between various traffic attributes at a large scale (MFD) on one of Seattle's highways, I5, using loop detector data and comparing it to the microscopic level (FD). The results indicate that aggregating the data for multiple mileposts results in a diagram with a much lower scatter. Additionally, the study aims to create an application using the Streamlit library in python that can generate plots of FDs for selected segments and MFDs for a range of segments on the I5 highway. 

## This repository consists of three modules:

#### 1 - A data_handler module to extract requested information for a list of mileposts on a specified route, direction, time, and date 

#### 2 - A logic module that fetches data from the first module to construct FD and MFD

#### 3- A streamlit interface coded in main.py to interact with a user 

## How to run the project?
 * make sure that GLOB_ADDRESS and SPLITTER in meta_query.py are compatible with you OS
 * run main.py and read the warning at the end and do as instruction says!
