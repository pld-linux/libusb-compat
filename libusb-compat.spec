#
# Conditional build:
%bcond_with	tests	# perform "make check"
#
Summary:	USB access library (libusb-1.0 to libusb-0.1 compatibility wrapper)
Summary(pl.UTF-8):	Biblioteka dostępu do USB (warstwa kompatybilności libusb-1.0 z libusb-0.1)
Name:		libusb-compat
Version:	0.1.5
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libusb/%{name}-%{version}.tar.bz2
# Source0-md5:	2780b6a758a1e2c2943bdbf7faf740e4
URL:		http://www.libusb.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libusb-devel >= 1.0.0
BuildRequires:	pkgconfig
Obsoletes:	libusb < 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a library for application access to USB devices.

libusb-compat-0.1 is a replacement for libusb-0.1.

It attempts to look, feel and behave identically. The difference is
that it just converts the libusb-0.1 function calls into their
libusb-1.0 equivalents.

%description -l pl.UTF-8
Biblioteka umożliwiająca dostęp do urządzeń USB z poziomu aplikacji.

libusb-compat-0.1 to zamiennik libusb-0.1.

Stara się wyglądać i zachowywać identycznie. Różnica jest taka, że
zamienia wywołania funkcji libusb-0.1 na odpowiedniki z libusb-1.0.

%package devel
Summary:	Header files for libusb-compat library
Summary(es.UTF-8):	Archivos de desarrollo de libusb-compat
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libusb-compat
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento da libusb-compat
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libusb-devel >= 1.0.0
Obsoletes:	libusb-devel < 1.0.0
Obsoletes:	libusb0.1-devel

%description devel
This package contains header files and other resources you can use to
incorporate libusb-0.1 into applications.

%description devel -l es.UTF-8
Bibliotecas de desarrolo para linusb-compat.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe i inne zasoby pozwalające
wykorzystywać API libusb-0.1 we własnych aplikacjach.

%description devel -l pt_BR.UTF-8
Bibliotecas de desenvolvimento para libusb-compat.

%package static
Summary:	libusb-compat static library
Summary(es.UTF-8):	Archivos de desarrollo de libusb-compat - estatico
Summary(pl.UTF-8):	Statyczna biblioteka libusb-compat
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento da libusb-compat - biblioteca estática
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libusb-static < 1.0

%description static
This is package with static libusb-compat library.

%description static -l es.UTF-8
Bibliotecas de desarrolo para linusb-compat - estatico.

%description static -l pl.UTF-8
Statyczna biblioteka libusb-compat.

%description static -l pt_BR.UTF-8
Bibliotecas de desenvolvimento para libusb-compat - estático.

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
%doc AUTHORS ChangeLog LICENSE NEWS README
%attr(755,root,root) %{_libdir}/libusb-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libusb-0.1.so.4

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
