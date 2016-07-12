#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.cache
Version  : 1.10.0
Release  : 16
URL      : http://tarballs.openstack.org/oslo.cache/oslo.cache-1.10.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.cache/oslo.cache-1.10.0.tar.gz
Summary  : Cache storage for Openstack projects.
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.cache-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : MarkupSafe-python
BuildRequires : PyYAML-python
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : appdirs-python
BuildRequires : debtcollector-python
BuildRequires : docutils-python
BuildRequires : dogpile.cache-python
BuildRequires : dogpile.core-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : hacking
BuildRequires : imagesize-python
BuildRequires : iso8601-python
BuildRequires : keystoneauth1-python
BuildRequires : mccabe-python
BuildRequires : monotonic-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : os-client-config-python
BuildRequires : oslo.config
BuildRequires : oslo.context-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.log-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pycodestyle-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : wrapt-python

%description
==========
oslo.cache
==========
.. image:: https://img.shields.io/pypi/v/oslo.cache.svg
:target: https://pypi.python.org/pypi/oslo.cache/
:alt: Latest Version

%package python
Summary: python components for the oslo.cache package.
Group: Default
Requires: dogpile.cache-python
Requires: oslo.config
Requires: oslo.i18n-python
Requires: oslo.log-python
Requires: oslo.utils-python
Requires: six-python

%description python
python components for the oslo.cache package.


%prep
%setup -q -n oslo.cache-1.10.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
