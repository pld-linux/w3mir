%include	/usr/lib/rpm/macros.perl
Summary:	A command-line client to download WWW documents
Summary(pl):	Klient command-line do ¶ci±gania serwisów WWW
Name:		w3mir
Version:	1.0.10
Release:	2
License:	Artistic
Group:		Applications/Networking
Vendor:		<janl@math.uio.no>
Source0:	http://langfeldt.net/w3mir/%{name}-%{version}.tar.gz
URL:		http://langfeldt.net/w3mir/
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
W3mir jest programem do kopiowania i mirrorowania WWW. G³ównym celem
jest kopiowanie kompletnych struktur katalogów, aby by³y mo¿liwe do
przegl±dania przez serwer WWW albo bezpo¶rednio z dysku lub CD-ROM-u.
W tym celu W3mir mo¿e poprawiaæ URL-e. Oprócz tego potrafi ¶ci±gaæ
pojedyncze dokumenty itp. W3mir obs³uguje HTML4 i ma czê¶ciow± obs³ugê
CSS, Javy, ActiveX i PDF.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README example.cfg multiscope.cfg w3mir-HOWTO.html
%{perl_vendorlib}/w3http.pm
%{perl_vendorlib}/w3pdfuri.pm
%{perl_vendorlib}/htmlop.pm
%{_mandir}/man1/w3mir.1*
%{_mandir}/man1/w3mfix.1*
%attr(755,root,root) %{_bindir}/w3mir
%attr(755,root,root) %{_bindir}/w3mfix
