Summary:	Sensors plugin for the Xfce panel
Summary(pl):	Wtyczka sensorów dla panelu Xfce
Name:		xfce4-sensors-plugin
Version:	0.3.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.bz2
# Source0-md5:	3eeaa4973c9a855d75f5e58fcf3f1991
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	lm_sensors-devel >= 2.8
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
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
