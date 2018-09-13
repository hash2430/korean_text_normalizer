# This code is modified from original work by https://github.com/carpedm20/multi-speaker-tacotron-tensorflow/tree/master/text
# how to compile and link for using C-Python interface for C programs
1. Create a python3.6 environment 
2. Configure the python src path in c_wrapper.c 
    ex) setenv("PYTHONPATH","/home/administrator/projects/txt_norm",1);
3. Add python env from step 1 to LD_LIBRARY_PATH
    ex) export LD_LIBRARY_PATH= "/home/administrator/anaconda2/envs/txt_norm/lib"
4. Compile and link with options to refer to the environment created from step 1.
    ex) gcc c_wrapper.c -L/home/administrator/anaconda2/envs/txt_norm/lib -lpython3.6m -I/home/administrator/anaconda2/envs/txt_norm/include/python3.6m

