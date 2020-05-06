all : dewittpe/latex-and-r dewittpe/rpy


dewittpe/latex-and-r : Dockerfile.latex-and-r
	docker build -t $@ -f $< .


dewittpe/rpy : Dockerfile.rpy
	docker build -t $@ -f $< .
