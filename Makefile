all : latex-and-r

latex-and-r : Dockerfile.latex-and-r
	docker build -t $@ -f $< .

