Project Overview: This is a simple project i created in python showcasing a Fraud Detection Analysis through the use of statistical and social network analysis.

Statistical Analysis:
* I used a basic statistical method (threshold based on mean + 2 standard deviations) to flag transactions with unusually high amounts as potential fraud.
* Later i visualised the distribution of transaction amounts with a histogram, separating the normal and fraudulent transactions.
Social Network Analysis:
* I built a directed graph using NetworkX to represent transactions between users.
* Identify suspicious users based on degree centrality (users with the most connections).
* Visualised the network with suspicious users highlighted in red.
Output: Generates two plots and a summary in python:
* Figure 1: A histogram showing transaction amounts, with fraudulent ones in red.
* Figure 2: A network graph showing user connections, with suspicious users in red.
* Prints a summary of total transactions, number of fraudulent transactions, and suspicious users.
How to Run
* Download the file and run in python
* Make sure the required libraries are installed: pip install pandas numpy networkx matplotlib
* Open the provided py file and run the script in python
* Check the generated plots in python (Figure 1 and Figure 2) and the console output for the results.

Statistical Analysis Results:
Purpose: Identify fraudulent transactions based on unusually high amounts.
* Method: The script flags transactions as fraudulent if their amount exceeds the threshold of mean_amount + 2 * std_amount.
  * Data Generation: Transaction amounts are generated from a normal distribution (mean=100, std=30). Approximately 10% of transactions (10 out of 100) are marked as fraudulent by multiplying their amounts by a random factor between 3 and 5, making them significantly larger.
  * Threshold Calculation:
    * Mean amount ≈ $100 (based on the normal distribution).
    * Standard deviation ≈ $30.
    * Threshold ≈ $100 + 2 * $30 = $160.
    * Transactions with amounts > $160 are flagged as fraudulent.
* Result: Approximately 10 transactions are flagged as fraudulent, as the script intentionally inflates 10% of amounts to be 3–5 times larger (e.g. $300 – $500).
Visualisation (Histogram):
* Description:
  * X-axis: Transaction amounts, ranging from approximately $0 to approximately $500 (due to the normal distribution and fraudulent inflation).
  * Y-axis: Frequency of transactions (number of transactions in each bin).
  * Blue Bars: Normal transactions, forming a bell-shaped curve centred around $100, with most amounts between $40 and $160 (within ±2 standard deviations).
  * Red Bars: Fraudulent transactions, appearing in higher bins (e.g. $160 – $500), forming a smaller, separate cluster or tail on the right.
  * Bins: 20 bins, providing a clear separation between normal and fraudulent amounts.
* Interpretation: The histogram shows that fraudulent transactions are outliers with significantly higher amounts, demonstrating the effectiveness of the statistical threshold in identifying anomalies.

Social Network Analysis Results
Purpose: Identify suspicious users based on their connectivity in the transaction network.
* Method:
  * Network Construction: A directed graph (nx.DiGraph) is built using NetworkX, where nodes are the 20 users (User_1 to User_20) and edges represent transactions (with weights as amounts).
  * Degree Centrality: Measures the number of connections (incoming and outgoing transactions) for each user, normalised by the total possible connections. Users with the highest centrality are considered suspicious, as they may be hubs in a fraud network.
  * Suspicious Users: The top 3 users by degree centrality are flagged as suspicious.
* Result: Due to the random selection of senders and receivers, some users will have more transactions than others. With 100 transactions and 20 users, each user is involved in approximately 10 transactions on average (as sender or receiver). The top 3 users likely have significantly more connections (e.g. 15 – 20 transactions each).
Visualisation (Network Graph):
* Description:
  * Nodes: 20 nodes labelled User_1 to User_20, drawn in light blue, representing users.
  * Edges: Directed arrows connecting users, representing transactions (100 edges total).
  * Suspicious Nodes: The top 3 users (e.g., User_3, User_6, User_18, though exact users depend on the random data) are highlighted in red with larger node sizes (700 vs. 500).
  * Layout: Spring layout (nx.spring_layout), where nodes with more connections tend to cluster centrally, and edges show the direction of transactions.
* Interpretation: The network graph reveals users with unusually high transaction activity, indicating potential fraud hubs. For example, a user with many incoming and outgoing transactions might be coordinating fraudulent activity. This demonstrates practical experience in social network analysis to uncover relational fraud patterns.

Console Summary
<br> Output: The script prints a summary to the console, which looks something like this (exact numbers may vary slightly due to randomness, but the seed ensures consistency):
*     Fraud Detection Summary:
      Total Transactions: 100
      Fraudulent Transactions: 7 (7.0%)
      Suspicious Users (High Connections): [‘User_5’, ‘User_13’, ‘User_2’]
<br> Total Transactions: Always 100, as specified in the script. 
<br> Fraudulent Transactions: Approximately 10 transactions (10%), as the script marks 10% of transactions as fraudulent. 
<br> Suspicious Users: The top 3 users by degree centrality, e.g. User_3, User_6, User_18. These users have the most connections, indicating they are involved in many transactions, which could suggest coordinated fraud.
