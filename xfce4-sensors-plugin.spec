# TODO: remove libexec workarond, will need whole xfce rebuild
Summary:	Sensors plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka sensorów dla panelu Xfce
Name:		xfce4-sensors-plugin
Version:	1.5.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-sensors-plugin/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	b6a3533605f397c3393f92881461ec5a
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-sensors-plugin
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libXNVCtrl-devel
BuildRequires:	libnotify-devel >= 0.7
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	libxfce4util-devel >= 4.17.2
BuildRequires:	lm_sensors-devel >= 2.8
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.000
BuildRequires:	xfce4-dev-tools >= 4.17.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
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

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
%doc AUTHORS NEWS NOTES README TODO
%attr(755,root,root) %{_bindir}/xfce4-sensors
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libxfce4-sensors-plugin.so
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/xfce4/panel/plugins/xfce4-sensors-plugin.css
%{_datadir}/xfce4/panel/plugins/xfce4-sensors-plugin.desktop
%{_desktopdir}/xfce4-sensors.desktop
%{_mandir}/man1/xfce4-sensors.1*
