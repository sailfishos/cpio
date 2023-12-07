Name:       cpio
Summary:    A GNU archiving program
Version:    2.14
Release:    1
License:    GPLv3+
URL:        http://www.gnu.org/software/cpio/
Source0:    %{name}-%{version}.tar.gz

# Patches from Fedora

# We use SVR4 portable format as default.
Patch1: cpio-2.14-rh.patch

# fix warn_if_file_changed() and set exit code to 1 when cpio fails to store
# file > 4GB (#183224)
# http://lists.gnu.org/archive/html/bug-cpio/2006-11/msg00000.html
Patch2: cpio-2.14-exitCode.patch

# Support major/minor device numbers over 127 (bz#450109)
# http://lists.gnu.org/archive/html/bug-cpio/2008-07/msg00000.html
Patch3: cpio-2.14-dev_number.patch

# Define default remote shell as /usr/bin/ssh (#452904)
Patch4: cpio-2.9.90-defaultremoteshell.patch

# Fix segfault with nonexisting file with patternnames (#567022)
# http://savannah.gnu.org/bugs/index.php?28954
# We have slightly different solution than upstream.
Patch5: cpio-2.14-patternnamesigsegv.patch

# Fix bad file name splitting while creating ustar archive (#866467)
# (fix backported from tar's source)
Patch7: cpio-2.10-longnames-split.patch

# Cpio does Sum32 checksum, not CRC (downstream)
Patch8: cpio-2.11-crc-fips-nit.patch

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
Requires:  %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
Man and info pages for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
./bootstrap \
    --no-git \
    --gnulib-srcdir=gnulib \
    --skip-po

%configure \
    --disable-nls

%make_build

%install
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
