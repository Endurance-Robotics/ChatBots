# Botabout makefile

topic_graph = chatbots

all: run

.ONESHELL:
run:
	dot -Kfdp -Tpng -o $(topic_graph).png $(topic_graph).dot &&
	gpicview $(topic_graph).png

.PHONY: clean

clean:
	rm $(topic_graph).png
