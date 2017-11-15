.PHONY : customer_profile_service agent_service inventory_service ticket_service job_service system_service  functional-test list install

customer_profile_service: 
	export PYTHONPATH=`pwd` && python2.7 -m pytest -v --instafail `pwd`/test/functional_test_suit/customer_profile_service/customer_profile_service.py --html=./report/customer_profile_service.html

inventory_service:
	export PYTHONPATH=`pwd` && python2. -m pytest -v --instafail `pwd`/test/functional_test_suit/inventory_service/inventory_service.py --html=./report/inventory_service.html

ticket_service: 
	export PYTHONPATH=`pwd` && python2. -m pytest -v --instafail  `pwd`/test/functional_test_suit/ticket_service/ticket_service.py --html=./report/ticket_service.html

job_service: 
	export PYTHONPATH=`pwd` && python2. -m pytest -v --instafail  `pwd`/test/functional_test_suit/job_service/job_service.py --html=./report/job_service.html

system_service: 
	export PYTHONPATH=`pwd` && python2. -m pytest -v --instafail  `pwd`/test/functional_test_suit/system_service/system_service.py --html=./report/system_service.html

agent_service: 
	export PYTHONPATH=`pwd` && python2. -m pytest -v --instafail  `pwd`/test/functional_test_suit/agent_service/agent_service.py --html=./report/agent_service.html

functional-test:  customer_profile_service inventory_service ticket_service job_service system_service agent_service pytest-html

list:
	@$(info Available Targets)
	@$(info ========= =======)
	@grep '^.PHONY:*' Makefile | sed 's/\.PHONY : //' |  tr " " "\n"

install:
	@$(info installing requirements...)
	python2.7 -m pip install -r requirements.txt --no-index

