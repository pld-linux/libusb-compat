#
# Conditional build:
%bcond_with	tests	# perform "make check"
#
Summary:	Compatibility layer for libusb-0.1
Summary(es.UTF-8):	libusb - Biblioteca USB
Summary(pl.UTF-8):	Dostęp z poziomu aplikacji do urządzeń USB
Summary(pt_BR.UTF-8):	libusb - Biblioteca para acesso a devices USB
Name:		libusb-compat
Version:	0.1.3
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libusb/%{name}-%{version}.tar.bz2
# Source0-md5:	570ac2ea085b80d1f74ddc7c6a93c0eb
URL:		http://www.libusb.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.7.6
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libusb-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a library for application access to USB devices.

libusb-compat-0.1 is a replacement for libusb-0.1.

It attempts to look, feel and behave identically. The difference is
that it just converts the libusb-0.1 function calls into their
libusb-1.0 equivalents.

%description -l es.UTF-8
Biblioteca de uso en devices USB.

%description -l pl.UTF-8
Biblioteka umożliwiająca dostęp do urządzeń USB z poziomu aplikacji.

%description -l pt_BR.UTF-8
Biblioteca para acesso em devices USB.

%package devel
Summary:	Header files for libusb library
Summary(es.UTF-8):	Archivos de desarrollo de libusb
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libusb
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento da libusb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libusb-devel >= 1.0.0
Obsoletes:	libusb0.1-devel

%description devel
This package contains header files and other resources you can use to
incorporate libusb-0.1 into applications.

%description devel -l es.UTF-8
Bibliotecas de desarrolo para linusb.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz dokumentacja pozwalająca na dodawanie obsługi
USB w swoich programach.

%description devel -l pt_BR.UTF-8
Bibliotecas de desenvolvimento para libusb.

%package static
Summary:	libusb static libraries
Summary(es.UTF-8):	Archivos de desarrollo de libusb - estatico
Summary(pl.UTF-8):	Statyczne biblioteki do obsługi USB
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento da libusb - biblioteca estática
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This is package with static libusb-0.1 libraries.

%description static -l es.UTF-8
Bibliotecas de desarrolo para linusb - estatico.

%description static -l pl.UTF-8
Statyczne biblioteki libusb.

%description static -l pt_BR.UTF-8
Bibliotecas de desenvolvimento para libusb - estático.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS ChangeLog
%attr(755,root,root) %{_libdir}/libusb-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libusb-*.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libusb-config
%attr(755,root,root) %{_libdir}/libusb.so
%{_libdir}/libusb.la
%{_includedir}/usb.h
%{_pkgconfigdir}/libusb.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libusb.a
