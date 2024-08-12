#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure_ac
# autospec version: v18
# autospec commit: f35655a
#
Name     : lksctp-tools
Version  : 1.0.20
Release  : 12
URL      : https://github.com/sctp/lksctp-tools/archive/lksctp-tools-1.0.20/lksctp-tools-1.0.20.tar.gz
Source0  : https://github.com/sctp/lksctp-tools/archive/lksctp-tools-1.0.20/lksctp-tools-1.0.20.tar.gz
Summary  : User-level SCTP API library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: lksctp-tools-bin = %{version}-%{release}
Requires: lksctp-tools-data = %{version}-%{release}
Requires: lksctp-tools-lib = %{version}-%{release}
Requires: lksctp-tools-license = %{version}-%{release}
Requires: lksctp-tools-man = %{version}-%{release}
BuildRequires : file
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is the lksctp-tools package for Linux Kernel SCTP Reference
Implementation.

%package bin
Summary: bin components for the lksctp-tools package.
Group: Binaries
Requires: lksctp-tools-data = %{version}-%{release}
Requires: lksctp-tools-license = %{version}-%{release}

%description bin
bin components for the lksctp-tools package.


%package data
Summary: data components for the lksctp-tools package.
Group: Data

%description data
data components for the lksctp-tools package.


%package dev
Summary: dev components for the lksctp-tools package.
Group: Development
Requires: lksctp-tools-lib = %{version}-%{release}
Requires: lksctp-tools-bin = %{version}-%{release}
Requires: lksctp-tools-data = %{version}-%{release}
Provides: lksctp-tools-devel = %{version}-%{release}
Requires: lksctp-tools = %{version}-%{release}

%description dev
dev components for the lksctp-tools package.


%package lib
Summary: lib components for the lksctp-tools package.
Group: Libraries
Requires: lksctp-tools-data = %{version}-%{release}
Requires: lksctp-tools-license = %{version}-%{release}

%description lib
lib components for the lksctp-tools package.


%package license
Summary: license components for the lksctp-tools package.
Group: Default

%description license
license components for the lksctp-tools package.


%package man
Summary: man components for the lksctp-tools package.
Group: Default

%description man
man components for the lksctp-tools package.


%prep
%setup -q -n lksctp-tools-lksctp-tools-1.0.20
cd %{_builddir}/lksctp-tools-lksctp-tools-1.0.20
pushd ..
cp -a lksctp-tools-lksctp-tools-1.0.20 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723481634
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%reconfigure --disable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
find ./src/func_tests -maxdepth 1 -type f -perm /u+x -name 'test_*' -exec {} \;

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1723481634
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lksctp-tools
cp %{_builddir}/lksctp-tools-lksctp-tools-%{version}/COPYING %{buildroot}/usr/share/package-licenses/lksctp-tools/faa78032a41c2bfe6bfd1df72ccd1bb7ab4f7a10 || :
cp %{_builddir}/lksctp-tools-lksctp-tools-%{version}/COPYING.lib %{buildroot}/usr/share/package-licenses/lksctp-tools/923576601c6fce213eacfa2c860643114a5bf356 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/checksctp
/V3/usr/bin/sctp_darn
/V3/usr/bin/sctp_status
/V3/usr/bin/sctp_test
/usr/bin/checksctp
/usr/bin/sctp_darn
/usr/bin/sctp_status
/usr/bin/sctp_test
/usr/bin/withsctp

%files data
%defattr(-,root,root,-)
/usr/share/lksctp-tools/checksctp.c
/usr/share/lksctp-tools/sctp_bind.c
/usr/share/lksctp-tools/sctp_darn.c
/usr/share/lksctp-tools/sctp_darn.h
/usr/share/lksctp-tools/sctp_load_libs.c
/usr/share/lksctp-tools/sctp_socket.c
/usr/share/lksctp-tools/sctp_socket.h
/usr/share/lksctp-tools/sctp_sockopt.c
/usr/share/lksctp-tools/sctp_status.c
/usr/share/lksctp-tools/sctp_test.c

%files dev
%defattr(-,root,root,-)
/usr/include/netinet/sctp.h
/usr/lib64/libsctp.so
/usr/lib64/pkgconfig/libsctp.pc
/usr/share/man/man3/sctp_bindx.3
/usr/share/man/man3/sctp_connectx.3
/usr/share/man/man3/sctp_getladdrs.3
/usr/share/man/man3/sctp_getpaddrs.3
/usr/share/man/man3/sctp_opt_info.3
/usr/share/man/man3/sctp_peeloff.3
/usr/share/man/man3/sctp_recvmsg.3
/usr/share/man/man3/sctp_recvv.3
/usr/share/man/man3/sctp_send.3
/usr/share/man/man3/sctp_sendmsg.3
/usr/share/man/man3/sctp_sendv.3

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libsctp.so.1.0.19
/V3/usr/lib64/lksctp-tools/libwithsctp.so.1.0.19
/usr/lib64/libsctp.so.1
/usr/lib64/libsctp.so.1.0.19
/usr/lib64/lksctp-tools/libwithsctp.so
/usr/lib64/lksctp-tools/libwithsctp.so.1
/usr/lib64/lksctp-tools/libwithsctp.so.1.0.19

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lksctp-tools/923576601c6fce213eacfa2c860643114a5bf356
/usr/share/package-licenses/lksctp-tools/faa78032a41c2bfe6bfd1df72ccd1bb7ab4f7a10

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man7/sctp.7
