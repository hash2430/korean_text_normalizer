Korean text normalizer
===
* Any comments or questions are welcome!!!

# How it works: Rule-based (not DNN-based)
+ Pattern matching: Patterns of number, english, chinese are described as pattern using regular expression at "patterns.py" module 
+ Dictianary searching: Once the pattern is found from above step, it searches how to read the specific non-korean word from "ko_dictionary.py" module.
# Interface
+ The user only needs to call korean.normalize(text) method.
# Calling order of normalizers
+ Once the korean.normalize(text) is called, each normalizers for specific patterns takes part in order. The order of normalizers are very important. If the order is messed up, there is no guratee this works as expected.
+ trim()
+ normalize_unit()
+ normalize_number()
+ normalize_english()
+ normalize_chinese()
+ normalize_dictionary_miss_alphabet() <== This part is for exception handling. 
# Exception handling
* How to handle English words that are not found in the dictionary?
* 1st option: read it as alphabet
* 2nd option: throw an exception
* => I chose the 1st option but also implemented for the second option and it is commented at the bottom of "korean.normalize() method to throw "DictionaryMissException"
# C-Interface: how to compile and link for using C-Python interface for C programs
1. Create a python3.6 environment 
2. Configure the python src path in c_wrapper.c 
    ex) setenv("PYTHONPATH","/home/administrator/projects/txt_norm",1);
3. Add python env from step 1 to LD_LIBRARY_PATH
    ex) export LD_LIBRARY_PATH= "/home/administrator/anaconda2/envs/txt_norm/lib"
4. Compile and link with options to refer to the environment created from step 1.
    ex) gcc c_wrapper.c -L/home/administrator/anaconda2/envs/txt_norm/lib -lpython3.6m -I/home/administrator/anaconda2/envs/txt_norm/include/python3.6m

