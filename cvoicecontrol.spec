Summary:	CVoiceControl is a speech recognition system enabling to use spoken commands
Summary(pl.UTF-8):	CVoiceControl jest narzędziem do wydawania poleceń przy pomocy mowy
Name:		cvoicecontrol
Version:	0.9alpha
Release:	5
License:	GPL
Group:		Applications/Sound
Source0:	http://www.kiecza.de/daniel/linux/%{name}-%{version}.tar.gz
# Source0-md5:	19df71e7e4d246450a60519a8c31b953
Patch0:		%{name}-make.patch
URL:		http://www.kiecza.de/daniel/linux/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	texinfo
BuildRequires:	pth
BuildRequires:	ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVoiceControl is a speech recognition system that enables a user to
connect spoken commands to Unix commands. It automagically detects
speech input from a microphone, performs recognition on this input and
in case of successful recognition - executes the associated Unix
command.

%description -l pl.UTF-8
CVoiceControl jest narzędziem do rozpoznawania mowy i umożliwia
wydawanie poleceń komputerowi przez mikrofon.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make} CFLAGS="%{rpmcflags} " CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install cvoicecontrol/cvoicecontrol  $RPM_BUILD_ROOT%{_bindir}
install cvoicecontrol/model_editor  $RPM_BUILD_ROOT%{_bindir}
install cvoicecontrol/microphone_config  $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS FAQ README cvoicecontrol/docs/en/index*.html
%attr(755,root,root) %{_bindir}/*
