import hashlib
import time
import json

class Block:
    """Represents a single block in the blockchain."""
    def __init__(self, index, previous_hash, transactions, difficulty=2):
        self.index = index  # Position of the block in the blockchain
        self.timestamp = time.time()  # Time of block creation
        self.transactions = transactions  # List of transactions in the block
        self.previous_hash = previous_hash  # Hash of the previous block
        self.nonce = 0  # Used for proof-of-work
        self.difficulty = difficulty  # Mining difficulty level
        self.hash = self.compute_hash()  # Current block hash

    def compute_hash(self):
        """Computes SHA-256 hash of the block data."""
        block_data = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine_block(self):
        """Performs proof-of-work by finding a hash that starts with a certain number of leading zeros."""
        while not self.hash.startswith('0' * self.difficulty):
            self.nonce += 1
            self.hash = self.compute_hash()

class Blockchain:
    """Manages the blockchain by handling block addition and validation."""
    def __init__(self, difficulty=2):
        self.chain = []  # List of blocks forming the blockchain
        self.difficulty = difficulty  # Difficulty level for mining
        self.create_genesis_block()

    def create_genesis_block(self):
        """Creates the first block (genesis block) with default values."""
        genesis_block = Block(0, "0", ["Genesis Block"], self.difficulty)
        genesis_block.mine_block()
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        """Adds a new block to the blockchain with given transactions."""
        prev_block = self.chain[-1]  # Get the previous block
        new_block = Block(len(self.chain), prev_block.hash, transactions, self.difficulty)
        new_block.mine_block()
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Validates the blockchain integrity by checking hashes and links."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.compute_hash() or current.previous_hash != previous.hash:
                return False
        return True

    def print_chain(self):
        """Prints the details of each block in the blockchain."""
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Current Hash: {block.hash}")
            print("-" * 50)

# Demonstration of Blockchain functionality
if __name__ == "__main__":
    blockchain = Blockchain(difficulty=3)
    blockchain.add_block(["Alice pays Bob 10 BTC"])  # Adding first transaction block
    blockchain.add_block(["Bob pays Charlie 5 BTC"])  # Adding second transaction block
    blockchain.print_chain()  # Print the blockchain details
    
    # Check if blockchain is valid
    print("Blockchain valid?", blockchain.is_chain_valid())
