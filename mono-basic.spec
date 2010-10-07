%define name mono-basic
%define version 2.8
%define release %mkrel 1

Summary: Visual Basic .NET support for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.go-mono.com/sources/%name/%{name}-%{version}.tar.bz2
License: BSD
Group: Development/Other
URL:		http://www.go-mono.com/ 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel >= 2.8
BuildRequires: locales
BuildArch: noarch

%description
This package contains the Visual Basic .NET compiler and language
runtime. This allows you to compile and run VB.NET application and
assemblies.

%prep
%setup -q -n %name-%version
#gw rename source file with parenthesis
cd vbnc/vbnc
sed -i -e "s^(^^" -e "s^)^^" vbnc.exe.sources
for x in source/Parser/Parser\(*.vb;do
  mv "$x" $(echo "$x" | sed -e "s^(^^" -e "s^)^^")
done


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
%_mandir/man1/vbnc.1*
%_prefix/lib/mono/2.0/vbnc*
%_prefix/lib/mono/gac/Microsoft.VisualBasic/
%_prefix/lib/mono/2.0/Microsoft.VisualBasic.dll
%_prefix/lib/mono/gac/Mono.Cecil.VB.Mdb
%_prefix/lib/mono/2.0/Mono.Cecil.VB.Mdb.dll
%_prefix/lib/mono/gac/Mono.Cecil.VB.Pdb
%_prefix/lib/mono/2.0/Mono.Cecil.VB.Pdb.dll
%_prefix/lib/mono/gac/Mono.Cecil.VB
%_prefix/lib/mono/2.0/Mono.Cecil.VB.dll


