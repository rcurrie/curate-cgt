build:
	docker build -t curate-cgt .

protoc:
	docker run --rm -v `pwd`:`pwd` -w `pwd` znly/protoc --python_out=curate/ -I curate/ curate/variants.proto


test:
	docker run -it --rm \
		--entrypoint=py.test \
		-v `pwd`:/app:ro \
		curate-cgt -p no:cacheprovider -s -x

shell:
	docker run -it --rm \
		--entrypoint=/bin/sh \
		-v `pwd`:/app \
		curate-cgt
