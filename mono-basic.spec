%define name mono-basic
%define version 2.10
%define release %mkrel 2

Summary: Visual Basic .NET support for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.go-mono.com/sources/%name/%{name}-%{version}.tar.bz2
License: BSD
Group: Development/Other
URL:		http://www.go-mono.com/ 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel >= 2.10
BuildRequires: locales
BuildArch: noarch

%description
This package contains the Visual Basic .NET compiler and language
runtime. This allows you to compile and run VB.NET application and
assemblies.

%package 2.0
Summary: Visual Basic .NET support for Mono 2.0 API
Group: Development/Other
Requires: %{name} = %{version}-%{release}
Conflicts: %{name} < 2.10-2

%description 2.0
This package contains the Visual Basic .NET compiler and language
runtime under 2.0 API. This allows you to compile and run VB.NET
application and assemblies.

%prep
%setup -q -n %name-%version

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
%{_bindir}/*
%{_prefix}/lib/mono/4.0/*
%{_prefix}/lib/mono/gac/Microsoft.VisualBasic/10.0.0.0*
%{_prefix}/lib/mono/gac/Mono.Cecil.VB.Mdb/0.9.3.0*
%{_prefix}/lib/mono/gac/Mono.Cecil.VB.Pdb/0.9.3.0*
%{_prefix}/lib/mono/gac/Mono.Cecil.VB/0.9.3.0*
%{_mandir}/man1/vbnc.1*

%files 2.0
%defattr(-,root,root)
%{_prefix}/lib/mono/2.0/*
%{_prefix}/lib/mono/gac/Microsoft.VisualBasic/8.0.0.0*
