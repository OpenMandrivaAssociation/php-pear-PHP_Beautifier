%define		_class		PHP
%define		_subclass	Beautifier
%define		upstream_name	%{_class}_%{_subclass}
%define __noautoreq /usr/bin/php

Name:		php-pear-%{upstream_name}
Version:	0.1.14
Release:	8
Summary:	Beautifier for PHP

License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/PHP_Beautifier/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Patch0:		php-pear-PHP_Beautifier-0.1.14-fix-path.patch
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This program reformat and beautify PHP source code files
automatically.

%prep
%setup -q -c
%patch0 -p1
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data/%{upstream_name}/licenses
rm -f %{buildroot}%{_bindir}/*.bat

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%doc %{upstream_name}-%{version}/examples
%doc %{upstream_name}-%{version}/licenses
%{_bindir}/php_beautifier
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




