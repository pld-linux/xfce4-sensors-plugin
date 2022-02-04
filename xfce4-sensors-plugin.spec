# TODO: remove libexec workarond, will need whole xfce rebuild
Summary:	Sensors plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka sensorów dla panelu Xfce
Name:		xfce4-sensors-plugin
Version:	1.4.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-sensors-plugin/1.4/%{name}-%{version}.tar.bz2
# Source0-md5:	e55dfea49b0c5e9edf068db3b8398240
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-sensors-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	lm_sensors-devel >= 2.8
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	libxfce4sensors.so.*

%description
This plugin displays various hardware sensor values in the Xfce panel.

%description -l pl.UTF-8
Ta wtyczka wyświetla różne dane z czujników sprzętowych na panelu
Xfce.

%prep
%setup -q

mkdir -p m4

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--libexecdir=%{_libdir} \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/modules/*.la
%{__rm}	$RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/libxfce4-sensors-plugin.la
%{__rm}	$RPM_BUILD_ROOT%{_pkgconfigdir}/libxfce4sensors-1.0.pc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hye,ie,pt_BR,ur_PK}

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
%attr(755,root,root) %{_bindir}/xfce4-sensors
%attr(755,root,root) %{_libdir}/xfce4/modules/libxfce4sensors.so*
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libxfce4-sensors-plugin.so
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/xfce4/panel/plugins/xfce4-sensors-plugin.css
%{_datadir}/xfce4/panel/plugins/xfce4-sensors-plugin.desktop
%{_desktopdir}/xfce4-sensors.desktop
%{_mandir}/man1/xfce4-sensors.1*
