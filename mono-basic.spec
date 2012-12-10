%define name mono-basic
%define version 2.10
%define release %mkrel 3

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


%changelog
* Fri May 04 2012 Götz Waschk <waschk@mandriva.org> 2.10-3mdv2012.0
+ Revision: 795870
- yearly rebuild

* Tue May 03 2011 Funda Wang <fwang@mandriva.org> 2.10-2
+ Revision: 663967
- split 2.0 api

* Thu Feb 17 2011 Götz Waschk <waschk@mandriva.org> 2.10-1
+ Revision: 638203
- new version
- bump mono dep
- update file list

* Thu Oct 07 2010 Götz Waschk <waschk@mandriva.org> 2.8-1mdv2011.0
+ Revision: 584071
- new version
- bump mono dep
- update file list

* Wed Sep 15 2010 Götz Waschk <waschk@mandriva.org> 2.6.2-2mdv2011.0
+ Revision: 578418
- fix build with new make

* Tue Mar 16 2010 Götz Waschk <waschk@mandriva.org> 2.6.2-1mdv2010.1
+ Revision: 521494
- update to new version 2.6.2

* Tue Dec 15 2009 Götz Waschk <waschk@mandriva.org> 2.6-1mdv2010.1
+ Revision: 478858
- update to new version 2.6

* Sat Jul 25 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.4.2-2mdv2010.0
+ Revision: 399759
- Rebuild

* Tue Jun 30 2009 Götz Waschk <waschk@mandriva.org> 2.4.2-1mdv2010.0
+ Revision: 390908
- new version

* Fri Apr 24 2009 Götz Waschk <waschk@mandriva.org> 2.4-1mdv2010.0
+ Revision: 368969
- new version

* Wed Jan 14 2009 Götz Waschk <waschk@mandriva.org> 2.2-1mdv2009.1
+ Revision: 329390
- new version
- drop patches
- add man page

* Sat Oct 11 2008 Götz Waschk <waschk@mandriva.org> 2.0-1mdv2009.1
+ Revision: 291910
- new version
- fix build

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.9-2mdv2009.0
+ Revision: 268147
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 08 2008 Götz Waschk <waschk@mandriva.org> 1.9-1mdv2009.0
+ Revision: 192396
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Götz Waschk <waschk@mandriva.org> 1.2.6-1mdv2008.1
+ Revision: 119269
- new version

* Thu Aug 30 2007 Götz Waschk <waschk@mandriva.org> 1.2.5-1mdv2008.0
+ Revision: 75984
- new version
- bump deps

* Thu May 17 2007 Götz Waschk <waschk@mandriva.org> 1.2.4-1mdv2008.0
+ Revision: 27606
- new version
- update file list
- bump deps


* Fri Feb 16 2007 Götz Waschk <waschk@mandriva.org> 1.2.3.1-1mdv2007.0
+ Revision: 121570
- depend on locales for build
- we can only build in UTF-8
- new version

* Wed Feb 07 2007 Götz Waschk <waschk@mandriva.org> 1.2.3-1mdv2007.1
+ Revision: 117073
- Import mono-basic

* Wed Feb 07 2007 Götz Waschk <waschk@mandriva.org> 1.2.3-1mdv2007.1
- initial package

