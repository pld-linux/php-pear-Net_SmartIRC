%define		status		stable
%define		pearname	Net_SmartIRC
%define		php_min_version 5.3.0
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - IRC client class
Summary(pl.UTF-8):	%{pearname} - klasa klienta IRC
Name:		php-pear-%{pearname}
Version:	1.1.8
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	90674becfb53561d0fd02f0c17badc71
URL:		http://pear.php.net/package/Net_SmartIRC/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= %{php_min_version}
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpdocdir		%{_docdir}/phpdoc

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
- sendbuffer with priority levels
- channel synching (tracking of users/modes/topic etc in variables)
- IRC functions: op, deop, voice, devoice, ban, unban, join, part,
  action, message, query, ctcp, mode, topic, nick, invite

In PEAR status of this package is: %{status}.

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
- sendbuffer z priorytetami
- synchronizacja kanałów (śledzienie użytkowników/trybów/motywów w
  zmiennych)
- funkcje IRC: op, deop, voice, devoice, ban, unban, join, part,
  action, message, query, ctcp, mode, topic, nick, invite.

Ta klasa ma w PEAR status: %{status}.

%package phpdoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	php-dirs

%description phpdoc
Documentation for %{name}.

%description phpdoc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%pear_package_setup

mv docs/%{pearname}/docs/HTML apidoc
mv docs/%{pearname}/docs/* .
rmdir docs/%{pearname}/docs
mv docs/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_phpdocdir}/%{pearname}
cp -a apidoc/* $RPM_BUILD_ROOT%{_phpdocdir}/%{pearname}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc CREDITS FEATURES README.md
%doc DOCUMENTATION HOWTO
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/SmartIRC.php
%{php_pear_dir}/Net/SmartIRC
%{_examplesdir}/%{name}-%{version}

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/%{pearname}
