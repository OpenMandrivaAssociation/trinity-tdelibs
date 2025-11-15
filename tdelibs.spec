#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !


# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
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

%if 0%{?mdkversion}
# breaks desktop files when not defined
%define dont_fix_xdg 1
%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1
%endif

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity
%global toolchain %(readlink /usr/bin/cc)


Name:			trinity-%{tde_pkg}
Version:		%{tde_version}
Release:		%{?!preversion:2}%{?preversion:0_%{preversion}}%{?dist}
Summary:		TDE Libraries
Group:			System/GUI/Other
URL:			http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:		GPL-2.0+
%else
License:		GPLv2+
%endif

#Vendor:			Trinity Desktop
#Packager:		Francois Andriot <francois.andriot@free.fr>

Prefix:			%{tde_prefix}

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:		%{name}-rpmlintrc

BuildRequires:  cmake make

Obsoletes:		tdelibs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		tdelibs = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-kdelibs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdelibs = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-kdelibs-apidocs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdelibs-apidocs = %{?epoch:%{epoch}:}%{version}-%{release}

# for set_permissions macro
%if 0%{?suse_version}
PreReq: permissions
%endif

# Trinity dependencies
BuildRequires:	libtqt4-devel = %{tde_epoch}:4.2.0
BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	libdbus-tqt-1-devel >= %{tde_epoch}:0.63
BuildRequires:	libdbus-1-tqt-devel >= %{tde_epoch}:0.9
BuildRequires:	trinity-filesystem >= %{tde_version}

Requires:		trinity-arts >= %{tde_epoch}:1.5.10
Requires:		trinity-filesystem >= %{tde_version}
# %if 0%{?mgaversion} >= 6
# %else
# Requires:		fileshareset >= 2.0
# %endif

BuildRequires:	trinity-tde-cmake >= %{tde_version}
%if "%{?toolchain}" != "clang"
BuildRequires:	gcc-c++
%endif
BuildRequires:	pkgconfig
BuildRequires:	fdupes

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

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
#  Not on openSUSE.
%if 0%{!?suse_version}
%define with_gamin 1
BuildRequires:	pkgconfig(gamin)
%endif

# PCRE support
%define with_pcre 1
BuildRequires:  pkgconfig(libpcre)

# PCRE2 support
BuildRequires:  pkgconfig(libpcre2-posix)

# INOTIFY support
# implied
%define with_inotify 1

# BZIP2 support
BuildRequires:  pkgconfig(bzip2)

# UTEMPTER support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos}
BuildRequires:	%{_lib}utempter-devel
%endif
%if 0%{?rhel} >=5 || 0%{?fedora}
BuildRequires:	libutempter-devel
%endif
%if 0%{?rhel} == 4
BuildRequires:	utempter
%endif
%if 0%{?suse_version} && 0%{?suse_version} < 1699
BuildRequires:	utempter-devel
%endif


# HSPELL support
%if 0%{!?suse_version}
%define with_hspell 1
BuildRequires:	hspell-devel
%endif

# JASPER support
%define with_jasper 1
BuildRequires:  pkgconfig(jasper)

# AVAHI support
%define with_avahi 1
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:  trinity-avahi-tqt-devel

# OPENEXR support
%define with_openexr 1
BuildRequires:	pkgconfig(OpenEXR)

# LIBTOOL
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?pclinuxos}
BuildRequires:	libtool-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libtool-ltdl-devel
%endif

# X11 support
BuildRequires:  pkgconfig(x11)

# ICEAUTH
%if 0%{?fedora} >= 34 || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos} || 0%{?rhel} >= 9 || 0%{?suse_version} >= 1220
Requires:		iceauth
BuildRequires:	iceauth
%endif

# Xorg
%if 0%{?rhel} >= 5 || ( 0%{?fedora} && 0%{?fedora} <= 33 )
Requires:		xorg-x11-server-utils
BuildRequires:	xorg-x11-server-utils
%endif
%if 0%{?rhel} == 4
Requires:		xorg-x11
BuildRequires:	xorg-x11
%endif

# XFT support
BuildRequires:  pkgconfig(xft)

# XZ support
%define with_lzma 1
BuildRequires:	pkgconfig(liblzma)

# Certificates support
BuildRequires:	ca-certificates
Requires:       openssl
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 6
%define	cacert	%{_sysconfdir}/pki/tls/certs/ca-bundle.crt
%endif
%if 0%{?fedora} == 18 || 0%{?fedora} == 19
%define	cacert	%{_sysconfdir}/ssl/certs/ca-certificates.crt
%endif

%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?mdkver} || 0%{?pclinuxos}
%if 0%{?pclinuxos} || 0%{?mgaversion} >= 8 || 0%{?mdkver} || 0%{?pclinuxos}
Requires:		rootcerts
%define	cacert	%{_sysconfdir}/pki/tls/certs/ca-bundle.crt
%else
%define	cacert	%{_sysconfdir}/ssl/certs/ca-bundle.crt
Requires:		openssl
%endif
%endif

%if 0%{?rhel} == 5
%define	cacert	%{_sysconfdir}/pki/tls/certs/ca-bundle.crt
Requires:		openssl
%endif

%if 0%{?suse_version}
%define cacert	%{_sysconfdir}/ssl/ca-bundle.pem
%endif
%if "%{cacert}" != ""
Requires:		%{cacert}
%endif

# XRANDR support
#  On RHEL5, xrandr library is too old.
# implied
%define with_xrandr 1
BuildRequires:  pkgconfig(xrandr)

# XCOMPOSITE support
BuildRequires:  pkgconfig(xcomposite)

# XT support
BuildRequires:  pkgconfig(xt)

### New features in TDE R14

# LIBMAGIC support
BuildRequires:  pkgconfig(libmagic)

# NETWORKMANAGER support
%define with_nm 1
BuildRequires:  pkgconfig(libnm)

# UDEV support
%define with_tdehwlib 1
BuildRequires:  pkgconfig(udev)


# HAL support
%if 0%{?rhel} == 5
%define with_hal 1
%endif

# UDISKS support
%if 0%{?rhel} == 6
%define with_udisks 1
BuildRequires:	udisks-devel
Requires:		udisks
%endif

# UDISKS2 support
%define with_udisks2 1
BuildRequires:  pkgconfig(udisks2)

# DEVICEKIT POWER support
%if 0%{?rhel} == 6
%define with_devkitpower 1
Requires:		DeviceKit-power
%endif

# UPOWER support
%define with_upower 1
BuildRequires:  pkgconfig(upower-glib)

# SYSTEMD support
%if 0%{?fedora} || 0%{?suse_version} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?rhel} >= 7
%define with_systemd 1
%endif

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
%if 0%{!?mdkversion}
%define with_elficon 1
BuildRequires:		libr-devel >= 0.6.0
%endif

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
%{tde_bindir}/imagetops
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
%if 0%{?with_elficon}
%{tde_bindir}/tdelfeditor
%endif
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
%if 0%{?suse_version}
%verify(not mode) %{tde_bindir}/kgrantpty
%verify(not mode) %{tde_bindir}/kpac_dhcp_helper
%verify(not mode) %{tde_bindir}/start_tdeinit
%else
%attr(4755,root,root) %{tde_bindir}/kgrantpty
%attr(4755,root,root) %{tde_bindir}/kpac_dhcp_helper
%attr(4711,root,root) %{tde_bindir}/start_tdeinit
%endif

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

%post
%if 0%{?suse_version}
# Sets permissions on setuid files (openSUSE specific)
%set_permissions %{tde_bindir}/kgrantpty
%set_permissions %{tde_bindir}/kpac_dhcp_helper
%set_permissions %{tde_bindir}/start_tdeinit
%endif

##########

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
%{?xcomposite_devel:Requires: pkgconfig(xcomposite)}
%{?xt_devel:Requires: pkgconfig(xt)}

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

##########

%if 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%autosetup -n %{tarball_name}-%{version}%{?preversion:~%{preversion}}

# RHEL 5: remove tdehwlib stuff from include files, to avoid FTBFS in tdebindings
%if 0%{?rhel} == 5
%__sed -i "tdecore/kinstance.h" \
       -i "tdecore/tdeglobal.h" \
       -e "/#ifdef __TDE_HAVE_TDEHWLIB/,/#endif/d"
%endif


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

if [ -d "/usr/X11R6" ]; then
  export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -L/usr/X11R6/%{_lib} -I/usr/X11R6/include"
fi

export TDEDIR="%{tde_prefix}"

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DBIN_INSTALL_DIR="%{tde_bindir}" \
  -DCONFIG_INSTALL_DIR="%{tde_confdir}" \
  -DDOC_INSTALL_DIR="%{tde_docdir}" \
  -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
  \
  -DWITH_ALL_OPTIONS=ON \
  -DWITH_ARTS=ON \
  -DWITH_ALSA=ON \
  -DWITH_LIBART=ON \
  -DWITH_LIBIDN=ON \
  -DWITH_SSL=ON \
  -DWITH_CUPS=ON \
  -DWITH_LUA=OFF \
  -DWITH_TIFF=ON \
  %{?!with_jasper:-DWITH_JASPER=OFF} \
  %{?!with_openexr:-DWITH_OPENEXR=OFF} \
  -DWITH_UTEMPTER=ON \
  %{?!with_avahi:-DWITH_AVAHI=OFF} \
  %{?!with_elficon:-DWITH_ELFICON=OFF} \
  %{?!with_pcre:-DWITH_PCRE=OFF} \
  %{?!with_inotify:-DWITH_INOTIFY=OFF} \
  %{?!with_gamin:-DWITH_GAMIN=OFF} \
  %{?!with_tdehwlib:-DWITH_TDEHWLIB=OFF} \
  %{?!with_tdehwlib:-DWITH_TDEHWLIB_DAEMONS=OFF} \
  %{?with_hal:-DWITH_HAL=ON} \
  %{?with_devkitpower:-DWITH_DEVKITPOWER=ON} \
  %{?with_systemd:-DWITH_LOGINDPOWER=ON} \
  %{?!with_upower:-DWITH_UPOWER=OFF} \
  %{?!with_udisks:-DWITH_UDISKS=OFF} \
  %{?!with_udisks2:-DWITH_UDISKS2=OFF} \
  -DWITH_UDEVIL=OFF \
  -DWITH_CONSOLEKIT=ON \
  %{?with_nm:-DWITH_NETWORK_MANAGER_BACKEND=ON} \
  -DWITH_SUDO_TDESU_BACKEND=OFF \
  -DWITH_OLD_XDG_STD=OFF \
  -DWITH_PCSC=ON \
  -DWITH_PKCS=ON \
  -DWITH_CRYPTSETUP=ON \
  %{?!with_lzma:-DWITH_LZMA=OFF} \
  -DWITH_LIBBFD=OFF \
  %{?!with_xrandr:-DWITH_XRANDR=OFF} \
  -DWITH_XCOMPOSITE=ON \
  -DWITH_KDE4_MENU_SUFFIX=OFF \
  \
  -DWITH_ASPELL=ON \
  %{?!with_hspell:-DWITH_HSPELL=OFF} \
  -DWITH_TDEICONLOADER_DEBUG=OFF \
%if 0%{?mdkversion}
  -DCMAKE_POLICY_DEFAULT_CMP0109=NEW \
%endif
  ..

%__make %{?_smp_mflags} || %__make


%install
%__make install DESTDIR="%{?buildroot}" -C build

# Use system-wide CA certificates
%if "%{?cacert}" != ""
%__rm -f "%{?buildroot}%{tde_datadir}/apps/kssl/ca-bundle.crt"
%__ln_s "%{cacert}" "%{?buildroot}%{tde_datadir}/apps/kssl/ca-bundle.crt"
%endif

# Symlinks duplicate files (mostly under 'ksgmltools2')
%fdupes -s "%{?buildroot}"

# Fix 'tderesources.desktop' (openSUSE only)
%if 0%{?suse_version}
%suse_update_desktop_file -r tderesources Qt X-TDE-settings-desktop
%endif

# Remove setuid bit on some binaries.
chmod 0755 "%{?buildroot}%{tde_bindir}/kgrantpty"
chmod 0755 "%{?buildroot}%{tde_bindir}/kpac_dhcp_helper"
chmod 0755 "%{?buildroot}%{tde_bindir}/start_tdeinit"

# fileshareset 2.0 is provided separately.
# Remove integrated fileshareset 1.0 .
%__rm -f "%{?buildroot}%{tde_bindir}/filesharelist"
%__rm -f "%{?buildroot}%{tde_bindir}/fileshareset"



%if 0%{?suse_version}
# Check permissions on setuid files (openSUSE specific)
%verifyscript
%verify_permissions -e %{tde_bindir}/kgrantpty
%verify_permissions -e %{tde_bindir}/kpac_dhcp_helper
%verify_permissions -e %{tde_bindir}/start_tdeinit
%endif

