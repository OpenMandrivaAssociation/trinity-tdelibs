%bcond clang 1
%bcond gamin 1
%bcond pcre 1
%bcond inotify 1
%bcond hspell 1
%bcond jasper 1
%bcond avahi 1
%bcond openexr 1
%bcond lzma 1
%bcond xrandr 1
%bcond nm 1
%bcond tdehwlib 1
%bcond udisks2 1
%bcond upower 1
%bcond systemd 1
%bcond elficon 0
%bcond xcomposite 1
%bcond xt 1
%bcond sudo 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !


# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 4

%define tde_pkg tdelibs


# breaks desktop files when not defined
%define dont_fix_xdg 1
%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Version:		%{tde_version}
Release:		%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:		TDE Libraries
Group:			System/GUI/Other
URL:			http://www.trinitydesktop.org/

License:		GPLv2+

#Vendor:			Trinity Desktop
#Packager:		Francois Andriot <francois.andriot@free.fr>

Prefix:			/opt/trinity

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:		%{name}-rpmlintrc

BuildSystem:  cmake
BuildOption:  -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:  -DCMAKE_SKIP_RPATH=OFF
BuildOption:  -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:  -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:  -DCMAKE_INSTALL_RPATH="%{prefix}/%{_lib}"
BuildOption:  -DCMAKE_NO_BUILTIN_CHRPATH=ON
BuildOption:  -DCMAKE_INSTALL_PREFIX="%{prefix}"
BuildOption:  -DCONFIG_INSTALL_DIR="%{_sysconfdir}/trinity"
BuildOption:  -DINCLUDE_INSTALL_DIR="%{prefix}/include/tde"
BuildOption:  -DPKGCONFIG_INSTALL_DIR="%{prefix}/%{_lib}/pkgconfig"
BuildOption:  -DWITH_ALL_OPTIONS=ON -DWITH_ARTS=ON -DWITH_ALSA=ON
BuildOption:  -DWITH_LIBART=ON -DWITH_LIBIDN=ON -DWITH_SSL=ON
BuildOption:  -DWITH_CUPS=ON -DWITH_LUA=OFF -DWITH_TIFF=ON 
BuildOption:  -DWITH_UTEMPTER=ON
BuildOption:  -DWITH_UDEVIL=OFF -DWITH_CONSOLEKIT=ON
BuildOption:  -DWITH_OLD_XDG_STD=OFF -DWITH_PCSC=ON
BuildOption:  -DWITH_PKCS=ON -DWITH_CRYPTSETUP=ON
BuildOption:  -DWITH_LIBBFD=OFF -DWITH_KDE4_MENU_SUFFIX=OFF
BuildOption:  -DWITH_ASPELL=ON -DWITH_TDEICONLOADER_DEBUG=OFF
BuildOption:  -DCMAKE_POLICY_DEFAULT_CMP0109=NEW
BuildOption:  -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
BuildOption:  -DWITH_JASPER=%{!?with_jasper:OFF}%{?with_jasper:ON}
BuildOption:  -DWITH_OPENEXR=%{!?with_openexr:OFF}%{?with_openexr:ON}
BuildOption:  -DWITH_AVAHI=%{!?with_avahi:OFF}%{?with_avahi:ON}
BuildOption:  -DWITH_ELFICON=%{!?with_elficon:OFF}%{?with_elficon:ON}
BuildOption:  -DWITH_PCRE=%{!?with_pcre:OFF}%{?with_pcre:ON}
BuildOption:  -DWITH_INOTIFY=%{!?with_inotify:OFF}%{?with_inotify:ON}
BuildOption:  -DWITH_GAMIN=%{!?with_gamin:OFF}%{?with_gamin:ON}
BuildOption:  -DWITH_TDEHWLIB=%{!?with_tdehwlib:OFF}%{?with_tdehwlib:ON}
BuildOption:  -DWITH_TDEHWLIB_DAEMONS=%{!?with_tdehwlib:OFF}%{?with_tdehwlib:ON}
BuildOption:  -DWITH_LOGINDPOWER=%{?with_systemd:ON}%{!?with_systemd:OFF}
BuildOption:  -DWITH_UPOWER=%{!?with_upower:OFF}%{?with_upower:ON}
BuildOption:  -DWITH_UDISKS2=%{!?with_udisks2:OFF}%{?with_udisks2:ON}
BuildOption:  -DWITH_NETWORK_MANAGER_BACKEND=%{?with_nm:ON}%{!?with_nm:OFF}
BuildOption:  -DWITH_SUDO_TDESU_BACKEND=%{?with_sudo:ON}%{!?with_sudo:OFF}
BuildOption:  -DWITH_LZMA=%{!?with_lzma:OFF}%{?with_lzma:ON}
BuildOption:  -DWITH_XRANDR=%{!?with_xrandr:OFF}%{?with_xrandr:ON}
BuildOption:  -DWITH_XCOMPOSITE=%{?with_xcomposite:ON}%{!?with_xcomposite:OFF}
BuildOption:  -DWITH_HSPELL=%{?!with_hspell:OFF}%{?with_hspell:ON}

Obsoletes:		tdelibs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		tdelibs = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-kdelibs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdelibs = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-kdelibs-apidocs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdelibs-apidocs = %{?epoch:%{epoch}:}%{version}-%{release}


# Trinity dependencies
BuildRequires:	libtqt4-devel = %{tde_epoch}:4.2.0
BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	libdbus-tqt-1-devel >= %{tde_epoch}:0.63
BuildRequires:	libdbus-1-tqt-devel >= %{tde_epoch}:0.9
BuildRequires:	trinity-filesystem >= %{tde_version}

Requires:		trinity-arts >= %{tde_epoch}:1.5.10
Requires:		trinity-filesystem >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

# KRB5 support
BuildRequires:	pkgconfig(krb5)

# XSLT support
BuildRequires:  pkgconfig(libxslt)

# ALSA support
BuildRequires:  pkgconfig(alsa)

# IDN support
BuildRequires:  pkgconfig(libidn) 

# CUPS support
BuildRequires:	pkgconfig(cups)

# TIFF support
BuildRequires:  pkgconfig(libtiff-4)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# ACL support
BuildRequires:  pkgconfig(libacl)

# GLIB2 support
BuildRequires:	pkgconfig(glib-2.0)

# LUA support are not ready yet
# BuildRequires:  pkgconfig(lua)

# LIBART_LGPL support
BuildRequires:	pkgconfig(libart-2.0)

# ASPELL support
BuildRequires:  aspell
BuildRequires:	aspell-devel

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# PCRE support
%{?with_pcre:BuildRequires:  pkgconfig(libpcre)}

# PCRE2 support
BuildRequires:  pkgconfig(libpcre2-posix)

# BZIP2 support
BuildRequires:  pkgconfig(bzip2)

# UTEMPTER support
BuildRequires:	%{_lib}utempter-devel

# HSPELL support
%{?with_hspell:BuildRequires:	hspell-devel}

# JASPER support
%{?with_jasper:BuildRequires:  pkgconfig(jasper)}

# AVAHI support
%if %{with avahi}
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:  trinity-avahi-tqt-devel
%endif

# OPENEXR support
%{?with_openexr:BuildRequires:	pkgconfig(OpenEXR)}

# LIBTOOL
BuildRequires:	libtool-devel

# X11 support
BuildRequires:  pkgconfig(x11)

# ICEAUTH
Requires:		iceauth
BuildRequires:	iceauth

# Xorg
BuildRequires:  pkgconfig(xorg-server)

# XFT support
BuildRequires:  pkgconfig(xft)

# XZ support
%{?with_lzma:BuildRequires:	pkgconfig(liblzma)}

# Certificates support
BuildRequires:	ca-certificates
Requires:       openssl

Requires:		rootcerts
%define	cacert	%{_sysconfdir}/pki/tls/certs/ca-bundle.crt

# XRANDR support
%{?with_xrandr:BuildRequires:  pkgconfig(xrandr)}

# XCOMPOSITE support
%{?with_xcomposite:BuildRequires:  pkgconfig(xcomposite)}

# XT support
%{?with_xt:BuildRequires:  pkgconfig(xt)}

### New features in TDE R14

# LIBMAGIC support
BuildRequires:  pkgconfig(libmagic)

# NETWORKMANAGER support
%{?with_nm:BuildRequires:  pkgconfig(libnm)}

# UDEV support
%{?with_tdehwlib:BuildRequires:  pkgconfig(udev)}

# UDISKS2 support
%{?with_udisks2:BuildRequires:  pkgconfig(udisks2)}

# UPOWER support
%{?with_upower:BuildRequires:  pkgconfig(upower-glib)}

# PCSCLITE support
BuildRequires:	pkgconfig(libpcsclite)

# PKCS11 support
BuildRequires:	pkgconfig(libpkcs11-helper-1)

# OPENSC support
BuildRequires:	opensc

# CRYPTSETUP support
BuildRequires:	pkgconfig(libcryptsetup)

# ELFICON support
# TODO - decide what needs this support and fix the condition
%{?with_elficon:BuildRequires:		libr-devel >= 0.6.0}

# ATTR support
BuildRequires: pkgconfig(libattr)

# INTLTOOL support
BuildRequires:	intltool

# WEBP support
BuildRequires:	pkgconfig(libwebp)

%description
Libraries for the Trinity Desktop Environment:
TDE Libraries included: tdecore (TDE core library), tdeui (user interface),
kfm (file manager), tdehtmlw (HTML widget), tdeio (Input/Output, networking),
kspell (spelling checker), jscript (javascript), kab (addressbook),
kimgio (image manipulation).

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING-DOCS COPYING.LIB README TODO
%{prefix}/bin/artsmessage
%{prefix}/bin/cupsdconf
%{prefix}/bin/cupsdoprint
%{prefix}/bin/dcop
%{prefix}/bin/dcopclient
%{prefix}/bin/dcopfind
%{prefix}/bin/dcopobject
%{prefix}/bin/dcopquit
%{prefix}/bin/dcopref
%{prefix}/bin/dcopserver
%{prefix}/bin/dcopserver_shutdown
%{prefix}/bin/dcopstart
%{prefix}/bin/imagetops
%{prefix}/bin/tdeab2tdeabc
%{prefix}/bin/kaddprinterwizard
%{prefix}/bin/tdebuildsycoca
%{prefix}/bin/tdecmshell
%{prefix}/bin/tdeconf_update
%{prefix}/bin/kcookiejar
%{prefix}/bin/tde-config
%{prefix}/bin/tde-menu
%{prefix}/bin/kded
%{prefix}/bin/tdeinit
%{prefix}/bin/tdeinit_shutdown
%{prefix}/bin/tdeinit_wrapper
%{prefix}/bin/tdesu_stub
%{prefix}/bin/kdetcompmgr
%{prefix}/bin/kdontchangethehostname
%{prefix}/bin/tdedostartupconfig
%{prefix}/bin/tdefile
%{prefix}/bin/kfmexec
%{prefix}/bin/tdehotnewstuff
%{prefix}/bin/kinstalltheme
%{prefix}/bin/tdeio_http_cache_cleaner
%{prefix}/bin/tdeio_uiserver
%{prefix}/bin/tdeioexec
%{prefix}/bin/tdeioslave
%{prefix}/bin/tdeiso_info
%{prefix}/bin/tdelauncher
%{?with_elficon:%{prefix}/bin/tdelfeditor}
%{prefix}/bin/tdemailservice
%{prefix}/bin/tdemimelist
%{prefix}/bin/tdesendbugmail
%{prefix}/bin/kshell
%{prefix}/bin/tdestartupconfig
%{prefix}/bin/tdetelnetservice
%{prefix}/bin/tdetradertest
%{prefix}/bin/kwrapper
%{prefix}/bin/lnusertemp
%{prefix}/bin/make_driver_db_cups
%{prefix}/bin/make_driver_db_lpr
%{prefix}/bin/meinproc
%{prefix}/bin/networkstatustestservice
%{prefix}/bin/start_tdeinit_wrapper
%{prefix}/bin/checkXML
%{prefix}/bin/ksvgtopng
%{prefix}/bin/tdeunittestmodrunner
%{prefix}/bin/preparetips
%{prefix}/%{_lib}/trinity/*
%{prefix}/%{_lib}/lib*.so.*
%{prefix}/%{_lib}/libtdeinit_*.la
%{prefix}/%{_lib}/libtdeinit_*.so
%{prefix}/share/applications/tde/*.desktop
%{prefix}/share/autostart/tdeab2tdeabc.desktop
%{prefix}/share/applnk/tdeio_iso.desktop
%{prefix}/share/apps/*
%exclude %{prefix}/share/apps/ksgmltools2/
%{prefix}/share/emoticons/*
%{prefix}/share/icons/crystalsvg/
%{prefix}/share/icons/default.tde
%{prefix}/share/icons/hicolor/index.theme
%{prefix}/share/locale/all_languages
%{prefix}/share/mimelnk/*/*.desktop
%{prefix}/share/services/*
%{prefix}/share/servicetypes/*
%{prefix}/share/doc/tde/HTML/en/common/*
%{prefix}/share/doc/tde/HTML/en/tdespell/

# Global Trinity configuration
%config(noreplace) %{_sysconfdir}/trinity

# Some setuid binaries need special care
%attr(4755,root,root) %{prefix}/bin/kgrantpty
%attr(4755,root,root) %{prefix}/bin/kpac_dhcp_helper
%attr(4711,root,root) %{prefix}/bin/start_tdeinit

%config %{_sysconfdir}/xdg/menus/tde-applications.menu
%config %{_sysconfdir}/xdg/menus/tde-applications.menu-no-kde

# DBUS stuff, related to TDE hwlib
%{prefix}/bin/tde_dbus_hardwarecontrol
%config %{_sysconfdir}/dbus-1/system.d/org.trinitydesktop.hardwarecontrol.conf
%{_datadir}/dbus-1/system-services/org.trinitydesktop.hardwarecontrol.service

%pre
# TDE Bug #1074
if [ -d "%{prefix}/share/locale/all_languages" ]; then
  rm -rf "%{prefix}/share/locale/all_languages"
fi

%package devel
Summary:	TDE Libraries (Development files)
Group:		Development/Libraries/X11
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	tdelibs-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdelibs-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdelibs-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdelibs-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:	libtqt3-mt-devel >= 3.5.0
Requires:	libtqt4-devel = %{tde_epoch}:4.2.0
Requires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
Requires:	pkgconfig(libart-2.0)
Requires:	pkgconfig(libattr)
Requires:	intltool
%{?with_xcomposite:Requires: pkgconfig(xcomposite)}
%{?with_xt:Requires: pkgconfig(xt)}

%description devel
This package includes the header files you will need to compile
applications for TDE.

%files devel
%defattr(-,root,root,-)
%{prefix}/bin/dcopidl*
%{prefix}/bin/*config_compiler
%{prefix}/bin/maketdewidgets
%{prefix}/share/apps/ksgmltools2/
%{prefix}/include/tde/*
%{prefix}/%{_lib}/*.la
%{prefix}/%{_lib}/*.so
%{prefix}/%{_lib}/*.a
%exclude %{prefix}/%{_lib}/libtdeinit_*.la
%exclude %{prefix}/%{_lib}/libtdeinit_*.so
%{prefix}/share/cmake/tdelibs.cmake
%{prefix}/%{_lib}/pkgconfig/tdelibs.pc


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{prefix}/%{_lib}/pkgconfig"
export TDEDIR="%{prefix}"

%install -a

# Use system-wide CA certificates
%if "%{?cacert}" != ""
%__rm -f "%{?buildroot}%{prefix}/share/apps/kssl/ca-bundle.crt"
%__ln_s "%{cacert}" "%{?buildroot}%{prefix}/share/apps/kssl/ca-bundle.crt"
%endif

# Symlinks duplicate files (mostly under 'ksgmltools2')
%fdupes -s "%{?buildroot}"

# Remove setuid bit on some binaries.
chmod 0755 "%{?buildroot}%{prefix}/bin/kgrantpty"
chmod 0755 "%{?buildroot}%{prefix}/bin/kpac_dhcp_helper"
chmod 0755 "%{?buildroot}%{prefix}/bin/start_tdeinit"

# fileshareset 2.0 is provided separately.
# Remove integrated fileshareset 1.0 .
%__rm -f "%{?buildroot}%{prefix}/bin/filesharelist"
%__rm -f "%{?buildroot}%{prefix}/bin/fileshareset"

