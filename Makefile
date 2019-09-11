ROOT_DIR=$(shell pwd)
# Tasks

test:
	python $(ROOT_DIR)/api-rate-limiter/tests/test_rate_mgr.py;\
	python $(ROOT_DIR)/api-rate-limiter/tests/test_rate_mgr_integration.py;\
