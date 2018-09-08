#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lksctp-tools
Version  : 1.0.17
Release  : 3
URL      : http://downloads.sourceforge.net/lksctp/lksctp-tools-1.0.17.tar.gz
Source0  : http://downloads.sourceforge.net/lksctp/lksctp-tools-1.0.17.tar.gz
Summary  : User-level SCTP API library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: lksctp-tools-bin
Requires: lksctp-tools-lib
Requires: lksctp-tools-license
Requires: lksctp-tools-data
Requires: lksctp-tools-man

%description
This is the lksctp-tools package for Linux Kernel SCTP Reference
Implementation.

%package bin
Summary: bin components for the lksctp-tools package.
Group: Binaries
Requires: lksctp-tools-data
Requires: lksctp-tools-license
Requires: lksctp-tools-man

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
Requires: lksctp-tools-lib
Requires: lksctp-tools-bin
Requires: lksctp-tools-data
Provides: lksctp-tools-devel

%description dev
dev components for the lksctp-tools package.


%package lib
Summary: lib components for the lksctp-tools package.
Group: Libraries
Requires: lksctp-tools-data
Requires: lksctp-tools-license

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
%setup -q -n lksctp-tools-1.0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536449279
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1536449279
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/lksctp-tools
cp COPYING %{buildroot}/usr/share/doc/lksctp-tools/COPYING
cp COPYING.lib %{buildroot}/usr/share/doc/lksctp-tools/COPYING.lib
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/man/man3/sctp_send.3
/usr/share/man/man3/sctp_sendmsg.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsctp.so.1
/usr/lib64/libsctp.so.1.0.17
/usr/lib64/lksctp-tools/libwithsctp.so
/usr/lib64/lksctp-tools/libwithsctp.so.1
/usr/lib64/lksctp-tools/libwithsctp.so.1.0.17

%files license
%defattr(-,root,root,-)
/usr/share/doc/lksctp-tools/COPYING
/usr/share/doc/lksctp-tools/COPYING.lib

%files man
%defattr(-,root,root,-)
/usr/share/man/man7/sctp.7
