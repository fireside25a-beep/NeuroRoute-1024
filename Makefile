.PHONY: all test demo clean verify audit sanitize
PROJECTS := neuroroute-1024 neuroroute-devtools-1024
all test demo clean:
	@for p in $(PROJECTS); do echo "== $$p :: $@ =="; $(MAKE) -C "projects/$$p" $@ || exit $$?; done
verify:
	python3 scripts/check_boundaries.py
	$(MAKE) clean
	$(MAKE) all
	$(MAKE) test
	$(MAKE) demo
audit:
	python3 scripts/check_boundaries.py
sanitize:
	@for p in $(PROJECTS); do echo "== $$p :: sanitize =="; $(MAKE) -C "projects/$$p" sanitize || exit $$?; done
