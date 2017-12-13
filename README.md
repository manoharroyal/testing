# dss-test
Repository including functional and integration tests

# Test Execution Steps

**1. cloning the repo and setup**
    
    1. git clone https://github.td.teradata.com/tmcindia/dss-test.git
    2. make install # will install all the required packages
    3. # Edit the configuration in env folder for customized enviroments

**2. show list of make targets**

    make list

**3. Execute individual or complete test suit**

    eg:
    # making individual test
    make customer_profile_service

    # making functional-test-suit
    make -k functional-test

**4. Running the Test Functions manually**

    steps:
        export PYTHONPATH=<project_root_directory>
        pytest <path_to_file_name.py> -k <test_function_name>

**5. Reports**

    The reports will be generated in the "report" folder in the parent directory

**6. Logs**

    The output logs will generated in the "logs" folder in the parent directory