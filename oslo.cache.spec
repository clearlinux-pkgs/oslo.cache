#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : oslo.cache
Version  : 1.31.2
Release  : 35
URL      : http://tarballs.openstack.org/oslo.cache/oslo.cache-1.31.2.tar.gz
Source0  : http://tarballs.openstack.org/oslo.cache/oslo.cache-1.31.2.tar.gz
Source99 : http://tarballs.openstack.org/oslo.cache/oslo.cache-1.31.2.tar.gz.asc
Summary  : Cache storage for OpenStack projects.
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.cache-license = %{version}-%{release}
Requires: oslo.cache-python = %{version}-%{release}
Requires: oslo.cache-python3 = %{version}-%{release}
Requires: Sphinx
Requires: dogpile.cache
Requires: openstackdocstheme
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.utils
Requires: oslotest
Requires: pymongo
Requires: python-memcached
Requires: python-mock
Requires: reno
Requires: six
Requires: sphinxcontrib-apidoc
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
Team and repository tags
        ========================

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
%setup -q -n oslo.cache-1.31.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544544049
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
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
