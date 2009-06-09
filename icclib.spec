%define lib_major 2
%define lib_name %mklibname icc %{lib_major}
%define lib_name_devel %mklibname icc -d

Name:    icclib
Version: 2.1
Release: %mkrel 0.beta.1
Summary: ICC profile I/O library

Group:     Graphics
License:   GPLv3
URL:       http://www.argyllcms.com/
Source0:   http://www.argyllcms.com/icclib.v%{version}beta.zip
# (fc) 2.1-0.beta.1mdv change build system to use autotools (Debian)
Patch0:    icclib-2.1-autotools.patch
# (fc) 2.1-0.beta.1mdv upstream bugfix 
Patch1:    icclib-2.1-bugfix.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%patch1 -p1 -b .bugfix

#needed by patch0
autoreconf -i

%build

%configure2_5x

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

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
%{_libdir}/*.la
%{_libdir}/*.a
%{_includedir}/*
