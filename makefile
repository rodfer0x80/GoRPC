.PHONY: build-embed
build-embed:
	echo "emb" | ./scripts/build.py

.PHONY: build-admin
build-admin:
	echo "adm" | ./scripts/build.py

.PHONY: build-interface
build-interface:
	echo "ifc" | ./scripts/build.py

.PHONY: build
build:
	echo "all" | ./scripts/build.py


.PHONY: run-admin
run-admin:
	echo "adm" | ./scripts/run.py

.PHONY: run-embed
run-embed:
	echo "emb" | ./scripts/run.py

.PHONY: run-interface
run-interface:
	echo "ifc" | ./scripts/run.py

.PHONY: run
run:
	echo "all" | ./scripts/run.py


.PHONY: clean
clean:
	./scripts/clean.sh
