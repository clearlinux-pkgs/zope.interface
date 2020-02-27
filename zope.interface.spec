#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.interface
Version  : 4.7.1
Release  : 54
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

.. image:: https://img.shields.io/pypi/pyversions/zope.interface.svg
        :target: https://pypi.org/project/zope.interface/
        :alt: Supported Python versions

.. image:: https://travis-ci.org/zopefoundation/zope.interface.svg?branch=master
        :target: https://travis-ci.org/zopefoundation/zope.interface

.. image:: https://readthedocs.org/projects/zopeinterface/badge/?version=latest
        :target: https://zopeinterface.readthedocs.io/en/latest/
        :alt: Documentation Status

This package is intended to be independently reusable in any Python
project. It is maintained by the `Zope Toolkit project
<https://zopetoolkit.readthedocs.io/>`_.

This package provides an implementation of "object interfaces" for Python.
Interfaces are a mechanism for labeling objects as conforming to a given
API or contract. So, this package can be considered as implementation of
the `Design By Contract`_ methodology support in Python.

.. _Design By Contract: http://en.wikipedia.org/wiki/Design_by_contract

For detailed documentation, please see https://zopeinterface.readthedocs.io/en/latest/

Changes
=======

4.7.1 (2019-11-11)
------------------

- Use Python 3 syntax in the documentation.  See `issue 119
  <https://github.com/zopefoundation/zope.interface/issue/119>`_.


4.7.0 (2019-11-11)
------------------

- Drop support for Python 3.4.

- Fix ``queryTaggedValue``, ``getTaggedValue``, ``getTaggedValueTags``
  subclass inheritance. See `PR 144
  <https://github.com/zopefoundation/zope.interface/pull/144>`_.

- Add support for Python 3.8.


4.6.0 (2018-10-23)
------------------

- Add support for Python 3.7

- Fix ``verifyObject`` for class objects with staticmethods on
  Python 3. See `issue 126
  <https://github.com/zopefoundation/zope.interface/issues/126>`_.


4.5.0 (2018-04-19)
------------------

- Drop support for 3.3, avoid accidental dependence breakage via setup.py.
  See `PR 110 <https://github.com/zopefoundation/zope.interface/pull/110>`_.
- Allow registering and unregistering instance methods as listeners.
  See `issue 12 <https://github.com/zopefoundation/zope.interface/issues/12>`_
  and `PR 102 <https://github.com/zopefoundation/zope.interface/pull/102>`_.
- Synchronize and simplify zope/__init__.py. See `issue 114
  <https://github.com/zopefoundation/zope.interface/issues/114>`_


4.4.3 (2017-09-22)
------------------

- Avoid exceptions when the ``__annotations__`` attribute is added to
  interface definitions with Python 3.x type hints. See `issue 98
  <https://github.com/zopefoundation/zope.interface/issues/98>`_.
- Fix the possibility of a rare crash in the C extension when
  deallocating items. See `issue 100
  <https://github.com/zopefoundation/zope.interface/issues/100>`_.


4.4.2 (2017-06-14)
------------------

- Fix a regression storing
  ``zope.component.persistentregistry.PersistentRegistry`` instances.
  See `issue 85 <https://github.com/zopefoundation/zope.interface/issues/85>`_.

- Fix a regression that could lead to the utility registration cache
  of ``Components`` getting out of sync. See `issue 93
  <https://github.com/zopefoundation/zope.interface/issues/93>`_.

4.4.1 (2017-05-13)
------------------

- Simplify the caching of utility-registration data. In addition to
  simplification, avoids spurious test failures when checking for
  leaks in tests with persistent registries. See `pull 84
  <https://github.com/zopefoundation/zope.interface/pull/84>`_.

- Raise ``ValueError`` when non-text names are passed to adapter registry
  methods:  prevents corruption of lookup caches.

4.4.0 (2017-04-21)
------------------

- Avoid a warning from the C compiler.
  (https://github.com/zopefoundation/zope.interface/issues/71)

- Add support for Python 3.6.

4.3.3 (2016-12-13)
------------------

- Correct typos and ReST formatting errors in documentation.

- Add API documentation for the adapter registry.

- Ensure that the ``LICENSE.txt`` file is included in built wheels.

- Fix C optimizations broken on Py3k.  See the Python bug at:
  http://bugs.python.org/issue15657
  (https://github.com/zopefoundation/zope.interface/issues/60)


4.3.2 (2016-09-05)
------------------

- Fix equality testing of ``implementedBy`` objects and proxies.
  (https://github.com/zopefoundation/zope.interface/issues/55)


4.3.1 (2016-08-31)
------------------

- Support Components subclasses that are not hashable.
  (https://github.com/zopefoundation/zope.interface/issues/53)


4.3.0 (2016-08-31)
------------------

- Add the ability to sort the objects returned by ``implementedBy``.
  This is compatible with the way interface classes sort so they can
  be used together in ordered containers like BTrees.
  (https://github.com/zopefoundation/zope.interface/issues/42)

- Make ``setuptools`` a hard dependency of ``setup.py``.
  (https://github.com/zopefoundation/zope.interface/issues/13)

- Change a linear algorithm (O(n)) in ``Components.registerUtility`` and
  ``Components.unregisterUtility`` into a dictionary lookup (O(1)) for
  hashable components. This substantially improves the time taken to
  manipulate utilities in large registries at the cost of some
  additional memory usage. (https://github.com/zopefoundation/zope.interface/issues/46)


4.2.0 (2016-06-10)
------------------

- Add support for Python 3.5

- Drop support for Python 2.6 and 3.2.


4.1.3 (2015-10-05)
------------------

- Fix installation without a C compiler on Python 3.5
  (https://github.com/zopefoundation/zope.interface/issues/24).


4.1.2 (2014-12-27)
------------------

- Add support for PyPy3.

- Remove unittest assertions deprecated in Python3.x.

- Add ``zope.interface.document.asReStructuredText``, which formats the
  generated text for an interface using ReST double-backtick markers.


4.1.1 (2014-03-19)
------------------

- Add support for Python 3.4.


4.1.0 (2014-02-05)
------------------

- Update ``boostrap.py`` to version 2.2.

- Add ``@named(name)`` declaration, that specifies the component name, so it
  does not have to be passed in during registration.


4.0.5 (2013-02-28)
------------------

- Fix a bug where a decorated method caused false positive failures on
  ``verifyClass()``.


4.0.4 (2013-02-21)
------------------

- Fix a bug that was revealed by porting zope.traversing. During a loop, the
  loop body modified a weakref dict causing a ``RuntimeError`` error.

4.0.3 (2012-12-31)
------------------

- Fleshed out PyPI Trove classifiers.

4.0.2 (2012-11-21)
------------------

- Add support for Python 3.3.

- Restored ability to install the package in the absence of ``setuptools``.

- LP #1055223:  Fix test which depended on dictionary order and failed randomly
  in Python 3.3.

4.0.1 (2012-05-22)
------------------

- Drop explicit ``DeprecationWarnings`` for "class advice" APIS (these
  APIs are still deprecated under Python 2.x, and still raise an exception
  under Python 3.x, but no longer cause a warning to be emitted under
  Python 2.x).

4.0.0 (2012-05-16)
------------------

- Automated build of Sphinx HTML docs and running doctest snippets via tox.

- Deprecate the "class advice" APIs from ``zope.interface.declarations``:
  ``implements``, ``implementsOnly``, and ``classProvides``.  In their place,
  prefer the equivalent class decorators: ``@implementer``,
  ``@implementer_only``, and ``@provider``.  Code which uses the deprecated
  APIs will not work as expected under Py3k.

- Remove use of '2to3' and associated fixers when installing under Py3k.
  The code is now in a "compatible subset" which supports Python 2.6, 2.7,
  and 3.2, including PyPy 1.8 (the version compatible with the 2.7 language
  spec).

- Drop explicit support for Python 2.4 / 2.5 / 3.1.

- Add support for PyPy.

- Add support for continuous integration using ``tox`` and ``jenkins``.

- Add 'setup.py dev' alias (runs ``setup.py develop`` plus installs
  ``nose`` and ``coverage``).

- Add 'setup.py docs' alias (installs ``Sphinx`` and dependencies).

- Replace all unittest coverage previously accomplished via doctests with
  unittests.  The doctests have been moved into a ``docs`` section, managed
  as a Sphinx collection.

- LP #910987:  Ensure that the semantics of the ``lookup`` method of
  ``zope.interface.adapter.LookupBase`` are the same in both the C and
  Python implementations.

- LP #900906:  Avoid exceptions due to tne new ``__qualname__`` attribute
  added in Python 3.3 (see PEP 3155 for rationale).  Thanks to Antoine
  Pitrou for the patch.

3.8.0 (2011-09-22)
------------------

- New module ``zope.interface.registry``.  This is code moved from
  ``zope.component.registry`` which implements a basic nonperistent component
  registry as ``zope.interface.registry.Components``.  This class was moved
  from ``zope.component`` to make porting systems (such as Pyramid) that rely
  only on a basic component registry to Python 3 possible without needing to
  port the entirety of the ``zope.component`` package.  Backwards
  compatibility import shims have been left behind in ``zope.component``, so
  this change will not break any existing code.

- New ``tests_require`` dependency: ``zope.event`` to test events sent by
  Components implementation.  The ``zope.interface`` package does not have a
  hard dependency on ``zope.event``, but if ``zope.event`` is importable, it
  will send component registration events when methods of an instance of
  ``zope.interface.registry.Components`` are called.

- New interfaces added to support ``zope.interface.registry.Components``
  addition: ``ComponentLookupError``, ``Invalid``, ``IObjectEvent``,
  ``ObjectEvent``, ``IComponentLookup``, ``IRegistration``,
  ``IUtilityRegistration``, ``IAdapterRegistration``,
  ``ISubscriptionAdapterRegistration``, ``IHandlerRegistration``,
  ``IRegistrationEvent``, ``RegistrationEvent``, ``IRegistered``,
  ``Registered``, ``IUnregistered``, ``Unregistered``,
  ``IComponentRegistry``, and ``IComponents``.

- No longer Python 2.4 compatible (tested under 2.5, 2.6, 2.7, and 3.2).

3.7.0 (2011-08-13)
------------------

- Move changes from 3.6.2 - 3.6.5 to a new 3.7.x release line.

3.6.7 (2011-08-20)
------------------

- Fix sporadic failures on x86-64 platforms in tests of rich comparisons
  of interfaces.

3.6.6 (2011-08-13)
------------------

- LP #570942:  Now correctly compare interfaces  from different modules but
  with the same names.

  N.B.: This is a less intrusive / destabilizing fix than the one applied in
  3.6.3:  we only fix the underlying cmp-alike function, rather than adding
  the other "rich comparison" functions.

- Revert to software as released with 3.6.1 for "stable" 3.6 release branch.

3.6.5 (2011-08-11)
------------------

- LP #811792:  work around buggy behavior in some subclasses of
  ``zope.interface.interface.InterfaceClass``, which invoke ``__hash__``
  before initializing ``__module__`` and ``__name__``.  The workaround
  returns a fixed constant hash in such cases, and issues a ``UserWarning``.

- LP #804832:  Under PyPy, ``zope.interface`` should not build its C
  extension.  Also, prevent attempting to build it under Jython.

- Add a tox.ini for easier xplatform testing.

- Fix testing deprecation warnings issued when tested under Py3K.

3.6.4 (2011-07-04)
------------------

- LP 804951:  InterfaceClass instances were unhashable under Python 3.x.

3.6.3 (2011-05-26)
------------------

- LP #570942:  Now correctly compare interfaces  from different modules but
  with the same names.

3.6.2 (2011-05-17)
------------------

- Moved detailed documentation out-of-line from PyPI page, linking instead to
  http://docs.zope.org/zope.interface .

- Fixes for small issues when running tests under Python 3.2 using
  ``zope.testrunner``.

- LP # 675064:  Specify return value type for C optimizations module init
  under Python 3:  undeclared value caused warnings, and segfaults on some
  64 bit architectures.

- setup.py now raises RuntimeError if you don't have Distutils installed when
  running under Python 3.

3.6.1 (2010-05-03)
------------------

- A non-ASCII character in the changelog made 3.6.0 uninstallable on
  Python 3 systems with another default encoding than UTF-8.

- Fix compiler warnings under GCC 4.3.3.

3.6.0 (2010-04-29)
------------------

- LP #185974:  Clear the cache used by ``Specificaton.get`` inside
  ``Specification.changed``.  Thanks to Jacob Holm for the patch.

- Add support for Python 3.1. Contributors:

    Lennart Regebro
    Martin v Loewis
    Thomas Lotze
    Wolfgang Schnerring

  The 3.1 support is completely backwards compatible. However, the implements
  syntax used under Python 2.X does not work under 3.X, since it depends on
  how metaclasses are implemented and this has changed. Instead it now supports
  a decorator syntax (also under Python 2.X)::

    class Foo:
        implements(IFoo)
        ...

  can now also be written::

    @implementer(IFoo):
    class Foo:
        ...

  There are 2to3 fixers available to do this change automatically in the
  zope.fixers package.

- Python 2.3 is no longer supported.


3.5.4 (2009-12-23)
------------------

- Use the standard Python doctest module instead of zope.testing.doctest, which
  has been deprecated.


3.5.3 (2009-12-08)
------------------

- Fix an edge case: make providedBy() work when a class has '__provides__' in
  its __slots__ (see http://thread.gmane.org/gmane.comp.web.zope.devel/22490)


3.5.2 (2009-07-01)
------------------

- BaseAdapterRegistry.unregister, unsubscribe: Remove empty portions of
  the data structures when something is removed.  This avoids leaving
  references to global objects (interfaces) that may be slated for
  removal from the calling application.


3.5.1 (2009-03-18)
------------------

- verifyObject: use getattr instead of hasattr to test for object attributes
  in order to let exceptions other than AttributeError raised by properties
  propagate to the caller

- Add Sphinx-based documentation building to the package buildout
  configuration. Use the ``bin/docs`` command after buildout.

- Improve package description a bit. Unify changelog entries formatting.

- Change package's mailing list address to zope-dev at zope.org as
  zope3-dev at zope.org is now retired.


3.5.0 (2008-10-26)
------------------

- Fix declaration of _zope_interface_coptimizations, it's not a top level
  package.

- Add a DocTestSuite for odd.py module, so their tests are run.

- Allow to bootstrap on Jython.

- Fix https://bugs.launchpad.net/zope3/3.3/+bug/98388: ISpecification
  was missing a declaration for __iro__.

- Add optional code optimizations support, which allows the building
  of C code optimizations to fail (Jython).

- Replace `_flatten` with a non-recursive implementation, effectively making
  it 3x faster.


3.4.1 (2007-10-02)
------------------

- Fix a setup bug that prevented installation from source on systems
  without setuptools.


3.4.0 (2007-07-19)
------------------

- Final release for 3.4.0.


3.4.0b3 (2007-05-22)
--------------------


- When checking whether an object is already registered, use identity
  comparison, to allow adding registering with picky custom comparison methods.


3.3.0.1 (2007-01-03)
--------------------

- Made a reference to OverflowWarning, which disappeared in Python
  2.5, conditional.


3.3.0 (2007/01/03)
------------------

New Features
++++++++++++

- Refactor the adapter-lookup algorithim to make it much simpler and faster.

  Also, implement more of the adapter-lookup logic in C, making
  debugging of application code easier, since there is less
  infrastructre code to step through.

- Treat objects without interface declarations as if they
  declared that they provide ``zope.interface.Interface``.

- Add a number of richer new adapter-registration interfaces
  that provide greater control and introspection.

- Add a new interface decorator to zope.interface that allows the
  setting of tagged values on an interface at definition time (see
  zope.interface.taggedValue).

Bug Fixes
+++++++++

- A bug in multi-adapter lookup sometimes caused incorrect adapters to
  be returned.


3.2.0.2 (2006-04-15)
--------------------

- Fix packaging bug:  'package_dir' must be a *relative* path.


3.2.0.1 (2006-04-14)
--------------------

- Packaging change:  suppress inclusion of 'setup.cfg' in 'sdist' builds.


3.2.0 (2006-01-05)
------------------

- Corresponds to the verison of the zope.interface package shipped as part of
  the Zope 3.2.0 release.


3.1.0 (2005-10-03)
------------------

- Corresponds to the verison of the zope.interface package shipped as part of
  the Zope 3.1.0 release.

- Made attribute resolution order consistent with component lookup order,
  i.e. new-style class MRO semantics.

- Deprecate 'isImplementedBy' and 'isImplementedByInstancesOf' APIs in
  favor of 'implementedBy' and 'providedBy'.


3.0.1 (2005-07-27)
------------------

- Corresponds to the verison of the zope.interface package shipped as part of
  the Zope X3.0.1 release.

- Fix a bug reported by James Knight, which caused adapter registries
  to fail occasionally to reflect declaration changes.


3.0.0 (2004-11-07)
------------------

- Corresponds to the verison of the zope.interface package shipped as part of
  the Zope X3.0.0 release.

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

%description python3
python3 components for the zope.interface package.


%prep
%setup -q -n zope.interface-4.7.1
cd %{_builddir}/zope.interface-4.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582847964
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
