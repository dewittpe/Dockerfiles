all : dewittpe/latex-and-r

dewittpe/latex-and-r : Dockerfile.latex-and-r
	docker build -t $@ -f $< .

