%define upstream_name	 Tie-Cache
%define upstream_version 0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
Summary:	LRU Cache in Memory
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements a least recently used (LRU) cache in memory through a
tie interface. Any time data is stored in the tied hash, that key/value pair
has an entry time associated with it, and as the cache fills up, those members
of the cache that are the oldest are removed to make room for new entries.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
perl -p -i -e 's|/usr/local/bin|/usr/bin|g;' Cache.pm
make

%check
make test

%install
%makeinstall_std
# Fix bogus dependency on Tie::Cache::LRU:
rm -f %{buildroot}%perl_vendorlib/Tie/bench.pl

%files
%doc CHANGES README
%{_mandir}/*/*
%{perl_vendorlib}/Tie


%changelog
* Thu Sep 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 429002
- new perl version macro

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.17-8mdv2009.0
+ Revision: 258655
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.17-7mdv2009.0
+ Revision: 246648
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.17-5mdv2008.1
+ Revision: 136362
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.17-5mdv2007.0
+ Revision: 108429
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Tie-Cache

* Thu Jun 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.17-4mdk
- Rebuild, cleanup

