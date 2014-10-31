.PHONY: build favicon

BOOTSTRAP = bower_components/bootstrap/dist
BOOTSTRAP_SOCIAL = bower_components/bootstrap-social
FA = bower_components/font-awesome
JQUERY = bower_components/jquery
ZERO_CLIPBOARD = bower_components/zeroclipboard
ASSET_DEST = assets

FAVICON_FILE = $(ASSET_DEST)/img/hawk-head.png

build:
	bower update
	gulp

	cp $(BOOTSTRAP)/css/* $(ASSET_DEST)/css
	cp $(BOOTSTRAP)/fonts/* $(ASSET_DEST)/fonts
	cp $(BOOTSTRAP)/js/* $(ASSET_DEST)/js
	cp $(BOOTSTRAP_SOCIAL)/*.css $(ASSET_DEST)/css
	cp $(FA)/css/* $(ASSET_DEST)/css
	cp $(FA)/fonts/* $(ASSET_DEST)/fonts
	cp $(JQUERY)/jquery.min.* $(ASSET_DEST)/js
	cp $(ZERO_CLIPBOARD)/ZeroClipboard.* $(ASSET_DEST)/js

favicon:
	@echo $(FAVICON_FILE)
	convert $(FAVICON_FILE) -resize 16x16 $(ASSET_DEST)/img/favicon-16.png
	convert $(FAVICON_FILE) -resize 32x32 $(ASSET_DEST)/img/favicon-32.png
	convert $(FAVICON_FILE) -resize 48x48 $(ASSET_DEST)/img/favicon-48.png
	convert $(FAVICON_FILE) -resize 57x57 $(ASSET_DEST)/img/favicon-57.png
	convert $(FAVICON_FILE) -resize 64x64 $(ASSET_DEST)/img/favicon-64.png
	convert $(FAVICON_FILE) -resize 72x72 $(ASSET_DEST)/img/favicon-72.png
	convert $(FAVICON_FILE) -resize 96x96 $(ASSET_DEST)/img/favicon-96.png
	convert $(FAVICON_FILE) -resize 120x120 $(ASSET_DEST)/img/favicon-120.png
	convert $(FAVICON_FILE) -resize 128x128 $(ASSET_DEST)/img/favicon-128.png
	convert $(FAVICON_FILE) -resize 144x144 $(ASSET_DEST)/img/favicon-144.png
	convert $(FAVICON_FILE) -resize 152x152 $(ASSET_DEST)/img/favicon-152.png
	convert $(FAVICON_FILE) -resize 195x195 $(ASSET_DEST)/img/favicon-195.png
	convert $(FAVICON_FILE) -resize 228x228 $(ASSET_DEST)/img/favicon-228.png

	convert $(ASSET_DEST)/img/favicon-16.png \
	    $(ASSET_DEST)/img/favicon-32.png \
	    $(ASSET_DEST)/img/favicon-48.png \
	    $(ASSET_DEST)/img/favicon-64.png \
	    $(ASSET_DEST)/img/favicon-128.png \
	    $(ASSET_DEST)/img/favicon.ico
