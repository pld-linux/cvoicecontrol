Summary:	CVoiceControl is a speech recognition system enabling to use spoken commands
Summary(pl):	CVoiceControl jest narzêdziem do wydawania poleceñ przy pomocy mowy
Name:		cvoicecontrol
Version:	0.9alpha
Release:	1
License:	GPL
Group:		Applications/Tools
Source0:	http://www.kiecza.de/daniel/linux/%{name]-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://www.kiecza.de/daniel/linux/
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  texinfo
BuildRequires:  ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVoiceControl is a speech recognition system that enables a user to
connect spoken commands to unix commands.  It automagically detects
speech input from a microphone, performs recognition on this input and
in case of successful recognition - executes the associated unix
command. 

%description -l pl
CVoiceControl jest narzêdziem do rozpoznawania mowy i umo¿liwia
wydawanie poleceñ komputerowi przez mikrofon.

%prep
%setup -q
%patch0 -p1

%build
./configure

%{__make} CFLAGS="%{rpmcflags} " CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install cvoicecontrol/cvoicecontrol  $RPM_BUILD_ROOT%{_bindir}
install cvoicecontrol/model_editor  $RPM_BUILD_ROOT%{_bindir}
install cvoicecontrol/microphone_config  $RPM_BUILD_ROOT%{_bindir}

gzip -9nf AUTHORS BUGS COPYING FAQ INSTALL README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/en/index*.html
%attr(755,root,root) %{_bindir}/*
