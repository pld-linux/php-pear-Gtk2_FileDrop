%include	/usr/lib/rpm/macros.php
%define		_class		Gtk2
%define		_subclass	FileDrop
%define		_status		beta
%define		_pearname	Gtk2_FileDrop

Summary:	%{_pearname} - make Gtk widgets accept file drops
Summary(pl):	%{_pearname} - obs³uga plików przez widgety Gtk
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	70c720d64cd050f066c2bee515a00a64
URL:		http://pear.php.net/package/Gtk2_FileDrop/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-gtk
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
Klasy pozwalaj±ce w ³atwy sposób na obs³ugê przez widget Gtk2
dodawanie na zasadzie przeci±gnij i upu¶c (drag & drop) plików lub
katalogów.

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
