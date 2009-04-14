Summary: Gives a fake chroot environment
Name: fakechroot
Version: 2.9
Release: 19%{?dist}
License: LGPLv2+
Group: Development/Tools
URL: http://fakechroot.alioth.debian.org/
Source0: http://ftp.debian.org/debian/pool/main/f/fakechroot/%{name}_%{version}.orig.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: fakechroot-libs = %{version}-%{release}

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

%build
%configure \
  --disable-dependency-tracking \
  --disable-static
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%check
#currently broken (reported upstream):
#cp: cannot stat `/bin/busybox': No such file or directory
#cp: cannot stat `/bin/csh': No such file or directory
#...
#FAIL: t.echoarg
#==================================
#1 of 1 tests failed
make check

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
* Tue Apr 14 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.9-19
- Update to 2.9.
- Removed fakechroot-2.8-initsocketlen.patch (upstream now).
- Removed int->ssize_t readlink type change (upstream testing for type
  now).
- Removed permission fix for scripts/ldd.fake scripts/restoremode.sh
  scripts/savemode.sh (fixed upstream).

* Wed Mar 18 2009 Richard W.M. Jones <rjones@redhat.com> - 2.8-18
- Create a fakeroot-libs subpackage so that the package is multilib aware.

* Thu Jan 15 2009 Rakesh Pandit <rakesh@fedoraproject.org> 2.8-16
- Fixed URL

* Sun Oct  5 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.8-15
- Fix getpeername/getsockname socklen initialization.

* Sun Aug 24 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.8-14
- %%check || : does not work anymore.

* Sun Aug  3 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.8-13
- Update to 2.8.

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
