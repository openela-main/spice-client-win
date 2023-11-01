%global spice_data_dir  %{_datadir}/spice


Name: spice-client-win
Version: 8.8
Release: 1%{?dist}
License: GPLv2+
Summary: Spice client MSI installers for Windows clients
Group: Virtualization/Management
URL: http://www.spice-space.org

Source0: virt-viewer-x86-9.0.msi
Source1: spice-client-win-8.8-1-sources.zip
Source2: spice-client-win-8.8-1-spec.zip
Source3: UsbDk_1.0.22_x64.msi
Source4: SpiceVersion.txt
Source5: virt-viewer-x64-9.0.msi
Source6: UsbDk_1.0.22_x86.msi

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Spice client MSI installers for Windows clients

%package x86
Summary: Spice client MSI installers for Windows clients (32 bit)
Group: Virtualization/Management

%description x86
Spice client MSI installers for Windows clients (32 bit)

%package x64
Summary: Spice client MSI installers for Windows clients (64 bit)
Group: Virtualization/Management

%description x64
Spice client MSI installers for Windows clients (64 bit)

%prep

%build

%install
rm -rf %{buildroot}
/usr/bin/install -d %{buildroot}%{spice_data_dir}


/bin/cp %{SOURCE0} %{buildroot}%{spice_data_dir}/
/bin/cp %{SOURCE3} %{buildroot}%{spice_data_dir}/
/bin/cp %{SOURCE4} %{buildroot}%{spice_data_dir}/
/bin/cp %{SOURCE5} %{buildroot}%{spice_data_dir}/
/bin/cp %{SOURCE6} %{buildroot}%{spice_data_dir}/

cp %{buildroot}%{spice_data_dir}/SpiceVersion{,_x64}.txt

# rhbz#1010211 -- rename msi files to format <name>-<arch>.msi (remove version)
pushd  %{buildroot}%{spice_data_dir}/
mv virt-viewer-x64*.msi virt-viewer-x64.msi
mv virt-viewer-x86*.msi virt-viewer-x86.msi
mv UsbDk*x64.msi usbdk-x64.msi
mv UsbDk*x86.msi usbdk-x86.msi

popd
 
%clean
rm -rf %{buildroot}

%files x64
%defattr(0644,root,root,0755)
%{spice_data_dir}/virt-viewer-x64.msi
%{spice_data_dir}/usbdk-x64.msi
%{spice_data_dir}/SpiceVersion_x64.txt


%files x86
%defattr(0644,root,root,0755)
%{spice_data_dir}/virt-viewer-x86.msi
%{spice_data_dir}/usbdk-x86.msi
%{spice_data_dir}/SpiceVersion.txt

%changelog
* Sun Feb 12 2023 Uri Lublin <uril@redhat.com> - 8.8-1
- mingw-virt-viewer 9.0-8
  Resolves: rhbz#2125277

* Wed Sep  7 2022 Uri Lublin <uril@redhat.com> - 8.7-1
- mingw-virt-viewer 9.0-7
  Resolves: rhbz#2062684

* Sun Aug 22 2021 Uri Lublin <uril@redhat.com> - 8.5-5
- mingw-virt-viewer 9.0-6
  Resolves: rhbz#1997058
  Resolves: rhbz#1918877
  Related:  rhbz#1939111
  Related:  rhbz#1942919

* Tue Feb 09 2021 Uri Lublin <uril@redhat.com> - 8.4-1
- mingw-virt-viewer 9.0-3
- mingw-libgovirt   0.3.7-5
- mingw-spice-gtk   0.38-5
  Related: rhbz#844683
  Related: rhbz#1839104 rhbz#1874740 rhbz#1017261
  Related: rhbz#1918459


* Mon Jun 29 2020 Uri Lublin <uril@redhat.com> - 8.3-2
- mingw-virt-viewer 9.0-2
- mingw-libgovirt   0.3.7-4
  Related: rhbz#1841952

* Mon Jun 15 2020 Uri Lublin <uril@redhat.com> - 8.3-1
- mingw-virt-viewer 9.0-1
- spice-usbdk-win   1.0-22
- mingw-spice-gtk   0.38-4
- mingw-libgovirt   0.3.7-2
- mingw-spice-protocol 0.14-2
  Related:  rhbz#1841952, rhbz#1179070, rhbz#1428402
  Related:  rhbz#1575043, rhbz#1640058, rhbz#1793019
  Related:  rhbz#1841951
  Related:  rhbz#1842532
  Related:  rhbz#1841949
  Related:  rhbz#1773899
  Related:  rhbz#1741202, rhbz#1741252

* Mon Aug 27 2018 Uri Lublin <uril@redhat.com> - 8.0-1
- mingw-virt-viewer 7.0-1
- spice-usbdk-win   1.0-20
- Rebase for RHEL-8.0
  Related: rhbz#1557012
