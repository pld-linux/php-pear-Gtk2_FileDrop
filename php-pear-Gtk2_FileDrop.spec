%include	/usr/lib/rpm/macros.php
%define		_class		Gtk2
%define		_subclass	FileDrop
%define		_status		beta
%define		_pearname	Gtk2_FileDrop

Summary:	%{_pearname} - make Gtk widgets accept file drops
Summary(pl):	%{_pearname} - obs�uga plik�w przez widgety Gtk
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	2
License:	PHP 2.0.2
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a13440fb583e751d4dd5023410b35ce4
URL:		http://pear.php.net/package/Gtk2_FileDrop/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(gtk2)
Requires:	php-pear
Requires:	php-pear-MIME_Type >= 1.0.0
Requires:	php-pear-PEAR >= 1:1.4.-0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A class which makes it easy to make a GtkWidget accept the dropping of
files or folders.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasy pozwalaj�ce w �atwy spos�b na obs�ug� przez widget Gtk2
dodawanie na zasadzie przeci�gnij i upu�� (drag & drop) plik�w lub
katalog�w.

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
%doc install.log docs/%{_pearname}/{examples/example.phpw,examples/big_example.phpw}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Gtk2/FileDrop.php
