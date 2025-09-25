Project Overview: This is a simple project i created in python showcasing a Fraud Detection Analysis through the use of statistical and social network analysis
<br>
Statistical analysis:
<br>
•	I used a basic statistical method (threshold based on mean + 2 standard deviations) to flag transactions with unusually high amounts as potential fraud.
<br>
•	Later i visualised the distribution of transaction amounts with a histogram, separating the normal and fraudulent transactions.
<br>
Social Network Analysis:
<br>
•	I built a directed graph using NetworkX to represent transactions between users.
<br>
•	Identify suspicious users based on degree centrality (users with the most connections).
<br>
•	Visualised the network with suspicious users highlighted in red.
<br>
Output: Generates two plots and a summary in python:
<br>
•	Figure 1: A histogram showing transaction amounts, with fraudulent ones in red.
<br>
•	Figure 2: A network graph showing user connections, with suspicious users in red.
<br>
•	Prints a summary of total transactions, number of fraudulent transactions, and suspicious users.
<br>
How to Run
<br>
•	Download the file and run in python
<br>
•	Make sure the required libraries are installed: pip install pandas numpy networkx matplotlib
<br>
•	Open the provided py file and run the script in python
<br>
•	Check the generated plots in python (Figure 1 and Figure 2) and the console output for the results.

