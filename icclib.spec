%define lib_major 2
%define lib_name %mklibname icc %{lib_major}
%define lib_name_devel %mklibname icc -d

Name:    icclib
Version: 2.12
Release: 3
Summary: ICC profile I/O library

Group:     Graphics
License:   GPLv3
URL:       http://www.argyllcms.com/
Source0:   http://www.argyllcms.com/icclib_V%{version}.zip
# (fc) 2.1-0.beta.1mdv change build system to use autotools (Debian)
Patch0:    icclib-2.1-autotools.patch


%description
The icclib is a set of routines which implement the reading and
writing of color profile files that conform to the International
Color Consortium (ICC) Profile Format Specification, Version 3.4.

%package -n %{lib_name}
Summary:        Libraries for icclib
Group:          System/Libraries

%description -n %{lib_name}
The icclib is a set of routines which implement the reading and
writing of color profile files that conform to the International
Color Consortium (ICC) Profile Format Specification, Version 3.4.

%package -n %{lib_name_devel}
Summary:        Development libraries, header files for icclib
Group:          Development/GNOME and GTK+
Requires:       %{lib_name} = %{version}
Provides:	icclib-devel = %{version}-%{release}

%description -n %{lib_name_devel}
The icclib is a set of routines which implement the reading and
writing of color profile files that conform to the International
Color Consortium (ICC) Profile Format Specification, Version 3.4.


%prep
%setup -q -c
%patch0 -p1 -b .autotools

#needed by patch0
autoreconf -i

%build

%configure2_5x

%make

%check
make check

%install

%makeinstall_std

%files 
%defattr(-,root,root,-)
%{_bindir}/*

%files -n %{lib_name}
%defattr(-,root,root,-)
%{_libdir}/*.so.%{lib_major}*

%files -n %{lib_name_devel}
%doc log.txt Readme.txt todo.txt
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/*


%changelog
* Wed Dec 07 2011 Götz Waschk <waschk@mandriva.org> 2.12-3mdv2012.0
+ Revision: 738499
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.12-2mdv2011.0
+ Revision: 611169
- rebuild

* Mon Jan 18 2010 Frederic Crozat <fcrozat@mandriva.com> 2.12-1mdv2010.1
+ Revision: 493023
- Update tarball to use argyllcms 1.1.0 icclib copy (should be 2.12 final)

* Tue Jan 05 2010 Frederic Crozat <fcrozat@mandriva.com> 2.12-0.rc3.1mdv2010.1
+ Revision: 486420
- update to argyllcms 1.1.0rc3 snapshot

* Tue Jun 30 2009 Frederic Crozat <fcrozat@mandriva.com> 2.11-1mdv2010.0
+ Revision: 390968
- Release 2.11 final
- Remove patch1, merged upstream

* Tue Jun 09 2009 Frederic Crozat <fcrozat@mandriva.com> 2.1-0.beta.1mdv2010.0
+ Revision: 384364
- import icclib


