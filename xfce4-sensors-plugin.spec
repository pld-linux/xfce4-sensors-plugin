Summary:	Sensors plugin for the Xfce panel
Summary(pl):	Wtyczka sensor�w dla panelu Xfce
Name:		xfce4-sensors-plugin
Version:	0.10.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-sensors-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	fa431e2b6bb0dd151047e05f7383a844
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-sensors-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	lm_sensors-devel >= 2.8
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.3.90.2
BuildRequires:	xfce4-panel-devel >= 4.3.90.1
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin displays various hardware sensor values in the Xfce panel.

%description -l pl
Ta wtyczka wy�wietla r�ne dane z czujnik�w sprz�towych na panelu
Xfce.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/xfce4/panel-plugins/*.desktop
