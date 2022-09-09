all: _list

ACE_VERSION ?= master
ACE_REMOTE ?= https://github.com/ajaxorg/ace-builds.git
ACE_TMP ?= ./build/ace

$(ACE_TMP):
	git clone --branch $(ACE_VERSION) $(ACE_REMOTE) $(ACE_TMP)

upgrade_ace: $(ACE_TMP)
	cd $(ACE_TMP) && git fetch --tags && git reset --hard $(ACE_VERSION)
	rsync --delete -r $(ACE_TMP)/src-min/ django_ace/static/django_ace/ace/

test:
	tox --parallel auto --recreate

clean:
	rm -rf build dist

build:
	python setup.py sdist bdist_wheel

publish-test: clean build
	twine upload -r testpypi --sign dist/*

publish: clean build
	@status=$$(git status --porcelain); \
	if test "x$${status}" = x; then \
		twine upload -r fdemmer-django-ace --sign dist/*; \
	else \
		echo Aborting upload: working directory is dirty >&2; \
	fi;


# list all targets (https://stackoverflow.com/a/26339924/652457)
.PHONY: _list
_list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs
