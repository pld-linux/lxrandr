#
# Conditional build:
%bcond_with		gtk3		# build GTK+3 disables GTK+2
%bcond_without		gtk2	# build with GTK+2

%if %{with gtk3}
%undefine	with_gtk2
%endif

Summary:	a GTK+2 interface to XRandR for LXDE desktop
Name:		lxrandr
Version:	0.1.2
Release:	4
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	8a7391581541bba58839ac11dbf5b575
Patch0:		mate-desktop.patch
URL:		http://wiki.lxde.org/en/LXRandR
BuildRequires:	gettext-tools
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK+ interface to XRandR for LXDE desktop.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	%{?with_gtk3:--enable-gtk3}
touch po/stamp-it
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{frp,ur_PK,tt_RU}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxrandr
%{_desktopdir}/lxrandr.desktop
%{_mandir}/man1/lxrandr*
