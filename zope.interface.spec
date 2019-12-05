#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.interface
Version  : 4.7.1
Release  : 52
URL      : https://files.pythonhosted.org/packages/c3/05/bf3130eb799548882ce61b7c3d2dbc5d4d5cc6e821efa8786c5273d56844/zope.interface-4.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c3/05/bf3130eb799548882ce61b7c3d2dbc5d4d5cc6e821efa8786c5273d56844/zope.interface-4.7.1.tar.gz
Summary  : Interfaces for Python
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.interface-license = %{version}-%{release}
Requires: zope.interface-python = %{version}-%{release}
Requires: zope.interface-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : setuptools

%description
``zope.interface``
==================
.. image:: https://img.shields.io/pypi/v/zope.interface.svg
:target: https://pypi.python.org/pypi/zope.interface/
:alt: Latest Version

%package license
Summary: license components for the zope.interface package.
Group: Default

%description license
license components for the zope.interface package.


%package python
Summary: python components for the zope.interface package.
Group: Default
Requires: zope.interface-python3 = %{version}-%{release}

%description python
python components for the zope.interface package.


%package python3
Summary: python3 components for the zope.interface package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.interface package.


%prep
%setup -q -n zope.interface-4.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573508089
# -Werror is for werrorists
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
mkdir -p %{buildroot}/usr/share/package-licenses/zope.interface
cp %{_builddir}/zope.interface-4.7.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.interface/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.interface/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
