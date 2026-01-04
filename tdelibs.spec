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
%define pkg_rel 7

%define tde_pkg tdelibs

%define tde_prefix /opt/trinity


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


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:		%{name}-rpmlintrc

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_INSTALL_PREFIX="%{tde_prefix}"
BuildOption:    -DCONFIG_INSTALL_DIR="%{_sysconfdir}/trinity"
BuildOption:    -DINCLUDE_INSTALL_DIR="%{tde_prefix}/include/tde"
BuildOption:    -DPKGCONFIG_INSTALL_DIR="%{tde_prefix}/%{_lib}/pkgconfig"
BuildOption:    -DWITH_ALL_OPTIONS=ON -DWITH_ARTS=ON -DWITH_ALSA=ON
BuildOption:    -DWITH_LIBART=ON -DWITH_LIBIDN=ON -DWITH_SSL=ON
BuildOption:    -DWITH_CUPS=ON -DWITH_LUA=OFF -DWITH_TIFF=ON 
BuildOption:    -DWITH_UTEMPTER=ON
BuildOption:    -DWITH_UDEVIL=OFF -DWITH_CONSOLEKIT=ON
BuildOption:    -DWITH_OLD_XDG_STD=OFF -DWITH_PCSC=ON
BuildOption:    -DWITH_PKCS=ON -DWITH_CRYPTSETUP=ON
BuildOption:    -DWITH_LIBBFD=OFF -DWITH_KDE4_MENU_SUFFIX=OFF
BuildOption:    -DWITH_ASPELL=ON -DWITH_TDEICONLOADER_DEBUG=OFF
BuildOption:    -DCMAKE_POLICY_DEFAULT_CMP0109=NEW
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
BuildOption:    -DWITH_JASPER=%{!?with_jasper:OFF}%{?with_jasper:ON}
BuildOption:    -DWITH_OPENEXR=%{!?with_openexr:OFF}%{?with_openexr:ON}
BuildOption:    -DWITH_AVAHI=%{!?with_avahi:OFF}%{?with_avahi:ON}
BuildOption:    -DWITH_ELFICON=%{!?with_elficon:OFF}%{?with_elficon:ON}
BuildOption:    -DWITH_PCRE=%{!?with_pcre:OFF}%{?with_pcre:ON}
BuildOption:    -DWITH_INOTIFY=%{!?with_inotify:OFF}%{?with_inotify:ON}
BuildOption:    -DWITH_GAMIN=%{!?with_gamin:OFF}%{?with_gamin:ON}
BuildOption:    -DWITH_TDEHWLIB=%{!?with_tdehwlib:OFF}%{?with_tdehwlib:ON}
BuildOption:    -DWITH_TDEHWLIB_DAEMONS=%{!?with_tdehwlib:OFF}%{?with_tdehwlib:ON}
BuildOption:    -DWITH_LOGINDPOWER=%{?with_systemd:ON}%{!?with_systemd:OFF}
BuildOption:    -DWITH_UPOWER=%{!?with_upower:OFF}%{?with_upower:ON}
BuildOption:    -DWITH_UDISKS2=%{!?with_udisks2:OFF}%{?with_udisks2:ON}
BuildOption:    -DWITH_NETWORK_MANAGER_BACKEND=%{?with_nm:ON}%{!?with_nm:OFF}
BuildOption:    -DWITH_SUDO_TDESU_BACKEND=%{?with_sudo:ON}%{!?with_sudo:OFF}
BuildOption:    -DWITH_LZMA=%{!?with_lzma:OFF}%{?with_lzma:ON}
BuildOption:    -DWITH_XRANDR=%{!?with_xrandr:OFF}%{?with_xrandr:ON}
BuildOption:    -DWITH_XCOMPOSITE=%{?with_xcomposite:ON}%{!?with_xcomposite:OFF}
BuildOption:    -DWITH_HSPELL=%{?!with_hspell:OFF}%{?with_hspell:ON}

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
%{tde_prefix}/bin/artsmessage
%{tde_prefix}/bin/cupsdconf
%{tde_prefix}/bin/cupsdoprint
%{tde_prefix}/bin/dcop
%{tde_prefix}/bin/dcopclient
%{tde_prefix}/bin/dcopfind
%{tde_prefix}/bin/dcopobject
%{tde_prefix}/bin/dcopquit
%{tde_prefix}/bin/dcopref
%{tde_prefix}/bin/dcopserver
%{tde_prefix}/bin/dcopserver_shutdown
%{tde_prefix}/bin/dcopstart
%{tde_prefix}/bin/imagetops
%{tde_prefix}/bin/tdeab2tdeabc
%{tde_prefix}/bin/kaddprinterwizard
%{tde_prefix}/bin/tdebuildsycoca
%{tde_prefix}/bin/tdecmshell
%{tde_prefix}/bin/tdeconf_update
%{tde_prefix}/bin/kcookiejar
%{tde_prefix}/bin/tde-config
%{tde_prefix}/bin/tde-menu
%{tde_prefix}/bin/kded
%{tde_prefix}/bin/tdeinit
%{tde_prefix}/bin/tdeinit_shutdown
%{tde_prefix}/bin/tdeinit_wrapper
%{tde_prefix}/bin/tdesu_stub
%{tde_prefix}/bin/kdetcompmgr
%{tde_prefix}/bin/kdontchangethehostname
%{tde_prefix}/bin/tdedostartupconfig
%{tde_prefix}/bin/tdefile
%{tde_prefix}/bin/kfmexec
%{tde_prefix}/bin/tdehotnewstuff
%{tde_prefix}/bin/kinstalltheme
%{tde_prefix}/bin/tdeio_http_cache_cleaner
%{tde_prefix}/bin/tdeio_uiserver
%{tde_prefix}/bin/tdeioexec
%{tde_prefix}/bin/tdeioslave
%{tde_prefix}/bin/tdeiso_info
%{tde_prefix}/bin/tdelauncher
%{?with_elficon:%{tde_prefix}/bin/tdelfeditor}
%{tde_prefix}/bin/tdemailservice
%{tde_prefix}/bin/tdemimelist
%{tde_prefix}/bin/tdesendbugmail
%{tde_prefix}/bin/kshell
%{tde_prefix}/bin/tdestartupconfig
%{tde_prefix}/bin/tdetelnetservice
%{tde_prefix}/bin/tdetradertest
%{tde_prefix}/bin/kwrapper
%{tde_prefix}/bin/lnusertemp
%{tde_prefix}/bin/make_driver_db_cups
%{tde_prefix}/bin/make_driver_db_lpr
%{tde_prefix}/bin/meinproc
%{tde_prefix}/bin/networkstatustestservice
%{tde_prefix}/bin/start_tdeinit_wrapper
%{tde_prefix}/bin/checkXML
%{tde_prefix}/bin/ksvgtopng
%{tde_prefix}/bin/tdeunittestmodrunner
%{tde_prefix}/bin/preparetips
%{tde_prefix}/%{_lib}/trinity/*
%{tde_prefix}/%{_lib}/lib*.so.*
%{tde_prefix}/%{_lib}/libtdeinit_*.la
%{tde_prefix}/%{_lib}/libtdeinit_*.so
%{tde_prefix}/share/applications/tde/*.desktop
%{tde_prefix}/share/autostart/tdeab2tdeabc.desktop
%{tde_prefix}/share/applnk/tdeio_iso.desktop
%{tde_prefix}/share/apps/*
%exclude %{tde_prefix}/share/apps/ksgmltools2/
%{tde_prefix}/share/emoticons/*
%{tde_prefix}/share/icons/crystalsvg/
%{tde_prefix}/share/icons/default.tde
%{tde_prefix}/share/icons/hicolor/index.theme
%{tde_prefix}/share/locale/all_languages
%{tde_prefix}/share/mimelnk/*/*.desktop
%{tde_prefix}/share/services/*
%{tde_prefix}/share/servicetypes/*
%{tde_prefix}/share/doc/tde/HTML/en/common/*
%{tde_prefix}/share/doc/tde/HTML/en/tdespell/

# Global Trinity configuration
%config(noreplace) %{_sysconfdir}/trinity

# Some setuid binaries need special care
%attr(4755,root,root) %{tde_prefix}/bin/kgrantpty
%attr(4755,root,root) %{tde_prefix}/bin/kpac_dhcp_helper
%attr(4711,root,root) %{tde_prefix}/bin/start_tdeinit

%config %{_sysconfdir}/xdg/menus/tde-applications.menu
%config %{_sysconfdir}/xdg/menus/tde-applications.menu-no-kde

# DBUS stuff, related to TDE hwlib
%{tde_prefix}/bin/tde_dbus_hardwarecontrol
%config %{_sysconfdir}/dbus-1/system.d/org.trinitydesktop.hardwarecontrol.conf
%{_datadir}/dbus-1/system-services/org.trinitydesktop.hardwarecontrol.service

%pre
# TDE Bug #1074
if [ -d "%{tde_prefix}/share/locale/all_languages" ]; then
  rm -rf "%{tde_prefix}/share/locale/all_languages"
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
%{tde_prefix}/bin/dcopidl*
%{tde_prefix}/bin/*config_compiler
%{tde_prefix}/bin/maketdewidgets
%{tde_prefix}/share/apps/ksgmltools2/
%{tde_prefix}/include/tde/*
%{tde_prefix}/%{_lib}/*.la
%{tde_prefix}/%{_lib}/*.so
%{tde_prefix}/%{_lib}/*.a
%exclude %{tde_prefix}/%{_lib}/libtdeinit_*.la
%exclude %{tde_prefix}/%{_lib}/libtdeinit_*.so
%{tde_prefix}/share/cmake/tdelibs.cmake
%{tde_prefix}/%{_lib}/pkgconfig/tdelibs.pc


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"
export TDEDIR="%{tde_prefix}"

%install -a

# Use system-wide CA certificates
%if "%{?cacert}" != ""
%__rm -f "%{?buildroot}%{tde_prefix}/share/apps/kssl/ca-bundle.crt"
%__ln_s "%{cacert}" "%{?buildroot}%{tde_prefix}/share/apps/kssl/ca-bundle.crt"
%endif

# Symlinks duplicate files (mostly under 'ksgmltools2')
%fdupes -s "%{?buildroot}"

# Remove setuid bit on some binaries.
chmod 0755 "%{?buildroot}%{tde_prefix}/bin/kgrantpty"
chmod 0755 "%{?buildroot}%{tde_prefix}/bin/kpac_dhcp_helper"
chmod 0755 "%{?buildroot}%{tde_prefix}/bin/start_tdeinit"

# fileshareset 2.0 is provided separately.
# Remove integrated fileshareset 1.0 .
%__rm -f "%{?buildroot}%{tde_prefix}/bin/filesharelist"
%__rm -f "%{?buildroot}%{tde_prefix}/bin/fileshareset"

