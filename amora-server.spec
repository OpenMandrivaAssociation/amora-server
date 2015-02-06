Name: amora-server
Version: 1.1
Release: 4
Summary: A mobile remote assistant (server)
License: GPLv2
Group: System/X11
URL: http://code.google.com/p/amora/
Source: http://amora.googlecode.com/files/amora-server-%{version}.tar.gz
BuildRequires: pkgconfig(imlib2)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xi)
BuildRequires: dbus-devel
Obsoletes: amora <= 0.9svn-1mdv2008.1

%description
Amora is an application that enables you to control your PC desktop using a
cellphone. It uses bluetooth to send mouse and keyboard events to the
graphical session. With it you can control your slides in OpenOffice.org,
movies or any other application. Amora also has a screenshot feature, where
you can see a thumbnail in the cellphone screen of the currently focused
window in your desktop.

In order to use amora, you need a mobile phone with amora-client
installed and running. The current client is implemented in Python
for S60 (Nokia cellphones) and is available at
http://code.google.com/p/amora/

%prep
%setup -q -n amora-server-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%{_bindir}/amorad
%{_mandir}/man7/amora.7.*
%{_mandir}/man8/amorad.8.*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-2mdv2011.0
+ Revision: 609970
- rebuild

* Mon Nov 30 2009 Funda Wang <fwang@mandriva.org> 1.1-1mdv2010.1
+ Revision: 471631
- new version 1.1

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2010.0
+ Revision: 436646
- rebuild

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-3mdv2009.1
+ Revision: 347699
- rebuild for latest bluez libs

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.0-2mdv2009.0
+ Revision: 226153
- rebuild

* Thu Jan 24 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0-1mdv2008.1
+ Revision: 157690
- new upstream version: 1.0
- new project/package name: amora-server
- adding manpages_names.patch (s/amora/amorad/, etc)
- adding help.patch (fixes --help message)
- project has new name: amora-server

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 12 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.9svn-1mdv2008.1
+ Revision: 108255
- add more build-requirements: libxtst-devel, libx11-devel
- add missing build-requirement for bluez-devel
- import amora

