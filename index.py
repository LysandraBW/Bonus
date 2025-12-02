from copy import deepcopy

class DB:
    def __init__(self):
        # The data stored before transaction.
        self.data_0 = {}
        # The data stored during transaction.
        self.data_1 = {}
        self.transaction_in_progress = False
    
    def begin_transaction(self):
        if self.transaction_in_progress:
            raise Exception("Already in Transaction!")
        
        self.data_1 = deepcopy(self.data_0)
        self.transaction_in_progress = True
    
    
    def put(self, k, v):
        if not isinstance(k, str):
            raise Exception("Key Must Be String!")
        
        if not isinstance(v, int):
            raise Exception("Value Must Be Integer!")
        
        if not self.transaction_in_progress:
            raise Exception("Transaction Must Be In Progress!")
        
        self.data_1[k] = v
    

    def get(self, k):
        if not isinstance(k, str):
            raise Exception("Key Must Be String!")

        return self.data_0.get(k, None)
    

    def commit(self):
        if not self.transaction_in_progress:
            raise Exception("Nothing to Commit!")
        
        self.data_0 = deepcopy(self.data_1)
        self.data_1 = {}
        self.transaction_in_progress = False
    

    def rollback(self):
        if not self.transaction_in_progress:
            raise Exception("Nothing to Rollback!")
        
        self.data_1 = {}
        self.transaction_in_progress = False



# TESTING
# I tried the simple examples in the assignment description below, nothing fancy!
# I could've done more, but since the code was simple, I felt that there *probably*
# wouldn't be an issue. Is there? I hope not, I'd look pretty silly.
PASSED = "Passed"
FAILED = "Failed"

db = DB()

# Test 1:
if db.get("A") == None:
    print(PASSED)
else:
    print(FAILED)

# Test 2:
try:
    db.put("A", 5)
except Exception:
    print(PASSED)
else:
    print(FAILED)

# Test 3:
db.begin_transaction()
if db.transaction_in_progress:
    print(PASSED)
else:
    print(FAILED)

# Test 4:
db.put("A", 5)

if db.get("A") == None:
    print(PASSED)
else:
    print(FAILED)

# Test 5:
db.put("A", 6)
db.commit()

if db.get("A") == 6:
    print(PASSED)
else:
    print(FAILED)

# Test 6:
try:
    db.commit()
except Exception:
    print(PASSED)
else:
    print(FAILED)

# Test 7:
try:
    db.rollback()
except Exception:
    print(PASSED)
else:
    print(FAILED)

# Test 8:
if db.get("B") == None:
    print(PASSED)
else:
    print(FAILED)

# Test 9:
db.begin_transaction()
db.put("B", 10)
db.rollback()

if db.get("B") == None:
    print(PASSED)
else:
    print(FAILED)