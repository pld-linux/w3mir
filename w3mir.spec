Summary:	A command-line client to download WWW documents.
Name:		w3mir
Version:	1.0.8
Release:	1
Group:		Applications/Networking
Vendor:		<janl@math.uio.no>
Source:         %{name}-%{version}.tar.gz
Patch:		Makefile.patch
URL:		http://www.math.uio.no/~janl/w3mir/
Copyright:	Artistic
BuildRoot:	/tmp/%{name}-%{version}-root
Requires:	perl-MIME-Base64, perl-libwww

%description
W3mir is a all purpose WWW copying and mirroring program. Its main
focus is copying complete directory structures keeping your copy
browseable through a web server, or directly off a disk or CDROM if
you want. W3mir will fix URLs that are redirected and everything else
that needs to be fixed to make your copy browseable. But it also does
the odd jobs, retrieving single documents, batch getting several
documents and more. You may tell w3mir not to change anything in the
retrieved documents. W3mir has been in development quite a long time
so you find options to do a lot of things needed when copying things
off the web.

With w3mir you may copy the entire contents of one directory hierarchy
of a web server, or several related hierarchies off as many servers as
you like. They don't even have to be related.

W3mir supports HTML4, and has partial support for CSS, Java, ActiveX
and Adobe Acrobat (PDF) files.

%prep
%setup

%build
perl Makefile.PL
patch -p1 < $RPM_SOURCE_DIR/Makefile.patch
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/site_perl
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/i386-linux/auto/w3mir
mkdir -p $RPM_BUILD_ROOT/usr/lib/perl5/i386-linux/5.00404
make install PREFIX=$RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%files
%doc Artistic Changes INSTALL README example.cfg multiscope.cfg
%doc w3mir-HOWTO.html
/usr/lib/perl5/site_perl/w3http.pm
/usr/lib/perl5/site_perl/w3pdfuri.pm
/usr/lib/perl5/site_perl/htmlop.pm
/usr/man/man1/w3mir.1
/usr/man/man1/w3mfix.1
/usr/bin/w3mir
/usr/bin/w3mfix
/usr/lib/perl5/site_perl/i386-linux/auto/w3mir/.packlist
