Summary: Gives a fake chroot environment
Name: fakechroot
Version: 2.9
Release: 23%{?dist}
License: LGPLv2+
Group: Development/Tools
URL: http://fakechroot.alioth.debian.org/
Source0: http://ftp.debian.org/debian/pool/main/f/fakechroot/%{name}_%{version}.orig.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: fakechroot-libs = %{version}-%{release}

# Required for patch0:
BuildRequires: autoconf, automake, libtool

# Fix build problems with recent glibc.  Sent upstream 20090414.
Patch0: fakechroot-scandir.patch

# Add FAKECHROOT_CMD_SUBST feature.
# Sent upstream 20090413.  Accepted upstream 20090418.
Patch1: fakechroot-cmd-subst.patch

# Patch to version of aclocal/automake.
Patch2: fakechroot-autogen.patch

%description
fakechroot runs a command in an environment were is additionally
possible to use the chroot(8) call without root privileges. This is
useful for allowing users to create their own chrooted environment
with possibility to install another packages without need for root
privileges.

%package libs
Summary: Gives a fake chroot environment (libraries)
Group: Development/Tools

%description libs
This package contains the libraries required by %{name}.

%prep
%setup -q

%patch0 -p0
%patch1 -p0
%patch2 -p1

# Patch0 updates autoconf, so rerun this:
./autogen.sh

%build
%configure \
  --disable-dependency-tracking \
  --disable-static
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%check
#make check

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE scripts/ldd.fake scripts/restoremode.sh scripts/savemode.sh
%{_bindir}/fakechroot
%{_mandir}/man1/fakechroot.1.gz

%files libs
%dir %{_libdir}/fakechroot
%exclude %{_libdir}/fakechroot/libfakechroot.la
%{_libdir}/fakechroot/libfakechroot.so

%changelog
* Mon May 11 2009 Richard W.M. Jones <rjones@redhat.com> - 2.9-23
- Patch autogen to not depend on specific aclocal/automake version.

* Mon May 11 2009 Richard W.M. Jones <rjones@redhat.com> - 2.9-22
- Backport newest fakechroot 2.9 from Rawhide.

* Sun May 06 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info>
- rebuilt for RHEL5 final

* Mon Jan  1 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.5-12
- Remove executable bits from scripts in documentation.

* Sun Dec 31 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.5-11
- Add %%{_libdir}/fakechroot to %%files.
- Fix license (is LGPL, not GPL).
- Add commented %%check (currently broken).
- Add ldd.fake and save/restoremode.sh to %%doc

* Fri Dec 29 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.5-10
- Extend the %%description a bit.

* Thu Dec 28 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.5-9
- Don't build static lib.
- Exclude libtool lib.

* Thu Nov 24 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.5.

* Sat Sep 17 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 2.4.

* Sun Jul  3 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.9+1.3.

* Sun Feb  6 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.5+1.2.4.

* Sun Jan 25 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.
