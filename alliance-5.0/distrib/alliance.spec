
%define       name            alliance
%define       ver             5.0
%define       prefix          /opt/alliance-5.0


Name:         %{name}
Summary:      Alliance VLSI CAD Sytem
Version:      %{ver}
Release:      %{release}%{dist}
License:      GPL
Group:        Applications/VLSI
Source:       %{name}-%{ver}.tar.gz
URL:          http://www-asim.lip6.fr/alliance/
Packager:     Jean-Paul Chaput <Jean-Paul.Chaput@lip6.fr>
BuildRoot:    %{_tmppath}/root-%{name}



%description
Alliance  is a complete set of free CAD tools  and  portable  libraries  for
VLSI design. It includes a VHDL  compiler  and  simulator,  logic  synthesis
tools, and automatic place and route  tools.  A  complete  set  of  portable
CMOS libraries is provided, including  a  RAM  generator,  a  ROM  generator
and a data-path compiler. Alliance is  the  result  of  a  ten  year  effort
spent at ASIM department of LIP6 laboratory of the  Pierre  et  Marie  Curie
University (Paris VI, France). Alliance has been used for research  projects
such as the 875 000 transistors StaCS superscalar microprocessor and 400 000
transistors IEEE Gigabit HSL Router.


%package tutorials
Summary:      Alliance VLSI CAD Sytem - Tutorials
Group:        Applications/VLSI


%description tutorials
Documentation and tutorials for the Alliance VLSI CAD Sytem.


%package sources
Summary:      Alliance VLSI CAD Sytem - sources
Group:        Applications/VLSI


%description sources
Sources of the Alliance VLSI CAD System, as you might guess...


%prep
%setup -n %{name}-%{ver}


%build
 if [ -d %{buildroot} ]; then rm -r %{buildroot}; fi

# Should be done in the Makefiles...
 mkdir -p %{buildroot}%{prefix}/etc

# As we use libraries for tools that we build in the same run, we have to
# do the "install" step within the "build" step.

 export     CPPFLAGS="-I%{buildroot}%{prefix}/include"
 export         LIBS="-L%{buildroot}%{prefix}/lib"
 export ALLIANCE_TOP=%{prefix}

 mkdir %{_os}
 if [ ! -f configure ]; then
   ./autostuff
 fi
 cd %{_os}
 ../configure --prefix=%{prefix} --enable-alc-shared
 make DESTDIR=%{buildroot} install

 cd ..
 rm -r %{_os}


%install
# Clean the source tree.
#(cd src; ./autostuff clean)

# Copy the sources in the install tree.
 mkdir -p %{buildroot}%{prefix}/src
 tar cf - * | (cd %{buildroot}%{prefix}/src; tar xvf -)

# Copy the Alliance autoconf macros in the right place.
#mkdir -p %{buildroot}/usr/share/aclocal
#(cd %{buildroot}%{prefix}/src; \
# cp alliance.m4 xpm.m4 motif.m4 %{buildroot}/usr/share/aclocal) 

# Set execution rights on the alc_env.* batchs and adjust ALLIANCE_TOP.
# This is not clean and has to be moved in the package itself in the
# future.
 chmod a+rx %{buildroot}%{prefix}/etc/alc_env.*
 sed "s,ALLIANCE_TOP *= *\([^;]*\),ALLIANCE_TOP=%{prefix}," \
    %{buildroot}%{prefix}/etc/alc_env.sh > \
    %{buildroot}%{prefix}/etc/alc_env.sh.1
 mv %{buildroot}%{prefix}/etc/alc_env.sh.1 \
    %{buildroot}%{prefix}/etc/alc_env.sh
 sed "s,setenv *ALLIANCE_TOP *\([^;]*\), setenv ALLIANCE_TOP %{prefix}," \
    %{buildroot}%{prefix}/etc/alc_env.csh > \
    %{buildroot}%{prefix}/etc/alc_env.csh.1
 mv %{buildroot}%{prefix}/etc/alc_env.csh.1 \
    %{buildroot}%{prefix}/etc/alc_env.csh


%post
 ln -sf %{prefix}/etc/alc_env.sh  /etc/profile.d
 ln -sf %{prefix}/etc/alc_env.csh /etc/profile.d

 grep "^%{prefix}/lib$" /etc/ld.so.conf &> /dev/null
 [ $? -ne 0 ] && echo "%{prefix}/lib" >> /etc/ld.so.conf

 /sbin/ldconfig


%preun
 if [ $1 -eq 0 ]; then
   rm -f /etc/profile.d/alc_env.sh
   rm -f /etc/profile.d/alc_env.csh

   grep -v "^%{prefix}/lib$" /etc/ld.so.conf > /etc/ld.so.conf.new
   # preserve permissions
   cat /etc/ld.so.conf.new > /etc/ld.so.conf
   rm -f /etc/ld.so.conf.new

   /sbin/ldconfig
 fi




%clean
 if [ -d %{buildroot} ]; then rm -r %{buildroot}; fi


%files
%attr(755, root, root) %{prefix}/etc/alc_env.*
%{prefix}/etc/*.dreal
%{prefix}/etc/*.graal
%{prefix}/etc/*.rds
%{prefix}/etc/*.elp
%{prefix}/etc/*.cfg
%{prefix}/etc/*.par
%{prefix}/etc/*.scapin
%{prefix}/etc/*.conf
%{prefix}/etc/*.mac
%{prefix}/etc/*.lef
%{prefix}/cells/*
%{prefix}/bin/*
%{prefix}/lib/*
%{prefix}/include/*
%{prefix}/man/man?/*
%{prefix}/doc/html/*
%{prefix}/doc/pdf/*


%files tutorials
%{prefix}/tutorials
%{prefix}/examples
%{prefix}/doc/overview
%{prefix}/doc/design-flow
%{prefix}/doc/alliance-run


%files sources
%{prefix}/src
#/usr/share/aclocal/*.m4


%changelog
* Wed Aug 26 2009 Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- Update to the latest CVS snapshot, including 64 bits support
  (courtesy of L. Jacomme).

* Thu Feb 17 2005 Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- Synch with current version: bug & compliance with gcc 3.4.x.

* Fri Jul 16 2004 Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- Added Tutorial sub-package (now managed by autoconf/automake).
- Removed release tag, must be given at compile time using the
  --define command line argument of rpmbuild (see mkdistrib).

* Sat Nov 15 2003 Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- assert is now in assert.h, patch mut.h to include it if
  GCC_VERSION >= 3003 (gcc >= 3.3.x).

* Sat Oct 18 2003 Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- Synched with 2003/10/18 version.
- Missing depcomp : added "--add-missing --copy" to the individual
  packages in autostuff, so the first who needs depcomp will add
  it at top level.

* Sun Oct 13 2002 Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- autoconf m4 macros moved back in the Alliance source tree to avoid
  re-declaration on our development computers (on which the macros
  are in teh source tree).
- Adopt the versioning scheme from czo.
- Try to switch to dynamic libraries.

* Wed Jul 17 2002  Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- Moved autoconf m4 macros to /usr/share/aclocal.
- Synched with the current CVS version of Alliance.

* Fri May 31 2002  Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- GenPat added.
- GenLib docs added.
- seplace/seroute/sea bug fixes.

* Thu May 16 2002  Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- Corrected buggy substitution of ALLIANCE_TOP in alc_env.csh.
- Remove the alc_env.* scripts in "/etc/profile.d" only if this
  is the last package to be removed.

* Mon May  6 2002  Jean-Paul.Chaput <Jean-Paul.Chaput@lip6.fr>
- Initial packaging for release 5.0 (alpha stage).
