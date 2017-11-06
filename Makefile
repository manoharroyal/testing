.PHONY : customer_profile_service agent_service inventory_service ticket_service job_service system_service init functional-test list

init:
	@export PYTHONPATH=`pwd`

customer_profile_service: init
	pytest -v `pwd`/test/functional_test_suit/customer_profile_service/customer_profile_service.py --html=./report/customer_profile_service.html

inventory_service: init
	pytest -v `pwd`/test/functional_test_suit/inventory_service/inventory_service.py --html=./report/inventory_service.html

ticket_service: init
	pytest -v `pwd`/test/functional_test_suit/ticket_service/ticket_service.py --html=./report/ticket_service.html

job_service: init
	pytest -v `pwd`/test/functional_test_suit/job_service/job_service.py --html=./report/job_service.html

system_service: init
	pytest -v `pwd`/test/functional_test_suit/system_service/system_service.py --html=./report/system_service.html

agent_service: init
	pytest -v `pwd`/test/functional_test_suit/agent_service/agent_service.py --html=./report/agent_service.html

functional-test: customer_profile_service inventory_service ticket_service job_service system_service agent_service pytest-html

list:
	@$(info Available Targets)
	@$(info ========= =======)
	@grep '^.PHONY:*' Makefile | sed 's/\.PHONY : //' |  tr " " "\n"
