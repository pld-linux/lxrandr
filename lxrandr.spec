Summary:	a GTK+2 interface to XRandR for LXDE desktop
Name:		lxrandr
Version:	0.1.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	ab2c7f6be7e4fe6d1a26e324d836453e
URL:		http://www.lxde.org/
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
a GTK+2 interface to XRandR for LXDE desktop.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{frp,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxrandr
%{_desktopdir}/lxrandr.desktop
%{_mandir}/man1/lxrandr*