import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# 1. Generate Synthetic Transaction Data
def generate_synthetic_data(n_transactions=100):
    users = [f'User_{i}' for i in range(1,21)]  # 20 users
    amounts = np.random.normal(loc=100, scale=30, size=n_transactions).round(2)
    senders = random.choices(users, k=n_transactions)
    receivers = random.choices(users, k=n_transactions)
    
    # Introduce fraudulent transactions (high amounts)
    fraud_indices = random.sample(range(n_transactions), int(n_transactions * 0.1))  # 10% fraud
    for idx in fraud_indices:
        amounts[idx] = amounts[idx] * random.uniform(3, 5)  # Inflate fraud amounts
    
    data = pd.DataFrame({
        'Sender': senders,
        'Receiver': receivers,
        'Amount': amounts
    })
    return data

# 2. Statistical Analysis: Detect Anomalies
def detect_anomalies(df):
    # Simple threshold: Flag transactions > 2 standard deviations above mean
    mean_amount = df['Amount'].mean()
    std_amount = df['Amount'].std()
    threshold = mean_amount + 2 * std_amount
    df['Is_Fraud'] = df['Amount'] > threshold
    return df

# 3. Social Network Analysis: Build and Analyze Network
def build_network(df):
    G = nx.DiGraph()
    for _, row in df.iterrows():
        G.add_edge(row['Sender'], row['Receiver'], weight=row['Amount'])
    
    # Calculate degree centrality (number of connections)
    degree_centrality = nx.degree_centrality(G)
    
    # Identify suspicious users (top 3 by centrality)
    suspicious_users = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:3]
    suspicious_users = [user for user, _ in suspicious_users]
    return G, suspicious_users

# 4. Visualise Results
def visualize_results(df, G, suspicious_users):
    # Plot 1: Transaction Amount Distribution
    plt.figure("Figure 1", figsize=(10, 5))
    plt.hist(df[df['Is_Fraud'] == False]['Amount'], bins=20, alpha=0.5, label='Normal', color='blue', edgecolor='black')
    plt.hist(df[df['Is_Fraud'] == True]['Amount'], bins=20, alpha=0.5, label='Fraudulent', color='red', edgecolor='black')
    plt.title('Transaction Amount Distribution')
    plt.xlabel('Amount')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
    
    # Plot 2: Transaction Network
    plt.figure("Figure 2", figsize=(10, 5))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=8)
    nx.draw_networkx_nodes(G, pos, nodelist=suspicious_users, node_color='red', node_size=700)
    plt.title('Transaction Network (Suspicious Users in Red)')
    plt.show()

# Main Execution
if __name__ == '__main__':
    # Generate data
    df = generate_synthetic_data()
    
    # Statistical analysis
    df = detect_anomalies(df)
    
    # Social network analysis
    G, suspicious_users = build_network(df)
    
    # Visualize results
    visualize_results(df, G, suspicious_users)
    
    # Print summary
    print("Fraud Detection Summary:")
    print(f"Total Transactions: {len(df)}")
    print(f"Fraudulent Transactions: {df['Is_Fraud'].sum()} ({df['Is_Fraud'].mean()*100:.1f}%)")
    print("Suspicious Users (High Connections):", suspicious_users)