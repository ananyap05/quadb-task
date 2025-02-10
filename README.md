# quadb-task
# Simple Blockchain Simulation

## Overview
This project is a basic blockchain simulation that demonstrates the core principles of blockchain technology. It includes block creation, hashing, proof-of-work, and blockchain validation.

## Features
- Blocks contain an index, timestamp, list of transactions, previous block hash, and current block hash.
- SHA-256 hashing algorithm is used for block integrity.
- Proof-of-work mechanism for mining blocks.
- Blockchain integrity validation to detect tampering.

## Prerequisites
Ensure you have Python installed on your system. You can download it from [Python.org](https://www.python.org/downloads/).

## Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/simple-blockchain.git
   ```
2. Navigate to the project directory:
   ```sh
   cd simple-blockchain
   ```
3. Install dependencies (if any, but none required for basic functionality):
   ```sh
   pip install -r requirements.txt
   ```

## Execution
1. Run the script to simulate the blockchain:
   ```sh
   python blockchain.py
   ```
2. The output will display the details of each block in the chain.
3. The script will also validate the blockchain integrity and indicate if any tampering is detected.

## Example Output
```
Index: 0
Timestamp: 1700000000.0000
Transactions: ["Genesis Block"]
Previous Hash: 0
Current Hash: 0000abcd1234...
--------------------------------------------------
Blockchain valid? True
```

## Additional Notes
- Modify `transactions` in `add_block()` to add new transactions.
- Change the `difficulty` parameter in `Blockchain()` to adjust mining difficulty.
- Experiment with tampering with block data to observe integrity detection.

## Contribution
Feel free to fork the repository and submit pull requests with improvements or additional features.

## License
This project is licensed under the MIT License.


