#
# Conditional build:
%bcond_without	gtk3	# use GTK+3 instead of GTK+2

Summary:	GTK+ interface to XRandR for LXDE desktop
Summary(pl.UTF-8):	Interfejs GTK+ do rozszerzenia XRandR dla środowiska LXDE
Name:		lxrandr
Version:	0.3.2
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# Source0-md5:	5101ab29d87fb2b56a5ec5bc8bc3f258
URL:		http://www.lxde.org/
BuildRequires:	gettext-tools
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.12.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK+ interface to XRandR for LXDE desktop.

%description -l pl.UTF-8
Interfejs GTK+ do rozszerzenia XRandR dla środowiska LXDE.

%prep
%setup -q

%build
%configure \
	%{?with_gtk3:--enable-gtk3} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unify name
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{tt_RU,tt}
# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/frp
# duplicate of ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxrandr
%{_desktopdir}/lxrandr.desktop
%{_mandir}/man1/lxrandr.1*
