Summary:	GUI builder plugin for Eclipse
Name:		eclipse-plugin-jigloo
Version:	3.9.5
Release:	1
License:	Free
Group:		Development/Languages
Source0:	http://cloudgarden1.com/jigloo_395.zip
# Source0-md5:	339ee1024056913d04ec84040ad9efc8
URL:		http://www.cloudgarden.com/jigloo/
BuildRequires:	unzip
Requires:	eclipse >= 3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  	%{_libdir}/eclipse

%description
Jigloo GUI Builder is a plugin for the Eclipse Java IDE and WebSphere
Studio, which allows you to build and manage both Swing and SWT GUI
classes.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}

cp -r plugins features $RPM_BUILD_ROOT%{_eclipsedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/eclipse/features/*
%{_libdir}/eclipse/plugins/*
