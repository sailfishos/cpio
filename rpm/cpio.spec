Name:       cpio
Summary:    A GNU archiving program
Version:    2.13
Release:    1
Group:      Applications/Archiving
License:    GPLv3+
URL:        http://www.gnu.org/software/cpio/
Source0:    ftp://ftp.gnu.org/gnu/cpio/%{name}-%{version}.tar.gz
Patch0:     cpio-2.6-setLocale.patch
Patch1:     cpio-2.9-rh.patch
Patch2:     cpio-2.13-exitCode.patch
Patch3:     cpio-2.9-dev_number.patch
Patch4:     cpio-2.9.90-defaultremoteshell.patch
Provides:   bundled(gnulib)
Provides:   gnu-cpio
BuildRequires:  texinfo
BuildRequires:  autoconf
BuildRequires:  gettext
BuildRequires:  bison

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
%setup -q -n %{name}-%{version}/upstream

# cpio-2.6-setLocale.patch
%patch0 -p1
# cpio-2.9-rh.patch
%patch1 -p1
# cpio-2.13-exitCode.patch
%patch2 -p1
# cpio-2.9-dev_number.patch
%patch3 -p1
# cpio-2.9.90-defaultremoteshell.patch
%patch4 -p1

%build
./bootstrap \
    --no-git \
    --gnulib-srcdir=gnulib \
    --skip-po

%configure \
    --disable-nls

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

%make_install

mkdir -p %{buildroot}/bin
ln -sf ..%{_bindir}/cpio %{buildroot}/bin/
rm -f %{buildroot}%{_prefix}/libexec/rmt
rm -f %{buildroot}%{_mandir}/man8/rmt.*

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
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
%{_docdir}/%{name}-%{version}
