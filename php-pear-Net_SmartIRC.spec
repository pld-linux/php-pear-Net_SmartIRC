%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	SmartIRC
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - IRC client class
Summary(pl.UTF-8):	%{_pearname} - klasa klienta IRC
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	042935bf413e7021aeea2971dd4d3997
Patch0:		%{name}-fix_includes.patch
Patch1:		%{name}-refs.patch
URL:		http://pear.php.net/package/Net_SmartIRC/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_SmartIRC is a PHP class for communication with IRC networks, which
conforms to the RFC 2812 (IRC protocol). It's an API that handles all
IRC protocol messages. This class is designed for creating IRC bots,
chats and show irc related info on webpages.

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
- IRC functions: op, deop, voice, devoice, ban, unban, join, part,
  action, message, query, ctcp, mode, topic, nick, invite

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Net_SmartIRC to klasa PHP do komunikacji z sieciami IRC zgodnymi z RFC
2812 (protokołem IRC). Jest to API obsługujące wszystkie komunikaty
protokołu IRC. Ta klasa została zaprojektowana do tworzenia botów
ircowych, chatów i pokazywania informacji związanych z ircem na
stronach WWW.

Lista możliwości:
- obsługa akcji dla API
- obsługa komunikatów dla API
- zabezpieczenie przed zapchaniem przy wysyłaniu/odbieraniu
- wykrywanie i zmiana pseudonimów w przypadku kolizji
- zdarzenia czasowe
- w pełni obiektowo zorientowane programowanie
- automatyczne wznawianie połączeń
- system śledzenia i logowania
- obsługa rozszerzeń PHP fsocks i socket
- zgodność z PHP od 4.1.x do 4.3.0
- sendbuffer z priorytetami
- synchronizacja kanałów (śledzienie użytkowników/trybów/motywów w
  zmiennych)
- funkcje IRC: op, deop, voice, devoice, ban, unban, join, part,
  action, message, query, ctcp, mode, topic, nick, invite.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}/%{_class}
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%doc docs/%{_pearname}/{CHANGELOG,CREDITS,FEATURES,README}
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
