%include	/usr/lib/rpm/macros.perl
Summary:	A command-line client to download WWW documents
Summary(pl):	Klient command-line do �ci�gania serwis�w WWW
Name:		w3mir
Version:	1.0.10
Release:	1
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
W3mir jest programem do kopiowania i mirrorowania WWW. G��wnym celem
jest kopiowanie kompletnych struktur katalog�w, aby by�y mo�liwe do
przegl�dania przez serwer WWW albo bezpo�rednio z dysku lub CD-ROM-u.
W tym celu W3mir mo�e poprawia� URL-e. Opr�cz tego potrafi �ci�ga�
pojedyncze dokumenty itp. W3mir obs�uguje HTML4 i ma cz�ciow� obs�ug�
CSS, Javy, ActiveX i PDF.

%prep
%setup -q

%build
perl Makefile.PL

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes.gz README.gz example.cfg multiscope.cfg w3mir-HOWTO.html
%{perl_sitelib}/w3http.pm
%{perl_sitelib}/w3pdfuri.pm
%{perl_sitelib}/htmlop.pm
%{_mandir}/man1/w3mir.1*
%{_mandir}/man1/w3mfix.1*
%attr(755,root,root) %{_bindir}/w3mir
%attr(755,root,root) %{_bindir}/w3mfix
