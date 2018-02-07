.PHONY : customer_profile_service agent_service inventory_service ticket_service auth_service job_service system_service box_service functional-test list install

customer_profile_service: 
	export PYTHONPATH=`pwd` && python2.7 -m pytest -v --instafail `pwd`/test/functional_test_suite/customer_profile_service/customer_profile_service.py --html=./report/customer_profile_service.html --junitxml=./report/customer_profile_service.xml

inventory_service:
	export PYTHONPATH=`pwd` && python2.7 -m pytest -v --instafail `pwd`/test/functional_test_suite/inventory_service/inventory_service.py --html=./report/inventory_service.html --junitxml=./report/inventory_service.xml

ticket_service: 
	export PYTHONPATH=`pwd` && python2.7 -m pytest -v --instafail  `pwd`/test/functional_test_suite/ticket_service/ticket_service.py --html=./report/ticket_service.html --junitxml=./report/ticket_service.xml

job_service: 
	export PYTHONPATH=`pwd` && python2.7 -m pytest -v --instafail  `pwd`/test/functional_test_suite/job_service/job_service.py --html=./report/job_service.html --junitxml=./report/job_service.xml

system_service: 
	export PYTHONPATH=`pwd` && python2.7 -m pytest -v --instafail  `pwd`/test/functional_test_suite/system_service/system_service.py --html=./report/system_service.html --junitxml=./report/system_service.xml

agent_service: 
	export PYTHONPATH=`pwd` && python2.7 -m pytest -v --instafail  `pwd`/test/functional_test_suite/agent_service/agent_service.py --html=./report/agent_service.html --junitxml=./report/agent_service.xml

auth_service:
	export PYTHONPATH=`pwd` && python2.7 -m pytest -v --instafail  `pwd`/test/functional_test_suite/auth_service/auth_service.py --html=./report/auth_service.html --junitxml=./report/auth_service.xml

box_service:
	export PYTHONPATH=`pwd` && python2.7 -m pytest -v --instafail  `pwd`/test/functional_test_suite/box_service/box_service.py --html=./report/box_service.html --junitxml=./report/box_service.xml

functional-test:  customer_profile_service inventory_service ticket_service job_service system_service agent_service auth_service box_service pytest-html

list:
	@$(info Available Targets)
	@$(info ========= =======)
	@grep '^.PHONY:*' GNUmakefile | sed 's/\.PHONY : //' |  tr " " "\n"

install:
	@$(info installing requirements...)
	python2.7 -m pip install -r requirements.txt

