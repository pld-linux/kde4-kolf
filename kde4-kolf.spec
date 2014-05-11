%define		_state		stable
%define		orgname		kolf
%define		qtver		4.8.0

Summary:	Miniature golf for KDE
Summary(pl.UTF-8):	Mini golf
Name:		kde4-%{orgname}
Version:	4.13.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	842d4741f1a1528bf18e55d98247a963
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kolf is a miniature golf game with block graphics and a 2D top-down
view. Courses are dynamic, and up to 10 people can play at once in
competition.

%description -l pl.UTF-8
Kolf to miniaturowa gra w golfa z blokowa grafiką i dwuwymiarowym
widokiem. Rundy są dynamiczne, a w zawodach może grać do 10 osób
naraz.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kolf
%attr(755,root,root) %{_libdir}/libkolfprivate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkolfprivate.so.?
%{_desktopdir}/kde4/kolf.desktop
%{_datadir}/apps/kolf
%{_iconsdir}/*/*/apps/kolf.png
