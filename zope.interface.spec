#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.interface
Version  : 4.1.3
Release  : 15
URL      : https://pypi.python.org/packages/source/z/zope.interface/zope.interface-4.1.3.tar.gz
Source0  : https://pypi.python.org/packages/source/z/zope.interface/zope.interface-4.1.3.tar.gz
Summary  : Interfaces for Python
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.interface-python
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
``zope.interface``
==================
.. image:: https://pypip.in/version/zope.interface/badge.svg?style=flat
:target: https://pypi.python.org/pypi/zope.interface/
:alt: Latest Version

%package python
Summary: python components for the zope.interface package.
Group: Default

%description python
python components for the zope.interface package.


%prep
%setup -q -n zope.interface-4.1.3

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m nose
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
