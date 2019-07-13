#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC43F0EE211DFED8 (infra-root@openstack.org)
#
Name     : oslo.cache
Version  : 1.36.0
Release  : 44
URL      : http://tarballs.openstack.org/oslo.cache/oslo.cache-1.36.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.cache/oslo.cache-1.36.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.cache/oslo.cache-1.36.0.tar.gz.asc
Summary  : Cache storage for OpenStack projects.
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.cache-license = %{version}-%{release}
Requires: oslo.cache-python = %{version}-%{release}
Requires: oslo.cache-python3 = %{version}-%{release}
Requires: dogpile.cache
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.utils
Requires: pymongo
Requires: python-memcached
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : dogpile.cache
BuildRequires : oslo.config
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : pymongo
BuildRequires : python-memcached
BuildRequires : six

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/oslo.cache.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package license
Summary: license components for the oslo.cache package.
Group: Default

%description license
license components for the oslo.cache package.


%package python
Summary: python components for the oslo.cache package.
Group: Default
Requires: oslo.cache-python3 = %{version}-%{release}

%description python
python components for the oslo.cache package.


%package python3
Summary: python3 components for the oslo.cache package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.cache package.


%prep
%setup -q -n oslo.cache-1.36.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561039460
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.cache
cp LICENSE %{buildroot}/usr/share/package-licenses/oslo.cache/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.cache/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
