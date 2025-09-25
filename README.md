Project Overview: This is a simple project i created in python showcasing a Fraud Detection Analysis through the use of statistical and social network analysis.

Statistical Analysis:

•	I used a basic statistical method (threshold based on mean + 2 standard deviations) to flag transactions with unusually high amounts as potential fraud.

•	Later i visualised the distribution of transaction amounts with a histogram, separating the normal and fraudulent transactions.

Social Network Analysis:
•	I built a directed graph using NetworkX to represent transactions between users.

•	Identify suspicious users based on degree centrality (users with the most connections).

•	Visualised the network with suspicious users highlighted in red.

Output: Generates two plots and a summary in python:
•	Figure 1: A histogram showing transaction amounts, with fraudulent ones in red.
•	Figure 2: A network graph showing user connections, with suspicious users in red.
•	Prints a summary of total transactions, number of fraudulent transactions, and suspicious users.

How to Run
•	Download the file and run in python
•	Make sure the required libraries are installed: pip install pandas numpy networkx matplotlib
•	Open the provided py file and run the script in python
•	Check the generated plots in python (Figure 1 and Figure 2) and the console output for the results.
