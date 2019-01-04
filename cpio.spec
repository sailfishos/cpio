Name:       cpio
Summary:    A GNU archiving program
Version:    2.11
Release:    2
Group:      Applications/Archiving
License:    GPLv3+
URL:        http://www.gnu.org/software/cpio/
Source0:    ftp://ftp.gnu.org/gnu/cpio/cpio-%{version}.tar.gz
Source1:    cpio.1
Patch0:     cpio-2.6-setLocale.patch
Patch1:     cpio-2.9-rh.patch
Patch2:     cpio-2.9-exitCode.patch
Patch3:     cpio-2.9-dev_number.patch
Patch4:     cpio-2.9.90-defaultremoteshell.patch
Patch5:     cpio-aarch64.patch
Patch6:     cpio-gets-aarch64.patch
Patch7:     cpio-2.11-CVE-2014-9112.patch
Patch8:     cpio-2.11-testsuite-CVE-2014-9112.patch
Patch9:     cpio-2.11-CVE-2015-1197.patch
BuildRequires:  texinfo
BuildRequires:  autoconf
BuildRequires:  gettext

%description
GNU cpio copies files into or out of a cpio or tar archive.  Archives
are files which contain a collection of other files plus information
about them, such as their file name, owner, timestamps, and access
permissions.  The archive can be another file on the disk, a magnetic
tape, or a pipe.  GNU cpio supports the following archive formats:  binary,
old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar and POSIX.1
tar.  By default, cpio creates binary format archives, so that they are
compatible with older cpio programs.  When it is extracting files from
archives, cpio automatically recognizes which kind of archive it is reading
and can read archives created on machines with a different byte-order.

Install cpio if you need a program to manage file archives.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
Man and info pages for %{name}.

%prep
%setup -q -n %{name}-%{version}

# cpio-2.6-setLocale.patch
%patch0 -p1
# cpio-2.9-rh.patch
%patch1 -p1
# cpio-2.9-exitCode.patch
%patch2 -p1
# cpio-2.9-dev_number.patch
%patch3 -p1
# cpio-2.9.90-defaultremoteshell.patch
%patch4 -p1
# cpio-aarch64.patch
%patch5 -p1
# cpio-gets-aarch64.patch
%patch6 -p1
# cpio-2.11-CVE-2014-9112.patch
%patch7 -p1
# cpio-2.11-testsuite-CVE-2014-9112.patch
%patch8 -p1
# cpio-2.11-CVE-2015-1197.patch
%patch9 -p1

%build
%reconfigure --disable-static \
    --disable-nls

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}%{_mandir}/man1
cp -a %{SOURCE1} %{buildroot}%{_mandir}/man1

mkdir -p $RPM_BUILD_ROOT/bin
ln -sf ../usr/bin/cpio $RPM_BUILD_ROOT/bin/
rm -rf %{buildroot}%{_prefix}/libexec/rmt

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m0644 -t $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
        AUTHORS ChangeLog NEWS README THANKS

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/*
/bin/cpio

%files doc
%defattr(-,root,root,-)
%{_infodir}/%{name}.*
%{_mandir}/man1/%{name}.*
%{_mandir}/man1/mt.*
%{_docdir}/%{name}-%{version}
