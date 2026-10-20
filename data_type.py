# =====================================================================
# 1. NUMERIC TYPES
# =====================================================================
my_int = 42                 # int: Whole numbers
my_float = 3.14159          # float: Decimal numbers
my_complex = 2 + 3j         # complex: Numbers with a real and imaginary part

# =====================================================================
# 2. SEQUENCE TYPES
# =====================================================================
my_str = "Calculator"       # str: Text wrapped in quotes
my_list = [1, 2, 2, "three"] # list: Ordered, editable list (allows duplicates)
my_tuple = (10, 20, 30)     # tuple: Ordered list that CANNOT be changed

# =====================================================================
# 3. MAPPING TYPE
# =====================================================================
# dict: Key-value pairs for structuring data
my_dict = {
    "app_name": "Terminal Calc", 
    "version": 2.0, 
    "is_safe": True
}

# =====================================================================
# 4. SET TYPES
# =====================================================================
my_set = {1, 2, 3, 3, 4}    # set: Unordered unique items (the duplicate 3 is removed)
my_frozenset = frozenset({5, 6, 7}) # frozenset: A set that CANNOT be changed

# =====================================================================
# 5. BOOLEAN TYPE
# =====================================================================
is_running = True           # bool: True or False (used for logic conditions)
has_error = False

# =====================================================================
# 6. BINARY TYPES
# =====================================================================
my_bytes = b"Hello"         # bytes: Immutable raw binary data
my_bytearray = bytearray(5) # bytearray: Mutable raw binary data
my_memview = memoryview(my_bytes) # memoryview: Inspects memory buffers directly

# =====================================================================
# 7. NONE TYPE
# =====================================================================
empty_result = None         # NoneType: Represents nothing/null


# =====================================================================
# PRINTING VALUES AND THEIR TYPES
# =====================================================================
print("--- Numeric ---")
print(my_int, type(my_int))
print(my_float, type(my_float))

print("\n--- Sequences ---")
print(my_str, type(my_str))
print(my_list, type(my_list))

print("\n--- Mapping & Sets ---")
print(my_dict, type(my_dict))
print(my_set, type(my_set)) # Will print {1, 2, 3, 4}

print("\n--- Boolean & None ---")
print(is_running, type(is_running))
print(empty_result, type(empty_result))