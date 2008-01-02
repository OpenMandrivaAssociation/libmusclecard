%define libmusclename %mklibname musclecard 1
%define pkgname libmusclecard

Summary: Muscle PCSC Framework for Linux libraries
Name: libmusclecard
Version: 1.3.3
Release: %mkrel 1
License: GPL
Group: System/Libraries
Source0: https://alioth.debian.org/download.php/1478/libmusclecard-%{version}.tar.gz
Source1: https://alioth.debian.org/download.php/1479/libmusclecard-%{version}.tar.gz.asc
URL: http://pcsclite.alioth.debian.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(id -u -n)
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
Provides: libmusclecard = %{version}-%{release}

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
Provides: libmusclecard-devel = %{version}-%{release}

%description -n %{libmusclename}-devel
This package contains files used for libmusclecard development.

%package -n %{libmusclename}-static-devel
Summary: Static library used for libmusclecard development
Group: Development/Other
Requires: %{name}-devel = %{version}
# up to version 1.3.0, libpcsclite had libmusclecard files
Conflicts: %{mklibname pcsclite 1 -d -s} < 1.3.0
Provides: libmusclecard-static-devel = %{version}-%{release}

%description -n %{libmusclename}-static-devel
This package contains a libmusclecard static library used for development.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure --enable-muscledropdir=%{_libdir}/pcsc/services
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install

# this file is included in %%doc
rm -rf %{buildroot}%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libmusclename} -p /sbin/ldconfig

%postun -n %{libmusclename} -p /sbin/ldconfig

%files -n %{libmusclename}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libmusclecard.so.*
%{_sbindir}/bundleTool
%{_mandir}/man8/bundleTool.8*

%files -n %{libmusclename}-devel
%defattr(-,root,root)
%doc ChangeLog.svn doc/*.pdf
%{_includedir}/PCSC/*
%{_libdir}/libmusclecard.so
%{_libdir}/libmusclecard.la
%{_libdir}/pkgconfig/libmusclecard.pc

%files -n %{libmusclename}-static-devel
%defattr(-,root,root)
%{_libdir}/libmusclecard.a


