.SILENT:

ifneq ("$(wildcard .env)","")
	include .env
endif

PREVIEW_FLAG =
ifeq ($(PREVIEW),1)
PREVIEW_FLAG = --preview
endif

dist: cs analyze test
cs: analyze/ruff-format
analyze: analyze/pyright
test: test/pytest

render:
	@for d in scene/*/ ; do \
		$(MAKE) PREVIEW=$(PREVIEW) render/$$d/hd@30 ; \
	done

preview/%: %
	poetry run manim render $</__init__.py --renderer opengl $(PREVIEW_FLAG)
debug/%: %
	poetry run manim render $</__init__.py --renderer opengl $(PREVIEW_FLAG) --enable_wireframe
render/%/4k@60: %
	poetry run manim render $</__init__.py --resolution 3840,2160 --fps 60 $(PREVIEW_FLAG)
render/%/4k@30: %
	poetry run manim render $</__init__.py --resolution 3840,2160 --fps 30 $(PREVIEW_FLAG)
render/%/hd@60: %
	poetry run manim render $</__init__.py --resolution 1920,1080 --fps 60 $(PREVIEW_FLAG)
render/%/hd@30: %
	poetry run manim render $</__init__.py --resolution 1920,1080 --fps 30 $(PREVIEW_FLAG)

analyze/ruff-check:
	poetry run ruff check
analyze/ruff-format:
	poetry run ruff format

analyze/pyright:
	poetry run pyright

test/pytest:
	poetry run pytest
