%include	/usr/lib/rpm/macros.php
%define		_class		CodeGen
%define		_subclass	MySQL
%define		_status		beta
%define		_pearname	CodeGen_MySQL
Summary:	%{_pearname} - abstract base package for MySQL code generators
Summary(pl.UTF-8):	%{_pearname} - abstrakcyjny pakiet podstawowy dla generatorów kodu MySQL
Name:		php-pear-%{_pearname}
Version:	0.9.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c856c5257e5015750af21be0078cb649
URL:		http://pear.php.net/package/CodeGen_MySQL/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-CodeGen >= 1.0.4
Requires:	php-pear-PEAR >= 1.4.0b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains common functionality used by all MySQL related
code generator packages. It is not functionally by itself though, it
just serves as an implementation framework for MySQL related code
generator packages just like CodeGen does for code generator packages
in general.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten zawiera wspólną funkcjonalność wykorzystywaną przez
wszystkie powiązane z MySQL pakiety generatorów kodu. Klasa ta sama w
sobie nie jest przydatna, służy natomiast jako framework dla pakietów
powiązanych z MySQL tak jak klasa CodeGen służy dla pozostałych klas
generujących kod.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/CodeGen/MySQL
%{php_pear_dir}/data/CodeGen_MySQL
