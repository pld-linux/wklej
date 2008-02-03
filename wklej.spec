Summary:	A wklej.org submitter
Summary(pl.UTF-8):	Aplikacja wysyłająca do wklej.org
Name:		wklej
Version:	0.0.9
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://wklej.org/apps/%{name}-%{version}.tar.gz
# Source0-md5:	a5896dbd7b0da6b53e3aebd173346228
URL:		http://wklej.org/
Requires:	perl-Config-Simple
Requires:	perl-libwww
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A wklej.org submitter.

%description
Aplikacja wysyłająca do wklej.org.

%prep
%setup -q -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -D %{name}-%{version}.pl $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
