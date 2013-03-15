%define		_class		PHP
%define		_subclass	Beautifier
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.1.14
Release:	7
Summary:	Beautifier for PHP
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/PHP_Beautifier/
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
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%doc %{upstream_name}-%{version}/licenses
%{_bindir}/php_beautifier
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.14-6mdv2012.0
+ Revision: 742237
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.14-5
+ Revision: 679562
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.14-4mdv2011.0
+ Revision: 613755
- the mass rebuild of 2010.1 packages

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.14-3mdv2010.1
+ Revision: 467961
- rediff path patch
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.1.14-2mdv2010.0
+ Revision: 441514
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.1.14-1mdv2009.1
+ Revision: 368312
- Update php pear PHP_Beautifier to version 0.1.14
  Update the diff patch

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.13-3mdv2009.1
+ Revision: 322651
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.13-2mdv2009.0
+ Revision: 237049
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.1.13-1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.13-1mdv2008.0
+ Revision: 15942
- rediffed P0
- 0.1.13


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.8-1mdv2007.0
+ Revision: 82515
- Import php-pear-PHP_Beautifier

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.8-1mdk
- 0.1.8
- rediffed P0

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.7-1mdk
- 0.1.7
- rediffed P0
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-5mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-4mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-3mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-1mdk
- initial Mandriva package (PLD import)

