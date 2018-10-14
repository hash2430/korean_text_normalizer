Korean text normalizer
===
* Any comments or questions are welcome!!!

1. How it works: Rule-based (not DNN-based)
1.1 Pattern matching: Patterns of number, english, chinese are described as pattern using regular expression at "patterns.py" module 
1.2 Dictianary searching: Once the pattern is found from above step, it searches how to read the specific non-korean word from "ko_dictionary.py" module.
2. Interface
2.1 The user only needs to call korean.normalize(text) method.
3. Calling order of normalizers
* Once the korean.normalize(text) is called, each normalizers for specific patterns takes part in order. The order of normalizers are very important. If the order is messed up, there is no guratnee this works as expected.
 trim
3.1 normalize_unit()
3.2 normalize_number()
3.3 normalize_english()
3.4 normalize_chinese()
3.5 normalize_dictionary_miss_alphabet() <== This part is for exception handling. 
4. Exception handling
* How to handle English words that are not found in the dictionary?
* 1st option: read it as alphabet
* 2nd option: throw an exception
* => I chose the 1st option but also implemented for the second option and it is commented at the bottom of "korean.normalize() method to throw "DictionaryMissException"
+ C-Interface: how to compile and link for using C-Python interface for C programs
+ Create a python3.6 environment 
+ Configure the python src path in c_wrapper.c 
    ex) setenv("PYTHONPATH","/home/administrator/projects/txt_norm",1);
+ Add python env from step 1 to LD_LIBRARY_PATH
    ex) export LD_LIBRARY_PATH= "/home/administrator/anaconda2/envs/txt_norm/lib"
+ Compile and link with options to refer to the environment created from step 1.
    ex) gcc c_wrapper.c -L/home/administrator/anaconda2/envs/txt_norm/lib -lpython3.6m -I/home/administrator/anaconda2/envs/txt_norm/include/python3.6m

