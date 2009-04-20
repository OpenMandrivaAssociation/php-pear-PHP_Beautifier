%define		_class		PHP
%define		_subclass	Beautifier
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - beautifier for PHP
Name:		php-pear-%{_pearname}
Version:	0.1.14
Release:	%mkrel 1
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/PHP_Beautifier/
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Patch0:		php-pear-PHP_Beautifier-0.1.14-path_fix.diff
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This program reformat and beautify PHP source code files
automatically.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%patch0 -p1

%build
cd %{_pearname}-%{version}/scripts
sed -i -e 's,"@php_bin@",/usr/bin/php,' php_beautifier

%install
rm -rf %{buildroot}

install -d %{buildroot}{%{_bindir},%{_datadir}/pear/%{_class}/%{_subclass}/{Batch/Output,Filter,StreamWrapper}}

install %{_pearname}-%{version}/scripts/php_beautifier %{buildroot}%{_bindir}
install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Batch/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Batch
install %{_pearname}-%{version}/%{_subclass}/Batch/Output/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Batch/Output
install %{_pearname}-%{version}/%{_subclass}/Filter/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Filter
install %{_pearname}-%{version}/%{_subclass}/StreamWrapper/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/StreamWrapper

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{examples,licenses,tests}
%attr(755,root,root) %{_bindir}/php_beautifier
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}
%{_datadir}/pear/packages/%{_pearname}.xml


