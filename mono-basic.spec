%define name mono-basic
%define version 2.0
%define release %mkrel 1

Summary: Visual Basic .NET support for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.go-mono.com/sources/%name/%{name}-%{version}.tar.bz2
#gw add file missing from the tarball
Patch: mono-basic-2.0-missing.patch
Patch1: mono-basic-2.0-version.patch
License: BSD
Group: Development/Other
URL:		http://www.go-mono.com/ 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel >= 1.2.5
BuildRequires: locales
BuildArch: noarch

%description
This package contains the Visual Basic .NET compiler and language
runtime. This allows you to compile and run VB.NET application and
assemblies.

%prep
%setup -q -n %name-%version
%patch -p1
%patch1 -p1

%build
export LC_ALL=UTF-8
./configure --prefix=%_prefix
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%_bindir/vbnc
%_prefix/lib/mono/2.0/vbnc*
%_prefix/lib/mono/gac/Microsoft.VisualBasic/
%_prefix/lib/mono/2.0/Microsoft.VisualBasic.dll


