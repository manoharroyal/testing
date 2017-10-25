.PHONY : customer_profile_service agent_service inventory_service ticket_service job_service system_service init functional-test

init:
	@export PYTHONPATH=/home/manohar/python/manohar-rest-api-test-code-a44d1daf6542

customer_profile_service:
	python2.7 -m pytest /home/manohar/python/manohar-rest-api-test-code-a44d1daf6542/customer_profile_service/customer_profile_service.py

inventory_service:
	python2.7 -m pytest /home/manohar/python/manohar-rest-api-test-code-a44d1daf6542/inventory_service/inventory_service.py

ticket_service:
	python2.7 -m pytest /home/manohar/python/manohar-rest-api-test-code-a44d1daf6542/ticket_service/ticket_service.py

job_service:
	python2.7 -m pytest /home/manohar/python/manohar-rest-api-test-code-a44d1daf6542/job_service/job_service.py

system_service:
	python2.7 -m pytest /home/manohar/python/manohar-rest-api-test-code-a44d1daf6542/system_service/system_service.py

agent_service:
	python2.7 -m pytest /home/manohar/python/manohar-rest-api-test-code-a44d1daf6542/agent_service/agent_service.py

functional-test: inventory_service customer_profile_service ticket_service job_service system_service agent_service
