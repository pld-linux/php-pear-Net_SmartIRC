%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	SmartIRC
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - IRC client class
Summary(pl):	%{_pearname} - klasa klienta IRC
Name:		php-pear-%{_pearname}
Version:	0.5.5p1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b51a6edd91bcf66c5027939c1bee6325
Patch0:		%{name}-fix_includes.patch
URL:		http://pear.php.net/package/Net_SmartIRC/	
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
#Provides:	pear(SmartIRC/defines.php) pear(SmartIRC/messagehandler.php)
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

%description -l pl
Net_SmartIRC to klasa PHP do komunikacji z sieciami IRC zgodnymi z RFC
2812 (protoko�em IRC). Jest to API obs�uguj�ce wszystkie komunikaty
protoko�u IRC. Ta klasa zosta�a zaprojektowana do tworzenia bot�w
ircowych, chat�w i pokazywania informacji zwi�zanych z ircem na
stronach WWW.

Lista mo�liwo�ci:
- obs�uga akcji dla API
- obs�uga komunikat�w dla API
- zabezpieczenie przed zapchaniem przy wysy�aniu/odbieraniu
- wykrywanie i zmiana pseudonim�w w przypadku kolizji
- zdarzenia czasowe
- w pe�ni obiektowo zorientowane programowanie
- automatyczne wznawianie po��cze�
- system �ledzenia i logowania
- obs�uga rozszerze� PHP fsocks i socket
- zgodno�� z PHP od 4.1.x do 4.3.0
- sendbuffer z priorytetami
- synchronizacja kana��w (�ledzienie u�ytkownik�w/tryb�w/motyw�w w
  zmiennych)
- funkcje IRC: op, deop, voice, devoice, ban, unban, join, part,
  action, message, query, ctcp, mode, topic, nick, invite.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/SmartIRC/{defines,messagehandler}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{CHANGELOG,CREDITS,FEATURES,LICENSE,README,docs,examples}
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
