Project Overview:
This is a simple project i created in python that showcases an example of Fraud Detection Analysis which is demonstrated through the use of statistical and social network analysis

Statistical Analysis:
- I used a basic statistical method (threshold based on mean + 2 standard deviations) to flag transactions with unusually high amounts as potential fraud.
- Later i visualise the distribution of transaction amounts with a histogram, separating the normal and fraudulent transactions.

Social Network Analysis:
- Built a directed graph using NetworkX to represent transactions between users.
- Identify suspicious users based on degree centrality (users with the most connections).
- Visualise the network with suspicious users highlighted in red.

Output:
Generates two plots saved as PNG files:
- amount_distribution.png: A histogram showing transaction amounts, with fraudulent ones in red.
- transaction_network.png: A network graph showing user connections, with suspicious users in red.
- Prints a summary of total transactions, number of fraudulent transactions, and suspicious users.

How to Run
- Make sure the required libraries are installed: pip install pandas numpy networkx matplotlib
- Save the code in as a py file and run the script in python
- Check the generated PNG files (amount_distribution.png and transaction_network.png) and the console output for results.
