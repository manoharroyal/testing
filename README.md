# dss-test
Repository including functional and integration tests

# Test Execution Steps

**1. cloning the repo and setup**
    
    git clone https://github.td.teradata.com/tmcindia/dss-test.git
    make install # will install all the required packages

**2. show list of make targets**

    make list

**3. Execute individual or complete test suit**

    eg:
    # making individual test
    make customer_profile_service

    # making functional-test-suit
    make -k functional-test

**Invidivudla**
eg


**4. Running the Test Functions manually**

    steps:
        export PYTHONPATH=<project_root_directory>
        pytest <path_to_file_name.py> -k <test_function_name>

**4. Reports**

    The reports will be generated in the "report" folder in the parent directory
