%define upstream_name	 Tie-Cache
%define upstream_version 0.17

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	LRU Cache in Memory
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module implements a least recently used (LRU) cache in memory through a
tie interface. Any time data is stored in the tied hash, that key/value pair
has an entry time associated with it, and as the cache fills up, those members
of the cache that are the oldest are removed to make room for new entries.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__perl} -p -i -e 's|/usr/local/bin|/usr/bin|g;' Cache.pm
%{__make}

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std
# Fix bogus dependency on Tie::Cache::LRU:
rm -f %{buildroot}%perl_vendorlib/Tie/bench.pl

%files
%defattr(-,root,root)
%doc CHANGES README
%{_mandir}/*/*
%{perl_vendorlib}/Tie
