%define 	modulename pam_sasl
Summary:	A PAM module to authenticate against a SASL mechanism
Name:		pam-%{modulename}
Version:	0.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://people.redhat.com/nalin/test/pam_sasl-0.0.tar.gz
# Source0-md5:	88e50269262fb50a604ee3301cb83c35
URL:		http://people.redhat.com/nalin/test/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	lynx
BuildRequires:	pam-devel
BuildRequires:	sed >= 4.0
Obsoletes:	pam_sasl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pam_sasl is a PAM module which allows authentication against SASL
mechanisms.

%prep
%setup -q -n %{modulename}-%{version}

#sed -i -e "s#root#$(id -u)#g" src/Makefile*
#sed -i -e "s#/lib/security#/%{_lib}/security#g" configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--libdir=/%{_lib} \


%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_lib}/security/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) /%{_lib}/security/pam_sasl.so
%{_mandir}/man?/*
