# Generated from metaclass-0.0.1.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	metaclass

Summary:	Adds a metaclass method to all Ruby objects
Name:		rubygem-%{rbname}

Version:	0.0.1
Release:	4
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/floehopper/metaclass
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Adds a metaclass method to all Ruby objects

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f test

%install
%gem_install

%files
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/metaclass
%{gem_dir}/gems/%{rbname}-%{version}/lib/metaclass/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{gem_dir}/doc/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/test
%{gem_dir}/gems/%{rbname}-%{version}/test/*.rb



