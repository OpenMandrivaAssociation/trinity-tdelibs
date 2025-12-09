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
%define pkg_rel 3

%define tde_pkg tdelibs
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

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

Prefix:			%{tde_prefix}

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:		%{name}-rpmlintrc

BuildSystem:  cmake
BuildOption:  -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:  -DCMAKE_SKIP_RPATH=OFF
BuildOption:  -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:  -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:  -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:  -DCMAKE_NO_BUILTIN_CHRPATH=ON
BuildOption:  -DWITH_GCC_VISIBILITY=ON
BuildOption:  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}"
BuildOption:  -DBIN_INSTALL_DIR="%{tde_bindir}"
BuildOption:  -DCONFIG_INSTALL_DIR="%{tde_confdir}"
BuildOption:  -DDOC_INSTALL_DIR="%{tde_docdir}"
BuildOption:  -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}"
BuildOption:  -DLIB_INSTALL_DIR="%{tde_libdir}"
BuildOption:  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig"
BuildOption:  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
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
%{?!with_jasper:BuildOption:  -DWITH_JASPER=OFF}
%{?!with_openexr:BuildOption:  -DWITH_OPENEXR=OFF}
%{?!with_avahi:BuildOption:  -DWITH_AVAHI=OFF}
%{?!with_elficon:BuildOption:  -DWITH_ELFICON=OFF}
%{?!with_pcre:BuildOption:  -DWITH_PCRE=OFF}
%{?!with_inotify:BuildOption:  -DWITH_INOTIFY=OFF}
%{?!with_gamin:BuildOption:  -DWITH_GAMIN=OFF}
%{?!with_tdehwlib:BuildOption:  -DWITH_TDEHWLIB=OFF}
%{?!with_tdehwlib:BuildOption:  -DWITH_TDEHWLIB_DAEMONS=OFF}
%{?with_systemd:BuildOption:  -DWITH_LOGINDPOWER=ON}
%{?!with_upower:BuildOption:  -DWITH_UPOWER=OFF}
%{?!with_udisks2:BuildOption:  -DWITH_UDISKS2=OFF}
%{?with_nm:BuildOption:  -DWITH_NETWORK_MANAGER_BACKEND=ON}
%{?with_sudo:BuildOption:  -DWITH_SUDO_TDESU_BACKEND=ON}
%{?!with_lzma:BuildOption:  -DWITH_LZMA=OFF}
%{?!with_xrandr:BuildOption:  -DWITH_XRANDR=OFF}
%{?with_xcomposite:BuildOption:  -DWITH_XCOMPOSITE=ON}
%{?!with_hspell:BuildOption:  -DWITH_HSPELL=OFF}

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
%{tde_bindir}/artsmessage
%{tde_bindir}/cupsdconf
%{tde_bindir}/cupsdoprint
%{tde_bindir}/dcop
%{tde_bindir}/dcopclient
%{tde_bindir}/dcopfind
%{tde_bindir}/dcopobject
%{tde_bindir}/dcopquit
%{tde_bindir}/dcopref
%{tde_bindir}/dcopserver
%{tde_bindir}/dcopserver_shutdown
%{tde_bindir}/dcopstart
# %{tde_bindir}/imagetops
%{tde_bindir}/tdeab2tdeabc
%{tde_bindir}/kaddprinterwizard
%{tde_bindir}/tdebuildsycoca
%{tde_bindir}/tdecmshell
%{tde_bindir}/tdeconf_update
%{tde_bindir}/kcookiejar
%{tde_bindir}/tde-config
%{tde_bindir}/tde-menu
%{tde_bindir}/kded
%{tde_bindir}/tdeinit
%{tde_bindir}/tdeinit_shutdown
%{tde_bindir}/tdeinit_wrapper
%{tde_bindir}/tdesu_stub
%{tde_bindir}/kdetcompmgr
%{tde_bindir}/kdontchangethehostname
%{tde_bindir}/tdedostartupconfig
%{tde_bindir}/tdefile
%{tde_bindir}/kfmexec
%{tde_bindir}/tdehotnewstuff
%{tde_bindir}/kinstalltheme
%{tde_bindir}/tdeio_http_cache_cleaner
%{tde_bindir}/tdeio_uiserver
%{tde_bindir}/tdeioexec
%{tde_bindir}/tdeioslave
%{tde_bindir}/tdeiso_info
%{tde_bindir}/tdelauncher
%{?with_elficon:%{tde_bindir}/tdelfeditor}
%{tde_bindir}/tdemailservice
%{tde_bindir}/tdemimelist
%{tde_bindir}/tdesendbugmail
%{tde_bindir}/kshell
%{tde_bindir}/tdestartupconfig
%{tde_bindir}/tdetelnetservice
%{tde_bindir}/tdetradertest
%{tde_bindir}/kwrapper
%{tde_bindir}/lnusertemp
%{tde_bindir}/make_driver_db_cups
%{tde_bindir}/make_driver_db_lpr
%{tde_bindir}/meinproc
%{tde_bindir}/networkstatustestservice
%{tde_bindir}/start_tdeinit_wrapper
%{tde_bindir}/checkXML
%{tde_bindir}/ksvgtopng
%{tde_bindir}/tdeunittestmodrunner
%{tde_bindir}/preparetips
%{tde_tdelibdir}/*
%{tde_libdir}/lib*.so.*
%{tde_libdir}/libtdeinit_*.la
%{tde_libdir}/libtdeinit_*.so
%{tde_datadir}/applications/tde/*.desktop
%{tde_datadir}/autostart/tdeab2tdeabc.desktop
%{tde_datadir}/applnk/tdeio_iso.desktop
%{tde_datadir}/apps/*
%exclude %{tde_datadir}/apps/ksgmltools2/
%{tde_datadir}/emoticons/*
%{tde_datadir}/icons/crystalsvg/
%{tde_datadir}/icons/default.tde
%{tde_datadir}/icons/hicolor/index.theme
%{tde_datadir}/locale/all_languages
%{tde_datadir}/mimelnk/*/*.desktop
%{tde_datadir}/services/*
%{tde_datadir}/servicetypes/*
%{tde_tdedocdir}/HTML/en/common/*
%{tde_tdedocdir}/HTML/en/tdespell/

# Global Trinity configuration
%config(noreplace) %{tde_confdir}

# Some setuid binaries need special care
%attr(4755,root,root) %{tde_bindir}/kgrantpty
%attr(4755,root,root) %{tde_bindir}/kpac_dhcp_helper
%attr(4711,root,root) %{tde_bindir}/start_tdeinit

%config %{_sysconfdir}/xdg/menus/tde-applications.menu
%config %{_sysconfdir}/xdg/menus/tde-applications.menu-no-kde

# DBUS stuff, related to TDE hwlib
%{tde_bindir}/tde_dbus_hardwarecontrol
%config %{_sysconfdir}/dbus-1/system.d/org.trinitydesktop.hardwarecontrol.conf
%{_datadir}/dbus-1/system-services/org.trinitydesktop.hardwarecontrol.service

%pre
# TDE Bug #1074
if [ -d "%{tde_datadir}/locale/all_languages" ]; then
  rm -rf "%{tde_datadir}/locale/all_languages"
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
%{tde_bindir}/dcopidl*
%{tde_bindir}/*config_compiler
%{tde_bindir}/maketdewidgets
%{tde_datadir}/apps/ksgmltools2/
%{tde_tdeincludedir}/*
%{tde_libdir}/*.la
%{tde_libdir}/*.so
%{tde_libdir}/*.a
%exclude %{tde_libdir}/libtdeinit_*.la
%exclude %{tde_libdir}/libtdeinit_*.so
%{tde_datadir}/cmake/tdelibs.cmake
%{tde_libdir}/pkgconfig/tdelibs.pc


%prep
%autosetup -n %{tarball_name}-%{version}%{?preversion:~%{preversion}}

%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"
export TDEDIR="%{tde_prefix}"

%install -a

# Use system-wide CA certificates
%if "%{?cacert}" != ""
%__rm -f "%{?buildroot}%{tde_datadir}/apps/kssl/ca-bundle.crt"
%__ln_s "%{cacert}" "%{?buildroot}%{tde_datadir}/apps/kssl/ca-bundle.crt"
%endif

# Symlinks duplicate files (mostly under 'ksgmltools2')
%fdupes -s "%{?buildroot}"

# Remove setuid bit on some binaries.
chmod 0755 "%{?buildroot}%{tde_bindir}/kgrantpty"
chmod 0755 "%{?buildroot}%{tde_bindir}/kpac_dhcp_helper"
chmod 0755 "%{?buildroot}%{tde_bindir}/start_tdeinit"

# fileshareset 2.0 is provided separately.
# Remove integrated fileshareset 1.0 .
%__rm -f "%{?buildroot}%{tde_bindir}/filesharelist"
%__rm -f "%{?buildroot}%{tde_bindir}/fileshareset"

