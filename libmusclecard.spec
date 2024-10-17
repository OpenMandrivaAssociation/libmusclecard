%define libmusclename %mklibname musclecard 1
%define pkgname libmusclecard

Summary: Muscle PCSC Framework for Linux libraries
Name: libmusclecard
Version: 1.3.6
Release: 4
License: GPL
Group: System/Libraries
Source0: https://alioth.debian.org/download.php/1478/libmusclecard-%{version}.tar.bz2
Source1: https://alioth.debian.org/download.php/1479/libmusclecard-%{version}.tar.bz2.asc
Patch0: libmusclecard-1.3.6-pcsclite-1.6.patch
URL: https://pcsclite.alioth.debian.org/
# actually, it needs 1.2.9-beta7 or higher, but I don't want
# to play with rpm e-v-r comparisons with a "beta" string in them
BuildRequires: libpcsclite-devel >= 1.3.0
BuildRequires: pkgconfig

%description
The purpose of PCSC Lite is to provide a Windows(R) SCard interface in a
very small form factor for communicating to smartcards and readers.
PCSC Lite uses the same winscard api as used under Windows(R).

The %{name}-devel package contains the header files and libraries
needed for compiling PCSC Lite programs. If you want to develop PCSC Lite-aware
programs, you'll need to install this package.

This package was tested to work with A.E.T. Europe B.V. SafeSign. This
package is suported by A.E.T. Europe B.V. when used in combination with
SafeSign.

%package -n %{libmusclename}
Summary: Muscle PCSC Framework for Linux libraries
Group: System/Libraries
# up to version 1.3.0, libpcsclite had libmusclecard files
Conflicts: pcsc-lite < 1.3.0
Provides: libmusclecard = %{EVRD}

%description -n %{libmusclename}
The purpose of PCSC Lite is to provide a Windows(R) SCard interface in a
very small form factor for communicating to smartcards and readers.
PCSC Lite uses the same winscard api as used under Windows(R).

The %{name}-devel package contains the header files and libraries
needed for compiling PCSC Lite programs. If you want to develop PCSC Lite-aware
programs, you'll need to install this package.

This package was tested to work with A.E.T. Europe B.V. SafeSign. This
package is suported by A.E.T. Europe B.V. when used in combination with
SafeSign.

%package -n %{libmusclename}-devel
Summary: Files used for libmusclecard development
Group: Development/Other
Requires: %{name} = %{version}
# up to version 1.3.0, libpcsclite had libmusclecard files
Conflicts: %{mklibname pcsclite 1 -d} < 1.3.0
Provides: libmusclecard-devel = %{EVRD}

%description -n %{libmusclename}-devel
This package contains files used for libmusclecard development.

%package -n %{libmusclename}-static-devel
Summary: Static library used for libmusclecard development
Group: Development/Other
Requires: %{name}-devel = %{version}
# up to version 1.3.0, libpcsclite had libmusclecard files
Conflicts: %{mklibname pcsclite 1 -d -s} < 1.3.0
Provides: libmusclecard-static-devel = %{EVRD}

%description -n %{libmusclename}-static-devel
This package contains a libmusclecard static library used for development.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p0

%build
autoreconf -fi
%configure2_5x --enable-muscledropdir=%{_libdir}/pcsc/services
%make

%install
%makeinstall_std

# this file is included in %%doc
rm -rf %{buildroot}%{_prefix}/doc

%files -n %{libmusclename}
%{_libdir}/libmusclecard.so.*

%files -n %{libmusclename}-devel
%doc AUTHORS COPYING ChangeLog
%doc ChangeLog.svn doc/*.pdf
%{_includedir}/PCSC/*
%{_libdir}/libmusclecard.so
%{_libdir}/pkgconfig/libmusclecard.pc
%{_sbindir}/bundleTool
%{_mandir}/man8/bundleTool.8*

%files -n %{libmusclename}-static-devel
%{_libdir}/libmusclecard.a




%changelog
* Mon Aug 30 2010 Funda Wang <fwang@mandriva.org> 1.3.6-2mdv2011.0
+ Revision: 574307
- rebuild for new pcsclite

* Fri May 01 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3.6-1mdv2010.0
+ Revision: 370045
- Update to new version 1.3.6
- Run autoreconf -fi for new libtool

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-2mdv2009.0
+ Revision: 229691
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 28 2007 Andreas Hasenack <andreas@mandriva.com> 1.3.3-1mdv2008.0
+ Revision: 32032
- added provides without the soname


* Tue Apr 03 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.3.3-1mdv2007.1
+ Revision: 150357
- Remove soname from .src.rpm pkgname.
- Remove soname from .src.rpm pkgname.
- Remove soname from .src.rpm pkgname (still fixing compatibility with iurt).
- Fixate main package name: avoids breakage with iurt .src.rpm check.

  + Andreas Hasenack <andreas@mandriva.com>
    - updated to version 1.3.3
    - Import libmusclecard1

