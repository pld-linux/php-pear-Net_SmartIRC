%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       SmartIRC
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - IRC Client Class
Summary(pl):	%{_pearname} - Klasa klienta IRC
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	0.9
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://sf.net/projects/phpsmartirc/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_SmartIRC is a PHP class for communication with IRC networks,
which conforms to the RFC 2812 (IRC protocol).
It's an API that handles all IRC protocol messages.
This class is designed for creating IRC bots, chats and show irc related info on webpages.

Featurelist:
- actionhandler for the API
- messagehandler for the API
- send/receive floodprotection
- detects and changes nickname on nickname collisions
- time events
- full object oriented programmed
- autoreconnect
- debugging/logging system
- supports fsocks and PHP socket extension
- supports PHP 4.1.x to 4.3.0
- sendbuffer with priority levels
- channel synching (tracking of users/modes/topic etc in variables)
- IRC functions: op, deop, voice, devoice, ban, unban, join, part, action, message, query, ctcp, mode, topic, nick, invite 

This class has in PEAR status: %{_status}.

%description -l pl

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/SmartIRC/{defines,messagehandler}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/%{_subclass}/{README,HOWTO,FEATURES,DOCUMENTATION,CHANGELOG,CREDITS,example*.php,docs}
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
