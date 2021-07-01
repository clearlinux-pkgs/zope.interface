#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.interface
Version  : 5.4.0
Release  : 73
URL      : https://files.pythonhosted.org/packages/ae/58/e0877f58daa69126a5fb325d6df92b20b77431cd281e189c5ec42b722f58/zope.interface-5.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ae/58/e0877f58daa69126a5fb325d6df92b20b77431cd281e189c5ec42b722f58/zope.interface-5.4.0.tar.gz
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
        ====================

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
Provides: pypi(zope.interface)
Requires: pypi(setuptools)

%description python3
python3 components for the zope.interface package.


%prep
%setup -q -n zope.interface-5.4.0
cd %{_builddir}/zope.interface-5.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618502429
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.interface
cp %{_builddir}/zope.interface-5.4.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.interface/a0b53f43aab58b46bf79ba756c50771c605ab4c5
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
