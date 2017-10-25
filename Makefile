.PHONY : customer_profile_service agent_service inventory_service ticket_service job_service system_service init functional-test

init:
	@export PYTHONPATH=/home/manohar/python/manohar-rest-api-test-code-a44d1daf6542

customer_profile_service:
	pytest /home/manohar/python/manohar-rest-api-test-code-a44d1daf6542/customer_profile_service/customer_profile_service.py --html=./report/customer_profile_service.html

inventory_service:
	pytest /home/manohar/python/manohar-rest-api-test-code-a44d1daf6542/inventory_service/inventory_service.py --html=./report/inventory_service.html

ticket_service:
	pytest /home/manohar/python/manohar-rest-api-test-code-a44d1daf6542/ticket_service/ticket_service.py --html=./report/ticket_service.html

job_service:
	pytest /home/manohar/python/manohar-rest-api-test-code-a44d1daf6542/job_service/job_service.py --html=./report/job_service.html

system_service:
	pytest /home/manohar/python/manohar-rest-api-test-code-a44d1daf6542/system_service/system_service.py --html=./report/system_service.html

agent_service:
	pytest /home/manohar/python/manohar-rest-api-test-code-a44d1daf6542/agent_service/agent_service.py --html=./report/agent_service.html

functional-test: customer_profile_service inventory_service ticket_service job_service system_service agent_service pytest-html
