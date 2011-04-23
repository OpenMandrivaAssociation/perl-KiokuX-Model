%define upstream_name    KiokuX-Model
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A simple application specific wrapper for L<KiokuDB>
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/KiokuX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(KiokuDB)
BuildRequires: perl(MooseX::StrictConstructor)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This base class makes it easy to create the KiokuDB manpage database
instances in your application. It provides a standard way to instantiate
and use a the KiokuDB manpage object in your apps.

As your app grows you can subclass it and provide additional convenience
methods, without changing the structure of the code, but simply swapping
your subclass for the KiokuX::Model manpage in e.g. the
Catalyst::Model::KiokuDB manpage or whatever you use to glue it in.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


