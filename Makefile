
.PHONY: all
all: website move_files
	@echo "Done."

.PHONY: website
website:
	@echo "Making the Website..."
	cd src && python3 website-render.py

.PHONY: move_files
move_files:
	cp -r src/static .
	cp src/templates/legal-statements.html .
	cp src/sitemap.xml .
	cp src/favicon.png .
	cp src/weblogo.png .
	mv src/index.html .
	rm -rf about-me
	mv src/about-me .
	cp src/templates/resume-cn.html about-me/
	
	rm -rf life
	mv src/life .
	
	rm -rf study
	mv src/study .
	
	rm -rf documentation
	mv src/documentation .
	
