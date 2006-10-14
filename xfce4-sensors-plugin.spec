Summary:	Sensors plugin for the Xfce panel
Summary(pl):	Wtyczka sensorów dla panelu Xfce
Name:		xfce4-sensors-plugin
Version:	0.7.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-sensors-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	10399ab7351c60e9e46e4d4375250157
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-sensors-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	lm_sensors-devel >= 2.8
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools
BuildRequires:	xfce4-panel-devel >= 4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin displays various hardware sensor values in the Xfce panel.

%description -l pl
Ta wtyczka wy¶wietla ró¿ne dane z czujników sprzêtowych na panelu
Xfce.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I %{_datadir}/xfce4/dev-tools/m4macros
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
