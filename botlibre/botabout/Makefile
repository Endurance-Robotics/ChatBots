# Botabout makefile

topic_graph = chatbots

all: run

.ONESHELL:
run:
	(command -v dot) &&
	dot -Tpng -o $(topic_graph).png $(topic_graph).dot &&
	(command -v gpicview) && gpicview $(topic_graph).png

.PHONY: clean
clean:
	rm $(topic_graph).png
