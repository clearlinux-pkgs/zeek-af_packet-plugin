#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zeek-af_packet-plugin
Version  : 3.1.1
Release  : 4
URL      : https://github.com/J-Gras/zeek-af_packet-plugin/archive/3.1.1/zeek-af_packet-plugin-3.1.1.tar.gz
Source0  : https://github.com/J-Gras/zeek-af_packet-plugin/archive/3.1.1/zeek-af_packet-plugin-3.1.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : ISC
Requires: zeek-af_packet-plugin-lib = %{version}-%{release}
Requires: zeek-af_packet-plugin-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : libpcap-dev
BuildRequires : linux-dev
BuildRequires : zeek-dev
BuildRequires : zeek-staticdev

%description
# Zeek::AF_Packet
This plugin provides native AF_Packet support for Zeek. For details about AF_Packet, see the corresponding [man page](http://man7.org/linux/man-pages/man7/packet.7.html).

%package lib
Summary: lib components for the zeek-af_packet-plugin package.
Group: Libraries
Requires: zeek-af_packet-plugin-license = %{version}-%{release}

%description lib
lib components for the zeek-af_packet-plugin package.


%package license
Summary: license components for the zeek-af_packet-plugin package.
Group: Default

%description license
license components for the zeek-af_packet-plugin package.


%prep
%setup -q -n zeek-af_packet-plugin-3.1.1
cd %{_builddir}/zeek-af_packet-plugin-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653338941
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake .. -DBinPAC_ROOT_DIR=$(zeek-config --binpac_root) \
-DBROKER_ROOT_DIR=$(zeek-config --broker_root) \
-DCAF_ROOT_DIR=$(zeek-config --caf_root) \
-DBRO_CONFIG_PLUGIN_DIR=$(zeek-config --plugin_dir) \
-DBRO_CONFIG_PREFIX=$(zeek-config --prefix) \
-DBRO_CONFIG_INCLUDE_DIR=$(zeek-config --include_dir) \
-DBRO_CONFIG_CMAKE_DIR=$(zeek-config --cmake_dir) \
-DCMAKE_MODULE_PATH=$(zeek-config --cmake_dir) \
-DKERNELHEADERS_ROOT_DIR=/usr/lib/modules/*/build
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1653338941
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zeek-af_packet-plugin
cp %{_builddir}/zeek-af_packet-plugin-3.1.1/COPYING %{buildroot}/usr/share/package-licenses/zeek-af_packet-plugin/47d40be49e9bbbef0991504c098ffac8fbdefc24
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/zeek/plugins/Zeek_AF_Packet/COPYING
/usr/lib64/zeek/plugins/Zeek_AF_Packet/README
/usr/lib64/zeek/plugins/Zeek_AF_Packet/VERSION
/usr/lib64/zeek/plugins/Zeek_AF_Packet/__bro_plugin__
/usr/lib64/zeek/plugins/Zeek_AF_Packet/lib/bif/__load__.zeek
/usr/lib64/zeek/plugins/Zeek_AF_Packet/lib/bif/af_packet.bif.zeek
/usr/lib64/zeek/plugins/Zeek_AF_Packet/scripts/__load__.zeek
/usr/lib64/zeek/plugins/Zeek_AF_Packet/scripts/af_packet/__load__.zeek
/usr/lib64/zeek/plugins/Zeek_AF_Packet/scripts/init.zeek
/usr/lib64/zeek/plugins/Zeek_AF_Packet/zeekctl/af_packet.py

%files lib
%defattr(-,root,root,-)
/usr/lib64/zeek/plugins/Zeek_AF_Packet/lib/Zeek-AF_Packet.linux-x86_64.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zeek-af_packet-plugin/47d40be49e9bbbef0991504c098ffac8fbdefc24
