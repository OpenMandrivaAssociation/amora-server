Name: amora-server
Version: 1.0
Release: %mkrel 1
Summary: A mobile remote assistant (server)
License: GPLv2
Group: System/X11
URL: http://code.google.com/p/amora/
# the svn on the tarball name is bogus, it's actually amora-1.0, see
# http://groups.google.com/group/amora-devel/browse_thread/thread/2a8f64a4fd6ce6ca
Source: http://amora.googlecode.com/files/amora-server-%{version}svn.tar.gz
Patch0: amora-server-1.0-manpages_names.patch
Patch1: amora-server-1.0-help.patch
BuildRequires: libimlib2-devel
BuildRequires: libbluez-devel
BuildRequires: libxtst-devel
BuildRequires: libx11-devel
BuildRoot: %{_tmppath}/%{name}-%{version}
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
%setup -q -n amora-server-%{version}svn
%patch0 -p0 -b .man_names
%patch1 -p0 -b .help

%build
# because of patch0
autoreconf -ifs
%configure
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/amorad
%{_mandir}/man7/amora.7.*
%{_mandir}/man8/amorad.8.*
