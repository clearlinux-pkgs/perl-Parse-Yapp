#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Parse-Yapp
Version  : 1.21
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/W/WB/WBRASWELL/Parse-Yapp-1.21.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/W/WB/WBRASWELL/Parse-Yapp-1.21.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Parse-Yapp-bin = %{version}-%{release}
Requires: perl-Parse-Yapp-man = %{version}-%{release}
Requires: perl-Parse-Yapp-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Parse::Yapp, Yet Another Parser Parser For Perl
Compiles yacc-like LALR grammars to generate Perl OO parser modules.

%package bin
Summary: bin components for the perl-Parse-Yapp package.
Group: Binaries

%description bin
bin components for the perl-Parse-Yapp package.


%package dev
Summary: dev components for the perl-Parse-Yapp package.
Group: Development
Requires: perl-Parse-Yapp-bin = %{version}-%{release}
Provides: perl-Parse-Yapp-devel = %{version}-%{release}
Requires: perl-Parse-Yapp = %{version}-%{release}

%description dev
dev components for the perl-Parse-Yapp package.


%package man
Summary: man components for the perl-Parse-Yapp package.
Group: Default

%description man
man components for the perl-Parse-Yapp package.


%package perl
Summary: perl components for the perl-Parse-Yapp package.
Group: Default
Requires: perl-Parse-Yapp = %{version}-%{release}

%description perl
perl components for the perl-Parse-Yapp package.


%prep
%setup -q -n Parse-Yapp-1.21
cd %{_builddir}/Parse-Yapp-1.21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/yapp

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Parse::Yapp.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/yapp.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
