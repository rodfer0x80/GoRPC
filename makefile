.PHONY: build-embed
build-embed:
	echo "embed" | ./scripts/build.py

.PHONY: build-admin
build-admin:
	echo "admin" | ./scripts/build.py

.PHONY: build-interface
build-interface:
	echo "interface" | ./scripts/build.py

.PHONY: build
build:
	echo "all" | ./scripts/build.py


.PHONY: run-admin
run-admin:
	echo "admin" | ./scripts/run.py

.PHONY: run-embed
run-embed:
	echo "embed" | ./scripts/run.py

.PHONY: run-interface
run-interface:
	echo "interface" | ./scripts/run.py

.PHONY: run
run:
	echo "all" | ./scripts/run.py


.PHONY: clean
clean:
	./scripts/clean.sh
