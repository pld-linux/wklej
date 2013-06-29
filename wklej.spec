Summary:	A wklej.org submitter
Summary(pl.UTF-8):	Aplikacja wysyłająca do wklej.org
Name:		wklej
Version:	0.2.0
Release:	2
License:	GPL v2+
Group:		Applications
Source0:	http://wklej.org/m/apps/%{name}-%{version}.tar.gz
# Source0-md5:	29dd23756e6d68f722b132f92a328a0a
URL:		http://wklej.org/skrypt/
BuildRequires:	rpm-pythonprov
Requires:	python
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A wklej.org submitter.

%description -l pl.UTF-8
Aplikacja wysyłająca do wklej.org.

%package examples
Summary:	Scripts for wklej program
Summary(pl.UTF-8):	Skrypty dla programu wklej
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description examples
Scripts for wklej program.

%description examples -l pl.UTF-8
Skrypty dla programu wklej.

%prep
%setup -q -c %{name}-%{version}
%{__sed} '1s@.*@#!%{__python}@' -i wklej

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}
install wklej $RPM_BUILD_ROOT%{_bindir}/
install wklej.vim $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wklej

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
