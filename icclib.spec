%define major	2
%define libname %mklibname icc %{major}
%define devname %mklibname icc -d
%define zipname ICCLib

Summary:	ICC profile I/O library
Name:		icclib
Version:	2.16
Release:	2
Group:		Graphics
License:	GPLv3
Url:		https://www.argyllcms.com/
Source0:	http://www.argyllcms.com/%{zipname}_V%{version}_src.zip

# (fc) 2.1-0.beta.1mdv change build system to use autotools (Debian)
Patch0:		icclib-2.1-autotools.patch
Patch1:		fix-linker-multiple-symbols.patch

%description
The icclib is a set of routines which implement the reading and
writing of color profile files that conform to the International
Color Consortium (ICC) Profile Format Specification, Version 3.4.

%package -n %{libname}
Summary:        Libraries for icclib
Group:          System/Libraries

%description -n %{libname}
The icclib is a set of routines which implement the reading and
writing of color profile files that conform to the International
Color Consortium (ICC) Profile Format Specification, Version 3.4.

%package -n %{devname}
Summary:        Development libraries, header files for icclib
Group:          Development/GNOME and GTK+
Requires:       %{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The icclib is a set of routines which implement the reading and
writing of color profile files that conform to the International
Color Consortium (ICC) Profile Format Specification, Version 3.4.

%prep
#%%setup -qc
%autosetup -p1 -n %{zipname}_V%{version}
#%%autopatch -p1

#needed by patch0
autoreconf -i

%build
%configure2_5x \
	--disable-static

%make_build

%check
make check

%install
%makeinstall_std

%files 
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libicc.so.%{major}*

%files -n %{devname}
%doc log.txt Readme.txt todo.txt
%{_libdir}/*.so
%{_includedir}/*

